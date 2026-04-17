#!/usr/bin/env python3
"""Generate a 'Redwood Nightfall' macOS Terminal theme — coastal redwood grove at dusk.

Warm dark palette pulled from a Northern California redwood grove right after
sunset: deep wet-bark brown for the background, fern-cream text, and accents
drawn from sequoia rust, redwood-sorrel green, lupine purple, fog-blue twilight,
and the last bands of orange light caught in the high canopy.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Redwood Nightfall — wet bark and fern at the bottom of the canopy after sunset.
BG            = color(28,  20,  18)    # wet redwood bark
FG            = color(220, 208, 178)   # fern-cream
BOLD          = color(240, 228, 198)   # bright sword-fern
CURSOR        = color(232, 116, 76)    # sequoia rust
SELECTION     = color(54,  38,  34)    # bark shadow

# ANSI — grove understory at dusk
ANSI_BLACK    = color(42,  30,  26)    # damp duff
ANSI_RED      = color(208, 92,  76)    # sequoia rust
ANSI_GREEN    = color(132, 168, 96)    # redwood sorrel
ANSI_YELLOW   = color(232, 176, 88)    # last-light canopy
ANSI_BLUE     = color(108, 144, 184)   # fog-blue twilight
ANSI_MAGENTA  = color(168, 116, 184)   # lupine
ANSI_CYAN     = color(124, 184, 168)   # creek-moss
ANSI_WHITE    = color(220, 208, 178)   # fern-cream

BR_BLACK      = color(112, 88,  76)    # ash bark
BR_RED        = color(240, 132, 108)   # warm ember
BR_GREEN      = color(180, 212, 132)   # fresh sorrel
BR_YELLOW     = color(248, 212, 124)   # gold-leaf canopy
BR_BLUE       = color(160, 192, 220)   # pale fog
BR_MAGENTA    = color(212, 160, 220)   # pale lupine
BR_CYAN       = color(168, 216, 200)   # mossy mist
BR_WHITE      = color(248, 240, 216)   # moon through fog

theme = {
    "name": "Redwood Nightfall",
    "type": "Window Settings",
    "ProfileCurrentVersion": 2.07,
    "BackgroundColor": BG,
    "TextColor": FG,
    "TextBoldColor": BOLD,
    "CursorColor": CURSOR,
    "SelectionColor": SELECTION,
    "ANSIBlackColor":         ANSI_BLACK,
    "ANSIRedColor":           ANSI_RED,
    "ANSIGreenColor":         ANSI_GREEN,
    "ANSIYellowColor":        ANSI_YELLOW,
    "ANSIBlueColor":          ANSI_BLUE,
    "ANSIMagentaColor":       ANSI_MAGENTA,
    "ANSICyanColor":          ANSI_CYAN,
    "ANSIWhiteColor":         ANSI_WHITE,
    "ANSIBrightBlackColor":   BR_BLACK,
    "ANSIBrightRedColor":     BR_RED,
    "ANSIBrightGreenColor":   BR_GREEN,
    "ANSIBrightYellowColor":  BR_YELLOW,
    "ANSIBrightBlueColor":    BR_BLUE,
    "ANSIBrightMagentaColor": BR_MAGENTA,
    "ANSIBrightCyanColor":    BR_CYAN,
    "ANSIBrightWhiteColor":   BR_WHITE,
    "columnCount": 110,
    "rowCount": 32,
    "useOptionAsMetaKey": True,
    "ShowWindowSettingsNameInTitle": False,
    "ShowActiveProcessInTitle": True,
    "ShowShellCommandInTitle": True,
}

script = Path(__file__).resolve()
out = script.parents[2] / "themes" / script.parent.name / "Redwood Nightfall.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
