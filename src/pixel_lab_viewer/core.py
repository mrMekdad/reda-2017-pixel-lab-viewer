"""Core workflow for Pixel Lab Viewer by Red@."""

PROJECT_NAME = "Pixel Lab Viewer"
DOMAIN_THEME = "image tooling"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
