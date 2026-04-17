#!/usr/bin/env python3
"""Generate a 'Hawaiian Beach' macOS Terminal theme — sunny tropical, palm green over warm sand."""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    """Build an archived NSColor (sRGB) blob for a .terminal plist."""
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    data = NSKeyedArchiver.archivedDataWithRootObject_(c)
    return bytes(data)


# Hawaiian beach / floral palette
# Background: warm sandy off-white with yellow-orange tint
BG            = color(255, 241, 214)   # sunlit sand
# Foreground: lush palm / tropical leaf green
FG            = color(34,  102, 52)    # palm leaf
BOLD          = color(20,  78,  40)    # darker fern
CURSOR        = color(214, 40,  70)    # hibiscus
SELECTION     = color(255, 218, 160)   # sunset glow

# ANSI (floral + beach inspired)
ANSI_BLACK    = color(52,  40,  30)    # volcanic rock
ANSI_RED      = color(214, 40,  70)    # hibiscus red
ANSI_GREEN    = color(58,  138, 67)    # monstera green
ANSI_YELLOW   = color(244, 162, 97)    # plumeria / papaya
ANSI_BLUE     = color(0,   119, 182)   # ocean blue
ANSI_MAGENTA  = color(199, 62,  148)   # orchid
ANSI_CYAN     = color(0,   180, 216)   # lagoon turquoise
ANSI_WHITE    = color(248, 237, 227)   # seafoam

BR_BLACK      = color(110, 94,  78)    # driftwood
BR_RED        = color(247, 94,  110)   # bougainvillea
BR_GREEN      = color(110, 181, 108)   # new fern
BR_YELLOW     = color(255, 195, 113)   # pineapple
BR_BLUE       = color(72,  166, 224)   # shallow water
BR_MAGENTA    = color(232, 121, 184)   # pink plumeria
BR_CYAN       = color(144, 224, 239)   # sea glass
BR_WHITE      = color(255, 250, 240)   # coral sand

theme = {
    "name": "Hawaiian Beach",
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
out = script.parents[2] / "themes" / script.parent.name / "Hawaiian Beach.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
