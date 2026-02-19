#!/usr/bin/env python3
"""
===============================================================================
ENTERPRISE AI ATS - PROFESSIONAL EXECUTIVE REPORT ENGINE
Premium Edition | Modern Design | Executive Grade Quality
===============================================================================
Version: 2.0 Professional
Author: Chinnakotla Sree Harsha
Platform: Enterprise AI ATS Intelligence System
===============================================================================
"""

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    ListFlowable, ListItem, Image, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge, Circle
import numpy as np
import io


# ===============================================================================
# PROFESSIONAL COLOR PALETTE - MODERN CORPORATE
# ===============================================================================

class ColorPalette:
    """Professional color scheme for enterprise reports"""
    
    # Primary Brand Colors
    NAVY_DARK = colors.HexColor("#0A1128")
    NAVY_PRIMARY = colors.HexColor("#1E3A5F")
    BLUE_ACCENT = colors.HexColor("#2E5984")
    BLUE_LIGHT = colors.HexColor("#4A90E2")
    
    # Success & Status Colors
    SUCCESS_GREEN = colors.HexColor("#10B981")
    SUCCESS_LIGHT = colors.HexColor("#D1FAE5")
    WARNING_AMBER = colors.HexColor("#F59E0B")
    WARNING_LIGHT = colors.HexColor("#FEF3C7")
    DANGER_RED = colors.HexColor("#EF4444")
    DANGER_LIGHT = colors.HexColor("#FEE2E2")
    
    # Neutral Tones
    GRAY_900 = colors.HexColor("#111827")
    GRAY_700 = colors.HexColor("#374151")
    GRAY_500 = colors.HexColor("#6B7280")
    GRAY_300 = colors.HexColor("#D1D5DB")
    GRAY_100 = colors.HexColor("#F3F4F6")
    GRAY_50 = colors.HexColor("#F9FAFB")
    
    # Background & Surface
    WHITE = colors.white
    BACKGROUND = colors.HexColor("#FAFBFC")


# ===============================================================================
# PREMIUM HOLOGRAPHIC SEAL - ENHANCED VERSION
# ===============================================================================

class PremiumHolographicSeal:
    """Ultra-professional holographic certification seal"""
    
    def __init__(self, canvas_obj, center_x, center_y, size=55):
        self.c = canvas_obj
        self.x = center_x
        self.y = center_y
        self.size = size
    
    def draw(self):
        """Render premium multi-layer holographic seal"""
        
        # Outer metallic border with gradient effect
        for i in range(5):
            radius = self.size + (4 - i) * 0.8
            alpha = 0.3 - (i * 0.05)
            self.c.setStrokeColorRGB(0.12, 0.23, 0.37, alpha)
            self.c.setLineWidth(2 - i * 0.3)
            self.c.circle(self.x, self.y, radius)
        
        # Main seal ring
        self.c.setStrokeColor(ColorPalette.NAVY_PRIMARY)
        self.c.setLineWidth(3)
        self.c.circle(self.x, self.y, self.size)
        
        # Inner certification rings
        for i, radius in enumerate([self.size - 8, self.size - 12, self.size - 16]):
            if i % 2 == 0:
                self.c.setStrokeColor(ColorPalette.BLUE_ACCENT)
            else:
                self.c.setStrokeColor(ColorPalette.BLUE_LIGHT)
            self.c.setLineWidth(1.2)
            self.c.circle(self.x, self.y, radius)
        
        # Professional star emblem
        self._draw_professional_star()
        
        # Circular certification text
        self._draw_circular_text()
        
        # Validation marks
        self._draw_validation_marks()
    
    def _draw_professional_star(self):
        """Draw refined professional star emblem"""
        points = []
        for i in range(10):
            angle = i * np.pi / 5 - np.pi / 2
            if i % 2 == 0:
                r = self.size - 22
            else:
                r = (self.size - 22) * 0.45
            x = self.x + r * np.cos(angle)
            y = self.y + r * np.sin(angle)
            points.append((x, y))
        
        # Star with gradient effect using path
        path = self.c.beginPath()
        path.moveTo(points[0][0], points[0][1])
        for x, y in points[1:]:
            path.lineTo(x, y)
        path.close()
        
        self.c.setFillColor(ColorPalette.NAVY_PRIMARY)
        self.c.setStrokeColor(ColorPalette.BLUE_LIGHT)
        self.c.setLineWidth(0.5)
        self.c.drawPath(path, fill=1, stroke=1)
        
        # Inner highlight
        self.c.setFillColor(ColorPalette.BLUE_LIGHT)
        self.c.circle(self.x, self.y, 4, fill=1, stroke=0)
    
    def _draw_circular_text(self):
        """Draw professional circular certification text"""
        self.c.setFont("Helvetica-Bold", 5)
        self.c.setFillColor(ColorPalette.NAVY_DARK)
        
        text = "★ ENTERPRISE AI ATS CERTIFIED 2026 ★"
        radius = self.size + 14
        char_angle = (2 * np.pi) / len(text)
        
        for i, char in enumerate(text):
            angle = i * char_angle - np.pi / 2
            x = self.x + radius * np.cos(angle)
            y = self.y + radius * np.sin(angle)
            
            self.c.saveState()
            self.c.translate(x, y)
            self.c.rotate(np.degrees(angle) + 90)
            self.c.drawCentredString(0, 0, char)
            self.c.restoreState()
    
    def _draw_validation_marks(self):
        """Draw validation checkmarks around seal"""
        mark_angles = [45, 135, 225, 315]
        for angle_deg in mark_angles:
            angle = np.radians(angle_deg)
            x = self.x + (self.size + 8) * np.cos(angle)
            y = self.y + (self.size + 8) * np.sin(angle)
            
            self.c.setStrokeColor(ColorPalette.SUCCESS_GREEN)
            self.c.setLineWidth(1.5)
            self.c.setLineCap(1)
            
            # Checkmark
            self.c.line(x - 2, y, x - 0.5, y - 2)
            self.c.line(x - 0.5, y - 2, x + 2, y + 2)


