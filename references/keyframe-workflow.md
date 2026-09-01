# Integrated Keyframe Workflow

Use this workflow for complete collage stills and paired start/end frames. An integrated image is a primary deliverable, not a failed attempt at layering.

## Output Modes

| Mode | Use when | Primary files |
|---|---|---|
| `integrated-keyframes` | The user wants complete storyboard stills or start/end images for downstream video generation | `complete.png` or `start.png` and `end.png` |
| `hybrid` | The complete design must be approved first and only selected objects need independent reuse or movement later | Complete frame plus selected transparent PNGs |
| `layered-assets` | The user explicitly needs a reconstructable layered package | Background, transparent layers, manifest, composite |

When unsure, stay integrated until a concrete independent-motion, replacement, or reuse need is known.

## Project Structure

Single still:

```text
project/
  project.json
  frame01/
    complete.png
```

Paired keyframes:

```text
project/
  project.json
  shot01/
    start.png
    end.png
  shot02/
    start.png
    end.png
```

Example project decisions:

```json
{
  "project": "example",
  "output_mode": "integrated-keyframes",
  "pairing": "start-end",
  "aspect_ratio": "4:3",
  "canvas": {"width": 2048, "height": 1536},
  "style_preset": "archival-editorial",
  "accent_color": "#3D66F5",
  "secondary_accent": null,
  "continuity_anchors": [
    "neutral paper surface",
    "recurring structural backing",
    "stable shadow direction",
    "consistent photographic contrast"
  ]
}
```

Continuity anchors describe functions, not mandatory objects. A folder, dossier, board, paper plane, or another physical backing may serve as the recurring structural anchor when it fits the story.

## Complete-Frame Design Order

Solve each image in this order:

1. Define one primary visual claim.
2. Choose one dominant subject or evidence cluster.
3. Establish a structural backing or stable physical surface.
4. Add only supporting papers, photos, tools, or marks that explain the claim.
5. Assign color roles before decorating.
6. Resolve overlap, edge cropping, physical scale, and contact shadows together.
7. Remove anything that competes with the primary claim at thumbnail size.

The complete composition should feel designed as one physical scene. Do not make it resemble an asset board, contact sheet, or collection of evenly spaced cutouts.

## Paired Start/End Frames

Each frame must be a complete standalone design. The pair should preserve:

- canvas and camera viewpoint;
- underlying paper world or work surface;
- recurring structural anchor;
- material treatment and edge roughness;
- palette roles and photographic contrast;
- object scale logic and shadow direction.

Change only what communicates the intended transition, such as object position, revealed evidence, opened paper, completed mark, changed focal photo, or a restrained shift in density. Avoid changing the entire layout, palette, camera, and prop set at once.

The end frame may add, remove, rotate, uncover, replace, or re-emphasize elements, but it should still look like the next state of the same designed world.

## Approval

For a new visual system:

1. generate the first complete start frame;
2. confirm hierarchy, density, palette roles, paper behavior, and recurring anchor;
3. lock those invariants;
4. generate the end frame and later shots from the locked system.

Do not require a layer contact sheet during integrated approval. The user is approving the visible design, not its internal decomposition.

## Optional Later Separation

If downstream production later reveals a need for independent motion:

- preserve the approved complete frame as the visual source of truth;
- list only the actual motion or reuse groups;
- keep connected anatomy and held objects together when separation would break structure;
- recreate or extract only those groups;
- state whether the derived assets can reconstruct the frame exactly.

Do not retroactively split every visible item merely because one object needs motion.

## Delivery Checks

- Every file has the intended aspect ratio and canvas size.
- Complete frames are fully opaque unless transparency is explicitly requested.
- Start/end pairs are clearly named and ordered.
- The focal claim survives thumbnail viewing.
- Series anchors recur without making every composition identical.
- The background and structural backing do not overpower the main information.
- No accidental random text, watermark, broken anatomy, malformed furniture, or floating prop appears.
