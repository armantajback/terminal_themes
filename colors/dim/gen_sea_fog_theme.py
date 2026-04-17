#!/usr/bin/env python3
"""Generate a 'Sea Fog' macOS Terminal theme — Pacific morning fog over the tide-line.

Mid-tone (dim) palette: cool fog-grey background pulled toward warmth, warm
sea-spray cream text, with accents drawn from the things just barely visible
through coastal fog — kelp, lagoon mist, sea heather, sun trying to break
through. Easier on the eyes than a light theme but without the high-contrast
jolt of true dark.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Sea Fog — Pacific morning fog rolling over the tide-line.
BG            = color(92,  105, 115)   # fog under grey sky
FG            = color(228, 221, 201)   # warm sea-spray cream
BOLD          = color(244, 236, 216)   # bright spray
CURSOR        = color(232, 144, 112)   # sun trying to break through
SELECTION     = color(61,  71,  80)    # deeper fog

# ANSI — coastal palette, just barely visible through the mist
ANSI_BLACK    = color(58,  67,  76)    # deepest fog
ANSI_RED      = color(216, 120, 120)   # muted coral
ANSI_GREEN    = color(134, 178, 128)   # kelp
ANSI_YELLOW   = color(216, 176, 104)   # sun-through-fog gold
ANSI_BLUE     = color(112, 144, 180)   # deep ocean
ANSI_MAGENTA  = color(184, 136, 180)   # sea heather
ANSI_CYAN     = color(128, 180, 176)   # lagoon mist
ANSI_WHITE    = color(228, 221, 201)   # sea-spray cream

BR_BLACK      = color(122, 133, 144)   # fog grey
BR_RED        = color(240, 152, 152)   # bright coral
BR_GREEN      = color(168, 208, 152)   # fresh kelp
BR_YELLOW     = color(240, 204, 136)   # sunlit gold
BR_BLUE       = color(156, 184, 220)   # bright sea
BR_MAGENTA    = color(216, 168, 212)   # bright heather
BR_CYAN       = color(168, 216, 212)   # bright mist
BR_WHITE      = color(248, 242, 222)   # pale spray

theme = {
    "name": "Sea Fog",
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
out = script.parents[2] / "themes" / script.parent.name / "Sea Fog.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
