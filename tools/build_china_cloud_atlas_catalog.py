from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "docs" / "clouds" / "china-cloud-atlas"
PLATES = ATLAS / "plates"
CATALOG = ATLAS / "plate-catalog.md"


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def escape_table(value: str) -> str:
    return normalize_space(value).replace("|", r"\|")


def extract_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for match in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", block, re.M):
        key = match.group(1).strip()
        value = match.group(2).strip()
        if key in {"---", "字段"} or value == "内容":
            continue
        fields[key] = value
    return fields


def extract_description(block: str, limit: int = 76) -> str:
    lines: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if (
            not stripped
            or stripped.startswith("![")
            or stripped.startswith("|")
            or stripped.startswith("##")
            or stripped.startswith("!!!")
        ):
            continue
        lines.append(stripped)
    description = normalize_space(" ".join(lines))
    return description if len(description) <= limit else f"{description[:limit - 3]}..."


def page_title(path: Path, text: str) -> str:
    match = re.search(r"^#\s+(.+)$", text, re.M)
    return match.group(1).strip() if match else path.stem


def section_for(position: int, headings: list[tuple[int, str]]) -> str:
    section = ""
    for heading_position, title in headings:
        if heading_position < position and title != "图版列表":
            section = title
    return section


def raw_page_link(fields: dict[str, str]) -> str:
    raw = fields.get("原分页", "")
    return raw.replace("../", "")


def place_or_height(fields: dict[str, str]) -> str:
    for key in ("拍摄地点", "飞行高度", "航行高度", "云底高度"):
        value = fields.get(key, "")
        if value and value not in {"原页未列出", "待校订"}:
            return value
    return ""


def extract_plate_entries() -> list[dict[str, str | int]]:
    entries: list[dict[str, str | int]] = []
    for path in sorted(PLATES.glob("*.md")):
        if path.name == "index.md":
            continue
        text = path.read_text(encoding="utf-8")
        headings = [(m.start(), m.group(1).strip()) for m in re.finditer(r"^##\s+(.+)$", text, re.M)]
        figures = list(re.finditer(r"^###\s+图\s*(\d+)：(.+)$", text, re.M))
        for idx, figure in enumerate(figures):
            start = figure.end()
            end = figures[idx + 1].start() if idx + 1 < len(figures) else len(text)
            block = text[start:end]
            fields = extract_fields(block)
            number = int(figure.group(1))
            entries.append(
                {
                    "number": number,
                    "title": figure.group(2).strip(),
                    "page_title": page_title(path, text),
                    "section": section_for(figure.start(), headings),
                    "link": path.relative_to(ATLAS).as_posix(),
                    "code": fields.get("云类代码", ""),
                    "pdf_page": raw_page_link(fields),
                    "place": place_or_height(fields),
                    "time": fields.get("拍摄时间", ""),
                    "direction": fields.get("拍摄方向", ""),
                    "photographer": fields.get("拍摄者", ""),
                    "description": extract_description(block),
                }
            )
    return sorted(entries, key=lambda item: int(item["number"]))


def validate_entries(entries: list[dict[str, str | int]]) -> None:
    numbers = [int(entry["number"]) for entry in entries]
    missing = [number for number in range(2, 281) if number not in numbers]
    duplicates = sorted(number for number in set(numbers) if numbers.count(number) > 1)
    if missing or duplicates:
        raise SystemExit(f"Invalid plate coverage: missing={missing}, duplicates={duplicates}")


def build_catalog(entries: list[dict[str, str | int]]) -> str:
    lines = [
        "# 中国云图：图版清单",
        "",
        "本清单由已校订的结构化图版页汇总生成，用于按图号快速定位《中国云图》图版。原始 OCR 分页仍保留在各条目的“原分页”链接中，字段不从 OCR 噪声中二次猜测。",
        "",
        '!!! note "范围"',
        "    图 1 是原书目录页，见 [前置页与目录](front-matter.md)。下表覆盖普通图版图 2-280；未在原页列出的字段保留为空或沿用结构化页中的“原页未列出”“待校订”。",
        "",
    ]
    current_group = ""
    for entry in entries:
        group = str(entry["page_title"])
        if group != current_group:
            current_group = group
            lines.extend(
                [
                    f"## {group}",
                    "",
                    "| 图号 | 标题 | 分组 | 云类/代码 | PDF 页 | 地点/高度 | 时间 | 方向 | 拍摄者 | 说明摘要 |",
                    "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
                ]
            )
        values = [
            f"[{entry['number']}]({entry['link']})",
            str(entry["title"]),
            str(entry["section"]),
            str(entry["code"]),
            str(entry["pdf_page"]),
            str(entry["place"]),
            str(entry["time"]),
            str(entry["direction"]),
            str(entry["photographer"]),
            str(entry["description"]),
        ]
        lines.append("| " + " | ".join(escape_table(value) for value in values) + " |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    entries = extract_plate_entries()
    validate_entries(entries)
    CATALOG.write_text(build_catalog(entries), encoding="utf-8")
    print(f"plate_rows={len(entries)}")


if __name__ == "__main__":
    main()
