# Riso Editorial Style

Use this preset when the user wants Riso, Risograph, screen-print, flat geometric ink, visible color registration, or a pop editorial print finish while retaining this Skill's layer-first storyboard workflow.

This preset borrows only reusable color, form, and print behavior. It does not require a complete poster redesign, a title, a stamp module, or a flattened one-pass render. Composition, text mode, layer granularity, approval, and delivery continue to follow `SKILL.md` and `references/layer-workflow.md`.

## Form

- Make every main object readable by optical mass first and internal detail second.
- Use one dominant silhouette plus one to five diagnostic features. Reduce hair, foliage, folds, seams, reflections, and repeated patterns to broad masses, one to three internal forms, or nothing.
- Preserve identity, count, action, relationship, setting function, and indispensable information. Simplification must not turn a specific subject into a generic icon.
- Use subject-specific curves, blunt angles, leaning axes, asymmetry, awkward proportion, crop, and overlap. Geometry organizes mass and hierarchy; it does not require boxes, rigid grids, or vector-smooth paths.
- Keep depth compressed but intelligible through overlap, enclosure, horizon strips, support planes, or scale relationships.

## Palette

Use neutral natural-white paper unless the user chooses another substrate. Do not default to cream, beige, sepia, yellowed, or aged paper.

Choose one palette recipe for the project and preserve it across all frames. Do not take one color from several recipes. Use two to four dominant simulated inks by default; this is a practical storyboard range, not a rule for physical Riso printing.

Representative planning palettes:

| Recipe | Ink roles |
|---|---|
| `electric-primary` | cobalt blue `#2455D6`, tomato red `#F04B23`, lemon yellow `#F4DF25`, natural white `#F4F0E6` |
| `botanical-clash` | grass green `#18A566`, warm orange `#F26A2E`, clear pink `#ED6FA8`, natural white `#F4F0E6` |
| `night-pop` | deep navy `#173B83`, cyan `#38BFD2`, lemon yellow `#F4DF25`, tomato red `#F04B23`, natural white `#F4F0E6` |
| `quiet-duotone` | choose one saturated warm or cool ink, one deep navy/green/charcoal ink, and natural white |

- Give color areas hierarchy: one large field, one or two medium masses, and smaller diagnostic marks.
- Prefer a clear warm/cool clash, complementary tension, or one discordant accent over several harmonious near-duplicates.
- Keep colors clean and separable. Use overprint only where two declared ink masses overlap.
- Avoid gradients and realistic light modeling. Tonal variation comes from ink density, halftone, or overprint.
- Keep black at or below roughly 25% of the canvas and target below 20% unless the user requests a dark print. Navy, deep green, brown, or saturated red may carry dark contrast instead.
- Preserve a source color only when it is identity-critical; otherwise the chosen ink recipe controls the rendering.

## Printed Edge and Junction System

- Major silhouettes have crisp, hard printed edges with visible broad low-frequency contour wobble. Wobble changes contour location, not sharpness.
- At major color junctions, vary narrow unequal gaps, exposed paper slivers, slight overlap, and small registration offsets. Do not use uniform outlines or equal wide gutters.
- Keep strong fields connected when hierarchy requires it; not every boundary needs a gap or offset.
- Do not add torn paper rims, pasted seams, drop shadows, paper curls, or floating-paper depth. Independent PNG layers may overlap in the composite without pretending to be separate physical scraps.

## Local Print Evidence

Keep most large fields clean. Before generation, name only a few structural zones where print evidence may concentrate:

- a halftone cluster inside one shadow or diagnostic form;
- a small registration drift at one or two color junctions;
- a localized uneven ink-density patch;
- a missing-ink rub or short drag aligned with the object's form;
- one intentional overprint intersection.

These marks support form and junctions. They never construct an object edge, replace anatomy, hide generic design, or become a global texture overlay.

## Prohibited Drift

- no watercolor, gouache, wet bleed, heavy dry brush, fuzzy pigment, or visible bristle direction;
- no polished vector smoothness, generic grain filter, uniform distress, or all-over halftone;
- no cut-paper craft, white sticker outline, pasted collage seam, contact shadow, curled paper, or 3D extrusion unless the user requests a hybrid style;
- no photographic microdetail retained under a Riso filter;
- no blurred contour wobble, equal gutters around every color, yellowed substrate, or black-dominant photocopy treatment;
- no invented title, stamp, pseudo-brand, watermark, or random glyphs.

## Project Record

Record the shared Riso decisions in `project.json`: palette recipe or explicit ink colors, paper substrate, black-area target, Riso intensity, and named local print zones. Reuse them across all frames unless the user approves a deliberate change.
