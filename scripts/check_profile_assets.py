"""Offline profile asset checks. This does not validate external websites."""
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def main():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for name in ("profile-banner.svg", "profile-banner-mobile.svg"):
        asset = ROOT / "assets" / name
        assert asset.is_file(), f"Missing profile banner: {name}"
        root = ElementTree.parse(asset).getroot()
        assert root.tag.endswith("svg"), f"Invalid SVG: {name}"
        assert f'assets/{name}' in readme, f"Missing README reference: {name}"
    assert 'alt="Yatharth Goyal' in readme, "Profile image needs descriptive alt text"
    print("PASS: desktop and mobile banners parse as SVG and are referenced")


if __name__ == "__main__":
    main()
