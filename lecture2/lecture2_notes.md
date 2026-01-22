# Lecture 2: Word Overlap (词汇重叠)

## 核心算法：Jaccard Similarity (杰卡德相似系数)

`soln_word_overlap.py` 是为了计算两个文档之间的相似度。最核心的数学概念是 **Jaccard Similarity**。

### 1. 核心公式 (Core Formula)

用来衡量两个集合 (Sets) 的相似度。

$$ J(A, B) = \frac{|A \cap B|}{|A \cup B|} = \frac{\text{Intersection (交集)}}{\text{Union (并集)}} $$

*   **Intersection (交集)**: 两个文档中共同出现的词。
*   **Union (并集)**: 两个文档中所有出现过的词（去重）。

### 2. 代码中的两种变体 (Two Variants in Code)

代码中通过 `-b` 参数控制两种模式，手动计算时需注意区分：

#### A. Binary Jaccard (命令行参数 `-b`)
*   **不考虑词频**，只看词是否出现。
*   把文档看作是一个 **Set (集合)**。
*   **示例**:
    *   Doc1: "apple banana" -> Set1: {apple, banana}
    *   Doc2: "apple orange" -> Set2: {apple, orange}
    *   Intersection: {apple} -> size 1
    *   Union: {apple, banana, orange} -> size 3
    *   Result: 1/3 = 0.333

#### B. Weighted / Count Jaccard (默认模式)
*   **考虑词频**。也称为 "Generalized Jaccard" 或 "Min-Max Similarity"。
*   **分子 (Intersection)**: 对于每个词，取两个文档中出现次数的**最小值**，然后求和。
    *   $\sum \min(\text{count}_A(w), \text{count}_B(w))$
*   **分母 (Union)**: 对于每个词，取两个文档中出现次数的**最大值**，然后求和。
    *   $\sum \max(\text{count}_A(w), \text{count}_B(w))$
*   **示例**:
    *   Doc1: "apple apple banana" -> {apple: 2, banana: 1}
    *   Doc2: "apple banana banana" -> {apple: 1, banana: 2}
    *   **Intersection**:
        *   apple: min(2, 1) = 1
        *   banana: min(1, 2) = 1
        *   Total Over = 1 + 1 = 2
    *   **Union**:
        *   apple: max(2, 1) = 2
        *   banana: max(1, 2) = 2
        *   Total Under = 2 + 2 = 4
    *   Result: 2/4 = 0.5

### 3. 其他重要概念 (Preprocessing)

在计算相似度之前，代码还做了以下预处理，这也是考试常考点：

1.  **Tokenization (分词)**:
    *   使用正则表达式 `[A-Za-z]+` 提取单词。这意味着标点符号会被忽略，数字也会被忽略。
    *   全部转为小写 (`line.lower()`)。
2.  **Stopword Removal (去停用词)**:
    *   过滤掉 `the`, `is`, `at` 等常见但无实际意义的词。代码中用 `-s` 指定停用词表。
3.  **Stemming (词干提取)** (可选 `-p`):
    *   使用 Porter Stemmer。
    *   例如：`running`, `runs`, `ran` -> `run`。这有助于增加匹配率。

### 4. 考试模拟 (Exam Simulation)

题目通常会给出两个短句，要求计算 Jaccard Similarity。

**Step 1**: 预处理 (转小写，去标点)。
**Step 2**: 构建集合 (Binary) 或 词频表 (Weighted)。
**Step 3**: 计算交集大小和并集大小。
**Step 4**: 做除法。

**易错点**:
*   Binary 模式下，重复词只算一次。
*   Weighted 模式下，交集取 Min，并集取 Max。