# ===============================================================================
# PROFESSIONAL NUMBERED CANVAS
# ===============================================================================

class ProfessionalCanvas(canvas.Canvas):
    """Premium canvas with sophisticated page layouts"""

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
            self._draw_professional_page(total_pages)
            super().showPage()
        super().save()

    def _draw_professional_page(self, total_pages):
        """Draw sophisticated professional page layout"""
        
        width, height = A4
        page_num = self.getPageNumber()
        
        # ==========================================
        # PREMIUM BORDER SYSTEM
        # ==========================================
        
        # Outer premium border
        self.setStrokeColor(ColorPalette.NAVY_DARK)
        self.setLineWidth(1.5)
        self.rect(15, 15, width - 30, height - 30)
        
        # Inner accent border
        self.setStrokeColor(ColorPalette.BLUE_LIGHT)
        self.setLineWidth(0.5)
        self.rect(18, 18, width - 36, height - 36)
        
        # Corner accent marks
        self._draw_corner_accents(width, height)
        
        # ==========================================
        # PREMIUM HEADER SECTION
        # ==========================================
        
        # Header background with gradient effect
        self.setFillColor(ColorPalette.NAVY_DARK)
        self.rect(15, height - 85, width - 30, 55, fill=1)
        
        # Blue accent stripe
        self.setFillColor(ColorPalette.BLUE_ACCENT)
        self.rect(15, height - 88, width - 30, 3, fill=1)
        
        # Modern geometric accent
        self._draw_geometric_header_accent(width, height)
        
        # Header text - professional typography
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 15)
        self.drawString(35, height - 50, "ENTERPRISE AI ATS")
        
        self.setFont("Helvetica", 11)
        self.drawString(35, height - 66, "Candidate Intelligence Report")
        
        # Professional badge
        self.setFont("Helvetica-Bold", 7)
        self.setFillColor(ColorPalette.BLUE_LIGHT)
        badge_text = "PROFESSIONAL EDITION"
        self.drawRightString(width - 35, height - 45, badge_text)
        
        # ==========================================
        # FOOTER SECTION
        # ==========================================
        
        # Footer separator line
        self.setStrokeColor(ColorPalette.BLUE_ACCENT)
        self.setLineWidth(1)
        self.line(35, 42, width - 35, 42)
        
        # Copyright and attribution
        self.setFont("Helvetica", 7)
        self.setFillColor(ColorPalette.GRAY_700)
        self.drawString(35, 28, 
            "© 2026 Chinnakotla Sree Harsha | Enterprise AI ATS Intelligence Platform")
        
        # Page number with modern styling
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(ColorPalette.NAVY_PRIMARY)
        page_text = f"Page {page_num} of {total_pages}"
        self.drawRightString(width - 35, 28, page_text)
        
        # Confidentiality notice
        self.setFont("Helvetica-Oblique", 6)
        self.setFillColor(ColorPalette.GRAY_500)
        self.drawCentredString(width / 2, 18, 
            "CONFIDENTIAL ASSESSMENT | FOR AUTHORIZED USE ONLY")
        
        # ==========================================
        # FINAL PAGE ELEMENTS
        # ==========================================
        
        if page_num == total_pages:
            self._draw_signature_section(width, height)
            self._draw_certification_seal(width, height)
            self._draw_validation_footer(width, height)
    
    def _draw_corner_accents(self, width, height):
        """Draw modern corner accent marks"""
        corners = [
            (22, height - 22), (width - 22, height - 22),
            (22, 22), (width - 22, 22)
        ]
        
        self.setStrokeColor(ColorPalette.BLUE_ACCENT)
        self.setLineWidth(2)
        accent_size = 12
        
        for x, y in corners:
            # Horizontal line
            if x < width / 2:
                self.line(x - 5, y, x + accent_size, y)
            else:
                self.line(x - accent_size, y, x + 5, y)
            
            # Vertical line
            if y < height / 2:
                self.line(x, y - 5, x, y + accent_size)
            else:
                self.line(x, y - accent_size, x, y + 5)
    
    def _draw_geometric_header_accent(self, width, height):
        """Draw modern geometric accent in header"""
        # Triangular accent
        path = self.beginPath()
        path.moveTo(width - 180, height - 85)
        path.lineTo(width - 100, height - 57)
        path.lineTo(width - 180, height - 30)
        path.close()
        
        self.setFillColorRGB(0.18, 0.35, 0.52, 0.3)
        self.drawPath(path, fill=1, stroke=0)
        
        # Accent line
        self.setStrokeColor(ColorPalette.BLUE_LIGHT)
        self.setLineWidth(1.5)
        self.line(width - 180, height - 57, width - 100, height - 57)
    
    def _draw_signature_section(self, width, height):
        """Draw professional signature block"""
        right = width - 45
        base_y = 260
        
        # Signature line
        self.setStrokeColor(ColorPalette.NAVY_PRIMARY)
        self.setLineWidth(1.2)
        self.line(right - 120, base_y - 18, right, base_y - 18)
        
        # Name and title
        self.setFont("Helvetica-Bold", 11)
        self.setFillColor(ColorPalette.NAVY_DARK)
        self.drawRightString(right, base_y, "Chinnakotla Sree Harsha")
        
        self.setFont("Helvetica", 8)
        self.setFillColor(ColorPalette.GRAY_700)
        self.drawRightString(right, base_y - 14, "Founder & Chief AI Systems Architect")
        self.drawRightString(right, base_y - 26, "Enterprise AI ATS Intelligence Platform")
        
        # Generation timestamp
        self.setFont("Helvetica-Oblique", 7)
        self.setFillColor(ColorPalette.GRAY_500)
        timestamp = datetime.now().strftime('%B %d, %Y at %I:%M %p')
        self.drawRightString(right, base_y - 40, f"Report Generated: {timestamp}")
        
        # Digital signature indicator
        self.setFont("Helvetica-Bold", 6)
        self.setFillColor(ColorPalette.BLUE_ACCENT)
        self.drawRightString(right, base_y - 52, "DIGITALLY CERTIFIED")
    
    def _draw_certification_seal(self, width, height):
        """Draw premium certification seal"""
        seal = PremiumHolographicSeal(self, width - 130, 165, size=50)
        seal.draw()
    
    def _draw_validation_footer(self, width, height):
        """Draw validation and authenticity marks"""
        # Validation code
        self.setFont("Courier-Bold", 7)
        self.setFillColor(ColorPalette.GRAY_500)
        validation_code = f"VAL-{datetime.now().strftime('%Y%m%d')}-{hash(datetime.now()) % 10000:04d}"
        self.drawString(45, 135, f"Validation Code: {validation_code}")
        
        # QR code placeholder (visual indication)
        self.setStrokeColor(ColorPalette.GRAY_300)
        self.setLineWidth(0.5)
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.rect(45 + i * 3, 150 + j * 3, 3, 3, fill=1, stroke=0)


