from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "docs" / "clouds" / "china-cloud-atlas"
PLATES = ATLAS / "plates"
CATALOG = ATLAS / "plate-catalog.md"
USAGE_INDEX = ATLAS / "usage-references-index.md"
STRUCTURED_FILES = [
    ATLAS / "front-matter.md",
    USAGE_INDEX,
    ATLAS / "plate-catalog.md",
    ATLAS / "text" / "index.md",
    ATLAS / "text" / "cloud-classification.md",
    ATLAS / "text" / "cloud-features.md",
    ATLAS / "text" / "cloud-coding.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def plate_files() -> list[Path]:
    return [p for p in sorted(PLATES.glob("*.md")) if p.name != "index.md"]


def collect_plate_headings() -> dict[int, tuple[str, Path]]:
    headings: dict[int, tuple[str, Path]] = {}
    duplicates: dict[int, list[Path]] = {}
    for path in plate_files():
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"^###\s+图\s*(\d+)：(.+)$", text, re.M):
            number = int(match.group(1))
            title = match.group(2).strip()
            if number in headings:
                duplicates.setdefault(number, [headings[number][1]]).append(path)
            headings[number] = (title, path)
    if duplicates:
        details = "; ".join(f"图 {n}: {', '.join(str(p) for p in paths)}" for n, paths in duplicates.items())
        fail(f"duplicate figure headings: {details}")
    return headings


def check_coverage(headings: dict[int, tuple[str, Path]]) -> None:
    missing = [number for number in range(2, 281) if number not in headings]
    extras = [number for number in headings if number < 2 or number > 280]
    if missing or extras:
        fail(f"invalid figure heading coverage: missing={missing}, extras={extras}")


def check_catalog_matches(headings: dict[int, tuple[str, Path]]) -> None:
    text = CATALOG.read_text(encoding="utf-8")
    rows: dict[int, str] = {}
    for line in text.splitlines():
        match = re.match(r"^\|\s*\[(\d+)\]\([^)]+\)\s*\|\s*([^|]+?)\s*\|", line)
        if match:
            rows[int(match.group(1))] = match.group(2).strip().replace(r"\|", "|")
    missing = [number for number in range(2, 281) if number not in rows]
    mismatches = [
        (number, headings[number][0], rows.get(number, ""))
        for number in range(2, 281)
        if number in rows and rows[number] != headings[number][0]
    ]
    if missing or mismatches:
        details = "; ".join(f"图 {n}: plates={a!r}, catalog={b!r}" for n, a, b in mismatches[:20])
        fail(f"catalog out of sync: missing={missing}, mismatches={details}")


def expand_number_cell(cell: str) -> list[int]:
    numbers: list[int] = []
    normalized = cell.replace("~", "-").replace("－", "-")
    for part in re.split(r"[、,，]\s*", normalized):
        part = part.strip()
        range_match = re.match(r"^(\d+)-(\d+)$", part)
        if range_match:
            start = int(range_match.group(1))
            end = int(range_match.group(2))
            numbers.extend(range(start, end + 1))
            continue
        number_match = re.match(r"^(\d+)", part)
        if number_match:
            numbers.append(int(number_match.group(1)))
    return numbers


def check_usage_index_coverage() -> None:
    text = USAGE_INDEX.read_text(encoding="utf-8")
    if "## 索引页" not in text:
        fail("usage index section missing")
    index_text = text.split("## 索引页", 1)[1]
    numbers: list[int] = []
    for line in index_text.splitlines():
        if not line.startswith("|") or "---" in line or "图号" in line:
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        figure_cell = ""
        if len(cells) == 5:
            figure_cell = cells[3]
        elif len(cells) == 4:
            figure_cell = cells[2]
        numbers.extend(expand_number_cell(figure_cell))
    unique = set(numbers)
    missing = [number for number in range(1, 281) if number not in unique]
    extras = [number for number in numbers if number < 1 or number > 280]
    if missing or extras:
        fail(f"usage index figure coverage invalid: missing={missing}, extras={extras}")


def collect_fields(block: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for match in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|$", block, re.M):
        key = match.group(1).strip()
        value = match.group(2).strip()
        if key not in {"字段", "---"}:
            fields[key] = value
    return fields


def check_required_plate_fields() -> None:
    required_fields = ["拍摄地点", "拍摄时间", "拍摄方向", "拍摄者", "原分页"]
    issues: list[str] = []
    for path in plate_files():
        text = path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^###\s+图\s*(\d+)：(.+)$", text, re.M))
        for index, match in enumerate(matches):
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            fields = collect_fields(text[match.end() : end])
            missing = [field for field in required_fields if field not in fields]
            pending = [
                field
                for field in required_fields
                if field in fields and fields[field] in {"", "待校订"}
            ]
            if missing or pending:
                details = []
                if missing:
                    details.append(f"missing={missing}")
                if pending:
                    details.append(f"pending={pending}")
                issues.append(f"{path.name} 图 {match.group(1)}: {', '.join(details)}")
    if issues:
        fail("required plate fields incomplete: " + "; ".join(issues[:30]))


def check_local_images_exist() -> None:
    missing: list[str] = []
    for path in plate_files():
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
            target = match.group(1).split("#", 1)[0].split("?", 1)[0]
            if target.startswith(("http://", "https://")):
                continue
            if not (path.parent / target).resolve().exists():
                missing.append(f"{path}: {target}")
    if missing:
        fail("missing local images: " + "; ".join(missing[:30]))


def check_common_residuals() -> None:
    plain_patterns = [
        "杨志虎",
        "沙州",
        "珠峰南侧积雨云和钩状卷云",
        "张家界层积云",
        "南极透光高积云",
        "南极极光",
    ]
    regex_patterns = [
        re.compile(r"^\|\s*卷云和高积云\s*\|\s*平原\s*\|\s*261\s*\|", re.M),
        re.compile(r"^\|\s*荚状云\s*\|\s*港湾\s*\|\s*262\s*\|", re.M),
        re.compile(r"^###\s+图\s*250：珠峰北面浓积云\s*$", re.M),
    ]
    files = STRUCTURED_FILES + plate_files()
    hits: list[str] = []
    for path in files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in plain_patterns:
            if pattern in text:
                hits.append(f"{path}: {pattern}")
        for pattern in regex_patterns:
            if pattern.search(text):
                hits.append(f"{path}: {pattern.pattern}")
    if hits:
        fail("known residual terms found: " + "; ".join(hits))


def main() -> None:
    headings = collect_plate_headings()
    check_coverage(headings)
    check_catalog_matches(headings)
    check_usage_index_coverage()
    check_required_plate_fields()
    check_local_images_exist()
    check_common_residuals()
    print("OK: china-cloud-atlas consistency checks passed")


if __name__ == "__main__":
    main()
