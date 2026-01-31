
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
import json
import os

def generate_pdf():
    # Register Font
    font_path = "/Library/Fonts/Arial Unicode.ttf"
    if not os.path.exists(font_path):
        font_path = "/System/Library/Fonts/PingFang.ttc"
        if not os.path.exists(font_path):
             print("Error: detailed font not found. Using default.")
             # Fallback logic could be added here, but assuming one exists for now based on user environment
             return

    try:
        pdfmetrics.registerFont(TTFont('ArialUnicode', font_path))
        font_name = 'ArialUnicode'
    except Exception as e:
        print(f"Font registration failed: {e}")
        return

    # Load Data
    with open('revision_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)


    doc = SimpleDocTemplate("Bilingual_Revision_Summary_v3.pdf", pagesize=A4, 
                            rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    story = []

    styles = getSampleStyleSheet()
    
    # Custom Styles
    style_title = ParagraphStyle('CustomTitle', 
                                 parent=styles['Title'], 
                                 fontName=font_name, 
                                 fontSize=24, 
                                 leading=30, 
                                 spaceAfter=20,
                                 textColor=colors.HexColor("#2c3e50"))
    
    style_part_header = ParagraphStyle('PartHeader',
                                      parent=styles['Heading1'],
                                      fontName=font_name,
                                      fontSize=20,
                                      leading=24,
                                      textColor=colors.HexColor("#c0392b"),
                                      spaceBefore=20,
                                      spaceAfter=20,
                                      alignment=1) # Center

    style_topic_header = ParagraphStyle('TopicHeader',
                                      parent=styles['Heading2'],
                                      fontName=font_name,
                                      fontSize=14,
                                      leading=18,
                                      textColor=colors.white,
                                      backColor=colors.HexColor("#34495e"),
                                      borderPadding=5,
                                      spaceBefore=10,
                                      spaceAfter=0,
                                      keepWithNext=True)

    style_content_en = ParagraphStyle('ContentEn',
                                      parent=styles['Normal'],
                                      fontName=font_name,
                                      fontSize=10,
                                      leading=14)
                                      
    style_content_cn = ParagraphStyle('ContentCn',
                                      parent=styles['Normal'],
                                      fontName=font_name,
                                      fontSize=10,
                                      leading=14,
                                      textColor=colors.HexColor("#555555"))

    style_label_q = ParagraphStyle('LabelQ',
                                   parent=styles['Normal'],
                                   fontName=font_name,
                                   fontSize=8,
                                   textColor=colors.HexColor("#2980b9"),
                                   spaceAfter=2)
    style_label_s = ParagraphStyle('LabelS',
                                   parent=styles['Normal'],
                                   fontName=font_name,
                                   fontSize=8,
                                   textColor=colors.HexColor("#27ae60"),
                                   spaceAfter=2)


    story.append(Paragraph("Machine Learning Revision Summary (Comprehensive v3)", style_title))
    story.append(Paragraph("Covers Part 1 (Basics) and Part 2 (Advanced).", style_content_en))
    story.append(Spacer(1, 20))

    col_width = 270

    for idx, item in enumerate(data):
        topic = item.get('topic', 'Untitled Question')
        
        # Check for Section Header
        if item.get('question_en') == "SECTION HEADER":
            story.append(PageBreak())
            story.append(Paragraph(topic, style_part_header))
            continue

        # 1. Topic Header (Full Width)
        story.append(KeepTogether([
            Paragraph(f"{topic}", style_topic_header),
        ]))

        # Prepare Content
        # Use simple replaces, if it was unicode, it should render fine.
        # If we used <super>, it is compatible with ReportLab
        q_en_text = item['question_en'].replace('\n', '<br/>')
        q_cn_text = item['question_cn'].replace('\n', '<br/>')
        s_en_text = item['solution_en'].replace('\n', '<br/>')
        s_cn_text = item['solution_cn'].replace('\n', '<br/>')

        # 2. Question Block
        q_content = [
            [Paragraph("<b>Question (English)</b>", style_label_q), Paragraph("<b>题目 (中文)</b>", style_label_q)],
            [Paragraph(q_en_text, style_content_en), Paragraph(q_cn_text, style_content_cn)]
        ]
        
        t_q = Table(q_content, colWidths=[col_width, col_width])
        t_q.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#eaf2f8")), # Very light blue
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0,0), (-1,-1), 0.5, colors.white),
        ]))

        # 3. Solution Block
        s_content = [
            [Paragraph("<b>Solution</b>", style_label_s), Paragraph("<b>解答</b>", style_label_s)],
            [Paragraph(s_en_text, style_content_en), Paragraph(s_cn_text, style_content_cn)]
        ]

        t_s = Table(s_content, colWidths=[col_width, col_width])
        t_s.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#eafaf1")), # Very light green
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0,0), (-1,-1), 0.5, colors.white),
        ]))

        # Add to story with spacing
        story.append(KeepTogether([
            t_q,
            t_s
        ]))
        story.append(Spacer(1, 12))

    doc.build(story)
    print("PDF Generated: Bilingual_Revision_Summary_v3.pdf")


if __name__ == "__main__":
    generate_pdf()
