# Layer Workflow and Manifest

Use this reference only for `layered-assets` output or the selectively separated portion of `hybrid` output. Complete integrated keyframes do not require this structure, alpha validation, manifests, or contact sheets.

## Asset Classes

Classify each visible object before generation.

| Class | Location | Rule |
|---|---|---|
| Static background | `frameNN/background.png` | Full canvas, opaque, never moves independently |
| Shared asset | `shared/<id>.png` | Generate once and reuse verbatim across frames |
| Frame asset | `frameNN/layers/<id>.png` | Independent transparent element used only in that frame |
| Composite | `frameNN/composite.png` | Deterministically assembled from background and layer files |
| Manifest | `frameNN/layout.json` | Records exact placement, scale, rotation, z-order, and opacity |
| Text overlay guide | `frameNN/text-overlay.json` | Records copy and safe placement for blank label layers; contains no rendered pixels |

Examples of shared assets include one canonical storefront, a paper question mark, a tape strip, a product cutout, a recurring word block, or an optional subject supplied for the current project. Reuse depends on identity, not category: two deliberately different question-mark designs are two assets.

Do not bundle or assume a fixed brand character, mascot, person, or logo. When the current request supplies an identity-sensitive asset, reuse the exact approved PNG rather than generating a stylistically similar replacement. A flattened collage containing the subject is not automatically a sufficient identity source. Record whether each supplied identity-sensitive asset is `exact-reuse`, `approved-extraction`, or `reference-led-regenerate` in `project.json`.

## Layer Granularity

Create a separate PNG when an element may need independent timing, movement, replacement, or depth ordering later.

Split according to known production behavior, not every semantic noun. Prefer three independent photo cards over one flattened three-photo board only when they will move, appear, or be replaced independently. Prefer one complete photo board when it behaves as a single physical collage piece. A shared backing paper may be its own layer when it has a separate role.

When the downstream motion or reuse need is not yet known, keep the design integrated and defer separation. Do not preemptively fragment the composition merely to preserve hypothetical flexibility.

Keep elements together when they must always behave as one physical cutout. Examples:

- Keep a character's connected hand and held object together when their relationship must never break.
- Keep a printed question mark and its torn backing paper together when they enter as one paper scrap.
- Separate an accent branch paper from a storefront if they appear at different times.
- Separate each storefront if each enters at a different time.
- Separate each word block, but not necessarily every letter, unless the letters animate independently.

Do not split anatomy into fragile micro-layers unless explicitly requested.

Identify exact duplicates before generation. Generate a reusable storefront, question mark, tape strip, arrow, product cutout, or other repeated motif once under `shared/` and reference that same file from each manifest. Do not create near-duplicate copies unless the visual direction calls for deliberate variation.

## Project Manifest

Use `project.json` for shared decisions:

```json
{
  "project": "example",
  "aspect_ratio": "4:3",
  "canvas": {"width": 2048, "height": 1536},
  "style_mode": "default",
  "style_preset": "archival-editorial",
  "accent_color": "#3D66F5",
  "secondary_accent": null,
  "background_density": "balanced",
  "shared_assets": [
    {"id": "optional-subject", "file": "shared/optional-subject.png", "source": "supplied-for-this-project", "policy": "exact-reuse"},
    {"id": "question-mark", "file": "shared/question-mark.png"}
  ]
}
```

## Frame Layout Manifest

Use center-based coordinates. `center_x` and `center_y` are pixels on the final canvas. Set either `width` or `height` to preserve the source aspect ratio; set both only when deliberate nonuniform scaling is acceptable.

```json
{
  "canvas": {
    "width": 2048,
    "height": 1536,
    "background": "background.png"
  },
  "layers": [
    {
      "id": "optional-subject",
      "file": "../shared/optional-subject.png",
      "center_x": 420,
      "center_y": 1030,
      "height": 760,
      "rotation": -2.0,
      "opacity": 1.0,
      "z": 10
    },
    {
      "id": "question-mark-1",
      "file": "../shared/question-mark.png",
      "center_x": 960,
      "center_y": 460,
      "width": 180,
      "rotation": 4.0,
      "opacity": 1.0,
      "z": 20
    }
  ]
}
```

Paths are resolved relative to the manifest file. Layers are composed in ascending `z` order, then original list order for ties.

## Blank Label Manifest

