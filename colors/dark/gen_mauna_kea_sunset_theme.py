#!/usr/bin/env python3
"""Generate the 'Mauna Kea Sunset' theme — molten sunset over volcanic twilight.

Dark-mode Hawaiian palette: deep plum/indigo zenith for the background, warm
cream sand-glow text, and sunset accents (lava coral, papaya gold, orchid,
lagoon-at-dusk teal) drawn from the moments after the sun drops below the
cloud line at the Mauna Kea summit.
"""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Mauna Kea Sunset — sun has just dropped below the cloud line at the summit.
# Background: deep volcanic twilight at the zenith; faintly warm so it doesn't
# read as cold blue-black. Foreground: warm sand-glow cream lit by the last light.
BG            = color(26,  20,  40)    # twilight zenith
FG            = color(232, 212, 184)   # warm sand glow
BOLD          = color(245, 228, 200)   # cloud underside
CURSOR        = color(255, 122, 90)    # molten lava
SELECTION     = color(74,  50,  90)    # bruised violet

# ANSI — sunset over the islands
ANSI_BLACK    = color(42,  31,  56)    # cinder shadow
ANSI_RED      = color(232, 77,  95)    # hibiscus / lava glow
ANSI_GREEN    = color(127, 184, 122)   # palm at dusk
ANSI_YELLOW   = color(244, 184, 92)    # sunset gold
ANSI_BLUE     = color(94,  143, 181)   # twilight ocean
ANSI_MAGENTA  = color(199, 111, 160)   # orchid silhouette
ANSI_CYAN     = color(107, 184, 184)   # lagoon at dusk
ANSI_WHITE    = color(232, 212, 184)   # warm sand

BR_BLACK      = color(106, 84,  124)   # cinder dust
BR_RED        = color(255, 130, 134)   # sunset coral
BR_GREEN      = color(168, 216, 158)   # palm shoot lit
BR_YELLOW     = color(255, 208, 140)   # papaya glow
BR_BLUE       = color(138, 180, 214)   # sky between gold and plum
BR_MAGENTA    = color(232, 154, 196)   # pink hibiscus glow
BR_CYAN       = color(156, 216, 214)   # foam catching last light
BR_WHITE      = color(250, 235, 208)   # cloud crown

theme = {
    "name": "Mauna Kea Sunset",
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
out = script.parents[2] / "themes" / script.parent.name / "Mauna Kea Sunset.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
