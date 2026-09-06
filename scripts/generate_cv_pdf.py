#!/usr/bin/env python3
"""Generate the downloadable CV from the site's structured data."""

from __future__ import annotations

import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "public" / "cv" / "Hongrui-Shi-CV.pdf"
CV_DATA = ROOT / "src" / "data" / "cv.json"
PUBLICATIONS_DATA = ROOT / "src" / "data" / "publications.json"

OXBLOOD = colors.HexColor("#7b2d26")
INK = colors.HexColor("#1a1a1a")
MUTED = colors.HexColor("#5f5c57")
RULE = colors.HexColor("#ddd8cf")


def clean(value: str) -> str:
    """Keep ReportLab's core fonts happy and use ASCII hyphens throughout."""
    return (
        value.replace("\u2011", "-")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2212", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
    )


def x(value: str) -> str:
    return escape(clean(value))


styles = getSampleStyleSheet()
name_style = ParagraphStyle(
    "Name",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=23,
    leading=25,
    textColor=INK,
    spaceAfter=2,
)
positioning_style = ParagraphStyle(
    "Positioning",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=10.2,
    leading=13.2,
    textColor=INK,
    spaceAfter=7,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7.8,
    leading=10,
    textColor=MUTED,
    spaceAfter=4,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=8.3,
    leading=10,
    textColor=MUTED,
    tracking=0.8,
    spaceBefore=10,
    spaceAfter=5,
    borderWidth=0,
)
title_style = ParagraphStyle(
    "EntryTitle",
    parent=styles["Normal"],
    fontName="Times-Bold",
    fontSize=9.5,
    leading=11.7,
    textColor=INK,
    spaceAfter=1.5,
)
meta_style = ParagraphStyle(
    "Meta",
    parent=styles["Normal"],
    fontName="Times-Italic",
    fontSize=8.1,
    leading=10.2,
    textColor=MUTED,
    spaceAfter=2,
)
body_style = ParagraphStyle(
    "Body",
    parent=styles["Normal"],
    fontName="Times-Roman",
    fontSize=8.35,
    leading=10.7,
    textColor=INK,
    spaceAfter=2,
)
date_style = ParagraphStyle(
    "Date",
    parent=styles["Normal"],
    fontName="Courier",
    fontSize=7.1,
    leading=9.5,
    textColor=MUTED,
    alignment=TA_RIGHT,
)
footer_style = ParagraphStyle(
    "Footer",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=7,
    textColor=MUTED,
)


def section_heading(label: str) -> Table:
    table = Table(
        [[Paragraph(x(label.upper()), section_style)]],
        colWidths=[174 * mm],
    )
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.5, RULE),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return table


def entry(date: str, body, keep: bool = True):
    table = Table(
        [[Paragraph(x(date), date_style), body]],
        colWidths=[33 * mm, 137 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, -1), 6),
                ("RIGHTPADDING", (1, 0), (1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )
    return KeepTogether([table]) if keep else table


def bullets(items: list[str]) -> ListFlowable:
    return ListFlowable(
        [ListItem(Paragraph(x(item), body_style), leftIndent=8) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=10,
        bulletFontName="Helvetica",
        bulletFontSize=4.5,
        bulletOffsetY=1.7,
        spaceAfter=0,
    )


def draw_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(20 * mm, 12.5 * mm, 190 * mm, 12.5 * mm)
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(20 * mm, 8.5 * mm, "Hongrui (Jimmy) Shi")
    canvas.drawRightString(190 * mm, 8.5 * mm, f"{doc.page}")
    canvas.restoreState()


def build() -> None:
    cv = json.loads(CV_DATA.read_text(encoding="utf-8"))
    publications = sorted(
        json.loads(PUBLICATIONS_DATA.read_text(encoding="utf-8")),
        key=lambda item: item["year"],
        reverse=True,
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=16 * mm,
        topMargin=16 * mm,
        bottomMargin=17 * mm,
        title="Hongrui Shi - Curriculum Vitae",
        author="Hongrui Shi",
        subject="Curriculum vitae",
    )

    story = [
        Paragraph("Hongrui (Jimmy) Shi", name_style),
        Paragraph(
            "Postdoctoral Research Associate at the University of Lincoln. "
            "Builds and evaluates computer-vision systems for UK habitat monitoring, "
            "with a focus on when their predictions can be trusted.",
            positioning_style,
        ),
        Paragraph(
            '<a href="mailto:hshi@lincoln.ac.uk" color="#7b2d26">hshi@lincoln.ac.uk</a>'
            ' &nbsp;·&nbsp; <a href="https://whitegivefive.github.io" color="#7b2d26">whitegivefive.github.io</a>'
            ' &nbsp;·&nbsp; <a href="https://scholar.google.com/citations?user=X6z1XHMAAAAJ" color="#7b2d26">Google Scholar</a>'
            ' &nbsp;·&nbsp; <a href="https://github.com/WhiteGiveFive" color="#7b2d26">GitHub</a>',
            contact_style,
        ),
        section_heading("Experience"),
    ]

    for item in cv["experience"]:
        body = [
            Paragraph(x(item["role"]), title_style),
            Paragraph(f'{x(item["org"])} · {x(item["where"])}', meta_style),
            bullets(item["items"]),
        ]
        story.append(entry(item["when"], body, keep=len(item["items"]) <= 2))

    story.append(section_heading("Education"))
    for item in cv["education"]:
        body = [Paragraph(x(item["degree"]), title_style), Paragraph(x(item["org"]), meta_style)]
        if item.get("note"):
            body.append(Paragraph(x(item["note"]), body_style))
        story.append(entry(item["when"], body))

    story.append(PageBreak())
    story.append(section_heading("Publications"))
    for pub in publications:
        authors = ", ".join(pub["authors"])
        authors_markup = x(authors).replace("Hongrui Shi", "<b>Hongrui Shi</b>", 1)
        links = []
        if pub.get("doi"):
            links.append(f'<a href="https://doi.org/{x(pub["doi"])}" color="#7b2d26">DOI</a>')
        if pub.get("code"):
            links.append(f'<a href="{x(pub["code"])}" color="#7b2d26">code</a>')
        venue = x(pub["venue"])
        if pub.get("pages"):
            venue += f', {x(pub["pages"])}'
        if links:
            venue += " · " + " · ".join(links)
        body = [
            Paragraph(x(pub["title"]), title_style),
            Paragraph(authors_markup, body_style),
            Paragraph(venue, meta_style),
        ]
        story.append(entry(str(pub["year"]), body))

    story.append(section_heading("Funding"))
    for item in cv["funding"]:
        body = [
            Paragraph(f'{x(item["what"])} <font name="Helvetica" size="6.5" color="#5f5c57">[{x(item["status"].upper())}]</font>', title_style),
            Paragraph(x(item["detail"]), body_style),
        ]
        story.append(entry(item["when"], body))

    story.append(section_heading("Talks"))
    for item in cv["talks"]:
        body = [Paragraph(x(item["what"]), title_style), Paragraph(x(item["where"]), meta_style)]
        story.append(entry(item["when"], body))

    story.append(section_heading("Service"))
    for item in cv["service"]:
        body = [Paragraph(x(item["what"]), title_style), Paragraph(x(item["detail"]), body_style)]
        story.append(entry(item["when"], body))

    story.append(Spacer(1, 2 * mm))
    doc.build(story, onFirstPage=draw_footer, onLaterPages=draw_footer)


if __name__ == "__main__":
    build()