Use `text-overlay.json` when `text_mode` is `blank-labels`. Give the editor enough information to add text in Jianying, CapCut, Premiere, or another tool without guessing placement:

```json
{
  "text_mode": "blank-labels",
  "items": [
    {
      "id": "feeling-relaxed",
      "label_layer": "../shared/feeling-relaxed-label.png",
      "text": "松弛感",
      "safe_box_in_label_pixels": {"x": 42, "y": 24, "width": 346, "height": 72},
      "alignment": "center",
      "suggested_style": {
        "weight": "bold",
        "color": "#171717",
        "max_lines": 1
      }
    }
  ]
}
```

The safe box uses pixels relative to the unscaled label PNG. Keep the actual label pixels completely blank inside that box. Do not render the `text` field into the composite.

## Background Rules

Generate background plates separately. They may contain:

- base archive paper;
- permanent graph/dot/newsprint fragments;
- permanent tape and faint drafting marks;
- quiet surface variation and edge fibers.

They must not contain:

- any person, character, mascot, logo, or other movable subject;
- photographic storefronts, products, price tags, service scenes, or other movable subjects;
- reusable question marks or word blocks;
- shadows cast by foreground assets;
- holes, silhouettes, or ghost remnants of removed foreground objects.

## Alpha Rules

- Save foreground layers as RGBA PNG.
- Require both transparent pixels and visible pixels.
- Treat fully opaque PNGs as failed transparency, even if their background looks white or checkerboard-like.
- Keep RGB values behind transparent pixels irrelevant; alpha defines visibility.
- Trim to the nonzero-alpha bounding box with 8–24 pixels of transparent padding.
- Avoid feathered digital halos. Retain only natural paper-edge softness.

Normalize generated PNGs through the bundled Pillow helper before downstream resizing or compositing. This re-encodes image pixels without embedded generation metadata that may confuse other image processors:

```bash
python scripts/collage_layers.py normalize input.png output.png --width 2048 --height 1536 --opaque
```

Use `--opaque` for background plates and composites only. Omit it for transparent foreground layers.

## Transparent Asset Generation

For each transparent asset:

- request one isolated object or one deliberately inseparable physical group;
- request a true transparent background and clean alpha edge;
- include all attached props and anatomy that belong to that object;
- exclude unrelated shadows, neighboring paper scraps, clipped fragments, and painted checkerboards;
- preserve the desired torn edge or cut edge inside the visible silhouette;
- leave no large transparent margins;
- keep the asset at useful working resolution.

For `blank-labels`, generate the complete visual treatment—torn paper, accent underline, tape, edge fibers, and shadow—but leave the intended text area genuinely empty. Do not insert placeholder words, fake glyphs, lorem ipsum, or faint guide text. Save each independently editable label as its own transparent PNG and record intended copy, safe box, alignment, and suggested treatment in `text-overlay.json`.

For `rendered-text`, prefer generating the paper shape separately and adding text deterministically in an editor or code-native step. If generated text is used, verify every character before approval. Keep written language consistent with the user's source copy; do not substitute English because a preferred font is missing.

For identity-sensitive assets supplied for the current project, never trade identity fidelity for transparency. If reference-conditioned generation fails genuine-alpha validation, retry once with a stricter transparency prompt while retaining the identity reference. If it fails again, stop and request a clean canonical asset or explicit permission for extraction. Do not drop the reference and approximate the subject from prose, and do not retain that identity as a built-in skill asset.

## Deterministic Composition

Use `scripts/collage_layers.py compose` to create the composite. Do not regenerate a new “matching” final image. This guarantees that the delivered PNGs can reconstruct the approved frame.

This requirement applies to a project whose deliverable is explicitly reconstructable layers. In `hybrid` mode, preserve the approved complete frame as the visual source of truth and state when selected regenerated or extracted assets cannot reconstruct it pixel-for-pixel.

When placement changes, edit `layout.json` and recompose. When appearance changes, replace only the relevant asset and recompose.

## Review Package

For each layered approval round, provide:

- composite preview;
- labeled contact sheet of transparent layers on a checkerboard preview only;
- a short list of shared and frame-specific assets;
- notes about any element baked into the background.

The checkerboard belongs only to the review preview and must never be present in the source PNG pixels.

Before delivery, also verify that rotations do not create unintended cropping, shared files are truly reused rather than regenerated, and the delivered background plus PNGs reconstruct the approved layered composite exactly.
