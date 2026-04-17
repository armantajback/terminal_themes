#!/usr/bin/env python3
"""Generate a 'Fiji' macOS Terminal theme — teal lagoon over warm sand."""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Fiji — South Pacific lagoon: warm coral sand background, deep teal text
# Background: soft warm sand, a touch cooler/lighter than Hawaiian
BG            = color(247, 236, 216)   # coral sand
# Foreground: deep lagoon teal — readable on sand
FG            = color(20,  108, 116)   # deep lagoon
BOLD          = color(8,   78,  88)    # reef shadow
CURSOR        = color(232, 112, 96)    # coral
SELECTION     = color(196, 228, 224)   # shallow tide

# ANSI — Fiji reef + flora
ANSI_BLACK    = color(46,  56,  60)    # wet basalt
ANSI_RED      = color(216, 84,  76)    # bright coral
ANSI_GREEN    = color(60,  140, 116)   # mangrove
ANSI_YELLOW   = color(232, 176, 84)    # tagimoucia gold
ANSI_BLUE     = color(28,  130, 168)   # deep ocean
ANSI_MAGENTA  = color(196, 96,  140)   # bougainvillea
ANSI_CYAN     = color(40,  176, 184)   # lagoon teal
ANSI_WHITE    = color(244, 232, 216)   # bleached shell

BR_BLACK      = color(96,  108, 112)   # driftwood grey
BR_RED        = color(240, 124, 116)   # sunset coral
BR_GREEN      = color(120, 192, 156)   # palm shoot
BR_YELLOW     = color(248, 208, 124)   # frangipani
BR_BLUE       = color(88,  176, 212)   # shallow blue
BR_MAGENTA    = color(228, 144, 184)   # pink hibiscus
BR_CYAN       = color(132, 220, 220)   # turquoise foam
BR_WHITE      = color(254, 248, 236)   # white sand

theme = {
    "name": "Fiji",
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
out = script.parents[2] / "themes" / script.parent.name / "Fiji.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
