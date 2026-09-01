---
name: generate-layered-collage
description: Create complete analog editorial collage storyboard stills, paired start/end keyframes, and optional reusable transparent PNG assets. Use when a user wants a collage keyframe, cut-paper storyboard, complete still for downstream video generation, layered image package, reusable subject/store/question-mark/product assets, blank text-label layers, or a deterministic composite. Default to integrated complete frames; split only elements that have a known need for independent motion, replacement, or reuse. Supports a built-in archival collage style or a user-supplied visual reference, with configurable accent colors. Excludes motion scripts, animation prompts, and video generation.
---

# Generate Layered Collage

Create visually complete collage keyframes first. Treat transparent layers as an optional production format, not a prerequisite for good composition.

## Boundaries

- Handle visual analysis, style definition, storyboard composition, complete raster keyframes, paired start/end frames, optional opaque backgrounds, transparent PNG layers, deterministic compositing, previews, and quality checks.
- Do not write animation beats, motion scripts, camera instructions, frame timing, or video prompts. Complete those as a separate task after the stills are approved.
- For new work, default to an integrated complete frame. Do not force the image model to generate every semantic object separately before the composition is visually solved.
- Use layers only when the user asks for them or an object has a known need for independent motion, replacement, depth order, or reuse.
- Do not silently lock the project to yellow, blue, or any other fixed palette. Treat accent colors and their visual roles as project parameters.

## Load References

Read only the references needed for the request:

- For the built-in visual language, read `references/default-style.md`.
- For complete stills and paired start/end frames, read `references/keyframe-workflow.md`.
- For optional transparent assets, directory structure, manifests, and deterministic compositing, read `references/layer-workflow.md`.
- For image-generation prompt construction, read `references/prompt-patterns.md`.

## Workflow

### 1. Establish the brief

Collect or infer:

- source copy, message, or scene intent;
- number of frames or semantic beats;
- aspect ratio and target resolution;
- `output_mode`: `integrated-keyframes`, `layered-assets`, or `hybrid`;
- optional people, characters, products, logos, or other identity references supplied for this project;
- `external_asset_policy`, only when such a reference is supplied: `exact-reuse`, `approved-extraction`, or `reference-led-regenerate`;
- `style_mode`: `default` or `reference-led`;
- `text_mode`: `blank-labels`, `rendered-text`, or `no-text`;
- primary accent color and any permitted secondary accent;
- desired background density: `quiet`, `balanced`, or `dense`;
- which visual anchors should recur across the series.

Default `output_mode` to `integrated-keyframes` for storyboard stills, start/end frames, and images intended for downstream video generation. Use `layered-assets` only when the user explicitly requests independently movable or reusable files. Use `hybrid` when the complete design should be approved first and only selected motion groups need to be recreated or extracted afterward.

Do not ask for information that can be safely inferred. If color is unspecified, either offer two or three suitable accent choices or, when the user asks for speed, select one and state it before generation.

Default to `blank-labels` only when the user expects later text editing. Otherwise prefer `no-text` for voice-over storyboards unless readable copy materially carries the visual claim. In integrated mode, blank labels may be baked into the complete frame; they do not need separate PNG files unless independent editing or movement is requested.

Do not assume that any recurring person, character, mascot, logo, or brand asset belongs to the skill. Include identity-sensitive material only when the current request supplies or explicitly invokes it. Prefer an approved transparent asset for `exact-reuse`. If only a flattened composite or loose identity reference is available, do not silently invent a replacement: request a canonical asset or make identity approval a separate checkpoint before the storyboard checkpoint.

For `reference-led` work, inspect one to three reference images before generating. Summarize the reusable style genes: material, palette, contrast, texture frequency, edge treatment, typography, spatial density, compositional rhythm, and color hierarchy. Do not copy protected characters, logos, or exact compositions unless the user owns or supplied them for that purpose.

### 2. Split the content into frames

Turn the message into a concise storyboard. Give each frame one primary visual claim. Avoid cramming every noun from the copy into the picture.

For integrated frames, define:

1. primary visual claim and focal subject;
2. structural anchor or backing plane;
3. supporting evidence, props, or paper fragments that serve the claim;
4. palette roles and focal path;
5. continuity invariants shared with neighboring frames;
6. controlled change between start and end frames, if paired.

Do not prepare a layer inventory unless `output_mode` is `layered-assets` or `hybrid`. When layers are required, split by actual motion or reuse group rather than automatically splitting every semantic noun. Follow `references/layer-workflow.md`.

### 3. Define the project layout

For `integrated-keyframes`, follow `references/keyframe-workflow.md`. Use a simple structure such as:

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

A single still may use `frame01/complete.png`. Do not create empty `layers/`, manifests, or contact sheets for an integrated-only project.

For `layered-assets` or `hybrid`, also read `references/layer-workflow.md` and use its layered structure only for the requested motion or reuse groups.

### 4. Design and approve the first complete frame

Use staged approval by default when establishing a new style:

