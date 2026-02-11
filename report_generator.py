# report_generator.py

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.lib.units import inch
import streamlit as st
import io

def generate_pdf_report(data_dict):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    elements = []
    styles = getSampleStyleSheet()

    elements.append(Paragraph("ATS Resume Analysis Report", styles['Title']))
    elements.append(Spacer(1, 0.3 * inch))

    table_data = [
        ["Metric", "Value"],
        ["Semantic Score", f"{data_dict['semantic']:.2f}%"],
        ["Keyword Score", f"{data_dict['keyword']:.2f}%"],
        ["Final ATS Score", f"{data_dict['final']:.2f}%"],
        ["Resume Word Count", str(data_dict['word_count'])]
    ]

    table = Table(table_data)
    table.setStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    elements.append(table)

    doc.build(elements)
    buffer.seek(0)

    st.download_button(
        label="Download Professional PDF Report",
        data=buffer,
        file_name="ATS_Report.pdf",
        mime="application/pdf"
    )
