#!/usr/bin/env python3
"""Validate, trim, preview, and deterministically compose collage PNG layers."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def fail(message: str) -> None:
    raise ValueError(message)


def open_rgba(path: Path) -> Image.Image:
    if not path.exists():
        fail(f"missing file: {path}")
    image = Image.open(path)
    image.load()
    return image.convert("RGBA")


def alpha_stats(image: Image.Image) -> tuple[int, int, tuple[int, int, int, int] | None]:
    alpha = image.getchannel("A")
    minimum, maximum = alpha.getextrema()
    return minimum, maximum, alpha.getbbox()


def validate_file(path: Path, require_transparency: bool = True) -> list[str]:
    issues: list[str] = []
    try:
        original = Image.open(path)
        original.load()
    except Exception as exc:
        return [f"cannot open: {exc}"]

    if original.format != "PNG":
        issues.append(f"expected PNG, got {original.format or 'unknown'}")
    has_alpha = original.mode in {"RGBA", "LA"} or "transparency" in original.info
    image = original.convert("RGBA")
    minimum, maximum, bbox = alpha_stats(image)

    if require_transparency and not has_alpha:
        issues.append("missing alpha channel")
    if maximum == 0 or bbox is None:
        issues.append("layer is fully transparent")
    if require_transparency and minimum == 255:
        issues.append("alpha is fully opaque; background is not transparent")

    if bbox:
        width, height = image.size
        left, top, right, bottom = bbox
        transparent_margin = min(left, top, width - right, height - bottom)
        if transparent_margin > max(width, height) * 0.2:
            issues.append("excessive transparent margin; trim the asset")

    return issues


def command_validate(args: argparse.Namespace) -> int:
    failed = False
    for raw_path in args.paths:
        path = Path(raw_path)
        issues = validate_file(path, require_transparency=not args.allow_opaque)
        if issues:
            failed = True
            print(f"FAIL {path}")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print(f"OK   {path}")
    return 1 if failed else 0


def command_trim(args: argparse.Namespace) -> int:
    source = Path(args.input)
    target = Path(args.output)
    image = open_rgba(source)
    _, maximum, bbox = alpha_stats(image)
    if maximum == 0 or bbox is None:
        fail(f"cannot trim fully transparent image: {source}")

    left, top, right, bottom = bbox
    padding = max(0, args.padding)
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(image.width, right + padding)
    bottom = min(image.height, bottom + padding)
    target.parent.mkdir(parents=True, exist_ok=True)
    image.crop((left, top, right, bottom)).save(target, "PNG")
    print(f"saved {target} ({right-left}x{bottom-top})")
    return 0


def command_normalize(args: argparse.Namespace) -> int:
    source = Path(args.input)
    target = Path(args.output)
    image = open_rgba(source)

    if (args.width is None) != (args.height is None):
        fail("provide both --width and --height, or neither")
    if args.width is not None and args.height is not None:
        size = (max(1, args.width), max(1, args.height))
        image = image.resize(size, Image.Resampling.LANCZOS)

    target.parent.mkdir(parents=True, exist_ok=True)
    if args.opaque:
        flattened = Image.new("RGB", image.size, args.matte)
        flattened.paste(image, mask=image.getchannel("A"))
        flattened.save(target, "PNG")
    else:
        image.save(target, "PNG")
    print(f"saved {target} ({image.width}x{image.height})")
    return 0


def resize_layer(image: Image.Image, layer: dict) -> Image.Image:
    width = layer.get("width")
    height = layer.get("height")
    if width is None and height is None:
        return image

    if width is not None:
        width = max(1, int(round(float(width))))
    if height is not None:
        height = max(1, int(round(float(height))))

    if width is None:
        width = max(1, int(round(image.width * height / image.height)))
    elif height is None:
        height = max(1, int(round(image.height * width / image.width)))

    return image.resize((width, height), Image.Resampling.LANCZOS)


def set_opacity(image: Image.Image, opacity: float) -> Image.Image:
    opacity = min(1.0, max(0.0, opacity))
    if math.isclose(opacity, 1.0):
        return image
    result = image.copy()
    alpha = result.getchannel("A").point(lambda value: round(value * opacity))
    result.putalpha(alpha)
    return result


def command_compose(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    canvas_spec = manifest["canvas"]
    width = int(canvas_spec["width"])
    height = int(canvas_spec["height"])
    base_dir = manifest_path.parent

    background_path = (base_dir / canvas_spec["background"]).resolve()
    background = open_rgba(background_path)
    if background.size != (width, height):
        fail(f"background size {background.size} does not match canvas {(width, height)}")
    if background.getchannel("A").getextrema()[0] != 255:
        fail("background must be fully opaque")
    canvas = background.copy()

    indexed_layers = list(enumerate(manifest.get("layers", [])))
    indexed_layers.sort(key=lambda item: (float(item[1].get("z", 0)), item[0]))

    for _, layer in indexed_layers:
        layer_path = (base_dir / layer["file"]).resolve()
        image = open_rgba(layer_path)
        issues = validate_file(layer_path, require_transparency=True)
        hard_issues = [issue for issue in issues if "excessive transparent margin" not in issue]
        if hard_issues:
            fail(f"invalid layer {layer.get('id', layer_path.name)}: {'; '.join(hard_issues)}")

        image = resize_layer(image, layer)
        image = set_opacity(image, float(layer.get("opacity", 1.0)))
        rotation = float(layer.get("rotation", 0.0))
        if not math.isclose(rotation, 0.0):
            image = image.rotate(-rotation, expand=True, resample=Image.Resampling.BICUBIC)

        center_x = float(layer["center_x"])
        center_y = float(layer["center_y"])
        x = int(round(center_x - image.width / 2))
        y = int(round(center_y - image.height / 2))
        canvas.alpha_composite(image, dest=(x, y))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output, "PNG")
    print(f"saved {output} ({width}x{height})")
    return 0


def checkerboard(size: tuple[int, int], cell: int = 16) -> Image.Image:
    width, height = size
    board = Image.new("RGB", size, "#eeeeee")
    draw = ImageDraw.Draw(board)
    for y in range(0, height, cell):
        for x in range(0, width, cell):
            if (x // cell + y // cell) % 2:
                draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill="#cfcfcf")
    return board


def command_contact_sheet(args: argparse.Namespace) -> int:
    source = Path(args.input_dir)
    files = sorted(path for path in source.rglob("*.png") if path.is_file())
    output = Path(args.output)
    files = [path for path in files if path.resolve() != output.resolve()]
    if not files:
        fail(f"no PNG files found under {source}")

    tile_w, tile_h = args.tile_width, args.tile_height
    label_h = 34
    columns = max(1, args.columns)
    rows = math.ceil(len(files) / columns)
    sheet = Image.new("RGB", (columns * tile_w, rows * (tile_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for index, path in enumerate(files):
        image = open_rgba(path)
        image.thumbnail((tile_w - 24, tile_h - 24), Image.Resampling.LANCZOS)
        tile = checkerboard((tile_w, tile_h))
        x = (tile_w - image.width) // 2
        y = (tile_h - image.height) // 2
        tile.paste(image, (x, y), image)
        col = index % columns
        row = index // columns
        origin_x = col * tile_w
        origin_y = row * (tile_h + label_h)
        sheet.paste(tile, (origin_x, origin_y))
        label = str(path.relative_to(source))
        draw.text((origin_x + 8, origin_y + tile_h + 9), label, fill="black", font=font)

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, "PNG")
    print(f"saved {output} ({sheet.width}x{sheet.height})")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="validate PNG and alpha properties")
    validate.add_argument("paths", nargs="+")
    validate.add_argument("--allow-opaque", action="store_true", help="allow fully opaque PNGs")
    validate.set_defaults(func=command_validate)

    trim = subparsers.add_parser("trim", help="crop a layer to its alpha bounds")
    trim.add_argument("input")
    trim.add_argument("output")
    trim.add_argument("--padding", type=int, default=12)
    trim.set_defaults(func=command_trim)

    normalize = subparsers.add_parser(
        "normalize", help="re-encode a PNG without metadata and optionally resize it"
    )
    normalize.add_argument("input")
    normalize.add_argument("output")
    normalize.add_argument("--width", type=int)
    normalize.add_argument("--height", type=int)
    normalize.add_argument("--opaque", action="store_true")
    normalize.add_argument("--matte", default="#ffffff")
    normalize.set_defaults(func=command_normalize)

    compose = subparsers.add_parser("compose", help="assemble a frame from a layout manifest")
    compose.add_argument("manifest")
    compose.add_argument("output")
    compose.set_defaults(func=command_compose)

    contact = subparsers.add_parser("contact-sheet", help="preview all PNG layers in a directory")
    contact.add_argument("input_dir")
    contact.add_argument("output")
    contact.add_argument("--columns", type=int, default=4)
    contact.add_argument("--tile-width", type=int, default=320)
    contact.add_argument("--tile-height", type=int, default=240)
    contact.set_defaults(func=command_contact_sheet)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return int(args.func(args))
    except (ValueError, KeyError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
