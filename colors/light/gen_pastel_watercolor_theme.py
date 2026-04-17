#!/usr/bin/env python3
"""Generate a 'Pastel Watercolor' macOS Terminal theme — soft washed blooms."""
import plistlib
from AppKit import NSColor
from Foundation import NSKeyedArchiver
from pathlib import Path


def color(r, g, b):
    c = NSColor.colorWithSRGBRed_green_blue_alpha_(r / 255.0, g / 255.0, b / 255.0, 1.0)
    return bytes(NSKeyedArchiver.archivedDataWithRootObject_(c))


# Pastel watercolor — like blooms painted on cold-press paper
# Background: warmest paper white with the faintest peach wash
BG            = color(253, 247, 240)   # paper wash
# Foreground: dusty teal — soft but legible against paper
FG            = color(96,  124, 132)   # dusty teal
BOLD          = color(72,  98,  108)   # deeper wash
CURSOR        = color(232, 152, 168)   # wash of pink
SELECTION     = color(244, 224, 232)   # bleed of rose

# ANSI — pastel garden, watercolor pigments diluted on the brush
ANSI_BLACK    = color(108, 100, 116)   # graphite mauve
ANSI_RED      = color(232, 144, 156)   # rose madder dilute
ANSI_GREEN    = color(168, 200, 156)   # sap green wash
ANSI_YELLOW   = color(244, 212, 144)   # naples yellow
ANSI_BLUE     = color(168, 192, 220)   # cerulean wash
ANSI_MAGENTA  = color(216, 168, 212)   # quinacridone lilac
ANSI_CYAN     = color(176, 216, 216)   # phthalo turquoise dilute
ANSI_WHITE    = color(244, 236, 228)   # cool paper

BR_BLACK      = color(150, 142, 158)   # silvered pencil
BR_RED        = color(248, 184, 188)   # blush bloom
BR_GREEN      = color(196, 224, 184)   # spring leaf wash
BR_YELLOW     = color(252, 232, 180)   # primrose wash
BR_BLUE       = color(204, 220, 240)   # sky after rain
BR_MAGENTA    = color(236, 204, 232)   # lilac petal
BR_CYAN       = color(212, 236, 232)   # sea-glass wash
BR_WHITE      = color(255, 252, 248)   # bare paper

theme = {
    "name": "Pastel Watercolor",
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
out = script.parents[2] / "themes" / script.parent.name / "Pastel Watercolor.terminal"
with out.open("wb") as f:
    plistlib.dump(theme, f, fmt=plistlib.FMT_XML)

print(f"Wrote {out}")
