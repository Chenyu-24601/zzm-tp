#!/usr/bin/env python3
"""将Markdown笔记转换为HTML和PDF"""

import markdown
from pathlib import Path
import subprocess
import os

# 读取Markdown文件
md_file = Path("/Users/ml/Downloads/zzm/TP-Lab/lectrue1/lecture1_复习笔记_基础版.md")
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# 转换Markdown为HTML
md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc', 'tables'])
html_body = md.convert(md_content)

# 创建完整的HTML文档，带打印友好的样式
html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture 1 复习笔记 - 超级基础版</title>
    <style>
        /* 通用样式 */
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB",
                         "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif;
            line-height: 1.8;
            color: #2c3e50;
            background: #fff;
            padding: 40px;
            max-width: 900px;
            margin: 0 auto;
        }}

        /* 标题样式 */
        h1 {{
            color: #1a1a1a;
            font-size: 32px;
            font-weight: 700;
            margin: 40px 0 20px 0;
            padding-bottom: 15px;
            border-bottom: 4px solid #3498db;
        }}

        h2 {{
            color: #2c3e50;
            font-size: 24px;
            font-weight: 600;
            margin: 35px 0 15px 0;
            padding-left: 15px;
            border-left: 5px solid #3498db;
        }}

        h3 {{
            color: #34495e;
            font-size: 20px;
            font-weight: 600;
            margin: 25px 0 12px 0;
        }}

        h4 {{
            color: #555;
            font-size: 16px;
            font-weight: 600;
            margin: 20px 0 10px 0;
        }}

        /* 段落 */
        p {{
            margin: 12px 0;
            font-size: 15px;
            line-height: 1.8;
        }}

        /* 强调 */
        strong {{
            color: #e74c3c;
            font-weight: 700;
        }}

        em {{
            color: #16a085;
            font-style: italic;
        }}

        /* 代码样式 */
        code {{
            background: #f5f5f5;
            color: #c7254e;
            padding: 3px 6px;
            border-radius: 4px;
            font-family: "SF Mono", Monaco, "Cascadia Code", "Roboto Mono", Consolas, "Courier New", monospace;
            font-size: 14px;
        }}

        pre {{
            background: #f8f9fa;
            border: 1px solid #e1e4e8;
            border-left: 4px solid #3498db;
            border-radius: 6px;
            padding: 20px;
            margin: 20px 0;
            overflow-x: auto;
            line-height: 1.6;
        }}

        pre code {{
            background: transparent;
            color: #24292e;
            padding: 0;
            font-size: 13px;
            display: block;
        }}

        /* 列表 */
        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}

        li {{
            margin: 8px 0;
            line-height: 1.8;
        }}

        /* 引用 */
        blockquote {{
            background: #fff9e6;
            border-left: 5px solid #f39c12;
            padding: 15px 20px;
            margin: 20px 0;
            color: #666;
        }}

        /* 表格 */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 14px;
        }}

        table th {{
            background: #3498db;
            color: white;
            padding: 12px;
            text-align: left;
            font-weight: 600;
        }}

        table td {{
            border: 1px solid #ddd;
            padding: 12px;
        }}

        table tr:nth-child(even) {{
            background: #f8f9fa;
        }}

        /* 水平线 */
        hr {{
            border: none;
            border-top: 2px solid #e1e4e8;
            margin: 30px 0;
        }}

        /* 打印样式 */
        @media print {{
            body {{
                padding: 20px;
                font-size: 12pt;
            }}

            h1 {{
                page-break-before: always;
                font-size: 24pt;
            }}

            h1:first-of-type {{
                page-break-before: avoid;
            }}

            h2 {{
                page-break-after: avoid;
                font-size: 18pt;
            }}

            h3 {{
                page-break-after: avoid;
                font-size: 14pt;
            }}

            pre, table {{
                page-break-inside: avoid;
            }}

            code {{
                font-size: 10pt;
            }}

            pre code {{
                font-size: 9pt;
            }}
        }}

        /* 特殊标记 */
        .highlight {{
            background: #fff3cd;
            padding: 2px 6px;
            border-radius: 3px;
        }}

        /* 练习题样式 */
        details {{
            background: #e8f5e9;
            border: 1px solid #4caf50;
            border-radius: 6px;
            padding: 15px;
            margin: 15px 0;
        }}

        summary {{
            cursor: pointer;
            font-weight: 600;
            color: #2e7d32;
            padding: 5px;
        }}

        summary:hover {{
            color: #1b5e20;
        }}
    </style>
</head>
<body>
    <div id="content">
        {html_body}
    </div>

    <script>
        // 自动打开浏览器打印对话框
        window.onload = function() {{
            // 给用户一点时间查看页面
            setTimeout(function() {{
                window.print();
            }}, 500);
        }};
    </script>
</body>
</html>
"""

# 保存HTML文件
html_file = md_file.parent / "lecture1_复习笔记_基础版.html"
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"✅ HTML文件已生成: {html_file}")

# 尝试用macOS的Safari打开并触发打印
try:
    # 打开HTML文件，会自动触发打印对话框
    subprocess.run(['open', str(html_file)], check=True)
    print("\n📄 浏览器打开中...")
    print("💡 提示：")
    print("   1. 浏览器会自动弹出打印对话框")
    print("   2. 在打印对话框中选择 '另存为PDF'")
    print("   3. PDF将保存在 lectrue1 文件夹中")
    print(f"\n🎯 建议PDF文件名: lecture1_复习笔记_基础版.pdf")
except Exception as e:
    print(f"\n⚠️  自动打开失败: {e}")
    print(f"\n请手动打开文件: {html_file}")
    print("然后按 Cmd+P 打印为PDF")
