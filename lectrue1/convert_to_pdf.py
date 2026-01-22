#!/usr/bin/env python3
"""将Markdown笔记转换为PDF"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# 读取Markdown文件
md_file = Path("/Users/ml/Downloads/zzm/TP-Lab/lectrue1/lecture1_复习笔记_基础版.md")
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# 转换Markdown为HTML
md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
html_content = md.convert(md_content)

# 创建完整的HTML文档，带样式
html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Lecture 1 复习笔记</title>
    <style>
        @page {{
            size: A4;
            margin: 2cm;
        }}

        body {{
            font-family: "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", sans-serif;
            line-height: 1.8;
            color: #333;
            font-size: 11pt;
        }}

        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-top: 30px;
            font-size: 24pt;
            page-break-before: always;
        }}

        h1:first-of-type {{
            page-break-before: avoid;
        }}

        h2 {{
            color: #34495e;
            border-left: 4px solid #3498db;
            padding-left: 15px;
            margin-top: 25px;
            font-size: 18pt;
        }}

        h3 {{
            color: #555;
            margin-top: 20px;
            font-size: 14pt;
        }}

        h4 {{
            color: #666;
            font-size: 12pt;
        }}

        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            font-size: 10pt;
            color: #c7254e;
        }}

        pre {{
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            border-left: 4px solid #3498db;
            padding: 15px;
            overflow-x: auto;
            border-radius: 4px;
            margin: 15px 0;
            line-height: 1.5;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
            color: #333;
            font-size: 9pt;
        }}

        blockquote {{
            border-left: 4px solid #e74c3c;
            padding-left: 15px;
            margin-left: 0;
            color: #666;
            font-style: italic;
            background-color: #fef5f5;
            padding: 10px 15px;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            font-size: 10pt;
        }}

        table th {{
            background-color: #3498db;
            color: white;
            padding: 10px;
            text-align: left;
            font-weight: bold;
        }}

        table td {{
            border: 1px solid #ddd;
            padding: 10px;
        }}

        table tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
        }}

        li {{
            margin: 5px 0;
        }}

        strong {{
            color: #e74c3c;
            font-weight: bold;
        }}

        em {{
            color: #16a085;
        }}

        hr {{
            border: none;
            border-top: 2px solid #ddd;
            margin: 25px 0;
        }}

        .emoji {{
            font-size: 14pt;
        }}

        /* 避免代码块跨页断开 */
        pre {{
            page-break-inside: avoid;
        }}

        /* 避免标题孤立在页面底部 */
        h1, h2, h3 {{
            page-break-after: avoid;
        }}

        /* 表格避免跨页 */
        table {{
            page-break-inside: avoid;
        }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# 转换为PDF
output_pdf = md_file.parent / "lecture1_复习笔记_基础版.pdf"
HTML(string=html_template).write_pdf(output_pdf)

print(f"✅ PDF已生成: {output_pdf}")
print(f"📄 文件大小: {output_pdf.stat().st_size / 1024:.1f} KB")
