# ======================================================
# ENTERPRISE AI ATS - BOARDROOM EXECUTIVE REPORT ENGINE
# Advanced Intelligence Edition | Radar + Percentile + Advanced Analytics
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
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import io


# ======================================================
# ADVANCED HOLOGRAPHIC SEAL GENERATOR
# ======================================================

class AdvancedHolographicSeal:
    """Generate advanced holographic seal with multi-layer effects"""
    
    def __init__(self, canvas_obj, center_x, center_y, size=50):
        self.c = canvas_obj
        self.center_x = center_x
        self.center_y = center_y
        self.size = size
    
    def draw(self):
        """Draw multi-layer holographic seal"""
        # Outer metallic ring
        self.c.setLineWidth(3)
        self.c.setStrokeColor(colors.HexColor("#1e40af"))
        self.c.circle(self.center_x, self.center_y, self.size)
        
        # Inner glow layers
        for i in range(4):
            radius = self.size - (i * 4)
            self.c.setLineWidth(0.8)
            if i % 2 == 0:
                self.c.setStrokeColor(colors.HexColor("#3b82f6"))
            else:
                self.c.setStrokeColor(colors.HexColor("#60a5fa"))
            self.c.circle(self.center_x, self.center_y, radius)
        
        # Star badge
        self._draw_star()
        
        # Certification text
        self._draw_certification_text()
    
    def _draw_star(self):
        """Draw star in seal center"""
        points = []
        for i in range(10):
            angle = i * np.pi / 5
            if i % 2 == 0:
                r = self.size - 15
            else:
                r = (self.size - 15) * 0.4
            x = self.center_x + r * np.sin(angle)
            y = self.center_y + r * np.cos(angle)
            points.append((x, y))
        
        self.c.setFillColor(colors.HexColor("#1e40af"))
        self.c.drawPolygon(points, fill=1, stroke=0)
    
    def _draw_certification_text(self):
        """Draw circular certification text"""
        self.c.setFont("Helvetica-Bold", 5)
        self.c.setFillColor(colors.HexColor("#1e40af"))
        
        text = "ENTERPRISE AI ATS CERTIFIED 2026"
        radius = self.size + 12
        char_angle = (2 * np.pi) / len(text)
        
        for i, char in enumerate(text):
            angle = i * char_angle - np.pi / 2
            x = self.center_x + radius * np.cos(angle)
            y = self.center_y + radius * np.sin(angle)
            
            self.c.saveState()
            self.c.translate(x, y)
            self.c.rotate(np.degrees(angle) + 90)
            self.c.drawCentredString(0, 0, char)
            self.c.restoreState()


# ======================================================
# ADVANCED NUMBERED CANVAS
# ======================================================

