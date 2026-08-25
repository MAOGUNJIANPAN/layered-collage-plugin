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

- Use clean neutral archival paper rather than yellowed tea-stained paper.
- Keep broad paper faces mostly matte and low-frequency.
- Permit subtle random scan grain and natural tonal variation.
- Concentrate fibers at torn edges.
- Confine strong halftone, photocopy grain, and print noise to photographic cutouts.
- Grid and dot paper may appear locally at low contrast. Keep their geometry regular and static.
- Avoid global texture overlays.
- Prohibit repeating curls, worm-like lines, embossed wallpaper patterns, maze patterns, wood-grain micro-lines, moire, and regular generated noise.

## Edge Language

- Photographs: hand-cut or torn-paper silhouette with a narrow paper rim where suitable.
- Characters: recognizable isolated cutouts with coherent anatomy and modest physical shadow.
- Accent paper: irregular torn edge, solid matte fill, sparse fiber detail.
- Tape: semi-opaque or fibrous, slightly misaligned, never glossy plastic.
- Marks: pencil or dry ink, thin, imperfect, and subordinate to the main subjects.

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