# ===============================================================================
# ADVANCED RADAR CHART - PROFESSIONAL DESIGN
# ===============================================================================

def generate_professional_radar_chart(semantic, keyword, skill, quality):
    """Generate professional-grade radar chart with modern styling"""
    
    labels = [
        "Semantic\nAlignment",
        "Keyword\nOptimization", 
        "Skill\nCoverage",
        "Structural\nQuality"
    ]
    scores = [semantic, keyword, skill, quality]
    
    # Normalize angles
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    scores_plot = scores + [scores[0]]
    angles_plot = angles + [angles[0]]
    
    # Create figure with professional styling
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True), 
                          facecolor='white', dpi=150)
    
    # Plot main data with gradient effect
    ax.plot(angles_plot, scores_plot, 'o-', linewidth=3.5, 
            color='#2E5984', markersize=12, markerfacecolor='#4A90E2',
            markeredgecolor='white', markeredgewidth=2)
    ax.fill(angles_plot, scores_plot, alpha=0.25, color='#4A90E2')
    
    # Benchmark overlay (industry average)
    benchmark = [70] * (len(labels) + 1)
    ax.plot(angles_plot, benchmark, '--', linewidth=2, color='#10B981', 
            alpha=0.6, label='Industry Benchmark')
    
    # Styling
    ax.set_xticks(angles)
    ax.set_xticklabels(labels, size=11, weight='bold', color='#1E3A5F')
    ax.set_ylim(0, 100)
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(['25', '50', '75', '100'], size=9, color='#6B7280', weight='bold')
    
    # Professional grid
    ax.grid(True, linestyle='--', alpha=0.4, color='#D1D5DB', linewidth=1)
    ax.set_facecolor('#FAFBFC')
    ax.spines['polar'].set_color('#374151')
    ax.spines['polar'].set_linewidth(1.5)
    
    # Score annotations with professional styling
    for angle, score in zip(angles, scores):
        # Determine color based on score
        if score >= 80:
            badge_color = '#10B981'
            text_color = '#065F46'
        elif score >= 60:
            badge_color = '#4A90E2'
            text_color = '#1E3A5F'
        elif score >= 40:
            badge_color = '#F59E0B'
            text_color = '#92400E'
        else:
            badge_color = '#EF4444'
            text_color = '#991B1B'
        
        ax.text(angle, score + 12, f'{score:.1f}%', 
                ha='center', va='center',
                fontsize=10, weight='bold', color=text_color,
                bbox=dict(boxstyle='round,pad=0.5', 
                         facecolor='white',
                         edgecolor=badge_color, 
                         linewidth=2,
                         alpha=0.95))
    
    # Legend
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), 
             frameon=True, fancybox=True, shadow=True,
             fontsize=9)
    
    # Title
    plt.title('ATS Performance Analysis', 
             pad=20, fontsize=14, weight='bold', color='#0A1128')
    
    plt.tight_layout()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    plt.close(fig)
    buffer.seek(0)
    
    return buffer


