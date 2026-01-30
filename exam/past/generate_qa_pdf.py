
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json
import os

def generate_pdf():
    # Register Font
    font_path = "/Library/Fonts/Arial Unicode.ttf"
    if not os.path.exists(font_path):
        # Fallback to system font if specific one not found, though we checked it exists.
        # Try PingFang if Arial Unicode is missing (unlikely based on check)
        font_path = "/System/Library/Fonts/PingFang.ttc"
        if not os.path.exists(font_path):
             print("Error: detailed font not found.")
             return

    # Note: For TTC, we might need index. For TTF, just path.
    # reportlab 3.x+ handles TTC with 'ttcname' but TTFont expects .ttf usually.
    # Arial Unicode.ttf is standard TTF.
    try:
        pdfmetrics.registerFont(TTFont('ArialUnicode', font_path))
        font_name = 'ArialUnicode'
    except Exception as e:
        print(f"Font registration failed: {e}")
        return

    # Load Data
    with open('questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    doc = SimpleDocTemplate("Exam_Concepts_Bilingual.pdf", pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.fontName = font_name
    
    # Styles for content
    # English style
    style_en = ParagraphStyle('EnStyle', parent=styles['Normal'], fontName=font_name, fontSize=10, leading=14)
    # Chinese style
    style_cn = ParagraphStyle('CnStyle', parent=styles['Normal'], fontName=font_name, fontSize=10, leading=14)
    
    # Header style
    style_header = ParagraphStyle('HeaderStyle', parent=styles['Heading3'], fontName=font_name, fontSize=12, alignment=1)

    story.append(Paragraph("Exam Concept Q&A Review (Bilingual)", title_style))
    story.append(Spacer(1, 20))

    # Table Data
    table_data = []
    # Header Row
    table_data.append([Paragraph("<b>English</b>", style_header), Paragraph("<b>Chinese (中文)</b>", style_header)])

    for item in data:
        topic = item.get('topic', '')
        q_en = f"<b>[{topic}] Q:</b> {item['question_en']}"
        a_en = f"<b>A:</b> {item['answer_en']}"
        full_en = f"{q_en}<br/><br/>{a_en}"

        q_cn = f"<b>[{topic}] 问:</b> {item['question_cn']}"
        a_cn = f"<b>答:</b> {item['answer_cn']}"
        full_cn = f"{q_cn}<br/><br/>{a_cn}"
        
        # Add row
        table_data.append([
            Paragraph(full_en, style_en),
            Paragraph(full_cn, style_cn)
        ])

    # Table Style
    table_style = TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (1, 0), colors.lightgrey),
        ('PADDING', (0, 0), (-1, -1), 6),
    ])

    # Create Table object
    # Widths: A4 width is ~595. Margins 30+30=60. Usable = 535. Split evenly ~267.
    col_width = 260
    table = Table(table_data, colWidths=[col_width, col_width])
    table.setStyle(table_style)

    story.append(table)
    
    doc.build(story)
    print("PDF Generated: Exam_Concepts_Bilingual.pdf")

if __name__ == "__main__":
    generate_pdf()
