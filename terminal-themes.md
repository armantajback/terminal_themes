# Terminal Themes

Five macOS Terminal themes inspired by tropical beaches and floral palettes, plus the Python scripts that generated them.

## Files

| Theme file | Generator |
|---|---|
| `Hawaiian Beach.terminal` | `gen_hawaiian_theme.py` |
| `Fiji.terminal` | `gen_fiji_theme.py` |
| `Cottage Floral.terminal` | `gen_floral_theme.py` |
| `Moody Wildflower.terminal` | `gen_moody_wildflower_theme.py` |
| `Pastel Watercolor.terminal` | `gen_pastel_watercolor_theme.py` |

## Importing

Double-click a `.terminal` file. Then in **Terminal → Settings → Profiles**, select the profile and click **Default** to make it stick across new windows.

## Palettes

### Hawaiian Beach — sunny tropical
- **BG** warm sand `#FFF1D6` · **FG** palm green `#226634`
- Cursor: hibiscus red · Selection: sunset glow
- ANSI: monstera, plumeria/papaya, ocean blue, orchid, lagoon turquoise, seafoam

### Fiji — South Pacific lagoon (teal-forward)
- **BG** coral sand `#F7ECD8` · **FG** deep lagoon teal `#146C74`
- Cursor: coral · Selection: shallow tide
- Cyan slot leans hard into Fiji turquoise — bright/foamy
- ANSI: bright coral, mangrove, tagimoucia gold, deep ocean, bougainvillea, lagoon teal, bleached shell

### Cottage Floral — English garden
- **BG** magnolia cream `#FCF4EA` · **FG** stem green `#3A5C3A`
- Cursor: garden rose · Selection: rose petal
- ANSI: camellia, daffodil, forget-me-not, foxglove, hydrangea, alyssum

### Moody Wildflower — dusk meadow
- **BG** twilight plum `#1E1824` · **FG** moonlit sage `#A8BC9E`
- Cursor: dusty rose · Selection: bruised iris
- Dusky/saturated rather than bright: dried goldenrod, dusky poppy, thistle, cornflower-at-dusk

### Pastel Watercolor — soft paper wash
- **BG** paper wash `#FDF7F0` · **FG** dusty teal `#607C84`
- Cursor: wash of pink · Selection: rose bleed
- Pigments-on-cold-press feel: naples yellow, sap green wash, quinacridone lilac, cerulean wash

## Tweaking

Each generator is a self-contained script. The palette is a block of `color(r, g, b)` calls near the top — edit RGB values, then rerun:

```bash
/usr/bin/python3 ~/Desktop/gen_fiji_theme.py
```

The script writes the `.terminal` file to the Desktop. Re-import (or delete the old profile in Terminal first if the name collides).

### Requirements

The generators use PyObjC (`AppKit`, `Foundation`) to archive `NSColor` values in the format Terminal expects. If a fresh machine errors on import:

```bash
/usr/bin/python3 -m pip install --user pyobjc-framework-Cocoa
```

## Format notes

Each `.terminal` file is an XML plist. Color values are `NSKeyedArchiver`-archived `NSColor` blobs (sRGB), which is why a script is easier than hand-editing — Terminal won't accept plain hex strings in this slot.

Profile defaults set: 110 cols × 32 rows, option-as-meta on, show active process in title.
