from renderer.palette import load_palette
from renderer.targets.zellij import render_zellij

PALETTE_FILE = "palette.toml"

def main():
    palette = load_palette(PALETTE_FILE)
    save_zellij = render_zellij(palette)
    save_zellij()

if __name__ == "__main__":
    main()
