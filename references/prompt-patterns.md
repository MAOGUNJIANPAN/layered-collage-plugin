# Prompt Patterns

Use these as components, not as rigid full prompts. Replace every placeholder.

## Integrated Complete Keyframe

```text
Create one complete, polished <ASPECT_RATIO> analog editorial collage keyframe at <RESOLUTION>. This is a final integrated composition, not a layer sheet, material board, mockup, or collection of isolated assets.

Primary visual claim: <PRIMARY_CLAIM>. Dominant subject or evidence cluster: <FOCAL_SUBJECT>. Structural anchor or physical backing: <STRUCTURAL_ANCHOR>. Supporting papers and props: <SUPPORTING_ELEMENTS>, included only where they clarify the claim. Use <STYLE_PROFILE> with density <DENSITY>.

Color roles: neutral paper, black, gray, and white carry most information; <STRUCTURAL_ACCENT> serves only as the subordinate backing or series anchor; <FOCAL_ACCENT> marks the main point; <ANNOTATION_ACCENT_OR_NONE> appears only in sparse technical annotations. Preserve exact supplied hex values. Do not let a large color field overpower the focal black-and-white information.

Compose the scene as one coherent physical paper world. Resolve scale, overlap, irregular cut or restrained torn edges, canvas-edge cropping, contact shadows, and narrative relationships together. Keep the main claim readable at thumbnail size. Use only relevant drafting marks, registration crosses, crop marks, grids, or annotations. No default cartoon starbursts or explosion badges.

Paper faces are matte, quiet, and low-frequency. Fibers stay mainly at torn edges. Strong halftone and photocopy grain stay inside photographic cutouts. Prohibit repeating curls, worm-like lines, embossed wallpaper patterns, maze textures, wood-grain micro-lines, moire, global crawling noise, random text, watermarks, broken anatomy, malformed furniture, floating props, asset-board spacing, and modern UI.
```

## Paired End Keyframe

```text
Create the complete end keyframe for the approved start frame. It must look like the next state of the same designed physical world, not a restyled remake.

Preserve exactly: <LOCKED_CAMERA_AND_CANVAS>, <PAPER_WORLD>, <STRUCTURAL_ANCHOR>, <PALETTE_ROLES>, <PHOTOGRAPHIC_CONTRAST>, <EDGE_TREATMENT>, <OBJECT_SCALE_LOGIC>, and <SHADOW_DIRECTION>.

Change only: <INTENDED_STATE_CHANGE>. The end frame must remain a polished standalone composition with one clear focal claim. Do not change the entire prop set, viewpoint, palette, paper material, or layout rhythm. Do not add unrelated decorative objects, random text, cartoon starbursts, new logos, or a different visual style.
```

## Background Plate

```text
Create a new <ASPECT_RATIO> opaque background plate at <RESOLUTION> for a layered collage storyboard. Use <STYLE_PROFILE>. Base materials: <BACKGROUND_MATERIALS>. Use <ACCENT_COLOR> only in the specified permanent background fragments. Density: <DENSITY>.

This is the static background only. Include no people, characters, storefronts, products, price tags, service photos, question marks, movable word blocks, foreground-object shadows, cutout-shaped gaps, or ghost remnants. The entire canvas must be fully opaque and visually complete behind future layers.

Paper faces are matte and low-frequency. Fibers appear mainly at torn edges. Permit subtle random scan grain, but prohibit repeating curls, worm-like lines, embossed wallpaper patterns, maze patterns, wood-grain micro-lines, moire, uniform texture overlays, watermarks, and modern UI.
```

## Transparent Photographic Cutout

```text
Create exactly one isolated <SUBJECT> as a transparent PNG layer for a handmade editorial collage. Use <STYLE_PROFILE>. Preserve <IDENTITY_AND_STRUCTURE>. Show the complete object with natural cut-paper or torn-paper edges and restrained physical paper shadow contained close to the silhouette.

True transparent background with a clean alpha channel. No white rectangle, no colored backdrop, no checkerboard painted into the pixels, no neighboring scraps, no tape unless specified, no unexplained fragments, no cropped extremities, no duplicate object, and no text unless specified. Keep the asset tightly framed with a small transparent margin.

Anatomy and object connections must be coherent: <ANATOMY_RULES>. Prohibit extra hands, arms, fingers, handles, props, or floating pieces. Keep strong halftone and photocopy texture inside the photographic cutout; prohibit repeating worm-like microtexture and moire.
```

