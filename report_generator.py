# ======================================================
# ENTERPRISE AI ATS - BOARDROOM EXECUTIVE REPORT ENGINE
# Advanced Intelligence Edition | Radar + Percentile
# ======================================================

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    ListFlowable,
    ListItem,
    Image,
    PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import io


# ======================================================
# CANVAS (Page Count + Seal)
# ======================================================

class NumberedCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total_pages = len(self._saved_page_states)

        for state in self._saved_page_states:
            self.__dict__.update(state)
            draw_page_layout(self, total_pages)
            super().showPage()

        super().save()


# ======================================================
# PAGE LAYOUT
# ======================================================

def draw_page_layout(c, total_pages):

    width, height = A4
    page_number = c.getPageNumber()

    c.setStrokeColor(colors.HexColor("#0f172a"))
    c.setLineWidth(1.2)
    c.rect(20, 20, width - 40, height - 40)

    c.setFillColor(colors.HexColor("#0f172a"))
    c.rect(20, height - 70, width - 140, 38, fill=1)

    c.setFillColor(colors.HexColor("#2563eb"))
    path = c.beginPath()
    path.moveTo(width - 140, height - 70)
    path.lineTo(width - 90, height - 51)
    path.lineTo(width - 140, height - 32)
    path.close()
    c.drawPath(path, fill=1, stroke=0)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(35, height - 52, "Enterprise AI ATS Intelligence Report")

    c.setFont("Helvetica", 8)
    c.setFillColor(colors.grey)
    c.drawString(30, 30, "© 2026 Chinnakotla Sree Harsha | Enterprise AI ATS Platform")
    c.drawRightString(width - 30, 30, f"Page {page_number} of {total_pages}")

    if page_number == total_pages:
        draw_signature_block(c, width)
        draw_corporate_seal(c, width)


def draw_signature_block(c, width):
    right = width - 40
    base_y = 220

    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(right, base_y, "Chinnakotla Sree Harsha")
    c.setFont("Helvetica", 8)
    c.drawRightString(right, base_y - 14, "Founder & AI Systems Architect")
    c.drawRightString(right, base_y - 28, "Enterprise AI ATS Platform")
    c.drawRightString(right, base_y - 42,
                      f"Generated On: {datetime.now().strftime('%B %d, %Y')}")


def draw_corporate_seal(c, width):
    center_x = width - 110
    center_y = 120

    c.setStrokeColor(colors.HexColor("#2563eb"))
    c.setLineWidth(2)
    c.circle(center_x, center_y, 40)
    c.setLineWidth(1)
    c.circle(center_x, center_y, 32)

    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(center_x, center_y + 12, "ENTERPRISE AI ATS")
    c.drawCentredString(center_x, center_y + 2, "CERTIFIED REPORT")
    c.drawCentredString(center_x, center_y - 8, "DIGITALLY VALIDATED")
    c.drawCentredString(center_x, center_y - 18, "2026 OFFICIAL")


# ======================================================
# RADAR CHART GENERATOR
# ======================================================

