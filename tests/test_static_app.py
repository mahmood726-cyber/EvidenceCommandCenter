from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_command_center_shell_contains_required_sections():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    required = [
        "<title>Evidence Intelligence Suite",
        'id="ecc-nav"',
        'id="ecc-hero"',
        'id="ecc-projects-grid"',
        'id="ecc-numbers-section"',
        'id="ecc-hamburger"',
    ]
    missing = [marker for marker in required if marker not in html]
    assert missing == []


def test_project_cards_and_scripts_are_present():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    assert html.count("ecc-project-card") >= 8
    assert "setInterval(function()" in html
    assert "IntersectionObserver" in html
    assert "{{" not in html
    assert "TODO" not in html
