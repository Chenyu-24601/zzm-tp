
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json
import os

def generate_pdf():
    # Register Font
    font_path = "/Library/Fonts/Arial Unicode.ttf"
    if not os.path.exists(font_path):
        font_path = "/System/Library/Fonts/PingFang.ttc"
        if not os.path.exists(font_path):
             print("Error: detailed font not found.")
             return

    try:
        pdfmetrics.registerFont(TTFont('ArialUnicode', font_path))
        font_name = 'ArialUnicode'
    except Exception as e:
        print(f"Font registration failed: {e}")
        return

    # Load Data
    with open('algo_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    doc = SimpleDocTemplate("Algorithm_Practice_Exam.pdf", pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []

    styles = getSampleStyleSheet()
    title_style = styles['Title']
    title_style.fontName = font_name
    
    # Styles
    style_en = ParagraphStyle('EnStyle', parent=styles['Normal'], fontName=font_name, fontSize=10, leading=14)
    style_cn = ParagraphStyle('CnStyle', parent=styles['Normal'], fontName=font_name, fontSize=10, leading=14)
    style_header = ParagraphStyle('HeaderStyle', parent=styles['Heading3'], fontName=font_name, fontSize=12, alignment=1)
    style_topic = ParagraphStyle('TopicStyle', parent=styles['Heading2'], fontName=font_name, fontSize=14, spaceAfter=6, textColor=colors.darkblue)

    story.append(Paragraph("Algorithm Practice Exam (Paper-and-Pencil Mode)", title_style))
    story.append(Spacer(1, 20))

    for idx, item in enumerate(data):
        topic = item.get('topic', '')
        
        # Section Header
        story.append(Paragraph(f"{idx+1}. {topic}", style_topic))
        

        # Pre-process newline replacements
        q_en_text = item['question_en'].replace('\n', '<br/>')
        q_cn_text = item['question_cn'].replace('\n', '<br/>')
        s_en_text = item['solution_en'].replace('\n', '<br/>')
        s_cn_text = item['solution_cn'].replace('\n', '<br/>')

        # Problem Table
        q_en = f"<b>Problem:</b><br/>{q_en_text}"
        q_cn = f"<b>题目:</b><br/>{q_cn_text}"
        
        # Solution Table
        s_en = f"<b>Solution:</b><br/>{s_en_text}"
        s_cn = f"<b>解析:</b><br/>{s_cn_text}"

        # Combine into one row
        # Row 1: Question
        row_q = [
            Paragraph(q_en, style_en),
            Paragraph(q_cn, style_cn)
        ]
        
        # Row 2: Solution (can use a different background color)
        row_s = [
            Paragraph(s_en, style_en),
            Paragraph(s_cn, style_cn)
        ]

        table_data = [
            [Paragraph("<b>English</b>", style_header), Paragraph("<b>Chinese (中文)</b>", style_header)],
            row_q,
            row_s
        ]

        col_width = 260
        table = Table(table_data, colWidths=[col_width, col_width])
        
        table_style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('BACKGROUND', (0, 0), (1, 0), colors.lightgrey), # Header background
            ('BACKGROUND', (0, 2), (1, 2), colors.whitesmoke), # Solution background
            ('PADDING', (0, 0), (-1, -1), 8),
        ])
        
        table.setStyle(table_style)
        
        # Keep everything for one problem together
        story.append(KeepTogether(table))
        story.append(Spacer(1, 15))

    doc.build(story)
    print("PDF Generated: Algorithm_Practice_Exam.pdf")

if __name__ == "__main__":
    generate_pdf()