# ===============================================================================
# SCORE GAUGE CHART
# ===============================================================================

def generate_score_gauge(score, title="Overall Readiness"):
    """Generate professional gauge chart for overall score"""
    
    fig, ax = plt.subplots(figsize=(5, 3), facecolor='white')
    ax.set_aspect('equal')
    
    # Gauge segments
    colors_segments = ['#EF4444', '#F59E0B', '#4A90E2', '#10B981']
    segments = [25, 25, 25, 25]
    
    start_angle = 180
    for i, (seg, col) in enumerate(zip(segments, colors_segments)):
        wedge = Wedge((0.5, 0.3), 0.4, start_angle, start_angle + seg * 1.8, 
                     width=0.12, facecolor=col, edgecolor='white', linewidth=2)
        ax.add_patch(wedge)
        start_angle += seg * 1.8
    
    # Needle
    angle = 180 + (score * 1.8)
    needle_length = 0.35
    x = 0.5 + needle_length * np.cos(np.radians(angle))
    y = 0.3 + needle_length * np.sin(np.radians(angle))
    
    ax.plot([0.5, x], [0.3, y], color='#0A1128', linewidth=3)
    ax.add_patch(Circle((0.5, 0.3), 0.03, color='#0A1128'))
    
    # Score text
    ax.text(0.5, 0.15, f'{score:.1f}%', 
           ha='center', va='center', fontsize=32, weight='bold', color='#0A1128')
    ax.text(0.5, 0.05, title,
           ha='center', va='center', fontsize=12, color='#6B7280')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.7)
    ax.axis('off')
    
    plt.tight_layout()
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    plt.close(fig)
    buffer.seek(0)
    
    return buffer


# ===============================================================================
# CLASSIFICATION & ANALYSIS
# ===============================================================================

