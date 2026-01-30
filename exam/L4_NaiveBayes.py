from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register a font that supports Chinese
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    
    # Styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontName='STSong-Light',
        fontSize=18,
        alignment=1, # Center
        spaceAfter=20
    )
    header_style = ParagraphStyle(
        'Header',
        parent=styles['Heading2'],
        fontName='STSong-Light',
        fontSize=14,
        spaceBefore=15,
        spaceAfter=10
    )
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontName='STSong-Light',
        fontSize=10,
        leading=14
    )
    bold_style = ParagraphStyle(
        'Bold',
        parent=styles['Normal'],
        fontName='STSong-Light',
        fontSize=10,
        leading=14,
        textColor=colors.black
    )

    # --- Content Data ---
    
    # Training Data 1
    data1_intro = [
        ("Part 1: Training Data (Movie Reviews)", "第一部分：训练数据（电影评论）"),
        ("Based on the provided slides, we have the following training corpus:", "基于提供的幻灯片，我们有以下训练语料库："),
        ("Total Docs: 7 (Pos: 3, Neg: 4). Vocabulary Size: 12.", "文档总数：7 (正面: 3, 负面: 4)。词汇表大小：12。")
    ]
    
    # Questions Part 1
    q_part1 = [
        ("Exercise 1: Standard Naive Bayes", "练习 1：基础朴素贝叶斯"),
        ("Classify the following sentence:\n'This was a fantastic story, great, lovely'", "对以下句子进行分类：\n'This was a fantastic story, great, lovely'"),
        ("Exercise 2: Repeated Words", "练习 2：重复词语"),
        ("Classify the following sentence:\n'Great great great'", "对以下句子进行分类：\n'Great great great'"),
        ("Exercise 3: Zero Probability", "练习 3：零概率问题"),
        ("Classify the following sentence:\n'Excellent cast, unimaginative ending'", "对以下句子进行分类：\n'Excellent cast, unimaginative ending'"),
        ("Exercise 4: Laplace Smoothing", "练习 4：拉普拉斯平滑"),
        ("Recalculate the classification for Exercise 3 ('Excellent cast, unimaginative ending') using Laplace (Add-1) Smoothing.", "使用拉普拉斯（加一）平滑重新计算练习 3 ('Excellent cast, unimaginative ending') 的分类结果。")
    ]
    
    # Training Data 2
    data2_intro = [
        ("Part 2: New Training Data", "第二部分：新训练数据"),
        ("Docs 1-3: Positive (words: sensitive, moving, brilliant, edgy...)\nDocs 4-7: Negative (words: neither, revelatory, flamboyant, awkward...)", "文档 1-3：正面 (单词: sensitive, moving, brilliant, edgy...)\n文档 4-7：负面 (单词: neither, revelatory, flamboyant, awkward...)")
    ]
    
    # Questions Part 2
    q_part2 = [
        ("Exercise 5: Standard NB (No Smoothing)", "练习 5：基础朴素贝叶斯（无平滑）"),
        ("Classify the text (Doc 8) using Standard NB without smoothing:\n'A flamboyant romcom, sensitive but awkward at times.'", "使用无平滑的基础朴素贝叶斯对文本 (Doc 8) 进行分类：\n'A flamboyant romcom, sensitive but awkward at times.'"),
        ("Exercise 6: Binary Naive Bayes", "练习 6：二值朴素贝叶斯"),
        ("Classify the same text (Doc 8) using Binary Naive Bayes (No smoothing). Count presence (1) or absence (0) instead of frequency.", "使用二值朴素贝叶斯（无平滑）对同一文本 (Doc 8) 进行分类。统计是否存在 (1或0) 而非词频。")
    ]

    # Part 3: Reflection
    q_part3 = [
        ("Bonus Reflection: Frequency vs. Presence", "思考题：词频 vs 存在"),
        ("Imagine a document has the word 'good' 20 times and 'bad' 1 time.\nHow would the Standard Naive Bayes model differ from the Binary Naive Bayes model in handling this?", "想象一个文档中单词 'good' 出现了 20 次，而 'bad' 出现了 1 次。\n基础朴素贝叶斯模型和二值朴素贝叶斯模型在处理这种情况时会有什么不同？")
    ]

    # Answers
    answers = [
        ("Answer 1", "答案 1"),
        ("Result: Positive\nP(+) * P(fan|+) * P(grt|+) * P(lov|+) = 0.00043\nP(-) term becomes 0 because P(fantastic|-) is 0.", "结果：正面 (Positive)\nP(+) * P(fan|+) * P(grt|+) * P(lov|+) = 0.00043\nP(-) 项变为 0，因为 P(fantastic|-) 为 0。"),
        
        ("Answer 2", "答案 2"),
        ("Result: Negative\nP(+) = 3/7 * (1/10)^3 = 0.00043\nP(-) = 4/7 * (2/8)^3 = 0.00893\nNegative probability is higher.", "结果：负面 (Negative)\nP(+) = 3/7 * (1/10)^3 = 0.00043\nP(-) = 4/7 * (2/8)^3 = 0.00893\n负面概率更高。"),
        
        ("Answer 3", "答案 3"),
        ("Result: Undefined (Zero Probability)\nP(unimaginative|+) is 0, making Positive prob 0.\nP(excellent|-) is 0, making Negative prob 0.\nModel fails without smoothing.", "结果：无法判断（零概率）\nP(unimaginative|+) 为 0，导致正面概率为 0。\nP(excellent|-) 为 0，导致负面概率为 0。\n没有平滑处理，模型失效。"),
        
        ("Answer 4", "答案 4"),
        ("Result: Negative\nApply smoothing (add 1 to numerator, add 12 to denominator).\nPos: 3/7 * (2/22) * (1/22) = 0.00176\nNeg: 4/7 * (1/20) * (2/20) = 0.00286", "结果：负面 (Negative)\n应用平滑（分子加 1，分母加 12）。\n正面: 3/7 * (2/22) * (1/22) = 0.00176\n负面: 4/7 * (1/20) * (2/20) = 0.00286"),
        
        ("Answer 5", "答案 5"),
        ("Result: Negative\nWord 'awkward' appears in Negative docs but NOT in Positive docs.\nP(awkward|+) = 0 -> Pos prob = 0.\nP(awkward|-) > 0 -> Neg prob > 0.", "结果：负面 (Negative)\n单词 'awkward' 出现在负面文档中，但未出现在正面文档中。\nP(awkward|+) = 0 -> 正面概率 = 0。\nP(awkward|-) > 0 -> 负面概率 > 0。"),
        
        ("Answer 6", "答案 6"),
        ("Result: Negative\nBinary NB checks if word exists in the class documents.\n'awkward' exists in 0/3 Positive docs -> P(awkward|+) = 0.\n'awkward' exists in 1/4 Negative docs -> P(awkward|-) = 0.25.\nPositive prob is 0.", "结果：负面 (Negative)\n二值朴素贝叶斯检查单词是否存在于该类别的文档中。\n'awkward' 出现在 0/3 个正面文档中 -> P(awkward|+) = 0。\n'awkward' 出现在 1/4 个负面文档中 -> P(awkward|-) = 0.25。\n正面概率为 0。"),
        
        ("Reflection Answer", "思考题答案"),
        ("Standard NB: Multiplies P('good'|class) 20 times. It cares deeply about frequency/intensity.\nBinary NB: Counts 'good' only once (1). It only cares that the word appeared, ignoring intensity.", "基础模型：会将 P('good'|类别) 连乘 20 次。它非常关注词频和情感强烈程度。\n二值模型：只计算 'good' 一次 (1)。它只关注单词是否出现，忽略了强度。")
    ]

    # --- Building the PDF ---

    # Title
    elements.append(Paragraph("Naive Bayes Practice / 朴素贝叶斯练习", title_style))
    elements.append(Paragraph("Part I: Questions / 第一部分：问题", header_style))
    elements.append(Spacer(1, 10))

    # Helper to add side-by-side rows
    def add_rows(content_list, style=normal_style):
        data = []
        for eng, chn in content_list:
            data.append([Paragraph(eng, style), Paragraph(chn, style)])
        t = Table(data, colWidths=[240, 240])
        t.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('topPadding', (0,0), (-1,-1), 10),
            ('bottomPadding', (0,0), (-1,-1), 10),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 10))

    # Add Questions
    elements.append(Paragraph("Dataset 1 Overview (数据概览 1)", bold_style))
    add_rows(data1_intro)
    
    add_rows(q_part1)
    
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("Dataset 2 Overview (数据概览 2)", bold_style))
    add_rows(data2_intro)
    add_rows(q_part2)

    # Add Reflection Question
    elements.append(Spacer(1, 10))
    elements.append(Paragraph("Part 3: Reflection / 第三部分：思考", header_style))
    add_rows(q_part3)

    # Page Break for Answers
    elements.append(PageBreak())
    elements.append(Paragraph("Part II: Answers / 第二部分：答案", header_style))
    add_rows(answers)

    doc.build(elements)
    return filename

pdf_filename = 'Naive_Bayes_Practice_v2.pdf'
create_pdf(pdf_filename)