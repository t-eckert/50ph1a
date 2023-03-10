from renderer.palette import Palette

def render_zellij(palette: Palette) -> callable:
    compiled = f""""50PH1A" {{
    fg "{palette.neutral[0]}"
    bg "{palette.neutral[9]}"
    black "{palette.neutral[9]}"
    red "{palette.red.dark}"
    green "{palette.green.dark}"
    yellow "{palette.yellow.dark}"
    blue "{palette.blue.dark}"
    magenta "{palette.purple.dark}"
    cyan "{palette.blue.medium}"
    white "{palette.neutral[0]}"
    orange "{palette.yellow.medium}"
}}"""

    def save_zellij() -> None:
        with open("zellij/50PH1A.kdl", "w") as f:
            f.write(compiled)

    return save_zellij

