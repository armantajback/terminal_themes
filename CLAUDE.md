# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A small collection of macOS Terminal.app color themes and the standalone Python generators that produce them. Both folders are bucketed by mode (three tiers):

- `themes/light/`, `themes/dim/`, `themes/dark/` — the `.terminal` plist files you import into Terminal.app
- `colors/light/`, `colors/dim/`, `colors/dark/` — one `gen_*_theme.py` per theme; each is self-contained and rebuilds its `.terminal` file
- `preview.py` — top-level previewer that renders each palette using 24-bit ANSI escapes (parses RGB tuples directly out of the generators, so palettes stay the single source of truth)

`dim` is mid-tone (~100–130 luma backgrounds): lower-glare than light themes without the high-contrast jolt of true dark — fog-grey, olive-shadow, clay-rust kinds of backgrounds. The bucket a generator lives in determines its output bucket — see "Regenerating" below. To reclassify a theme, just `mv` the generator (and its `.terminal`) between buckets. No build system, no tests, no package.

## Regenerating a theme

```bash
/usr/bin/python3 colors/light/gen_fiji_theme.py
```

Use the system Python at `/usr/bin/python3` — the scripts depend on PyObjC (`AppKit`, `Foundation`), which ships with macOS's bundled Python. If missing on a fresh machine: `/usr/bin/python3 -m pip install --user pyobjc-framework-Cocoa`.

Each generator computes its output path from its own location:

```python
script = Path(__file__).resolve()
out = script.parents[2] / "themes" / script.parent.name / "<Name>.terminal"
```

So `colors/<bucket>/gen_X.py` → `themes/<bucket>/X.terminal` for any of the three buckets. Output is independent of CWD and auto-mirrors whichever bucket the script lives in.

## Previewing

```bash
/usr/bin/python3 preview.py
```

Renders each theme as a Claude-Code-style panel (bullet items, `Write(...)` tool call, dimmed line-numbered code block with keyword/string/number/comment colors, `… +N lines (ctrl+o to expand)` hint, ✓/▣/☐ checkbox list, divider, `>` prompt, status bar with a highlighted pill) followed by the 16 ANSI swatches in two rows. Everything is drawn with 24-bit truecolor escapes, so colors show correctly regardless of which theme your terminal is currently using. Press Enter to advance, Ctrl-C to quit.

The previewer auto-discovers `colors/*/gen_*_theme.py` (one level deep), sorts in `light → dim → dark` order, and tags each banner with its bucket (`━━━ Fiji  ·  light ━━━`). It regex-parses lines like `BG = color(247, 236, 216)` out of each generator; if you rename a palette variable, update `PALETTE_KEYS` in `preview.py`. The first-line tagline shown under each banner is whatever follows ` — ` in the generator's module docstring. To restyle a sample row, edit `sample_rows()` — each row is a list of `(text, fg_key)` or `(text, fg_key, bg_key)` tuples, where keys are `fg`/`bg`/`bold`/`dim`/`auto`/`ansi:<name>`/`br:<name>` and `auto` picks black or white based on the bg's luminance (used for the pill).

## Why a script instead of editing the plist

Color values in a `.terminal` file are not hex strings — they are `NSKeyedArchiver`-archived `NSColor` blobs (sRGB) embedded as base64 `<data>` in the XML plist. Terminal.app rejects plain hex in those slots. The `color(r, g, b)` helper at the top of each script is the only sane way to produce a valid blob; hand-editing the XML will not work.

## Generator structure (shared across all generators)

Every `gen_*_theme.py` follows the same shape:
1. `color(r, g, b)` — wraps `NSColor.colorWithSRGBRed_green_blue_alpha_` + `NSKeyedArchiver`.
2. A palette block: `BG`, `FG`, `BOLD`, `CURSOR`, `SELECTION`, then 8 `ANSI_*` + 8 `BR_*` (bright) slots. **Edit RGB tuples here to retune a theme.**
3. A `theme` dict assembling those into the plist keys Terminal expects (`BackgroundColor`, `ANSIRedColor`, `ANSIBrightRedColor`, …) plus profile defaults (`columnCount: 110`, `rowCount: 32`, `useOptionAsMetaKey: True`, `ShowActiveProcessInTitle: True`).
4. `plistlib.dump(theme, f, fmt=plistlib.FMT_XML)` to write.

When adding a new theme, copy an existing generator into the appropriate `colors/{light,dim,dark}/` bucket, then swap the palette + the `name` field + the output filename in the `out =` line. The bucket folder name is reused as the `themes/` subdir, so don't hardcode the bucket name anywhere — let `script.parent.name` derive it. Keep the profile defaults consistent unless there's a reason to diverge.

The first-line module docstring should follow `"""Generate the 'X' theme — short tagline."""` because `preview.py` extracts the part after ` — ` and shows it under the banner.

## Installing a theme

Double-click the `.terminal` file, then in **Terminal → Settings → Profiles** select it and click **Default**. If you're re-importing after a regen and the name collides, delete the old profile first.
