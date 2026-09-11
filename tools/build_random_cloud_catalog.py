from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "docs" / "clouds" / "china-cloud-atlas"
PLATES = ATLAS / "plates"
OUTPUT = ROOT / "docs" / "assets" / "registry" / "random-clouds.json"


def fields_from(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for match in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|$", block, re.M):
        key, value = match.group(1).strip(), match.group(2).strip()
        if key not in {"字段", "---"}:
            fields[key] = value
    return fields


def first_paragraph(block: str) -> str:
    lines: list[str] = []
    in_table = False
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("|"):
            in_table = True
            continue
        if in_table and not stripped:
            in_table = False
            continue
        if not stripped or stripped.startswith(("![", "#", ">", "!!!")):
            continue
        if not in_table:
            lines.append(stripped)
    text = re.sub(r"\s+", " ", " ".join(lines)).strip()
    return text or "暂无图注摘要，打开原图版页查看完整资料。"


def page_title(text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else fallback


def build() -> list[dict[str, str | int]]:
    entries: list[dict[str, str | int]] = []
    for path in sorted(PLATES.glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        title = page_title(text, path.stem)
        figures = list(re.finditer(r"^###\s+图\s*(\d+)：(.+)$", text, re.M))
        for index, figure in enumerate(figures):
            end = figures[index + 1].start() if index + 1 < len(figures) else len(text)
            block = text[figure.end() : end]
            fields = fields_from(block)
            image_match = re.search(r"page-(\d+)\.webp", block)
            if not image_match:
                continue
            number = int(figure.group(1))
            image_page = int(image_match.group(1))
            cloud_title = figure.group(2).strip()
            code = fields.get("云类代码", "待校订")
            place = fields.get("拍摄地点", fields.get("飞行高度", "原页未列出"))
            time = fields.get("拍摄时间", "原页未列出")
            direction = fields.get("拍摄方向", "原页未列出")
            summary = first_paragraph(block)
            entries.append(
                {
                    "number": f"图 {number}",
                    "numberValue": number,
                    "title": cloud_title,
                    "code": code,
                    "category": title,
                    "image": f"../../assets/images/clouds/china-cloud-atlas/page-{image_page:03d}.webp",
                    "location": place,
                    "time": time,
                    "direction": direction,
                    "summary": summary,
                    "origin": f"该图属于《中国云图》的“{title}”图版，具体形态和环境线索见图注。",
                    "features": summary,
                    "classification": f"本照片归入《中国云图》{title}，图号为图 {number}。",
                    "source": f"../china-cloud-atlas/plates/{path.stem}/",
                }
            )
    entries.sort(key=lambda item: int(item["numberValue"]))
    if len(entries) != len({item["numberValue"] for item in entries}):
        raise SystemExit("duplicate figure numbers found")
    if [item["numberValue"] for item in entries] != list(range(2, 281)):
        raise SystemExit("random catalog must cover figures 2-280")
    return entries


def main() -> None:
    entries = build()
    OUTPUT.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"random_cloud_entries={len(entries)}")


if __name__ == "__main__":
    main()
