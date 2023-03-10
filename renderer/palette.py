from dataclasses import dataclass

import tomllib

@dataclass
class Color:
    name: str
    light: str
    medium: str
    dark: str

@dataclass
class Palette:
    neutral: list[str]
    red: Color
    yellow: Color
    green: Color
    blue: Color
    purple: Color

def load_palette(file: str) -> Palette:
    with open (file, "rb") as f:
        p = tomllib.load(f)

    palette = Palette(
        neutral=p["neutrals"],
        red=Color(
            name="red",
            light=p["red"]["light"],
            medium=p["red"]["medium"],
            dark=p["red"]["dark"],
        ),
        yellow=Color(
            name="yellow",
            light=p["yellow"]["light"],
            medium=p["yellow"]["medium"],
            dark=p["yellow"]["dark"],
        ),
        green=Color(
            name="green",
            light=p["green"]["light"],
            medium=p["green"]["medium"],
            dark=p["green"]["dark"],
        ),
        blue=Color(
            name="blue",
            light=p["blue"]["light"],
            medium=p["blue"]["medium"],
            dark=p["blue"]["dark"],
        ),
        purple=Color(
            name="purple",
            light=p["purple"]["light"],
            medium=p["purple"]["medium"],
            dark=p["purple"]["dark"],
        ),
    )

    return palette

