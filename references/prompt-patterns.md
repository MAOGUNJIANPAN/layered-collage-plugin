# Prompt Patterns

Use these as components, not as rigid full prompts. Replace every placeholder.

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

Correct the failed layer, not the composite:

```text
Regenerate only <ASSET_ID>. Preserve <LOCKED_PROPERTIES>. Correct <FAILURE>. Do not alter <UNCHANGED_PROPERTIES>. Return one tightly cropped transparent PNG with genuine alpha and no additional elements.
```

## Prompt Assembly Checklist

Before generation, ensure the prompt specifies:

- exactly one asset or one background plate;
- intended file role;
- identity and structural invariants;
- style profile and approved accent color;
- exact text, if any;
- edge and shadow behavior;
- transparency or opacity requirement;
- prohibited artifacts relevant to that asset;
- whether it is shared or frame-specific.
