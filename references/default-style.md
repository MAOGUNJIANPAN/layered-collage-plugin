# Default Style: Archival Editorial Collage

Use this preset when the user asks for the established vintage collage look or supplies no other style reference.

## Style Genes

- 20th-century magazine editorial design, old archive graphics, Dada collage, constructivist composition, independent art zine, analog cut-and-paste craft.
- Neutral off-white, pale stone, cool gray, charcoal, and black form the base palette.
- Use one configurable high-chroma accent color: `<ACCENT_COLOR>`. Do not assume yellow.
- Allow a secondary accent only when requested, and keep it below roughly 5% of the canvas.
- Combine black-and-white or low-saturation photographic cutouts with torn papers, tape, graph paper, dot-grid paper, photocopy fragments, pencil marks, arrows, and circles.
- Maintain four to six readable depth levels through overlap, slight rotation, offset edges, and restrained physical shadow.
- Let the primary subject occupy about 50–60% of the composition unless the brief calls for a denser poster.
- Preserve purposeful negative space. Fill dead areas with quiet paper structure, not decorative clutter.

## Paper and Texture

- Treat cleanliness as the finish standard for this preset, not as a different composition style. Preserve the archival, Dada, constructivist, and zine design language above.
- Make the collage feel physical through controlled cutting, paper rims, overlap, scale, black-and-white photography against pure accent blocks, and restrained contact shadows—not through dirt or dense surface noise.
- Use clean neutral archival paper rather than yellowed tea-stained paper. The result should resemble a professionally assembled physical collage that was high-quality scanned and lightly restored.
- Keep broad paper faces, pure color blocks, faces, text-safe areas, and negative space flat, matte, calm, and nearly texture-free.
- Permit only faint, low-contrast, low-frequency tonal variation on broad paper faces.
- Concentrate sparse fibers at torn outer edges. Never spread fibers, cracks, or hair-like lines across a paper interior, face, text, or color block.
- Confine visible halftone, photocopy grain, and print noise to photographic cutouts, and keep them subtle enough to preserve anatomy and facial features.
- Grid and dot paper may appear locally at low contrast. Keep their geometry regular and static.
- Avoid global texture overlays.
- Prohibit repeating curls, worm-like lines, fingerprint patterns, waves, embossed wallpaper, maze patterns, wood-grain micro-lines, hair-like strands, moire, clustered particles, texture clumps, and regular generated noise.
- Prohibit stains, mold, oil, water damage, burn marks, corrosion, heavy creases, dirty gray veils, and other aging effects unless the user explicitly asks for one. An intentional aging effect must remain localized and must never become procedural microtexture.

## Edge Language

- Photographs: hand-cut or torn-paper silhouette with a narrow paper rim where suitable.
- Characters: recognizable isolated cutouts with coherent anatomy and a very light, close physical shadow.
- Accent paper: irregular torn edge, solid matte fill, sparse fiber detail.
- Tape: semi-opaque or fibrous, slightly misaligned, never glossy plastic.
- Marks: pencil or dry ink, thin, imperfect, and subordinate to the main subjects.
- Keep contact shadows soft, restrained, and directionally consistent across the frame. Do not curl, buckle, float, or heavily extrude paper layers.

## Typography

- Avoid readable text unless it serves the concept.
- When needed, use clipped magazine lettering, narrow grotesk type, typewriter labels, or bold black print on torn paper.
- Keep spelling exact. Generate words as independent movable layers when animation or later repositioning is expected.
- Do not combine unrelated type styles within one short phrase.

## Density Presets

### Quiet

- 2–3 main foreground assets.
- Broad clean paper fields.
- One or two faint grid/dot fragments.

### Balanced

- 3–6 foreground assets.
- Several paper depth changes.
- Local grid, dot, newsprint, tape, and drafting marks.
- Recommended default.

### Dense

- 6–10 foreground assets with controlled overlap.
- More print fragments and paper seams.
- Preserve at least one calm area and one unmistakable focal path.

## Color Parameter

Store the project accent color in `project.json`, for example:

```json
{
  "style_preset": "archival-editorial",
  "accent_color": "#3D66F5",
  "secondary_accent": null,
  "background_density": "balanced"
}
```

If the user supplies a hex value, preserve it. If the user supplies a color name, select a representative value and state it. If no color is supplied, offer a small set derived from the subject or choose one explicitly when the user prefers no questions.