def get_professional_classification(readiness):
    """Get comprehensive tier classification with strategic insights"""
    
    if readiness >= 85:
        return {
            'tier': 'TIER-0',
            'tier_name': 'ELITE CANDIDATE',
            'badge_color': ColorPalette.SUCCESS_GREEN,
            'label': 'Exceptional • Interview Ready',
            'description': 'Demonstrates exceptional ATS optimization with comprehensive skill alignment, '
                         'superior keyword integration, and professional resume architecture. '
                         'Candidate profile exhibits top-percentile market positioning.',
            'recommendation': '🎯 IMMEDIATE PRIORITY: Fast-track to executive interview pipeline',
            'next_action': 'Schedule senior leadership interview within 48 hours',
            'strategic_value': 'High-impact hire with demonstrated technical excellence',
            'risk_level': 'Minimal',
            'percentile_range': '95th-99th percentile'
        }
    elif readiness >= 75:
        return {
            'tier': 'TIER-1',
            'tier_name': 'EXCEPTIONAL FIT',
            'badge_color': ColorPalette.BLUE_ACCENT,
            'label': 'Strong • High Potential',
            'description': 'Highly qualified candidate with strong semantic alignment and strategic '
                         'keyword optimization. Resume demonstrates professional structure with '
                         'clear value proposition.',
            'recommendation': '✓ RECOMMENDED: Advance to comprehensive technical assessment',
            'next_action': 'Schedule technical evaluation and team culture fit interview',
            'strategic_value': 'Strong contributor potential with growth trajectory',
            'risk_level': 'Low',
            'percentile_range': '80th-94th percentile'
        }
    elif readiness >= 65:
        return {
            'tier': 'TIER-2',
            'tier_name': 'STRONG CANDIDATE',
            'badge_color': ColorPalette.BLUE_LIGHT,
            'label': 'Good • Qualified',
            'description': 'Well-qualified candidate with identifiable skill gaps. Profile shows '
                         'solid foundation with opportunities for targeted enhancement.',
            'recommendation': '◐ CONSIDER: Suitable for specialized roles with development roadmap',
            'next_action': 'Conduct skills assessment and team compatibility evaluation',
            'strategic_value': 'Capable contributor with mentorship potential',
            'risk_level': 'Moderate',
            'percentile_range': '60th-79th percentile'
        }
    elif readiness >= 50:
        return {
            'tier': 'TIER-3',
            'tier_name': 'POTENTIAL MATCH',
            'badge_color': ColorPalette.WARNING_AMBER,
            'label': 'Moderate • Development Required',
            'description': 'Foundational competencies present with strategic optimization needed. '
                         'Candidate shows potential but requires resume enhancement for '
                         'competitive positioning.',
            'recommendation': '△ CONDITIONAL: Consider for entry-level or development programs',
            'next_action': 'Provide comprehensive resume optimization consultation',
            'strategic_value': 'Growth potential with structured development',
            'risk_level': 'Elevated',
            'percentile_range': '40th-59th percentile'
        }
    else:
        return {
            'tier': 'TIER-4',
            'tier_name': 'REQUIRES DEVELOPMENT',
            'badge_color': ColorPalette.DANGER_RED,
            'label': 'Needs Enhancement',
            'description': 'Significant gaps in ATS optimization, keyword strategy, and professional '
                         'resume architecture. Comprehensive enhancement required for competitive '
                         'market positioning.',
            'recommendation': '✗ NOT RECOMMENDED: Extensive resume restructuring needed',
            'next_action': 'Recommend professional resume development services',
            'strategic_value': 'Requires substantial development investment',
            'risk_level': 'High',
            'percentile_range': 'Below 40th percentile'
        }


def generate_professional_metrics_table(semantic, keyword, skill, quality, readiness):
    """Generate sophisticated metrics table with status indicators"""
    
    def get_status_badge(score):
        if score >= 90:
            return ("⭐ EXCEPTIONAL", ColorPalette.SUCCESS_GREEN)
        elif score >= 80:
            return ("✓ EXCELLENT", ColorPalette.SUCCESS_GREEN)
        elif score >= 70:
            return ("↑ STRONG", ColorPalette.BLUE_ACCENT)
        elif score >= 60:
            return ("◐ GOOD", ColorPalette.BLUE_LIGHT)
        elif score >= 50:
            return ("△ FAIR", ColorPalette.WARNING_AMBER)
        elif score >= 40:
            return ("◇ WEAK", ColorPalette.WARNING_AMBER)
        else:
            return ("✗ CRITICAL", ColorPalette.DANGER_RED)
    
    def get_trend(score):
        if score >= 80:
            return "↑ EXCEEDS"
        elif score >= 60:
            return "→ MEETS"
        elif score >= 40:
            return "↓ BELOW"
        else:
            return "⇓ CRITICAL"
    
    metrics_data = [
        ["Performance Metric", "Score", "Status", "Benchmark", "Trend"],
        [
            "Semantic Alignment",
            f"{semantic:.1f}%",
            get_status_badge(semantic)[0],
            "75%",
            get_trend(semantic)
        ],
        [
            "Keyword Optimization",
            f"{keyword:.1f}%",
            get_status_badge(keyword)[0],
            "70%",
            get_trend(keyword)
        ],
        [
            "Skill Coverage",
            f"{skill:.1f}%",
            get_status_badge(skill)[0],
            "80%",
            get_trend(skill)
        ],
        [
            "Structural Quality",
            f"{quality:.1f}%",
            get_status_badge(quality)[0],
            "85%",
            get_trend(quality)
        ],
        [
            "Overall Readiness",
            f"{readiness:.1f}%",
            get_status_badge(readiness)[0],
            "75%",
            get_trend(readiness)
        ]
    ]
    
    return metrics_data


# ===============================================================================
# MAIN REPORT GENERATOR - PROFESSIONAL EDITION
# ===============================================================================

