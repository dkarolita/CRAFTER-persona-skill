#!/usr/bin/env python3
"""Convert CRAFTER persona JSON into a readable DOCX document.

This script uses only Python's standard library. It writes a minimal DOCX file
that opens in Microsoft Word, Google Docs, LibreOffice, and Apple Pages.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path
from typing import Any
from xml.sax.saxutils import escape

MINIMUM_CHARACTERISTIC_LABELS = {
    "motivation": "Motivation",
    "goals": "Goals",
    "pain_points": "Pain Points",
}

QUALITY_TEXT_KEYS = ("grounding", "realism")
QUALITY_LIST_KEYS = ("risks", "refinement_suggestions")


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float, bool)):
        return str(value)
    return json.dumps(value, ensure_ascii=False, indent=2)


def normalize_lines(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [as_text(item) for item in value if as_text(item)]
    text = as_text(value)
    if not text:
        return []
    lines = [line.strip() for line in re.split(r"\n+", text) if line.strip()]
    cleaned = []
    for line in lines:
        cleaned.append(re.sub(r"^[-*•]\s*", "", line).strip())
    return [line for line in cleaned if line]


def paragraph(text: str = "", style: str | None = None) -> str:
    style_xml = ""
    if style:
        style_xml = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>'
    safe = escape(text)
    return f"<w:p>{style_xml}<w:r><w:t xml:space=\"preserve\">{safe}</w:t></w:r></w:p>"


def bullet(text: str) -> str:
    safe = escape(text)
    return (
        '<w:p><w:pPr><w:numPr><w:ilvl w:val="0"/>'
        '<w:numId w:val="1"/></w:numPr></w:pPr>'
        f'<w:r><w:t xml:space="preserve">{safe}</w:t></w:r></w:p>'
    )


def heading(text: str, level: int = 1) -> str:
    style = "Title" if level == 0 else f"Heading{min(level, 3)}"
    return paragraph(text, style)


def section(title: str, body: Any, *, bullets: bool = False) -> list[str]:
    parts = [heading(title, 1)]
    lines = normalize_lines(body)
    if not lines:
        parts.append(paragraph("Not specified."))
    elif bullets:
        parts.extend(bullet(line) for line in lines)
    else:
        parts.extend(paragraph(line) for line in lines)
    return parts


def factor_lines(factors: Any) -> list[str]:
    if not isinstance(factors, list):
        return normalize_lines(factors)
    lines = []
    for factor in factors:
        if isinstance(factor, dict):
            title = as_text(factor.get("title") or factor.get("name"))
            name = as_text(factor.get("name"))
            desc = as_text(factor.get("description"))
            label = title or name or "Factor"
            detail = desc or name
            lines.append(f"{label}: {detail}" if detail else label)
        else:
            text = as_text(factor)
            if text:
                lines.append(text)
    return lines


def quality_lines(quality: Any) -> list[str]:
    if not isinstance(quality, dict):
        return normalize_lines(quality)
    lines = []
    for key in QUALITY_TEXT_KEYS:
        value = as_text(quality.get(key))
        if value:
            lines.append(f"{key.replace('_', ' ').title()}: {value}")
    for key in QUALITY_LIST_KEYS:
        values = normalize_lines(quality.get(key))
        if values:
            label = key.replace("_", " ").title()
            lines.extend(f"{label}: {value}" for value in values)
    return lines


def minimum_characteristic_lines(value: Any) -> list[str]:
    if not isinstance(value, dict):
        return normalize_lines(value)
    lines = []
    for key, label in MINIMUM_CHARACTERISTIC_LABELS.items():
        item = value.get(key)
        if isinstance(item, dict):
            internal = as_text(item.get("internal"))
            external = as_text(item.get("external"))
            relationship = as_text(item.get("relationship"))
            if internal:
                lines.append(f"{label} - Internal: {internal}")
            if external:
                lines.append(f"{label} - External: {external}")
            if relationship:
                lines.append(f"{label} - Relationship: {relationship}")
        else:
            text = as_text(item)
            if text:
                lines.append(f"{label}: {text}")
    return lines


def unwrap_persona_payload(data: dict[str, Any]) -> dict[str, Any]:
    """Accept common wrappers while keeping the documented schema primary."""
    for key in ("persona", "data"):
        value = data.get(key)
        if isinstance(value, dict) and "result" in value:
            return value
    return data


def build_document(data: dict[str, Any]) -> str:
    data = unwrap_persona_payload(data)
    result = data.get("result", {})
    taxonomy = data.get("taxonomy", {})
    domain = taxonomy.get("domain", {}) if isinstance(taxonomy, dict) else {}

    name = as_text(result.get("full_name")) or "CRAFTER Persona"
    domain_label = as_text(domain.get("label") or domain.get("key"))
    title = f"{name} - {domain_label}" if domain_label else name

    parts = [
        heading(title, 0),
        paragraph("Generated with the CRAFTER persona workflow."),
    ]

    quote = as_text(result.get("quote"))
    if quote:
        parts.extend([heading("Quote", 1), paragraph(f'"{quote}"')])

    parts.extend(section("Executive Summary", result.get("bullets"), bullets=True))
    narrative = result.get("narrative", result.get("narative"))
    parts.extend(section("Narrative", narrative))
    parts.extend(section("Mixed Persona View", result.get("mixed")))

    if isinstance(taxonomy, dict):
        detail = as_text(taxonomy.get("detail"))
        if detail:
            parts.extend(section("Context Detail", detail))
        parts.extend(
            [heading("Internal Factors", 1)]
            + [bullet(line) for line in factor_lines(taxonomy.get("internal"))]
        )
        parts.extend(
            [heading("External Factors", 1)]
            + [bullet(line) for line in factor_lines(taxonomy.get("external"))]
        )

    min_lines = minimum_characteristic_lines(
        data.get("minimum_human_characteristics")
    )
    if min_lines:
        parts.extend(
            [heading("Motivation, Goals, And Pain Points", 1)]
            + [bullet(line) for line in min_lines]
        )

    parts.extend(
        section(
            "Requirements Or Design Insights",
            data.get("requirements_insights"),
            bullets=True,
        )
    )
    parts.extend(
        section(
            "Assumptions And Evidence Notes",
            data.get("assumptions"),
            bullets=True,
        )
    )

    q_lines = quality_lines(data.get("quality_review"))
    if q_lines:
        parts.extend(
            [heading("Quality Review", 1)]
            + [bullet(line) for line in q_lines]
        )

    body = "".join(parts)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/>
    </w:sectPr>
  </w:body>
</w:document>
"""


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOCUMENT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:rPr><w:sz w:val="22"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:rPr><w:b/><w:sz w:val="36"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:rPr><w:b/><w:sz w:val="28"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:rPr><w:b/><w:sz w:val="24"/></w:rPr></w:style>
  <w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:rPr><w:b/><w:sz w:val="22"/></w:rPr></w:style>
</w:styles>
"""

NUMBERING = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="•"/>
      <w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>
"""


def write_docx(data: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    document_xml = build_document(data)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", RELS)
        docx.writestr("word/_rels/document.xml.rels", DOCUMENT_RELS)
        docx.writestr("word/document.xml", document_xml)
        docx.writestr("word/styles.xml", STYLES)
        docx.writestr("word/numbering.xml", NUMBERING)


def load_persona_json(input_path: Path) -> dict[str, Any]:
    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"Could not read input file: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Input is not valid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object.")
    return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert CRAFTER persona JSON into a DOCX document."
    )
    parser.add_argument("input_json", type=Path, help="Path to persona JSON file")
    parser.add_argument("output_docx", type=Path, help="Path for output DOCX file")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        data = load_persona_json(args.input_json)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    if args.output_docx.suffix.lower() != ".docx":
        print("Output path must end with .docx.", file=sys.stderr)
        return 1

    try:
        write_docx(data, args.output_docx)
    except Exception as exc:
        print(f"Failed to write DOCX: {exc}", file=sys.stderr)
        return 1

    print(f"Wrote {args.output_docx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
