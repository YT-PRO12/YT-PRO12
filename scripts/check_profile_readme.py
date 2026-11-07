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
    assert 'src="assets/profile-banner.svg"' in content
    assert 'alt="Yatharth Goyal' in content
    print(f"PASS: profile includes {len(expected)} expected links and banner alt text")


if __name__ == "__main__":
    main()
