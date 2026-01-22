#!/bin/bash
# 自动化HTML转PDF脚本（使用AppleScript控制浏览器）

HTML_FILE="/Users/ml/Downloads/zzm/TP-Lab/lectrue1/lecture1_复习笔记_基础版.html"
PDF_FILE="/Users/ml/Downloads/zzm/TP-Lab/lectrue1/lecture1_复习笔记_基础版.pdf"

echo "🚀 开始自动转换PDF..."

# 使用AppleScript打开Safari并保存为PDF
osascript <<EOF
tell application "Safari"
    activate
    open location "file://$HTML_FILE"
    delay 2

    tell application "System Events"
        keystroke "p" using command down
        delay 1

        -- 点击PDF下拉菜单
        keystroke tab
        keystroke tab
        keystroke space
        delay 0.5

        -- 选择"存储为PDF"
        keystroke down
        keystroke return
        delay 1

        -- 输入文件名
        keystroke "g" using {command down, shift down}
        delay 0.5
        keystroke "$PDF_FILE"
        keystroke return
        delay 0.5

        keystroke return
    end tell

    delay 2
    quit
end tell
EOF

echo "✅ PDF转换完成！"
echo "📁 文件位置: $PDF_FILE"
