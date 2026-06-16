from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "cloud" / "中国云图【作 者】中国气象局.pdf"
TMP = ROOT / "tmp" / "pdfs" / "china-cloud-atlas"
OUT = ROOT / "docs" / "clouds" / "china-cloud-atlas"
IMG_OUT = ROOT / "docs" / "assets" / "images" / "clouds" / "china-cloud-atlas"

PDFTOPPM = Path(r"D:\Program\poppler-25.12.0\Library\bin\pdftoppm.exe")
TESSERACT = Path(r"D:\Program\Tesseract\tesseract.exe")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def render_page(page: int, dpi: int) -> Path:
    raw_dir = TMP / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    prefix = raw_dir / f"page-{page:03d}"
    expected = raw_dir / f"page-{page:03d}-{page:03d}.png"
    if not expected.exists():
        run(
            [
                str(PDFTOPPM),
                "-f",
                str(page),
                "-l",
                str(page),
                "-r",
                str(dpi),
                "-png",
                str(PDF),
                str(prefix),
            ]
        )
    return expected


def rotate_page(raw: Path, page: int) -> Path:
    rotated_dir = TMP / "rotated"
    rotated_dir.mkdir(parents=True, exist_ok=True)
    out = rotated_dir / f"page-{page:03d}.png"
    if not out.exists():
        image = Image.open(raw)
        # The book pages are stored sideways in the PDF. Rotating 270 degrees
        # makes captions and metadata horizontal for OCR and web reading.
        image.rotate(270, expand=True).save(out)
    return out


def ocr_page(image: Path, page: int, psm: int) -> Path:
    ocr_dir = TMP / "ocr"
    ocr_dir.mkdir(parents=True, exist_ok=True)
    out_base = ocr_dir / f"page-{page:03d}"
    out_txt = out_base.with_suffix(".txt")
    if not out_txt.exists():
        run(
            [
                str(TESSERACT),
                str(image),
                str(out_base),
                "-l",
                "chi_sim+eng",
                "--psm",
                str(psm),
                "txt",
            ]
        )
    return out_txt


def publish_image(image: Path, page: int) -> Path:
    IMG_OUT.mkdir(parents=True, exist_ok=True)
    out = IMG_OUT / f"page-{page:03d}.png"
    if not out.exists():
        Image.open(image).save(out, optimize=True)
    return out


def clean_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def parse_fields(text: str) -> dict[str, str]:
    compact = re.sub(r"[ \t]+", " ", text)
    fields: dict[str, str] = {}

    fig = re.search(r"图\s*(\d+)", compact)
    if fig:
        fields["figure"] = f"图 {fig.group(1)}"

    code = re.search(r"\b(C[ilrntusabop0-9.]{1,6}|A[sc][a-z0-9.]{0,5}|N[is][a-z0-9.]{0,5})\b", compact)
    if code:
        fields["code"] = code.group(1).replace("0", "o")

    for label, key in [
        ("拍摄地点", "location"),
        ("拍摄时间", "time"),
        ("拍摄方向", "direction"),
        ("拍 摄 者", "photographer"),
        ("拍摄者", "photographer"),
    ]:
        pattern = rf"{label}\s*[:：]?\s*([^\n]+)"
        m = re.search(pattern, text)
        if m:
            fields[key] = m.group(1).strip()

    return fields


def page_markdown(page: int, image_rel: str, text: str) -> str:
    fields = parse_fields(text)
    title = fields.get("figure", f"PDF 第 {page} 页")
    heading = title
    if fields.get("code"):
        heading += f" - {fields['code']}"

    lines = [f"## {heading}", "", f"![{title}]({image_rel})", ""]

    if fields:
        lines.extend(["| 字段 | 内容 |", "| --- | --- |"])
        for key, label in [
            ("figure", "图号"),
            ("code", "云类代码"),
            ("location", "拍摄地点"),
            ("time", "拍摄时间"),
            ("direction", "拍摄方向"),
            ("photographer", "拍摄者"),
        ]:
            if key in fields:
                lines.append(f"| {label} | {fields[key]} |")
        lines.append("")

    if text:
        lines.extend(["### OCR 文本", "", "```text", text, "```", ""])
    else:
        lines.extend(["!!! note \"OCR 状态\"", "    本页暂未识别出可靠文本，保留原页图像。", ""])

    return "\n".join(lines)


def write_section(start: int, end: int) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    section = OUT / f"pages-{start:03d}-{end:03d}.md"
    chunks = [
        f"# 《中国云图》PDF 第 {start}-{end} 页",
        "",
        "本页由扫描版 PDF 自动提取生成。每个条目保留原页图像，并附 OCR 文本供检索和后续校订。",
        "",
    ]

    for page in range(start, end + 1):
        raw = render_page(page, dpi=300)
        rotated = rotate_page(raw, page)
        txt_path = ocr_page(rotated, page, psm=3)
        text = clean_text(txt_path.read_text(encoding="utf-8", errors="ignore"))
        image = publish_image(rotated, page)
        rel = Path("..") / ".." / "assets" / "images" / "clouds" / "china-cloud-atlas" / image.name
        chunks.append(page_markdown(page, rel.as_posix(), text))

    section.write_text("\n".join(chunks), encoding="utf-8")


def write_index(total_pages: int) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    sections = sorted(OUT.glob("pages-*.md"))
    lines = [
        "# 中国云图",
        "",
        "来源文件：`cloud/中国云图【作 者】中国气象局.pdf`。",
        "",
        f"页数：{total_pages} 页。",
        "",
        "处理说明：该 PDF 为扫描图像型文件，已按页保留旋转校正后的原图，并使用 Tesseract OCR 生成可检索文本。OCR 文本需要后续人工校订，原图作为主要事实依据。",
        "",
        "## 分卷页面",
        "",
    ]
    for section in sections:
        label = section.stem.replace("pages-", "第 ").replace("-", "-") + " 页"
        lines.append(f"- [{label}]({section.name})")
    lines.append("")
    (OUT / "index.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--total-pages", type=int, default=314)
    args = parser.parse_args()
    write_section(args.start, args.end)
    write_index(args.total_pages)


if __name__ == "__main__":
    main()
