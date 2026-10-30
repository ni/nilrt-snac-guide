"""Render NIST requirement data plus dispositions as reStructuredText."""

import re
import textwrap

from snac_docs.dispositions import STATUSES

MIN_TABLE_WIDTH = 82
WRAP_WIDTH = 76
NEWPAGE = ".. raw:: latex\n\n    \\newpage\n"
_ASSIGNMENT = re.compile(r"\[(Assignment:[^\]]*)\]")


def slug(heading):
    """Sphinx-style label for a heading; keeps the guide's existing anchors."""
    return re.sub(r"[^a-z0-9]", "-", heading.lower())


def _heading(label_text, char, overline):
    rule = char * len(label_text)
    lines = [f".. _{slug(label_text)}:", ""]
    lines += [rule, label_text, rule] if overline else [label_text, rule]
    return "\n".join(lines) + "\n"


def _italic_assignments(text):
    return _ASSIGNMENT.sub(r"[*\1*]", text)


def _wrap(text, width=72, initial="", subsequent=""):
    return textwrap.fill(
        text,
        width=width,
        initial_indent=initial,
        subsequent_indent=subsequent,
        break_long_words=False,
        break_on_hyphens=False,
    )


def _statement_lines(node, depth=0):
    """Render a statement tree as RST; lists use NIST's a./1. labelling."""
    lines = []
    indent = "   " * depth
    for index, item in enumerate(node["items"]):
        label = chr(ord("a") + index) if depth == 0 else str(index + 1)
        marker = f"{label}. "
        text = _italic_assignments(item["text"])
        lines.append(_wrap(text, 72, indent + marker, indent + " " * len(marker)))
        if item["items"]:
            lines.append("")
            lines.append("\n".join(_statement_lines(item, depth + 1)))
        lines.append("")
    return lines[:-1] if lines else lines


def _render_statement(node):
    parts = []
    if node["text"]:
        parts.append(_wrap(_italic_assignments(node["text"])))
    if node["items"]:
        parts.append("\n".join(_statement_lines(node)))
    return "\n\n".join(parts) + "\n"


def _grid_table(header, cells, width):
    border = "+" + "-" * (width - 2) + "+"
    header_rule = "+" + "=" * (width - 2) + "+"
    inner = width - 4

    def row(lines):
        return [f"| {line.ljust(inner)} |" for line in lines]

    out = [border, *row([header]), header_rule]
    for cell in cells:
        out += [*row(cell), border]
    return "\n".join(out) + "\n"


def _paragraph_lines(paragraph):
    text = paragraph.rstrip()
    if "\n" in text:
        return text.splitlines()
    return _wrap(text, WRAP_WIDTH - 2).splitlines()


def _summary_table(status):
    rows = list(STATUSES.items())
    width = max(len(label) for _, label in rows)
    header = "Control Summary Information"
    width = max(width, len(header))
    border = f"+---+-{'-' * width}-+"
    out = [border, f"|   | {header.ljust(width)} |", f"+===+={'=' * width}=+"]
    for key, label in rows:
        mark = "X" if key == status else " "
        out += [f"| {mark} | {label.ljust(width)} |", border]
    return "\n".join(out) + "\n"


def _disposition_table(paragraphs):
    cells = [_paragraph_lines(p) for p in paragraphs]
    widest = max(len(line) for cell in cells for line in cell)
    width = max(MIN_TABLE_WIDTH, widest + 4)
    return _grid_table("Solution Implementation", cells, width)


def render_requirement(req, disposition):
    """Render one NIST requirement and its disposition as reStructuredText."""
    heading_text = f"{req['id']}. {req['title']}"
    if "withdrawn" in req:
        heading_text = f"{req['id']}. Withdrawn: {req['withdrawn']}"
        return _heading(heading_text, "-", True) + "\n" + NEWPAGE
    body = [
        _heading(heading_text, "-", True),
        _render_statement(req["statement"]),
        "**DISCUSSION**\n",
        _wrap(req["discussion"]) + "\n" if req["discussion"] else None,
        _summary_table(disposition["status"]),
        _disposition_table(disposition["disposition"]),
        NEWPAGE,
    ]
    return "\n".join(part for part in body if part is not None)


def render_family(family, controls):
    """Render a complete NIST family and its controls as reStructuredText."""
    heading = _heading(f"{family['id']}. {family['title']}", "=", True)
    sections = [heading]
    for req in family["requirements"]:
        sections.append(render_requirement(req, controls.get(req["id"])))
    return "\n\n".join(sections)


def render_summary_table(nist_data, controls):
    """Three-column grid table of every family and active control."""
    rows = []
    for family in nist_data["families"]:
        heading = f"{family['id']}. {family['title']}"
        rows.append((heading, family["title"], ""))
        for req in family["requirements"]:
            if "withdrawn" in req:
                continue
            heading = f"{req['id']}. {req['title']}"
            status = STATUSES[controls[req["id"]]["status"]]
            rows.append((heading, req["title"], status))
    cells = [
        (f":ref:`{h[: h.index(' ') ]} <{slug(h)}>`", f":ref:`{t} <{slug(h)}>`", s)
        for h, t, s in rows
    ]
    widths = [max(len(c[i]) for c in cells) + 2 for i in range(3)]
    border = "+" + "+".join("-" * w for w in widths) + "+"
    out = [border]
    for row in cells:
        out.append("|" + "|".join(f" {c.ljust(w - 1)}" for c, w in zip(row, widths)) + "|")
        out.append(border)
    return "\n".join(out) + "\n"