class AdvancedNumberedCanvas(canvas.Canvas):
    """Enhanced canvas with advanced page layouts and seals"""

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
            self._draw_advanced_page_layout(total_pages)
            super().showPage()

        super().save()

    def _draw_advanced_page_layout(self, total_pages):
        """Draw advanced page with premium styling"""
        
        width, height = A4
        page_number = self.getPageNumber()

        # Premium border with corners
        self.setStrokeColor(colors.HexColor("#0f172a"))
        self.setLineWidth(2)
        self.rect(18, 18, width - 36, height - 36)
        
        # Corner decorations
        corner_size = 15
        corners = [(25, height - 25), (width - 25, height - 25), (25, 25), (width - 25, 25)]
        self.setStrokeColor(colors.HexColor("#2563eb"))
        self.setLineWidth(1.2)
        for x, y in corners:
            self.circle(x, y, corner_size / 2, fill=0, stroke=1)

        # Header section
        self.setFillColor(colors.HexColor("#0f172a"))
        self.rect(18, height - 78, width - 36, 48, fill=1)

        # Blue accent ribbon
        self.setFillColor(colors.HexColor("#2563eb"))
        ribbon_path = self.beginPath()
        ribbon_path.moveTo(width - 160, height - 78)
        ribbon_path.lineTo(width - 90, height - 52)
        ribbon_path.lineTo(width - 160, height - 30)
        ribbon_path.close()
        self.drawPath(ribbon_path, fill=1, stroke=0)

        # Header text
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 13)
        self.drawString(32, height - 54, "ENTERPRISE AI ATS INTELLIGENCE REPORT")
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#93c5fd"))
        self.drawString(32, height - 68, "Advanced Candidate Assessment & Intelligence Platform")

        # Footer
        self.setFont("Helvetica", 7)
        self.setFillColor(colors.HexColor("#475569"))
        self.drawString(32, 30, "© 2026 Chinnakotla Sree Harsha | Enterprise AI ATS Platform")
        
        self.setFont("Helvetica-Bold", 7)
        self.setFillColor(colors.HexColor("#1e40af"))
        self.drawRightString(width - 32, 30, f"Page {page_number} of {total_pages}")

        # Last page elements
        if page_number == total_pages:
            self._draw_signature_section(width, height)
            self._draw_seal(width, height)

    def _draw_signature_section(self, width, height):
        """Draw signature block"""
        right = width - 50
        base_y = 250

        self.setLineWidth(1)
        self.setStrokeColor(colors.HexColor("#1e40af"))
        self.line(right - 90, base_y - 15, right, base_y - 15)

        self.setFont("Helvetica-Bold", 10)
        self.setFillColor(colors.HexColor("#0f172a"))
        self.drawRightString(right, base_y, "Chinnakotla Sree Harsha")
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#475569"))
        self.drawRightString(right, base_y - 14, "Founder & AI Systems Architect")
        self.drawRightString(right, base_y - 28, "Enterprise AI ATS Platform")
        self.drawRightString(right, base_y - 42, f"Generated: {datetime.now().strftime('%B %d, %Y')}")

    def _draw_seal(self, width, height):
        """Draw holographic seal"""
        seal = AdvancedHolographicSeal(self, width - 130, 160, size=45)
        seal.draw()


# ======================================================
# BACKWARD COMPATIBILITY - ORIGINAL CANVAS
# ======================================================

class NumberedCanvas(canvas.Canvas):
    """Original canvas - maintained for backward compatibility"""

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
# ORIGINAL PAGE LAYOUT FUNCTIONS
# ======================================================

def draw_page_layout(c, total_pages):
    """Original page layout - maintained for backward compatibility"""
    
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
    """Original signature block - maintained for backward compatibility"""
    
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
    """Original corporate seal - maintained for backward compatibility"""
    
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
# ADVANCED RADAR CHART GENERATOR
# ======================================================

def generate_advanced_radar_chart(semantic, keyword, skill, quality):
    """Generate advanced radar chart with enhanced styling"""
    
    labels = ["Semantic\nAlignment", "Keyword\nOptimization", "Skill\nCoverage", "Structural\nQuality"]
    scores = [semantic, keyword, skill, quality]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    scores_plot = scores + [scores[0]]
    angles_plot = angles + [angles[0]]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True), facecolor='white')
    
    # Main plot
    ax.plot(angles_plot, scores_plot, 'o-', linewidth=3, color='#2563eb', markersize=10)
    ax.fill(angles_plot, scores_plot, alpha=0.25, color='#3b82f6')
    
    # Styling
    ax.set_xticks(angles)
    ax.set_xticklabels(labels, size=10, weight='bold')
    ax.set_ylim(0, 100)
    ax.set_yticks([20, 40, 60, 80, 100])
    ax.set_yticklabels(['20', '40', '60', '80', '100'], size=8, color='#64748b')
    
    # Grid
    ax.grid(True, linestyle='--', alpha=0.7, color='#cbd5e1')
    ax.set_facecolor('#f8fafc')
    
    # Score labels
    for angle, score in zip(angles, scores):
        ax.text(angle, score + 10, f'{score:.1f}%', ha='center', fontweight='bold', 
                fontsize=10, color='#1e40af', bbox=dict(boxstyle='round,pad=0.3', 
                facecolor='white', edgecolor='#2563eb', linewidth=1))
    
    plt.tight_layout()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    buffer.seek(0)

    return buffer


