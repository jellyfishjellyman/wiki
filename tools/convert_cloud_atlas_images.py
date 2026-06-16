from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
IMG_DIR = ROOT / "docs" / "assets" / "images" / "clouds" / "china-cloud-atlas"
MD_DIR = ROOT / "docs" / "clouds" / "china-cloud-atlas"


def convert_images() -> None:
    for png in sorted(IMG_DIR.glob("page-*.png")):
        webp = png.with_suffix(".webp")
        if webp.exists() and webp.stat().st_mtime >= png.stat().st_mtime:
            continue
        with Image.open(png) as image:
            image.save(webp, "WEBP", quality=82, method=6)


def rewrite_markdown_links() -> None:
    for md in sorted(MD_DIR.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        updated = text.replace(".png)", ".webp)")
        if updated != text:
            md.write_text(updated, encoding="utf-8")


def main() -> None:
    convert_images()
    rewrite_markdown_links()


if __name__ == "__main__":
    main()
