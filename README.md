# Terminal Themes

> Arman did not write this readme, claude did. Arman just gave it inspiration and gaurdrails for the themes. He is not responsible for claude's attempts and inducing AI psychosis.

13 macOS Terminal themes plus the Python scripts that build them. Three buckets — light, dim (mid-tone), dark.

## Themes

### Light

| Preview | Theme |
|---|---|
| ![Fiji](screenshots/light/Fiji.png) | **Fiji** — teal lagoon over warm sand |
| ![Cottage Floral](screenshots/light/Cottage%20Floral.png) | **Cottage Floral** — English garden blooms over magnolia cream |
| ![Hawaiian Beach](screenshots/light/Hawaiian%20Beach.png) | **Hawaiian Beach** — sunny tropical, palm green over warm sand |
| ![Pastel Watercolor](screenshots/light/Pastel%20Watercolor.png) | **Pastel Watercolor** — soft washed blooms |
| ![Pink Wisteria](screenshots/light/Pink%20Wisteria.png) | **Pink Wisteria** — cascading blossoms in dappled sun |

### Dim

Mid-tone backgrounds — easier on the eyes than light, not as dark as dark.

| Preview | Theme |
|---|---|
| ![Olive Grove Noon](screenshots/dim/Olive%20Grove%20Noon.png) | **Olive Grove Noon** — silvery sage in Mediterranean midday |
| ![Sea Fog](screenshots/dim/Sea%20Fog.png) | **Sea Fog** — Pacific morning fog over the tide-line |
| ![Terracotta Tile](screenshots/dim/Terracotta%20Tile.png) | **Terracotta Tile** — sun-warmed clay in a Mediterranean alley |

### Dark

Warm dark backgrounds — no cold blue-blacks.

| Preview | Theme |
|---|---|
| ![Lava Rock Beach](screenshots/dark/Lava%20Rock%20Beach.png) | **Lava Rock Beach** — black-sand shore under tropical stars |
| ![Mauna Kea Sunset](screenshots/dark/Mauna%20Kea%20Sunset.png) | **Mauna Kea Sunset** — molten sunset over volcanic twilight |
| ![Moody Wildflower](screenshots/dark/Moody%20Wildflower.png) | **Moody Wildflower** — dusk meadow palette |
| ![Redwood Nightfall](screenshots/dark/Redwood%20Nightfall.png) | **Redwood Nightfall** — coastal redwood grove at dusk |
| ![Velvet Garden](screenshots/dark/Velvet%20Garden.png) | **Velvet Garden** — English walled garden at dusk, lantern-lit |

## Install

Double-click a `.terminal` file in `themes/<bucket>/`. In **Terminal → Settings → Profiles**, select the new profile and click **Default**. If a re-import collides with an existing profile of the same name, delete the old one first.

## Preview themes in your terminal

```bash
/usr/bin/python3 preview.py
```

Steps through every theme using truecolor escapes, so colors render correctly no matter which theme your terminal is currently using. Press Enter to advance, Ctrl-C to quit.

## Edit a palette

Each `colors/<bucket>/gen_*_theme.py` is one self-contained file. The palette is a block of `color(r, g, b)` calls near the top — change the RGB values and rerun:

```bash
/usr/bin/python3 colors/light/gen_fiji_theme.py
```

The `.terminal` file rebuilds in `themes/<same-bucket>/`. Re-import in Terminal.

## Rebuild screenshots

```bash
/usr/bin/python3 gen_screenshots.py
```

## Add a new theme

1. Pick a bucket — `light`, `dim`, or `dark`
2. Copy any existing generator into `colors/<bucket>/` and rename it
3. Change the palette tuples, the `name` field, and the filename in `out =`
4. Update the docstring's first line — the part after ` — ` shows up as the tagline in `preview.py`
5. Run the generator, then `gen_screenshots.py`

## Layout

```
themes/{light,dim,dark}/   *.terminal
colors/{light,dim,dark}/   gen_*_theme.py
screenshots/{light,dim,dark}/   *.png
preview.py
gen_screenshots.py
```

The bucket folder name decides where a generator's `.terminal` file lands. To move a theme between buckets, `mv` the generator (and the `.terminal`) and rerun.

## Why a script instead of editing the .terminal file directly

Color values inside a `.terminal` file aren't hex strings — they're `NSKeyedArchiver`-archived `NSColor` blobs (sRGB), embedded as base64 in the XML. Terminal.app rejects plain hex in those slots, so hand-editing the XML doesn't work. The `color(r, g, b)` helper at the top of each generator is what builds a valid blob.

## Requirements

System Python at `/usr/bin/python3` with PyObjC (ships with macOS) and Pillow (only needed by `gen_screenshots.py`):

```bash
/usr/bin/python3 -m pip install --user pyobjc-framework-Cocoa pillow
```
