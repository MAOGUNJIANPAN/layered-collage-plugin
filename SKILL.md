---
name: generate-layered-collage
description: Create storyboard stills and reusable transparent PNG assets for analog editorial collage projects. Use when a user wants a collage keyframe, layered image package, cut-paper storyboard, reusable subject/store/question-mark/product assets, blank text-label layers for later editing, or a final composite that can later be animated. Generate backgrounds and independent layers first instead of extracting them from a flattened image. Supports archival and clean editorial presets or a user-supplied visual reference, with configurable accent colors. Excludes motion scripts, animation prompts, and video generation.
---

# Generate Layered Collage

Build collage artwork from reusable image layers. Treat the composite as the result of the layers, never as an unrelated rerender.

## Boundaries

- Handle visual analysis, style definition, storyboard composition, opaque backgrounds, transparent PNG layers, deterministic compositing, previews, and quality checks.
- Do not write animation beats, motion scripts, camera instructions, frame timing, or video prompts. Complete those as a separate task after the stills are approved.
- Do not create a flat final image first and then remove its background unless the user explicitly asks for recovery of an existing artwork. For new work, generate layer-first.
- Do not silently lock the project to yellow. Treat accent color as a project parameter.

## Load References

Read only the references needed for the request:

- For the built-in archival visual language, read `references/default-style.md`.
- For a cleaner poster-like collage with strict hierarchy, limited decoration, and quiet paper surfaces, read `references/clean-editorial-style.md`.
- For directory structure, manifest fields, reusable assets, and compositing rules, read `references/layer-workflow.md`.
- For image-generation prompt construction, read `references/prompt-patterns.md`.

## Workflow

### 1. Establish the brief

Collect or infer:

- source copy, message, or scene intent;
- number of frames or semantic beats;
- aspect ratio and target resolution;
- optional people, characters, products, logos, or other identity references supplied for this project;
- `external_asset_policy`, only when such a reference is supplied: `exact-reuse`, `approved-extraction`, or `reference-led-regenerate`;
- `style_mode`: `default` or `reference-led`;
- `style_preset`: `archival-editorial`, `clean-editorial`, or a temporary reference-led profile;
- `text_mode`: `blank-labels`, `rendered-text`, or `no-text`;
- primary accent color and any permitted secondary accent;
- desired background density: `quiet`, `balanced`, or `dense`;
- which motifs may be reused across frames.

Do not ask for information that can be safely inferred. If color is unspecified, either offer two or three suitable accent choices or, when the user asks for speed, select one and state it before generation.

Default to `blank-labels` for storyboards intended for Jianying, CapCut, Premiere, After Effects, or another editor unless the user explicitly wants finished text inside the artwork. In this mode, generate the styled paper labels without glyphs and record the intended copy and placement separately.

Do not assume that any recurring person, character, mascot, logo, or brand asset belongs to the skill. Include identity-sensitive material only when the current request supplies or explicitly invokes it. Prefer an approved transparent asset for `exact-reuse`. If only a flattened composite or loose identity reference is available, do not silently invent a replacement: request a canonical asset or make identity approval a separate checkpoint before the storyboard checkpoint.

For `reference-led` work, inspect one to three reference images before generating. Summarize the reusable style genes: material, palette, contrast, texture frequency, edge treatment, typography, spatial density, and compositional rhythm. Do not copy protected characters, logos, or exact compositions unless the user owns or supplied them for that purpose.

### 2. Split the content into frames

Turn the message into a concise storyboard. Give each frame one primary visual claim. Avoid cramming every noun from the copy into the picture.

When `style_preset` is `clean-editorial`, establish a composition budget before the layer inventory: one dominant subject, two to four directly relevant supporting elements, three to six functional guide marks at most, and roughly 25–40% negative space. Treat these as design targets rather than a reason to split one semantic object into arbitrary pieces. Do not distribute elements evenly or turn the frame into a specimen board or nine-grid.

Before generating, prepare a layer inventory for every frame:

1. opaque background;
2. shared reusable layers;
3. frame-specific photographic or character layers;
4. accent-paper and graphic layers;
5. exact text layers, if any;
6. final composite assembled from items 1–5.

When the project is intended for later animation, default to one layer per semantic object even though this skill does not write the motion plan. For example, three reference photos should normally be three PNGs, not one flattened photo board. Combine them only when the backing and contents are intentionally one inseparable physical collage piece.

Identify exact duplicates before generation. Generate a reusable shop, question mark, tape strip, arrow, or other repeated motif once under `shared/` and reference the same file from multiple manifests. Do not make near-duplicate copies unless the visual direction calls for deliberate variation.

### 3. Define the project layout

Follow `references/layer-workflow.md`. Use this default structure:

```text
project/
  project.json
  shared/
    question-mark.png
    optional-subject.png
  frame01/
    background.png
    layers/
    layout.json
    text-overlay.json
    composite.png
  frame02/
    background.png
    layers/
    layout.json
    composite.png
```

Keep every background at the full canvas size and fully opaque. Keep each foreground asset tightly cropped with genuine transparency. The final composite must retain the exact canvas dimensions.

### 4. Design and generate only the first frame

Use staged approval by default:

1. plan the full series lightly;
2. fully generate frame 1 and its reusable shared assets;
3. compose frame 1 from those exact assets;
4. show the composite and a labeled layer preview;
5. ask the user to lock or revise style, density, color, and composition;
6. continue the remaining frames only after approval.

