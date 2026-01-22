# Lecture 1: Chinese Segmentation (中文分词)

## 核心算法：正向最大匹配 (Forward Maximum Matching, FMM)

你在 `soln_chinese_segmentation.py` 中看到的 `segment1` 和 `segment2` 函数都是**正向最大匹配**算法的实现。这是最基础也是“纸笔考试”中最常考的分词算法之一。

### 1. 核心思想 (Core Idea)

*   **贪心策略 (Greedy Strategy)**：从当前位置开始，尽可能地匹配字典中最长的词。
*   **方向**：从左向右 (Left to Right)。

### 2. 算法步骤 (Algorithm Steps)

假设我们要通过纸笔手动模拟这个算法，步骤如下：

1.  **设定窗口大小 (`MAXWORDLEN`)**：代码中设为 5。这意味着我们最多看 5 个字符。
2.  **指针定位**：`current` 指向句子未处理部分的开头。
3.  **匹配循环**：
    *   尝试长度 `len = MAXWORDLEN` (或者句子剩余长度，取较小值)。
    *   取出子串 `candidate = sentence[current : current + len]`。
    *   **查词典**：
        *   如果 `candidate` 在词典中 -> **匹配成功**。将该词加入结果，`current` 向后移动 `len` 个位置。停止当前匹配循环，开始切分下一个词。
        *   如果不在词典中 -> `len` 减 1，重复上述步骤。
    *   **特殊情况**：如果 `len` 减到了 1，无论单字是否在词典中，都将其作为一个词切分出来（代码行 59: `if i == 1 or candidate in wordset`）。这是一种简单的未登录词（Out Of Vocabulary）处理方式。

### 3. 代码关键点 (Code Highlights)

```python
def segment1(sentence, wordset):
    words = []
    sentlen = len(sentence)
    current = 0
    while current < sentlen:  # 主循环：遍历整个句子
        # 确定最大尝试长度：不能超过剩余句子长度，也不能超过预设最大词长
        maxlen = min(sentlen - current, MAXWORDLEN)
        
        # 内层循环：从长到短尝试
        for i in range(maxlen, 0, -1):
            candidate = sentence[current : current + i]
            # 两个条件满足其一即可切分：
            # 1. 长度为1 (单字保底)
            # 2. 在词典中
            if i == 1 or candidate in wordset:
                words.append(candidate)
                current += i  # 指针前移
                break         # 找到最长匹配后，立即跳出内层循环
    return words
```

### 4. 考试模拟示例 (Exam Simulation)

假设词典：`['我', '爱', '北京', '天安', '天安门']`
MAXWORDLEN = 5
句子：“我爱北京天安门”

1.  **Current = 0 ("我")**:
    *   Try len=5: "我爱北京天" (X)
    *   ...
    *   Try len=1: "我" (Match! "我" is in wordset or len=1) -> Result: ["我"], Current moves to 1.
2.  **Current = 1 ("爱")**:
    *   ... -> Result: ["我", "爱"], Current moves to 2.
3.  **Current = 2 ("北")**:
    *   Try len=5...
    *   Try len=2: "北京" (Match!) -> Result: ["我", "爱", "北京"], Current moves to 4.
4.  **Current = 4 ("天")**:
    *   Try len=3: "天安门" (Match!) -> Result: ["我", "爱", "北京", "天安门"], Current moves to 7.
5.  **End**.

**注意**：如果有由“天安”和“门”组成的句子（假设“天安门”不在词典，“天安”在），FMM 会优先匹配“天安”。

### 5. 优缺点 (Pros & Cons)
*   **优点**：简单，速度快，只需要一个词典。
*   **缺点**：歧义处理能力差（Ambiguity）。例如：“只有/才/能/” vs “只有/才能/”。FMM倾向于切分长词，可能会切错。
