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

## Optional Composition Pattern: Design Dossier on a Work Surface

Use this pattern when the story concerns design reasoning, research, comparison, evidence, editing, or implementation. It extends the archival collage preset; it does not replace the existing poster-like composition.

- Establish one recurring structural anchor such as a file folder, dossier, backing board, drawing sheet, map, or proof packet.
- Place one dominant evidence cluster above it: a focal photograph, drawing, annotated plan, product proof, or character panel.
- Let supporting sheets overlap as one physical stack rather than distributing objects evenly across the canvas.
- Crop a few relevant work tools at the canvas edge to imply a real studio or review session. Suitable tools depend on the story and may include a ruler, caliper, pencil, camera, microphone, phone, binder clip, or another task-specific object.
- Keep object scale, perspective, surface contact, and shadow direction physically coherent. A prop must look placed on the same surface, not pasted from an unrelated asset board.
- Use registration crosses, crop marks, drafting circles, grids, measurements, or sparse handwritten annotations as mature technical signals when relevant.
- Do not add props from a fixed checklist. Every visible tool and paper should support the current narrative claim.
- Do not default to cartoon starbursts, explosion badges, playful stickers, or childish attention symbols. Use them only when the user or subject explicitly calls for that tone.

## Series Continuity

- Build a family through recurring functions: stable paper world, structural anchor, photographic contrast, edge treatment, palette roles, and shadow direction.
- Reuse a visual anchor without copying the same composition. The focal subject, paper stack, crop, and density may change from frame to frame.
- Keep camera viewpoint and physical scale logic stable within a paired start/end shot.
- Treat props at the canvas edge as continuity cues, but rotate or replace them only when the narrative changes.
- Each frame must remain a complete standalone design; continuity should not make later frames feel like unfinished variations.

## Color Roles and Hierarchy

- Let neutral black, gray, white, and paper tones carry most information.
- A larger cool or saturated color field may serve as a physical backing, folder, or structural anchor, but it must remain subordinate to the focal claim at thumbnail size.
- Use the primary high-chroma accent on the most important subject, evidence, brand cue, or action point.
- Reserve an optional secondary accent for tiny annotations, registration marks, or a specific contrasting reference; keep it sparse.
- Assign colors by role before generation. Do not confuse a contextual color mentioned in the story with the brand color of a supplied subject.
- These are hierarchy rules, not fixed swatches. Preserve user-supplied hexadecimal values and do not hardcode blue, yellow, or red into the preset.
- If a colored background or backing plane makes black-and-white information hard to read, reduce its area, saturation, or contrast before weakening the primary subject.

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
- Mix controlled hand-cut edges with a few visibly torn paper edges. Avoid making every sheet a perfect rectangle, but do not let aggressive tears destroy faces, text, or structural clarity.

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