This checkpoint is mandatory when establishing a new style. Skip it only if the user explicitly requests immediate batch generation.

### 5. Generate backgrounds and layers

Use the image-generation capability for raster creation and editing. When a local reference image is supplied, inspect it before generating.

Generate in this order:

1. opaque background with only elements that will never move independently;
2. shared transparent assets;
3. frame-specific transparent assets;
4. blank label or exact-text elements as separate assets when they must move independently;
5. layout manifest;
6. deterministic composite.

For each transparent asset:

- request one isolated object only;
- request a true transparent background and clean alpha edge;
- include all attached props and anatomy that belong to that object;
- exclude unrelated shadows, neighboring paper scraps, clipped fragments, and painted checkerboards;
- preserve the desired torn edge or cut edge inside the visible silhouette;
- leave no large transparent margins;
- keep the asset at useful working resolution.

For `clean-editorial`, keep the cutout language consistent across every asset: clear controlled irregular contours, an optional narrow off-white paper rim, flat paper faces, and one shared direction and softness for contact shadows. Do not use dirt, fibers, or heavy aging as a substitute for collage depth.

For `blank-labels`, generate the complete visual treatment—torn paper, accent underline, tape, edge fibers, and shadow—but leave the intended text area genuinely empty. Do not insert placeholder words, fake glyphs, lorem ipsum, or faint guide text. Save each blank label as its own transparent PNG. Record intended text, safe box, alignment, and suggested treatment in `text-overlay.json`; keep these instructions outside the pixels.

For `rendered-text`, prefer generating the paper shape separately and adding text deterministically in an editor or code-native step. If generated text is used, verify every character before approval.

Keep written language consistent with the user's source copy. Do not translate Chinese copy into English merely because a preferred font is missing. For voice-over storyboards, omit readable headlines by default unless text materially carries the visual claim or the user requests it. If the required script cannot be rendered exactly, use a language-neutral visual device or pause for a font choice.

For identity-sensitive assets supplied for the current project, never trade identity fidelity for transparency. If a reference-conditioned generation fails genuine-alpha validation, retry once with a stricter transparency prompt while retaining the identity reference. If it fails again, stop and request a clean canonical asset or explicit permission for extraction; do not drop the reference and approximate the subject from prose. Do not retain that identity as a built-in skill asset or assumption.

### 6. Validate every asset

Use `scripts/collage_layers.py` rather than visual guesswork:

```bash
python scripts/collage_layers.py validate project/shared/*.png project/frame01/layers/*.png
python scripts/collage_layers.py normalize generated-background.png project/frame01/background.png --width 2048 --height 1536 --opaque
python scripts/collage_layers.py trim input.png output.png --padding 12
python scripts/collage_layers.py compose project/frame01/layout.json project/frame01/composite.png
python scripts/collage_layers.py contact-sheet project/frame01/layers project/frame01/layers-preview.png
```

Regenerate an asset when it lacks genuine alpha, contains a checkerboard baked into pixels, has malformed anatomy, includes unexplained fragments, or departs from the approved style. The helper script may validate, trim, preview, and composite; it must not be used to cosmetically fake a failed transparent image.

### 7. Perform visual quality control

Inspect both the isolated assets and the assembled composite at 100% zoom.

Check:

- one coherent style across all layers;
- no extra hands, arms, fingers, props, or detached fragments;
- no broken hand-to-wrist or object-to-hand connection;
- exact text spelling and punctuation;
- no repeating worm-like curls, embossed wallpaper texture, maze pattern, moire, or global crawling microtexture;
- halftone and photocopy grain stay inside photographic cutouts rather than covering every paper surface;
- torn fibers occur mainly at paper edges;
- no excessive JPEG compression, blur, or repeated-edit damage;
- shared files are truly reused instead of regenerated;
- no unintended cropping after rotation;
- final composite is assembled from the delivered background and PNGs;
- `clean-editorial` frames preserve the planned negative space, one unmistakable focal subject, limited palette, and no more than the planned decorative marks;
- decorative arrows, grids, circles, numbers, and paper strips explain hierarchy or direction instead of merely filling empty space;
- paper shadows are light, close, and directionally consistent; broad paper faces and pure color blocks remain calm and even;
- photographs are purposefully cropped cutouts or integrated paper objects, not unexplained full rectangles pasted into the composition.

When a single layer is wrong, replace that layer and recompose. Do not repeatedly edit the flattened composite.

### 8. Deliver

Provide:

- approved frame composites;
- one opaque background per frame;
- one transparent PNG per independently movable element;
- reusable elements once under `shared/`;
- one `layout.json` per frame;
- one `text-overlay.json` per frame when blank labels are used;
- a labeled contact sheet for quick review;
- an archive only when useful or requested.

State any deliberately baked-in background elements. Do not claim a PSD unless a real layered PSD has been created. A folder of PNG layers plus manifests is the standard deliverable.

## Style Expansion

Treat the built-in archival and clean editorial styles as separate presets, not the entire skill.

For a new collage style:

1. require or request one to three useful references;
2. extract style genes without adding them permanently;
3. run the first-frame approval workflow;
4. use the temporary profile for the project;
5. add it as a named preset only after the user explicitly approves updating the skill.

Keep new presets separate from the default so their palettes and material rules do not leak into one another.
