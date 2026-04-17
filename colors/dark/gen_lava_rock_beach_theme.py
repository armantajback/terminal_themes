#!/usr/bin/env python3
"""Generate a 'Lava Rock Beach' macOS Terminal theme — black-sand shore under tropical stars.

Dark Hawaiian counterpart to the Hawaiian Beach palette: wet-basalt black sand
for the background, moonlit sea-foam cream for text, with bioluminescent
plankton cyan, torch-flame gold, and moonlit-hibiscus accents pulled from a
warm tropical night on a volcanic shore.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Lava Rock Beach — moonlit black-sand shore, bioluminescent surf at the waterline.
BG            = color(18,  14,  16)    # wet basalt
FG            = color(228, 218, 200)   # moonlit sea foam
BOLD          = color(245, 238, 222)   # bright foam
CURSOR        = color(126, 240, 220)   # plankton glow
SELECTION     = color(50,  36,  48)    # wet sand shadow

# ANSI — tropical night on a volcanic coast
ANSI_BLACK    = color(38,  30,  36)    # basalt
ANSI_RED      = color(220, 88,  92)    # hibiscus at midnight
ANSI_GREEN    = color(108, 180, 138)   # palm silhouette glow
ANSI_YELLOW   = color(232, 188, 110)   # torch flame
ANSI_BLUE     = color(98,  138, 188)   # deep night ocean
ANSI_MAGENTA  = color(196, 110, 168)   # orchid in moonlight
ANSI_CYAN     = color(126, 220, 218)   # bioluminescent foam
ANSI_WHITE    = color(228, 218, 200)   # moon foam

BR_BLACK      = color(96,  84,  92)    # driftwood ash
BR_RED        = color(244, 132, 130)   # coral ember
BR_GREEN      = color(150, 220, 168)   # phosphor green
BR_YELLOW     = color(248, 214, 140)   # fire glow
BR_BLUE       = color(140, 184, 220)   # starlit blue
BR_MAGENTA    = color(232, 158, 200)   # pink hibiscus moonlit
BR_CYAN       = color(170, 240, 232)   # cresting wave
BR_WHITE      = color(252, 246, 232)   # sea spray

theme = {
    "name": "Lava Rock Beach",
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
out = script.parents[2] / "themes" / script.parent.name / "Lava Rock Beach.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
