# TP-Lab 学习资料 / TP-Lab Study Materials

本仓库包含 COM6115 课程的所有实验材料和学习笔记。

This repository contains all lab materials and study notes for COM6115 course.

## 📚 目录结构 / Directory Structure

### Lecture 1: 中文分词 / Chinese Word Segmentation
- **主题**: 贪婪匹配算法 (Greedy Match Algorithm)
- **文件**:
  - `COM6115_Lab1.pdf` - 实验说明
  - `soln_chinese_segmentation.py` - 解决方案代码
  - `lecture1_复习笔记_基础版.md` - ⭐ **超详细复习笔记**（推荐！）
  - `lecture1_复习笔记_基础版.pdf` - PDF版本，可打印
  - `chinese_segmentation_resources/` - 数据和测试文件

### Lecture 2: 正则表达式 / Regular Expressions
- **主题**: 文本匹配和词汇重叠分析
- **文件**:
  - `Brief Introduction to Regular Expressions.pdf`
  - `soln_word_overlap.py` - 使用正则表达式的解决方案
  - `word_overlap_code_data/` - 新闻文本数据

### Lecture 3: 词性标注 / POS Tagging
- **主题**: 朴素词性标注器
- **文件**:
  - `COM6115_Lab3.pdf`
  - `soln_postagger.py`
  - `naive_pos_tagging_code_data/` - 训练和测试数据

### Lecture 4: Zipf定律 / Zipf's Law
- **主题**: 词频分布统计分析
- **文件**:
  - `COM6115_Lab4.pdf`
  - `soln_Zipf_plot.py`
  - `zipfs_law_code_data.zip`

### Lecture 5: 文本处理 / Text Processing
- **A部分**: 正则表达式扩展
- **B部分**: 推特情感分析预处理
- **文件**:
  - `A/` - 正则表达式练习
  - `B/` - 文本预处理和情感分析

### Lecture 6: 情感分析 / Sentiment Analysis
- **主题**: PMI (Pointwise Mutual Information) 方法
- **文件**:
  - `SA_PMI_Gradable_full.ipynb` - Jupyter Notebook
  - `sa_tweets.zip` - 推特数据集

### Lecture 7: 命名实体识别 / Named Entity Recognition (NER)
- **文件**:
  - `COM6115_Lab7.pdf`
  - `NERlab.zip` - 练习材料

### Lecture 8: 高级NLP / Advanced NLP
- **文件**:
  - `lab.ipynb` - 练习版本
  - `lab_with_solutions.ipynb` - 带解答版本
  - `Tweets_short.csv` - 数据集

## 🎯 学习重点 / Key Learning Points

### Lecture 1 核心算法
**贪婪匹配算法** (Maximum Match Algorithm):
- 从左到右处理文本
- 每次尝试匹配最长的词（5→4→3→2→1）
- 时间复杂度: O(n × m)，其中 m 为最大词长（常数）
- 空间复杂度: O(词典大小)

**关键代码**:
```python
for i in range(maxlen, 0, -1):  # 从长到短尝试
    candidate = sentence[current:current+i]
    if i == 1 or candidate in wordset:  # 兜底 or 匹配
        words.append(candidate)
        current += i
        break
```

**为什么这样设计？**
1. `range(maxlen, 0, -1)` - 贪婪策略：优先最长匹配
2. `i == 1` - 兜底机制：防止未登录词导致死循环
3. `set` 数据结构 - O(1) 查找速度，比 list 快得多

## 📖 复习笔记特色 / Study Notes Features

### ⭐ lecture1_复习笔记_基础版.md
这份笔记专为**代码基础薄弱**的同学准备：

- ✅ **逐行代码解释**：每一行都有详细说明
- ✅ **图解算法过程**：用可视化方式展示算法执行
- ✅ **手工模拟练习**：教你如何在纸笔考试中答题
- ✅ **常见错误避坑**：标注易错点
- ✅ **记忆口诀**：帮助记忆核心概念

**示例图解**:
```
位置：  0  1  2  3
句子：  中 文 句 子
        ↑
     从这里开始
```

## 🛠️ 使用方法 / How to Use

### 运行Python代码
```bash
# Lecture 1 示例
cd lectrue1
python3 soln_chinese_segmentation.py \
    chinese_segmentation_resources/chinesetrad_wordlist.utf8 \
    chinese_segmentation_resources/chinesetext.utf8 \
    output.txt
```

### 运行Jupyter Notebook
```bash
# Lecture 6 示例
cd lecture6
jupyter notebook SA_PMI_Gradable_full.ipynb
```

## 📝 纸笔考试准备建议 / Exam Preparation Tips

### 1. 理解算法原理
- 不要死记代码，要理解**为什么**这样设计
- 能用自己的话解释算法流程
- 会手工模拟算法执行过程

### 2. 掌握核心概念
- **时间复杂度**: 为什么用 set 而不是 list？
- **边界条件**: 为什么需要 `i == 1` 这个条件？
- **数据结构选择**: 不同数据结构的优缺点

### 3. 练习手工模拟
给定句子和词典，在纸上一步步执行算法：
1. 标注当前位置
2. 列出尝试的候选词
3. 说明匹配结果
4. 写出最终分词

## 🤝 贡献 / Contributing

欢迎提交 issue 或 pull request 来改进学习资料！

Feel free to submit issues or pull requests to improve the study materials!

## 📄 许可 / License

本仓库仅用于学习交流，请勿用于商业用途。

This repository is for educational purposes only.

## 📮 联系 / Contact

如有问题，请通过 GitHub Issues 联系。

For questions, please contact via GitHub Issues.

---

**祝学习顺利！Good luck with your studies!** 🎓