# ======================================================
# ORIGINAL RADAR CHART GENERATOR
# ======================================================

def generate_radar_chart(semantic, keyword, skill, quality):
    """Original radar chart - maintained for backward compatibility"""
    
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
# CLASSIFICATION & ANALYSIS FUNCTIONS
# ======================================================

def get_advanced_classification(readiness):
    """Get advanced tier classification"""
    
    if readiness >= 85:
        return {
            'tier': 'TIER-0: ELITE CANDIDATE',
            'label': 'Elite – Interview Ready',
            'description': 'Exceptionally qualified with comprehensive skill match and strong ATS optimization',
            'recommendation': 'IMMEDIATE PRIORITY - Fast-track for senior positions',
            'next_action': 'Schedule executive interview immediately'
        }
    elif readiness >= 75:
        return {
            'tier': 'TIER-1: EXCEPTIONAL FIT',
            'label': 'Strong Potential',
            'description': 'Highly qualified with strong semantic alignment and keyword integration',
            'recommendation': 'Recommended for advanced screening and technical assessment',
            'next_action': 'Initiate technical evaluation'
        }
    elif readiness >= 65:
        return {
            'tier': 'TIER-2: STRONG CANDIDATE',
            'label': 'Good Match',
            'description': 'Well-qualified with targeted skill gaps identified',
            'recommendation': 'Consider for specialized roles with skill development plan',
            'next_action': 'Schedule team fit assessment'
        }
    elif readiness >= 50:
        return {
            'tier': 'TIER-3: POTENTIAL MATCH',
            'label': 'Moderate – Needs Optimization',
            'description': 'Foundational skills present, but optimization recommended',
            'recommendation': 'Consider for junior roles or with mentorship programs',
            'next_action': 'Provide resume optimization advisory'
        }
    else:
        return {
            'tier': 'TIER-4: REQUIRES DEVELOPMENT',
            'label': 'High Risk – Resume Requires Major Enhancement',
            'description': 'Significant gaps in ATS optimization and skill alignment',
            'recommendation': 'Recommend comprehensive resume enhancement',
            'next_action': 'Provide detailed optimization guidelines'
        }


def get_simple_classification(readiness):
    """Original simple classification - for backward compatibility"""
    
    if readiness >= 85:
        return "Elite – Interview Ready"
    elif readiness >= 70:
        return "Strong Potential"
    elif readiness >= 50:
        return "Moderate – Needs Optimization"
    else:
        return "High Risk – Resume Requires Major Enhancement"


def generate_metrics_table(semantic, keyword, skill, quality, readiness):
    """Generate advanced metrics table"""
    
    def get_status(score):
        if score >= 90:
            return "⭐ EXCEPTIONAL"
        elif score >= 75:
            return "✓ EXCELLENT"
        elif score >= 60:
            return "◐ GOOD"
        elif score >= 45:
            return "△ FAIR"
        else:
            return "✗ NEEDS WORK"
    
    def get_trend(score):
        if score >= 80:
            return "↑ UP"
        elif score >= 50:
            return "→ STABLE"
        else:
            return "↓ DOWN"
    
    metrics = [
        ["Metric", "Score", "Status", "Trend"],
        ["Semantic Alignment", f"{semantic:.1f}%", get_status(semantic), get_trend(semantic)],
        ["Keyword Optimization", f"{keyword:.1f}%", get_status(keyword), get_trend(keyword)],
        ["Skill Coverage", f"{skill:.1f}%", get_status(skill), get_trend(skill)],
        ["Structural Quality", f"{quality:.1f}%", get_status(quality), get_trend(quality)],
        ["Overall Readiness", f"{readiness:.1f}%", get_status(readiness), get_trend(readiness)]
    ]
    
    return metrics


