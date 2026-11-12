"""Static SVG accessibility checks; no browser or external image hosting required."""
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


def validate_banner(path):
    svg = ElementTree.parse(path).getroot()
    assert svg.tag.endswith("svg"), f"{path.name}: not SVG"
    assert svg.get("role") == "img", f"{path.name}: missing image role"
    refs = set(svg.get("aria-labelledby", "").split())
    assert {"title", "desc"} <= refs, f"{path.name}: missing label references"
    elements = {
        element.get("id"): (element.text or "").strip()
        for element in svg.iter()
        if element.get("id") in {"title", "desc"}
    }
    assert elements.get("title"), f"{path.name}: missing accessible title"
    assert elements.get("desc"), f"{path.name}: missing accessible description"
    assert svg.get("viewBox"), f"{path.name}: missing responsive viewBox"


def main():
    for filename in ("profile-banner.svg", "profile-banner-mobile.svg"):
        validate_banner(ROOT / "assets" / filename)
    print("PASS: both GitHub profile banners expose title and description")


if __name__ == "__main__":
    main()
