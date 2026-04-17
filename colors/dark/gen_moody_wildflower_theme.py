#!/usr/bin/env python3
"""Generate a 'Moody Wildflower' macOS Terminal theme — dusk meadow palette."""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Moody wildflower — twilight meadow, dusty blooms against deep plum sky
# Background: deep twilight plum, just warm enough to feel earthy not cold
BG            = color(30,  24,  36)    # twilight plum
# Foreground: moonlit sage — readable but soft, like leaves at dusk
FG            = color(168, 188, 158)   # moonlit sage
BOLD          = color(204, 220, 196)   # silvered fern
CURSOR        = color(214, 124, 138)   # dusty rose
SELECTION     = color(70,  54,  82)    # bruised iris

# ANSI — wildflowers seen at dusk, all dusty + saturated rather than bright
ANSI_BLACK    = color(48,  40,  56)    # storm shadow
ANSI_RED      = color(184, 88,  96)    # dusky poppy
ANSI_GREEN    = color(124, 154, 110)   # meadow leaf
ANSI_YELLOW   = color(204, 168, 100)   # dried goldenrod
ANSI_BLUE     = color(112, 132, 178)   # cornflower at dusk
ANSI_MAGENTA  = color(168, 108, 168)   # thistle bloom
ANSI_CYAN     = color(124, 168, 174)   # foggy chicory
ANSI_WHITE    = color(214, 204, 196)   # bone moonlight

BR_BLACK      = color(96,  82,  108)   # heather stem
BR_RED        = color(220, 124, 132)   # wild bergamot
BR_GREEN      = color(168, 198, 142)   # young yarrow
BR_YELLOW     = color(232, 200, 132)   # evening primrose
BR_BLUE       = color(160, 178, 220)   # moon harebell
BR_MAGENTA    = color(212, 156, 212)   # fading foxglove
BR_CYAN       = color(170, 212, 216)   # mist on water
BR_WHITE      = color(244, 236, 228)   # pale moon

theme = {
    "name": "Moody Wildflower",
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
out = script.parents[2] / "themes" / script.parent.name / "Moody Wildflower.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