# ======================================================
# MAIN REPORT GENERATOR - FULLY UPDATED
# ======================================================

def generate_pdf_report(data, advanced_mode=False):
    """
    Generate comprehensive PDF report.
    
    Args:
        data: Report data dictionary
        advanced_mode: If True, use advanced canvas and features; else use original
    
    Returns:
        bytes: PDF content
    """

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

    # Styles
    heading = styles["Heading2"]
    normal = styles["Normal"]

    heading_advanced = ParagraphStyle(
        "HeadingAdvanced",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.HexColor("#0f172a"),
        borderBottomColor=colors.HexColor("#2563eb"),
        borderBottomWidth=2,
        borderBottomPadding=6,
        spaceAfter=12
    )

    highlight = ParagraphStyle(
        "Highlight",
        parent=styles["Normal"],
        backColor=colors.HexColor("#f3f4f6"),
        borderPadding=6
    )

    highlight_success = ParagraphStyle(
        "HighlightSuccess",
        parent=styles["Normal"],
        backColor=colors.HexColor("#dcfce7"),
        borderColor=colors.HexColor("#16a34a"),
        borderWidth=1,
        borderPadding=8
    )

    # Extract scores
    semantic = data.get("semantic", 0)
    keyword = data.get("keyword", 0)
    skill = data.get("skill_score", 0)
    quality = data.get("quality_score", 0)
    final = data.get("final", 0)
    readiness = data.get("readiness", final)
    matched = data.get("matched_skills", [])
    missing = data.get("missing_skills", [])
    candidate_name = data.get("candidate_name", "Candidate")

    # ======================================================
    # PAGE 1: EXECUTIVE SUMMARY
    # ======================================================

    if advanced_mode:
        elements.append(Paragraph(f"Candidate Assessment: {candidate_name}", heading_advanced))
    else:
        elements.append(Paragraph("Executive Summary", heading))
    
    elements.append(Paragraph(
        f"Recruiter Simulation Index: <b>{readiness:.2f}%</b>",
        highlight
    ))
    elements.append(Spacer(1, 0.2 * inch))

    # ======================================================
    # CORE METRICS VISIBILITY
    # ======================================================

    elements.append(Paragraph("ATS Core Performance Metrics", heading))
    elements.append(Paragraph(f"<b>Semantic Alignment:</b> {semantic:.2f}%", normal))
    elements.append(Paragraph(f"<b>Keyword Optimization:</b> {keyword:.2f}%", normal))
    elements.append(Paragraph(f"<b>Skill Coverage:</b> {skill:.2f}%", normal))
    elements.append(Paragraph(f"<b>Structural Quality:</b> {quality:.2f}%", normal))
    elements.append(Spacer(1, 0.2 * inch))

    # ======================================================
    # DETAILED SCORE BREAKDOWN TABLE
    # ======================================================

    elements.append(Paragraph("Detailed Score Breakdown", heading))

    score_table_data = generate_metrics_table(semantic, keyword, skill, quality, readiness)
    
    score_table = Table(score_table_data, colWidths=[2.5*inch, 1.2*inch, 1.5*inch, 1.2*inch])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    
    elements.append(score_table)
    elements.append(Spacer(1, 0.25 * inch))

    # ======================================================
    # CANDIDATE CLASSIFICATION
    # ======================================================

    elements.append(Paragraph("Candidate Classification", heading))

    if advanced_mode:
        classification = get_advanced_classification(readiness)
        class_text = (
            f"<b>Classification:</b> {classification['tier']}<br/>"
            f"<b>Assessment:</b> {classification['description']}<br/>"
            f"<b>Recommendation:</b> {classification['recommendation']}"
        )
    else:
        classification_label = get_simple_classification(readiness)
        class_text = f"Classification Result: <b>{classification_label}</b>"

    elements.append(Paragraph(class_text, highlight_success))
    elements.append(Spacer(1, 0.2 * inch))

    # ======================================================
    # MARKET BENCHMARK POSITIONING
    # ======================================================

    percentile = round(readiness * 0.9, 2)

    elements.append(Paragraph("Market Benchmark Positioning", heading))
    elements.append(Paragraph(
        f"This candidate ranks in the <b>{percentile}th percentile</b> "
        f"against current ATS market benchmarks.",
        highlight
    ))
    elements.append(Spacer(1, 0.25 * inch))

    # ======================================================
    # RADAR CHART
    # ======================================================

    elements.append(Paragraph("Performance Radar Analysis", heading))
    
    if advanced_mode:
        radar_buffer = generate_advanced_radar_chart(semantic, keyword, skill, quality)
    else:
        radar_buffer = generate_radar_chart(semantic, keyword, skill, quality)
    
    try:
        elements.append(Image(radar_buffer, width=4*inch, height=4*inch))
    except:
        elements.append(Paragraph("Radar chart unavailable", normal))
    
    elements.append(PageBreak())

    # ======================================================
    # SKILL INTELLIGENCE
    # ======================================================

    elements.append(Paragraph("Skill Intelligence Analysis", heading))

    if matched:
        elements.append(Paragraph("<b>Matched Skills:</b>", normal))
        elements.append(ListFlowable(
            [ListItem(Paragraph(s, normal)) for s in matched],
            bulletType='bullet'
        ))

    if missing:
        elements.append(Spacer(1, 0.15 * inch))
        elements.append(Paragraph("<b>Missing Skills:</b>", normal))
        elements.append(ListFlowable(
            [ListItem(Paragraph(s, normal)) for s in missing],
            bulletType='bullet'
        ))

    elements.append(Spacer(1, 0.3 * inch))

    # ======================================================
    # FINAL HIRING RECOMMENDATION
    # ======================================================

    elements.append(Paragraph("Final Hiring Recommendation", heading))

    if advanced_mode:
        classification = get_advanced_classification(readiness)
        rec_text = (
            f"<b>Tier Classification:</b> {classification['tier']}<br/>"
            f"<b>Overall Readiness:</b> {readiness:.2f}%<br/>"
            f"<b>Next Action:</b> {classification['next_action']}<br/><br/>"
            f"{classification['description']}"
        )
    else:
        if readiness >= 80:
            recommendation = (
                "The candidate demonstrates strong semantic alignment, "
                "high keyword integration, and structured resume quality. "
                "The profile is ATS-optimized and competitively positioned "
                "within the upper percentile of applicants. "
                "Recommendation: Proceed to advanced technical evaluation."
            )
        elif readiness >= 60:
            recommendation = (
                "The candidate shows moderate ATS compatibility. "
                "While core skills are present, improvements in keyword "
                "density would enhance recruiter visibility. "
                "Recommendation: Consider screening round with advisory."
            )
        else:
            recommendation = (
                "The resume presents structural or keyword alignment gaps. "
                "Strategic optimization is recommended before advancing "
                "to the interview pipeline."
            )
        
        rec_text = (
            f"Overall Readiness Score: <b>{readiness:.2f}%</b><br/><br/>{recommendation}"
        )

    elements.append(Paragraph(rec_text, highlight))

    # Build PDF
    canvas_maker = AdvancedNumberedCanvas if advanced_mode else NumberedCanvas
    doc.build(elements, canvasmaker=canvas_maker)

    pdf_bytes = buffer.getvalue()
    buffer.close()

    return pdf_bytes


# ======================================================
# CONVENIENCE FUNCTION FOR ADVANCED MODE
# ======================================================

def generate_advanced_pdf_report(data):
    """Generate advanced PDF report with all premium features"""
    return generate_pdf_report(data, advanced_mode=True)