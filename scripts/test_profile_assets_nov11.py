"""Offline profile banner checks, independent of external image hosts."""
import unittest
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


class ProfileBannerTests(unittest.TestCase):
    def test_mobile_and_desktop_banners_are_svg(self):
        for filename in ("profile-banner.svg", "profile-banner-mobile.svg"):
            with self.subTest(filename=filename):
                path = ROOT / "assets" / filename
                self.assertTrue(path.is_file())
                parsed = ElementTree.parse(path)
                self.assertTrue(parsed.getroot().tag.endswith("svg"))

    def test_readme_references_both_local_banners(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("assets/profile-banner.svg", readme)
        self.assertIn("assets/profile-banner-mobile.svg", readme)


if __name__ == "__main__":
    unittest.main()