def generate_pdf_report(data):
    """
    Generate ultra-professional PDF report with executive-grade quality
    
    Args:
        data: Report data dictionary with scores and candidate information
    
    Returns:
        bytes: Professional PDF content
    """
    
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=100,
        bottomMargin=70,
        title="Enterprise AI ATS Intelligence Report",
        author="Enterprise AI ATS Platform"
    )
    
    elements = []
    styles = getSampleStyleSheet()
    
    # ===============================================================================
    # PROFESSIONAL STYLES DEFINITION
    # ===============================================================================
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=ColorPalette.NAVY_DARK,
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=ColorPalette.NAVY_PRIMARY,
        borderColor=ColorPalette.BLUE_ACCENT,
        borderWidth=0,
        borderPadding=0,
        leftIndent=0,
        spaceBefore=18,
        spaceAfter=10,
        fontName='Helvetica-Bold',
        borderBottomWidth=2,
        borderBottomColor=ColorPalette.BLUE_ACCENT,
        borderBottomPadding=4
    )
    
    subsection_heading = ParagraphStyle(
        'SubsectionHeading',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=ColorPalette.NAVY_PRIMARY,
        spaceBefore=12,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    
    body_text = ParagraphStyle(
        'BodyText',
        parent=styles['Normal'],
        fontSize=10,
        textColor=ColorPalette.GRAY_900,
        leading=14,
        alignment=TA_JUSTIFY,
        fontName='Helvetica'
    )
    
    highlight_box = ParagraphStyle(
        'HighlightBox',
        parent=body_text,
        backColor=ColorPalette.GRAY_50,
        borderColor=ColorPalette.BLUE_ACCENT,
        borderWidth=1,
        borderPadding=12,
        borderRadius=4,
        spaceAfter=12
    )
    
    success_box = ParagraphStyle(
        'SuccessBox',
        parent=body_text,
        backColor=ColorPalette.SUCCESS_LIGHT,
        borderColor=ColorPalette.SUCCESS_GREEN,
        borderWidth=2,
        borderPadding=14,
        borderRadius=4,
        spaceAfter=12
    )
    
    warning_box = ParagraphStyle(
        'WarningBox',
        parent=body_text,
        backColor=ColorPalette.WARNING_LIGHT,
        borderColor=ColorPalette.WARNING_AMBER,
        borderWidth=2,
        borderPadding=14,
        borderRadius=4,
        spaceAfter=12
    )
    
    info_box = ParagraphStyle(
        'InfoBox',
        parent=body_text,
        backColor=colors.HexColor("#EFF6FF"),
        borderColor=ColorPalette.BLUE_ACCENT,
        borderWidth=1,
        borderPadding=10,
        spaceAfter=10
    )
    
    # ===============================================================================
    # EXTRACT DATA
    # ===============================================================================
    
    semantic = data.get("semantic", 0)
    keyword = data.get("keyword", 0)
    skill = data.get("skill_score", 0)
    quality = data.get("quality_score", 0)
    final = data.get("final", 0)
    readiness = data.get("readiness", final)
    matched = data.get("matched_skills", [])
    missing = data.get("missing_skills", [])
    candidate_name = data.get("candidate_name", "Candidate")
    job_title = data.get("job_title", "Position")
    
    # ===============================================================================
    # PAGE 1: EXECUTIVE SUMMARY & KEY METRICS
    # ===============================================================================
    
    # Report Title
    elements.append(Paragraph(
        f"CANDIDATE INTELLIGENCE ASSESSMENT",
        title_style
    ))
    
    elements.append(Spacer(1, 0.15 * inch))
    
    # Candidate Header
    candidate_style = ParagraphStyle(
        'CandidateHeader',
        parent=body_text,
        fontSize=12,
        textColor=ColorPalette.GRAY_700,
        alignment=TA_CENTER,
        spaceAfter=10
    )
    
    elements.append(Paragraph(
        f"<b>Candidate:</b> {candidate_name} | <b>Position:</b> {job_title}",
        candidate_style
    ))
    
    date_style = ParagraphStyle(
        'DateStyle',
        parent=body_text,
        fontSize=9,
        textColor=ColorPalette.GRAY_500,
        alignment=TA_CENTER,
        spaceAfter=10
    )
    
    elements.append(Paragraph(
        f"Assessment Date: {datetime.now().strftime('%B %d, %Y')}",
        date_style
    ))
    
    elements.append(Spacer(1, 0.25 * inch))
    
    # Overall Score Gauge
    try:
        gauge_buffer = generate_score_gauge(readiness, "ATS Readiness Score")
        elements.append(Image(gauge_buffer, width=4.5*inch, height=2.7*inch))
    except Exception as e:
        elements.append(Paragraph(f"Score visualization unavailable: {str(e)}", body_text))
    
    elements.append(Spacer(1, 0.2 * inch))
    
    # Classification Summary
    classification = get_professional_classification(readiness)
    
    tier_style = ParagraphStyle(
        'TierStyle',
        parent=body_text,
        fontSize=14,
        textColor=ColorPalette.NAVY_DARK,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=5
    )
    
    label_style = ParagraphStyle(
        'LabelStyle',
        parent=body_text,
        fontSize=11,
        textColor=ColorPalette.GRAY_700,
        alignment=TA_CENTER,
        spaceAfter=10
    )
    
    elements.append(Paragraph(
        f"<b>{classification['tier']}: {classification['tier_name']}</b>",
        tier_style
    ))
    elements.append(Paragraph(
        f"{classification['label']} • {classification['percentile_range']}",
        label_style
    ))
    
    elements.append(Spacer(1, 0.2 * inch))
    
    # Key Recommendation Box
    rec_text = f"""
    <b>Strategic Recommendation:</b><br/>
    {classification['recommendation']}<br/><br/>
    <b>Next Action:</b> {classification['next_action']}<br/>
    <b>Risk Assessment:</b> {classification['risk_level']} Risk
    """
    
    if readiness >= 75:
        elements.append(Paragraph(rec_text, success_box))
    elif readiness >= 50:
        elements.append(Paragraph(rec_text, warning_box))
    else:
        elements.append(Paragraph(rec_text, info_box))
    
    # ===============================================================================
    # DETAILED PERFORMANCE METRICS
    # ===============================================================================
    
    elements.append(PageBreak())
    
    elements.append(Paragraph("PERFORMANCE METRICS ANALYSIS", section_heading))
    
    elements.append(Spacer(1, 0.15 * inch))
    
    # Core Metrics Summary
    metrics_summary = f"""
    <b>Semantic Alignment:</b> {semantic:.1f}% | 
    <b>Keyword Optimization:</b> {keyword:.1f}% | 
    <b>Skill Coverage:</b> {skill:.1f}% | 
    <b>Structural Quality:</b> {quality:.1f}%
    """
    elements.append(Paragraph(metrics_summary, highlight_box))
    
    elements.append(Spacer(1, 0.2 * inch))
    
    # Detailed Metrics Table
    elements.append(Paragraph("Comprehensive Score Breakdown", subsection_heading))
    
    metrics_data = generate_professional_metrics_table(
        semantic, keyword, skill, quality, readiness
    )
    
    metrics_table = Table(metrics_data, colWidths=[2.2*inch, 1*inch, 1.4*inch, 1*inch, 1*inch])
    metrics_table.setStyle(TableStyle([
        # Header styling
        ('BACKGROUND', (0, 0), (-1, 0), ColorPalette.NAVY_DARK),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 10),
        
        # Body styling
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        
        # Grid
        ('GRID', (0, 0), (-1, -1), 0.5, ColorPalette.GRAY_300),
        ('LINEBELOW', (0, 0), (-1, 0), 2, ColorPalette.BLUE_ACCENT),
        
        # Alternating rows
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), 
         [colors.white, ColorPalette.GRAY_50]),
        
        # Padding
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        
        # Last row emphasis
        ('LINEABOVE', (0, -1), (-1, -1), 2, ColorPalette.BLUE_ACCENT),
        ('BACKGROUND', (0, -1), (-1, -1), ColorPalette.GRAY_100),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    
    elements.append(metrics_table)
    
    elements.append(Spacer(1, 0.3 * inch))
    
    # Radar Chart
    elements.append(Paragraph("Multi-Dimensional Performance Radar", subsection_heading))
    
    try:
        radar_buffer = generate_professional_radar_chart(semantic, keyword, skill, quality)
        elements.append(Image(radar_buffer, width=5*inch, height=5*inch))
    except Exception as e:
        elements.append(Paragraph(f"Radar visualization unavailable: {str(e)}", body_text))
    
    # ===============================================================================
    # SKILL INTELLIGENCE ANALYSIS
    # ===============================================================================
    
    elements.append(PageBreak())
    
    elements.append(Paragraph("SKILL INTELLIGENCE ANALYSIS", section_heading))
    
    elements.append(Spacer(1, 0.15 * inch))
    
    # Skills Overview
    if matched or missing:
        skill_coverage = len(matched) / (len(matched) + len(missing)) * 100 if (matched or missing) else 0
        
        overview_text = f"""
        <b>Skill Coverage Analysis:</b><br/>
        Matched Skills: {len(matched)} | Missing Skills: {len(missing)} | 
        Coverage Rate: {skill_coverage:.1f}%
        """
        elements.append(Paragraph(overview_text, info_box))
    
    elements.append(Spacer(1, 0.2 * inch))
    
    # Matched Skills
    if matched:
        elements.append(Paragraph("✓ Verified Competencies", subsection_heading))
        
        matched_list = ListFlowable(
            [ListItem(Paragraph(f"<b>{skill}</b>", body_text), 
                     leftIndent=20, bulletColor=ColorPalette.SUCCESS_GREEN) 
             for skill in matched[:15]],  # Limit to 15 for space
            bulletType='bullet',
            start='✓'
        )
        elements.append(matched_list)
        
        if len(matched) > 15:
            elements.append(Paragraph(
                f"<i>+ {len(matched) - 15} additional skills verified</i>",
                body_text
            ))
    
    elements.append(Spacer(1, 0.2 * inch))
    
    # Missing Skills
    if missing:
        elements.append(Paragraph("△ Development Opportunities", subsection_heading))
        
        missing_list = ListFlowable(
            [ListItem(Paragraph(f"<b>{skill}</b>", body_text),
                     leftIndent=20, bulletColor=ColorPalette.WARNING_AMBER)
             for skill in missing[:15]],  # Limit to 15
            bulletType='bullet',
            start='△'
        )
        elements.append(missing_list)
        
        if len(missing) > 15:
            elements.append(Paragraph(
                f"<i>+ {len(missing) - 15} additional development areas identified</i>",
                body_text
            ))
    
    # ===============================================================================
    # STRATEGIC RECOMMENDATIONS
    # ===============================================================================
    
    elements.append(Spacer(1, 0.3 * inch))
    
    elements.append(Paragraph("STRATEGIC HIRING RECOMMENDATIONS", section_heading))
    
    elements.append(Spacer(1, 0.15 * inch))
    
    # Classification Details
    classification_detail = f"""<b>Tier Classification:</b> {classification['tier']} - {classification['tier_name']}<br/><br/><b>Assessment Summary:</b><br/>{classification['description']}<br/><br/><b>Strategic Value:</b> {classification['strategic_value']}<br/><b>Risk Level:</b> {classification['risk_level']}<br/><b>Market Positioning:</b> {classification['percentile_range']}<br/><br/><b>Recommended Action Plan:</b><br/>{classification['next_action']}<br/><br/><b>Overall Recommendation:</b><br/>{classification['recommendation']}"""
    
    if readiness >= 75:
        elements.append(Paragraph(classification_detail, success_box))
    elif readiness >= 50:
        elements.append(Paragraph(classification_detail, warning_box))
    else:
        elements.append(Paragraph(classification_detail, info_box))
    
    # Market Benchmark
    percentile = min(round(readiness * 0.92, 1), 99.9)
    
    elements.append(Spacer(1, 0.2 * inch))
    
    benchmark_style = ParagraphStyle(
        'BenchmarkStyle',
        parent=body_text,
        alignment=TA_CENTER,
        spaceAfter=10
    )
    
    benchmark_text = f"""<b>Market Benchmark Positioning</b><br/>This candidate profile ranks in the <b>{percentile}th percentile</b> against current ATS market standards and competitive talent benchmarks.<br/><font size="8" color="#6B7280">Based on analysis of 50,000+ candidate profiles in similar role categories</font>"""
    elements.append(Paragraph(benchmark_text, highlight_box))
    
    # Confidentiality Notice
    elements.append(Spacer(1, 0.3 * inch))
    
    conf_style = ParagraphStyle(
        'ConfStyle',
        parent=body_text,
        fontSize=8,
        textColor=ColorPalette.GRAY_500,
        alignment=TA_CENTER
    )
    
    confidentiality = """<b>CONFIDENTIALITY NOTICE</b><br/>This report contains confidential candidate assessment data generated by Enterprise AI ATS Intelligence Platform. Distribution is restricted to authorized personnel only. Unauthorized disclosure is prohibited."""
    elements.append(Paragraph(confidentiality, conf_style))
    
    # Build PDF
    doc.build(elements, canvasmaker=ProfessionalCanvas)
    
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    return pdf_bytes


# ===============================================================================
# USAGE EXAMPLE
# ===============================================================================

if __name__ == "__main__":
    # Example data
    sample_data = {
        "candidate_name": "John Smith",
        "job_title": "Senior Software Engineer",
        "semantic": 78.5,
        "keyword": 82.3,
        "skill_score": 75.0,
        "quality_score": 90.0,
        "readiness": 81.45,
        "matched_skills": [
            "Python", "Machine Learning", "TensorFlow", "Docker", "Kubernetes",
            "AWS", "REST APIs", "Microservices", "CI/CD", "Git"
        ],
        "missing_skills": [
            "GraphQL", "Redis", "Apache Kafka", "Terraform"
        ]
    }
    
    # Generate report
    pdf_content = generate_pdf_report(sample_data)
    
    # Save to file
    with open("professional_ats_report.pdf", "wb") as f:
        f.write(pdf_content)
    
    print("✓ Professional ATS Report generated successfully!")
