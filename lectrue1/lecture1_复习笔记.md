# Lecture 1 复习笔记 - 中文分词（Chinese Word Segmentation）

## 一、题目要求翻译

### 问题背景
中文是一种**象形文字系统**（logographic writing system），其特点是：
- 单个字符可以代表完整的词或短语
- 某些词由多个字符组成
- **传统中文没有空格分隔词语**（这是核心问题！）

例如：`中文句子由连续的一系列单词组成。`
正确分词：`中文 句子 由 连续 的 一系列 单词 组成`

### 任务目标
实现**贪婪匹配算法**（Greedy Match / Maximum Match Algorithm）来自动分词。

---

## 二、核心算法：贪婪匹配（Greedy Match）

### 算法原理（★★★ 考试重点）

**核心思想：从左到右，每次尽可能匹配最长的词**

#### 算法步骤（伪代码）：
```
1. 从句子开头开始（position = 0）
2. 设置长度 = 最大词长（MaxLength = 5）
3. 当 长度 > 1 时：
   a) 提取从position开始、长度为length的字符串
   b) 检查字典中是否存在？
      - 是：输出该词 + 空格，position跳到词尾，重复步骤2
      - 否：长度减1，继续尝试
4. 如果长度 = 1（找不到匹配）：
   - 输出单个字符 + 空格
   - position + 1
5. 重复直到句子结束
```

### 为什么最大词长设为5？
- 统计分析显示：**大多数中文词≤5个字符**
- 限制搜索范围，提高效率

---

## 三、代码详解 - 为什么要这样写？

### 方案1：segment1() - 基于索引的实现

```python
def segment1(sentence, wordset):
    words = []
    sentlen = len(sentence)
    current = 0  # 当前处理位置

    while current < sentlen:
        # 计算剩余字符能尝试的最大长度
        maxlen = min(sentlen - current, MAXWORDLEN)

        # 从最长开始往短尝试
        for i in range(maxlen, 0, -1):
            candidate = sentence[current:current+i]

            # 关键判断！
            if i == 1 or candidate in wordset:
                words.append(candidate)
                current += i  # 跳到下一个位置
                break

    return words
```

#### 关键设计解释：

**Q1: 为什么要 `min(sentlen - current, MAXWORDLEN)`？**
- **防止越界**：如果句尾剩余字符<5，只能尝试剩余长度
- 例如：还剩3个字符，就只能尝试3、2、1长度

**Q2: 为什么 `range(maxlen, 0, -1)`？**
- **贪婪策略的核心**！从长到短尝试，优先匹配最长词
- `range(5, 0, -1)` → 5, 4, 3, 2, 1

**Q3: 为什么判断条件是 `i == 1 or candidate in wordset`？**
- **i == 1**：如果尝试到单字符仍不在词典，就**强制接受单字符**
  - 这是**兜底策略**，防止无限循环
  - 对应算法步骤4：未知词也要处理
- **candidate in wordset**：找到词典中的词

**Q4: 为什么用 `break`？**
- 一旦找到匹配（或降到单字符），立即停止当前位置的循环
- 跳到下一个位置继续处理

---

### 方案2：segment2() - 基于字符串切片的实现

```python
def segment2(sentence, wordset):
    words = []

    while sentence:  # 字符串非空时继续
        maxlen = min(len(sentence), MAXWORDLEN)

        for wlen in range(maxlen, 0, -1):
            candidate = sentence[:wlen]  # 从头部取wlen个字符

            if wlen == 1 or candidate in wordset:
                words.append(candidate)
                sentence = sentence[wlen:]  # 切掉已处理部分
                break

    return words
```

#### 与segment1的区别：

| 特性 | segment1 | segment2 |
|------|----------|----------|
| **核心思路** | 用索引(current)追踪位置 | 直接修改sentence字符串 |
| **提取候选词** | `sentence[current:current+i]` | `sentence[:wlen]` |
| **位置更新** | `current += i` | `sentence = sentence[wlen:]` |
| **循环条件** | `while current < sentlen` | `while sentence` |

**为什么两种方法都可行？**
- **本质相同**：都是从左到右、贪婪匹配
- segment1：**空间换时间**（保留原字符串，用索引）
- segment2：**更Pythonic**（利用字符串切片特性）

---

## 四、UTF-8编码部分（★ 考试可能考）

### 为什么需要指定编码？

```python
with open(word_list_file, encoding="utf8") as words_in:
```

**原因：**
- 中文字符不在ASCII范围内
- UTF-8用**3个字节**编码一个中文字符
- Python必须知道如何解码字节流

### UTF-8编码示例
文件二进制：`\xe4\xb8\x80` → Unicode码点：U+4E00 → 显示：`一`

**编码规则（3字节中文）：**
```
1110zzzz 10yyyyyy 10xxxxxx
```

---

## 五、数据结构选择（★★ 重要）

### 为什么用 `set` 存储词典？

```python
word_set = set()
with open(word_list_file, encoding="utf8") as words_in:
    for line in words_in:
        word_set.add(line.strip())
```

**关键原因：**
- **查找速度**：`candidate in wordset` 是O(1)操作
- 如果用list：每次查找是O(n)，17000个词会很慢！

| 操作 | list | set |
|------|------|-----|
| 查找 | O(n) | O(1) |
| 存储 | 有序 | 无序（但不需要顺序） |

---

## 六、算法局限性（思考题）

### 贪婪算法的问题：
1. **只看局部最优**，不考虑全局
   - 例如："南京市长江大桥"
   - 可能分成："南京市 长江 大桥"
   - 也可能："南京 市长 江大桥"（错误！）

2. **依赖词典质量**
   - 词典不完整 → 错误分词
   - 新词、专有名词无法识别

### 可能的改进方向：
- **双向匹配**：从左、从右同时匹配，取交集
- **统计方法**：基于词频、n-gram模型
- **机器学习**：序列标注（CRF、LSTM）

---

## 七、纸笔考试重点总结

### 必须掌握：
1. ✅ **贪婪匹配算法流程**（能写伪代码）
2. ✅ **为什么从长到短尝试**（贪婪策略）
3. ✅ **为什么i==1时强制接受**（处理未登录词）
4. ✅ **set vs list 的时间复杂度差异**
5. ✅ **UTF-8编码基本原理**（中文3字节）

### 可能的考题形式：
- 给定句子和词典，手工执行算法得出分词结果
- 解释为什么某个设计选择（如用set、从长到短）
- 分析算法的时间/空间复杂度
- 改进算法的可能方向

### 复杂度分析：
- **时间复杂度**：O(n × m)
  - n = 句子长度
  - m = 最大词长（常数5）
  - 实际接近O(n)
- **空间复杂度**：O(|词典|)

---

## 八、关键代码片段（务必记忆）

```python
# 核心循环结构
for i in range(maxlen, 0, -1):  # 从长到短
    candidate = sentence[current:current+i]
    if i == 1 or candidate in wordset:  # 兜底 or 匹配
        words.append(candidate)
        current += i
        break
```

**记忆要点：**
- `range(max, 0, -1)` 降序
- `i == 1` 是兜底
- `break` 找到即停

---

**最后提醒：**
这个算法虽然简单，但体现了**贪婪算法**的经典思想：
- 每步做局部最优选择（最长匹配）
- 不回溯
- 效率高但不保证全局最优

在纸笔考试中，重点是**理解算法逻辑**和**设计决策的原因**，而不是记住具体语法！
