"""Static checks for the public GitHub profile, without network requests."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    content = (ROOT / "README.md").read_text(encoding="utf-8")
    expected = {
        "official resume": "https://yatharth-engineering-portfolio.vercel.app/resume/Yatharth_Goyal_Resume.pdf",
        "portfolio": "https://yatharth-engineering-portfolio.vercel.app/",
        "AegisED": "https://github.com/YT-PRO12/AegisED",
        "MERN": "https://github.com/YT-PRO12/MERN-Full-Stack-Engineering.",
        "Grid Flex": "https://github.com/YT-PRO12/Grid-Flex",
        "EduPredict AI": "https://github.com/YT-PRO12/EduPredictAI",
    }
    for label, link in expected.items():
        assert link in content, f"Missing {label} link: {link}"
    for anchor, heading in (
        ("#selected-projects", "## Selected projects"),
        ("#engineering-toolkit", "## Engineering toolkit"),
    ):
        assert f'href="{anchor}"' in content, f"Missing navigation: {anchor}"
        assert heading in content, f"Broken navigation target: {heading}"
    assert content.count("https://yatharth-engineering-portfolio.vercel.app/resume/Yatharth_Goyal_Resume.pdf") >= 2
    for section in ("## Selected projects", "## Engineering toolkit", "## Foundations I keep building"):
        assert section in content, f"Missing profile section: {section}"
    for anchor, section in (
        ("#selected-projects", "## Selected projects"),
        ("#engineering-toolkit", "## Engineering toolkit"),
    ):
        assert f'href="{anchor}"' in content, f"Broken navigation link: {anchor}"
        assert section in content, f"Missing navigation destination: {section}"
    assert 'src="assets/profile-banner.svg"' in content
    assert 'alt="Yatharth Goyal' in content
    print(f"PASS: profile includes {len(expected)} expected links and banner alt text")


if __name__ == "__main__":
    main()