## Transparent Paper Graphic

```text
Create exactly one isolated <GRAPHIC> printed on <PAPER_DESCRIPTION> as a transparent PNG collage layer. Use <ACCENT_COLOR> according to <COLOR_PLACEMENT>. The printed content must read exactly: <EXACT_CONTENT>.

Treat the graphic and its backing paper as one physical cutout. True transparent background and clean alpha channel. Natural torn edge, matte paper face, sparse edge fibers, no white canvas, no checkerboard, no additional symbols, no altered spelling, no duplicate marks, no unrelated shadows, and no large transparent margins. Avoid repeating curls, embossed patterns, maze textures, and moire.
```

## Transparent Blank Label

```text
Create exactly one isolated blank <LABEL_TYPE> as a transparent PNG collage layer. Use <PAPER_DESCRIPTION> with <ACCENT_COLOR> applied only to <COLOR_PLACEMENT>. Preserve the approved torn edge, tape, paper shadow, and analog print treatment.

Leave the entire intended text safe area completely empty and visually calm. No letters, numbers, punctuation, placeholder words, pseudo-writing, watermark, logo, or faint guide text. True transparent background and clean alpha channel. Keep the label tightly cropped with a small transparent margin. Avoid repeating curls, embossed patterns, maze textures, and moire.
```

## Optional Referenced Subject

```text
Create exactly one isolated subject cutout based only on the identity reference supplied for this project. Preserve the defining identity features: <IDENTITY_FEATURES>. Pose: <POSE>. Attached props: <PROPS_OR_NONE>.

Use <STYLE_PROFILE> and produce a true transparent PNG. Keep the subject as one coherent cut-paper object unless the brief explicitly requires separate parts. For people or characters, all visible hands must connect naturally to wrists and arms; every finger must be continuous; no hidden extra arm may emerge from an elbow or torso. Preserve abstract heads, logos, symbols, packaging, or product structure exactly when present in the supplied reference.
```

Use this pattern only when the current request supplies or explicitly invokes the subject. When an approved transparent asset exists, prefer exact reuse. Do not use this prompt to approximate an established identity from a flattened collage, and do not retain the subject as a built-in skill asset.

## Text Language Rule

```text
Use the same written language as the user's source copy. Render the required text verbatim: <EXACT_CONTENT>. Do not translate it, paraphrase it, or substitute English for missing fonts. If exact rendering is unavailable, omit the text and preserve the visual claim through symbols or request a font choice.
```

Apply the text-language rule only in `rendered-text` mode. In `blank-labels` mode, keep all intended copy in `text-overlay.json` and render no glyphs at all.

## Style-Consistency Suffix

```text
Match the approved first frame in paper tone, halftone scale, edge roughness, print contrast, physical shadow softness, collage depth, and accent-color behavior. Do not reinterpret the style, increase warmth, smooth the cut edges, or apply a global texture overlay.
```

## Correction Prompt

For an integrated frame, regenerate a new complete version rather than repeatedly degrading the raster:

```text
Regenerate the complete <FRAME_ID> as a new image. Preserve <LOCKED_INVARIANTS>. Correct <DESIGN_FAILURE>. Keep <UNCHANGED_CONTENT_AND_COLOR_ROLES>. Return one polished complete keyframe, not isolated assets or a layer sheet.
```

For a layered deliverable, correct the failed layer rather than the composite:

```text
Regenerate only <ASSET_ID>. Preserve <LOCKED_PROPERTIES>. Correct <FAILURE>. Do not alter <UNCHANGED_PROPERTIES>. Return one tightly cropped transparent PNG with genuine alpha and no additional elements.
```

## Prompt Assembly Checklist

Before generation, ensure the prompt specifies:

- exactly one complete frame, one asset, or one background plate;
- intended file role;
- identity and structural invariants;
- style profile and approved accent color;
- exact text, if any;
- edge and shadow behavior;
- transparency or opacity requirement;
- prohibited artifacts relevant to that asset;
- whether it is shared or frame-specific.

For complete frames, also specify the primary visual claim, structural anchor, palette roles, series invariants, and whether the frame is a start or end state. Do not request alpha transparency or layer isolation unless the selected output mode requires it.