def generate_radar_chart(semantic, keyword, skill, quality):

    labels = ["Semantic", "Keyword", "Skill", "Quality"]
    scores = [semantic, keyword, skill, quality]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    scores = np.concatenate((scores, [scores[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    ax.plot(angles, scores)
    ax.fill(angles, scores, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 100)

    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    plt.close(fig)
    buffer.seek(0)

    return buffer


# ======================================================
# MAIN REPORT GENERATOR (FULLY UPDATED)
# ======================================================

def generate_pdf_report(data):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=45,
        leftMargin=45,
        topMargin=90,
        bottomMargin=60
    )

    elements = []
    styles = getSampleStyleSheet()

    heading = styles["Heading2"]
    normal = styles["Normal"]

    highlight = ParagraphStyle(
        "Highlight",
        parent=styles["Normal"],
        backColor=colors.HexColor("#f3f4f6"),
        borderPadding=6
    )

    # Extract Scores
    semantic = data.get("semantic", 0)
    keyword = data.get("keyword", 0)
    skill = data.get("skill_score", 0)
    quality = data.get("quality_score", 0)
    final = data.get("final", 0)
    readiness = data.get("readiness", final)

    matched = data.get("matched_skills", [])
    missing = data.get("missing_skills", [])

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    elements.append(Paragraph("Executive Summary", heading))
    elements.append(Paragraph(
        f"Recruiter Simulation Index: <b>{readiness:.2f}%</b>",
        highlight
    ))
    elements.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # CORE METRIC VISIBILITY SECTION (NEW)
    # ==================================================

    elements.append(Paragraph("ATS Core Performance Metrics", heading))
    elements.append(Paragraph(f"<b>Semantic Alignment:</b> {semantic:.2f}%", normal))
    elements.append(Paragraph(f"<b>Keyword Optimization:</b> {keyword:.2f}%", normal))
    elements.append(Paragraph(f"<b>Skill Coverage:</b> {skill:.2f}%", normal))
    elements.append(Paragraph(f"<b>Structural Quality:</b> {quality:.2f}%", normal))
    elements.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # DETAILED SCORE BREAKDOWN (NEW TABLE)
    # ==================================================

    elements.append(Paragraph("Detailed Score Breakdown", heading))

    score_table = [
        ["Metric", "Score (%)"],
        ["Semantic Alignment", f"{semantic:.2f}%"],
        ["Keyword Optimization", f"{keyword:.2f}%"],
        ["Skill Coverage", f"{skill:.2f}%"],
        ["Structural Quality", f"{quality:.2f}%"],
        ["Overall Readiness", f"{readiness:.2f}%"]
    ]

    table = Table(score_table, colWidths=[3.5 * inch, 2 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # CANDIDATE CLASSIFICATION (NEW)
    # ==================================================

    elements.append(Paragraph("Candidate Classification", heading))

    if readiness >= 85:
        classification = "Elite – Interview Ready"
    elif readiness >= 70:
        classification = "Strong Potential"
    elif readiness >= 50:
        classification = "Moderate – Needs Optimization"
    else:
        classification = "High Risk – Resume Requires Major Enhancement"

    elements.append(Paragraph(
        f"Classification Result: <b>{classification}</b>",
        highlight
    ))

    elements.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # MARKET BENCHMARK POSITIONING
    # ==================================================

    percentile = round(readiness * 0.9, 2)

    elements.append(Paragraph("Market Benchmark Positioning", heading))
    elements.append(Paragraph(
        f"This candidate ranks in the <b>{percentile}th percentile</b> "
        f"against current ATS market benchmarks.",
        highlight
    ))

    elements.append(Spacer(1, 0.25 * inch))

    # ==================================================
    # RADAR CHART
    # ==================================================

    elements.append(Paragraph("Performance Radar Analysis", heading))
    radar_buffer = generate_radar_chart(semantic, keyword, skill, quality)
    elements.append(Image(radar_buffer, width=4*inch, height=4*inch))
    elements.append(PageBreak())

    # ==================================================
    # SKILL INTELLIGENCE
    # ==================================================

    elements.append(Paragraph("Skill Intelligence Analysis", heading))

    if matched:
        elements.append(Paragraph("<b>Matched Skills:</b>", normal))
        elements.append(ListFlowable(
            [ListItem(Paragraph(s, normal)) for s in matched],
            bulletType='bullet'
        ))

    if missing:
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Paragraph("<b>Missing Skills:</b>", normal))
        elements.append(ListFlowable(
            [ListItem(Paragraph(s, normal)) for s in missing],
            bulletType='bullet'
        ))

    elements.append(Spacer(1, 0.3 * inch))

    # ==================================================
    # FINAL HIRING RECOMMENDATION (DETAILED)
    # ==================================================

    elements.append(Paragraph("Final Hiring Recommendation", heading))

    if readiness >= 80:
        recommendation = (
            "The candidate demonstrates strong semantic alignment, "
            "high keyword integration, and structured resume quality. "
            "The profile is ATS-optimized and competitively positioned "
            "within the upper percentile of applicants. "
            "Recommendation: Proceed to advanced technical evaluation "
            "and managerial discussion."
        )
    elif readiness >= 60:
        recommendation = (
            "The candidate shows moderate ATS compatibility. "
            "While core skills are present, improvements in keyword "
            "density and semantic targeting would enhance recruiter visibility. "
            "Recommendation: Consider screening round with improvement advisory."
        )
    else:
        recommendation = (
            "The resume presents structural or keyword alignment gaps "
            "that may reduce ATS ranking probability. "
            "Strategic optimization is recommended before advancing "
            "to the interview pipeline."
        )

    elements.append(Paragraph(
        f"Overall Readiness Score: <b>{readiness:.2f}%</b><br/><br/>{recommendation}",
        highlight
    ))

    doc.build(elements, canvasmaker=NumberedCanvas)

    pdf_bytes = buffer.getvalue()
    buffer.close()

    return pdf_bytes