1. plan the full series lightly;
2. fully generate the first complete frame;
3. inspect hierarchy, palette roles, paper behavior, prop relevance, and series anchors;
4. show the complete frame for approval;
5. lock or revise style, density, color, and composition;
6. continue the remaining frames only after approval.

If the user requests immediate batch generation, proceed without the checkpoint. When a paired start/end shot is the first sample, generate the start frame first, approve its visual system, then generate the end frame with explicit continuity invariants.

### 5. Generate according to output mode

Use the image-generation capability for raster creation and editing. When a local reference image is supplied, inspect it before generating.

#### Integrated keyframes

- Generate one complete, polished frame in a single composition-aware pass.
- Solve scale, overlap, cropping, color hierarchy, physical shadows, and narrative relationships together.
- Keep every prop relevant to the current visual claim; do not fill space from a generic decoration list.
- For paired frames, preserve the same visual world while changing only the intended state. Use `references/keyframe-workflow.md`.
- Regenerate a new frame when the design must change substantially. Do not repeatedly degrade the same raster through many edits.

#### Layered assets

- Generate an opaque background plus only the independently needed transparent assets.
- Compose the final frame deterministically from the delivered files.
- Follow all alpha, manifest, text-label, identity, and validation rules in `references/layer-workflow.md`.

#### Hybrid

- Approve the complete integrated frame first.
- Identify only the elements with a real downstream motion, replacement, or reuse need.
- Recreate or extract those groups as transparent assets while using the approved frame as the composition and style reference.
- Preserve the integrated frame as the visual source of truth. Do not imply pixel-perfect reconstruction when regenerated layers differ from it.

Keep written language consistent with the user's source copy. Do not translate Chinese copy into English merely because a preferred font is missing. If generated text is required, verify every character. If exact rendering is unavailable, omit the text, use a language-neutral device, or pause for a font choice.

### 6. Validate the appropriate deliverable

For integrated keyframes, verify canvas size, opacity, file integrity, start/end pairing, and cross-frame visual continuity. Do not fail an integrated image because it has no alpha channel or layer manifest.

For layered or hybrid deliverables, use `scripts/collage_layers.py` rather than visual guesswork:

```bash
python scripts/collage_layers.py validate project/shared/*.png project/frame01/layers/*.png
python scripts/collage_layers.py normalize generated-background.png project/frame01/background.png --width 2048 --height 1536 --opaque
python scripts/collage_layers.py trim input.png output.png --padding 12
python scripts/collage_layers.py compose project/frame01/layout.json project/frame01/composite.png
python scripts/collage_layers.py contact-sheet project/frame01/layers project/frame01/layers-preview.png
```

Regenerate an asset when it lacks genuine alpha, contains a checkerboard baked into pixels, has malformed anatomy, includes unexplained fragments, or departs from the approved style. The helper script may validate, trim, preview, and composite; it must not be used to cosmetically fake a failed transparent image.

### 7. Perform visual quality control

Inspect final frames at 100% zoom. When layers exist, inspect both the isolated assets and the assembled composite.

Check:

- one coherent style across the series;
- the primary claim reads before the backing plane and decorative marks;
- recurring anchors create continuity without forcing identical compositions;
- props reinforce the current narrative and physical setting;
- no extra hands, arms, fingers, props, or detached fragments;
- no broken hand-to-wrist, chair-to-leg, stool-to-leg, or object-to-hand connections;
- exact text spelling and punctuation;
- no repeating worm-like curls, embossed wallpaper texture, maze pattern, moire, or global crawling microtexture;
- halftone and photocopy grain stay inside photographic cutouts rather than covering every paper surface;
- torn fibers occur mainly at paper edges and remain controlled;
- no excessive JPEG compression, blur, or repeated-edit damage;
- start/end pairs retain stable camera, scale logic, paper world, palette, and shadow direction;
- when layers exist, shared files are truly reused and the final composite is assembled from the delivered files.

For a failed integrated composition, regenerate the complete frame with locked invariants and a focused correction brief. For a failed independent layer, replace that layer and recompose.

### 8. Deliver

For `integrated-keyframes`, provide:

- approved complete stills or paired start/end frames;
- the project-level continuity and palette decisions when useful;
- no unnecessary layer package.

For `layered-assets`, provide:

- approved frame composites;
- one opaque background per frame;
- one transparent PNG per independently needed element;
- reusable elements once under `shared/`;
- one `layout.json` per layered frame;
- one `text-overlay.json` when blank labels require later editing;
- a labeled contact sheet when useful.

For `hybrid`, provide the approved complete frame plus only the requested transparent assets and reconstruction notes. State any elements that remain baked into the complete frame. Do not claim a PSD unless a real layered PSD has been created.

## Style Expansion

Treat the built-in archival collage style as one preset, not the entire skill.

For a new collage style:

1. require or request one to three useful references;
2. extract style genes without replacing the existing default;
3. run the first-frame approval workflow;
4. use the temporary profile for the project;
5. add it as a named preset or optional composition pattern only after the user explicitly approves updating the skill.

Preserve existing presets and elements when adding a new approved pattern. Keep palettes and material rules scoped so one project does not leak into another.
