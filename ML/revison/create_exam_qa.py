
import json

# --- Helper to ensure unicode ---
# (Strings are naturally unicode in Python 3, but explicit is good mentally)

part1_data = [
    {
        "topic": "PART 1: BASICS",
        "question_en": "SECTION HEADER",
        "question_cn": "第一部分：基础知识",
        "solution_en": "SECTION HEADER",
        "solution_cn": "SECTION HEADER"
    },
    {
        "topic": "Supervised vs Unsupervised Learning (Basics Q1)",
        "question_en": "Define Supervised and Unsupervised Learning.",
        "question_cn": "定义监督学习和无监督学习。",
        "solution_en": "<b>Supervised Learning</b>: Learning a mapping from inputs x to outputs y, given a labeled dataset of pairs (x, y). Example: Classification, Regression.<br/><b>Unsupervised Learning</b>: Finding patterns or structure in data x without any corresponding target labels y. Example: Clustering, Dimensionality Reduction.",
        "solution_cn": "<b>监督学习</b>：在给定标记数据集 (x, y) 的情况下，学习从输入 x 到输出 y 的映射。例如：分类，回归。<br/><b>无监督学习</b>：在没有对应目标标签 y 的情况下，寻找数据 x 中的模式或结构。例如：聚类，降维。"
    },
    {
        "topic": "Regression vs Classification (Basics Q2)",
        "question_en": "Give an example of a (1) regression and (2) classification problem.",
        "question_cn": "举例说明 (1) 回归问题 和 (2) 分类问题。",
        "solution_en": "<b>Regression</b>: Predicting global temp in 2050 (continuous output).<br/><b>Classification</b>: Identifying isopod species from image (discrete class output).",
        "solution_cn": "<b>回归</b>：预测2050年的全球气温（连续输出）。<br/><b>分类</b>：从图像中识别等足虫物种（离散类别输出）。"
    },
    {
        "topic": "Data Splits (Basics Q3)",
        "question_en": "Define Training set, Validation set, and Test set.",
        "question_cn": "定义训练集、验证集和测试集。",
        "solution_en": "<b>Training set</b>: Used to fit the model parameters.<br/><b>Validation set</b>: Used for model selection and hyperparameter tuning during training.<br/><b>Test set</b>: Used only *once* at the end to evaluate the final performance on unseen data.",
        "solution_cn": "<b>训练集</b>：用于拟合模型参数。<br/><b>验证集</b>：在训练期间用于模型选择和超参数调整。<br/><b>测试集</b>：仅在最后使用*一次*，用于评估未见数据的最终性能。"
    },
    {
        "topic": "Leave-one-out Cross Validation (Basics Q4)",
        "question_en": "Describe Leave-one-out cross validation.",
        "question_cn": "描述留一法交叉验证 (LOOCV)。",
        "solution_en": "An extreme case of k-fold CV where k equals the number of data points (N). We train on N-1 sample and test on 1 sample, repeating this N times. It is computationally expensive but uses almost all data for training.",
        "solution_cn": "k折交叉验证的极端情况，其中k等于数据点的数量(N)。我们在N-1个样本上训练并在1个样本上测试，重复N次。计算成本很高，但几乎使用了所有数据进行训练。"
    },
    {
        "topic": "Generalisation (Basics Q5)",
        "question_en": "What is Generalisation?",
        "question_cn": "什么是泛化？",
        "solution_en": "The ability of a trained model to perform well on new, unseen data, not just the data it was trained on. Poor generalisation often implies overfitting.",
        "solution_cn": "训练好的模型在新的、未见过的数据上也能表现良好的能力，而不仅仅是在训练数据上。泛化能力差通常意味着过拟合。"
    },
    {
        "topic": "Extrapolation vs Interpolation (Basics Q6)",
        "question_en": "Give examples of Extrapolation and Interpolation.",
        "question_cn": "举例说明外推和内插。",
        "solution_en": "<b>Extrapolation</b>: Predicting outside the range of training data, e.g., Weather forecasting into the future.<br/><b>Interpolation</b>: Predicting within the range of known data, e.g., Predicting a student's grade based on attendance using relation learnt from the rest of the class.",
        "solution_cn": "<b>外推</b>：在训练数据范围之外进行预测，例如：未来的天气预报。<br/><b>内插</b>：在已知数据范围内进行预测，例如：根据从班级其他同学那里学到的关系，利用出勤率预测某个学生的成绩。"
    },
    {
        "topic": "Objective Function (Basics Q7)",
        "question_en": "What is an Objective Function?",
        "question_cn": "什么是目标函数？",
        "solution_en": "A function to be minimised or maximised (e.g., cost function or loss function) to estimate the best parameters for a model.",
        "solution_cn": "用于估计模型最佳参数的需要最小化或最大化的函数（例如成本函数或损失函数）。"
    },
    {
        "topic": "Circular Analysis (Basics Q8)",
        "question_en": "Define Circular Analysis and give an example.",
        "question_cn": "定义循环分析并举例。",
        "solution_en": "Selecting analysis details/parameters using the test data itself.<br/><b>Example</b>: Adjusting fMRI preprocessing parameters to get the 'best' result on the test data. This invalidates the test result (data leakage).",
        "solution_cn": "使用测试数据本身选择分析细节/参数。<br/><b>例子</b>：调整 fMRI 预处理参数以在测试数据上获得“最佳”结果。这会使测试结果无效（数据泄漏）。"
    },
    {
        "topic": "Expectation Equation (Entropy Q1)",
        "question_en": "Write equation for expectation of a function f(X) of discrete random variable X.",
        "question_cn": "写出离散随机变量 X 的函数 f(X) 的期望方程。",
        "solution_en": "E[f(X)] = ∑ p(x<sub>i</sub>) f(x<sub>i</sub>).",
        "solution_cn": "E[f(X)] = ∑ p(x<sub>i</sub>) f(x<sub>i</sub>)。"
    },
    {
        "topic": "Entropy Equation (Entropy Q2)",
        "question_en": "Write the equation for entropy of discrete random variable X.",
        "question_cn": "写出离散随机变量 X 的熵方程。",
        "solution_en": "H[X] = - ∑ p(x<sub>i</sub>) log p(x<sub>i</sub>).",
        "solution_cn": "H[X] = - ∑ p(x<sub>i</sub>) log p(x<sub>i</sub>)。"
    },
    {
        "topic": "Log Base (Entropy Q3)",
        "question_en": "What base do you need to use for your log to get an answer in bits?",
        "question_cn": "你需要使用什么底数的对数才能得到以比特 (bits) 为单位的答案？",
        "solution_en": "Base 2.",
        "solution_cn": "底数 2。"
    },
    {
        "topic": "Entropy of Dice (Entropy Q4)",
        "question_en": "What is the entropy of a fair dice roll, in bits?",
        "question_cn": "掷公平骰子的熵是多少（比特）？",
        "solution_en": "The 6 outcomes have probability 1/6.<br/>H = - ∑ (1/6) log<sub>2</sub>(1/6) = - log<sub>2</sub>(1/6) = log<sub>2</sub>(6) ≈ 2.585 bits.",
        "solution_cn": "6个结果的概率均为 1/6。<br/>H = - ∑ (1/6) log<sub>2</sub>(1/6) = - log<sub>2</sub>(1/6) = log<sub>2</sub>(6) ≈ 2.585 比特。"
    },
    {
        "topic": "Entropy of Coin (Entropy Q5)",
        "question_en": "What is the entropy of an unfair coin toss (90% chance of heads)?",
        "question_cn": "不公平抛硬币（90% 几率正面向上）的熵是多少？",
        "solution_en": "P(H)=0.9, P(T)=0.1.<br/>H = - (0.9 log<sub>2</sub> 0.9 + 0.1 log<sub>2</sub> 0.1) ≈ 0.469 bits.",
        "solution_cn": "P(H)=0.9, P(T)=0.1。<br/>H = - (0.9 log<sub>2</sub> 0.9 + 0.1 log<sub>2</sub> 0.1) ≈ 0.469 比特。"
    },
    {
        "topic": "Conditional Entropy (Entropy Q6)",
        "question_en": "Define conditional entropy (in words).",
        "question_cn": "定义条件熵（用文字描述）。",
        "solution_en": "The expectation (over Y) of the entropy of X given Y. It represents the uncertainty remaining in X after observing Y.",
        "solution_cn": "给定 Y 时 X 的熵的（关于 Y 的）期望。它表示在观察到 Y 后 X 中剩余的不确定性。"
    },
    {
        "topic": "Entropy Calculation (Entropy Q7)",
        "question_en": "Calculate conditional entropy of rain given cloud state.<br/>P(Cloud)=0.8, P(Rain|Cloud)=0.3, P(Rain|NoCloud)=0.05.",
        "question_cn": "计算给定云状态下雨的条件熵。<br/>P(Cloud)=0.8, P(Rain|Cloud)=0.3, P(Rain|NoCloud)=0.05。",
        "solution_en": "H(Rain|Cloud) (p=0.3) = 0.88<br/>H(Rain|NoCloud) (p=0.05) = 0.29<br/>H(Rain|C) = P(C)H(R|C) + P(~C)H(R|~C)<br/>= 0.8 × 0.88 + 0.2 × 0.29 = 0.76 bits.",
        "solution_cn": "H(Rain|Cloud) (p=0.3) = 0.88<br/>H(Rain|NoCloud) (p=0.05) = 0.29<br/>H(Rain|C) = P(C)H(R|C) + P(~C)H(R|~C)<br/>= 0.8 × 0.88 + 0.2 × 0.29 = 0.76 比特。"
    },
    {
        "topic": "Information Gain (Entropy Q8)",
        "question_en": "Define Information Gain.",
        "question_cn": "定义信息增益。",
        "solution_en": "The expected reduction in entropy given new information.<br/>IG(Y, X) = H(X) - H(X|Y).",
        "solution_cn": "给定新信息后的预期熵减少量。<br/>IG(Y, X) = H(X) - H(X|Y)。"
    },
    {
        "topic": "Marginal Probability (Entropy Q9)",
        "question_en": "Using example in Q7, what is the marginal probability of rain?",
        "question_cn": "使用 Q7 中的示例，下雨的边缘概率是多少？",
        "solution_en": "P(Rain) = P(R|C)P(C) + P(R|~C)P(~C)<br/>= 0.3×0.8 + 0.05×0.2<br/>= 0.24 + 0.01 = 0.25 (25%).",
        "solution_cn": "P(Rain) = P(R|C)P(C) + P(R|~C)P(~C)<br/>= 0.3×0.8 + 0.05×0.2<br/>= 0.24 + 0.01 = 0.25 (25%)。"
    },
    {
        "topic": "Entropy Comparison (Entropy Q10)",
        "question_en": "What is the entropy of rain/no-rain? Confirm it is not less than the conditional entropy.",
        "question_cn": "下雨/不下雨的熵是多少？确认它小于条件熵。",
        "solution_en": "Using P(Rain)=0.25:<br/>H(R) = -(0.25 log<sub>2</sub> 0.25 + 0.75 log<sub>2</sub> 0.75) ≈ 0.81 bits.<br/>0.81 (Unconditional) ≥ 0.76 (Conditional in Q7). Holds true.",
        "solution_cn": "使用 P(Rain)=0.25:<br/>H(R) = -(0.25 log<sub>2</sub> 0.25 + 0.75 log<sub>2</sub> 0.75) ≈ 0.81 比特。<br/>0.81 (无条件) ≥ 0.76 (Q7中的条件熵)。成立。"
    },
    {
        "topic": "Performance Metrics (End-to-End Q1)",
        "question_en": "How to compute: (a) RMSE, (b) Mean Absolute Error, (c) Negative Log-Predictive Density (NLPD).",
        "question_cn": "如何计算：(a) 均方根误差 (RMSE)，(b) 平均绝对误差，(c) 负对数预测密度 (NLPD)。",
        "solution_en": "(a) RMSE: √( 1/N ∑ (y - y<sub>pred</sub>)<sup>2</sup> )<br/>(b) MAE: 1/N ∑ |y - y<sub>pred</sub>|<br/>(c) NLPD: - 1/N ∑ log p(y<sub>i</sub> | x<sub>i</sub>) (Evaluates probabilistic forecasts)",
        "solution_cn": "(a) RMSE: √( 1/N ∑ (y - y<sub>pred</sub>)<sup>2</sup> )<br/>(b) MAE: 1/N ∑ |y - y<sub>pred</sub>|<br/>(c) NLPD: - 1/N ∑ log p(y<sub>i</sub> | x<sub>i</sub>) (评估概率预测)"
    },
    {
        "topic": "Confusion Matrix (End-to-End Q2)",
        "question_en": "Draw confusion matrix. 10 Bees (7 correct, 2 wasp, 1 fly). 5 Wasps (all correct). 8 Flies (4 correct, 4 wasp).",
        "question_cn": "绘制混淆矩阵。10只蜜蜂（7只正确，2只黄蜂，1只苍蝇）。5只黄蜂（全部正确）。8只苍蝇（4只正确，4只黄蜂）。",
        "solution_en": "Rows(True)/Cols(Pred):<br/>Bee: [7,2,1]<br/>Wasp: [0,5,0]<br/>Fly: [0,4,4]",
        "solution_cn": "行(真实)/列(预测):<br/>蜜蜂: [7,2,1]<br/>黄蜂: [0,5,0]<br/>苍蝇: [0,4,4]"
    },
    {
        "topic": "Time Series Validation (End-to-End Q3)",
        "question_en": "Traffic prediction using random cross-validation works well. (a) Problem? (b) Solution?",
        "question_cn": "使用随机交叉验证的交通预测效果很好。(a) 问题？(b) 解决方案？",
        "solution_en": "(a) <b>Data Leakage</b>: Neighbouring times are highly correlated. Random split allows training on t+1 to predict t.<br/>(b) Use <b>Time-Series Split</b> (Train on past, Test on future) or split by different days to ensure independence.",
        "solution_cn": "(a) <b>数据泄漏</b>：相邻时间高度相关。随机分割允许利用 t+1 的数据训练来预测 t。<br/>(b) 使用<b>时间序列分割</b>（在过去的数据上训练，在未来的数据上测试）或按不同的日期分割以确保独立性。"
    },
    {
        "topic": "Decision Trees - Purity (DT Q1)",
        "question_en": "How is 'purity' used in decision trees?",
        "question_cn": "如何在决策树中使用“纯度”？",
        "solution_en": "We choose split features to maximize purity of child nodes. Purity means labels are unmixed (low entropy/Gini for classification) or low variance (for regression).",
        "solution_cn": "我们选择分裂特征以最大化子节点的纯度。纯度意味着标签未混合（分类中低熵/基尼系数）或低方差（回归中）。"
    },
    {
        "topic": "Information Gain Calculation (DT Q2)",
        "question_en": "Calculate Information Gain for 'vibration' feature. 16 turbines, H[state]=0.95. Vib: 8 (5 fail, 3 ok). No Vib: 8 (1 fail, 7 ok).",
        "question_cn": "计算“振动”特征的信息增益。16台涡轮机，H[state]=0.95。振动：8（5故障，3正常）。无振动：8（1故障，7正常）。",
        "solution_en": "H[state|vib] = 0.75.<br/>IG = 0.95 - 0.75 = 0.2 bits.",
        "solution_cn": "H[state|vib] = 0.75.<br/>IG = 0.95 - 0.75 = 0.2 比特。"
    },
    {
        "topic": "Overfitting in Trees (DT Q3)",
        "question_en": "How to avoid overfitting in decision trees?",
        "question_cn": "如何避免决策树中的过拟合？",
        "solution_en": "Pruning (pre-pruning: limit depth; or post-pruning: remove nodes).",
        "solution_cn": "剪枝（预剪枝：限制深度；或后剪枝：移除节点）。"
    },
    {
        "topic": "Bagging Confidence Interval (Ensemble Q1)",
        "question_en": "How to use bagging for 95% CI on NN prediction?",
        "question_cn": "如何使用 Bagging 进行神经网络预测的 95% 置信区间？",
        "solution_en": "1. Resample training data with replacement (bootstrap).<br/>2. Train multiple models.<br/>3. Get distribution of predictions.<br/>4. Find 2.5% and 97.5% percentiles of the predictions.",
        "solution_cn": "1. 有放回地重采样训练数据 (Bootstrap)。<br/>2. 训练多个模型。<br/>3. 获取预测分布。<br/>4. 找到预测值的 2.5% 和 97.5% 分位数。"
    },
    {
        "topic": "Random Forest Steps (Ensemble Q2)",
        "question_en": "Explain Random Forest algorithm.",
        "question_cn": "解释随机森林算法。",
        "solution_en": "1. <b>Bootstrap</b>: Generate samples with replacement.<br/>2. <b>Build Trees</b>: Train decision trees on samples.<br/>3. <b>Subspace Sampling</b>: At each split, consider only a random subset of features.<br/>4. <b>Aggregate</b>: Majority vote (classification) or average (regression).",
        "solution_cn": "1. <b>Bootstrap</b>：有放回地生成样本。<br/>2. <b>构建树</b>：在样本上训练决策树。<br/>3. <b>子空间采样</b>：在每个分裂处，仅考虑随机的特征子集。<br/>4. <b>聚合</b>：多数投票（分类）或平均（回归）。"
    },
    {
        "topic": "Linear Regression SSE (LR Q1)",
        "question_en": "Write sum-squared error (SSE) in vector notation.",
        "question_cn": "用向量符号写出平方误差和 (SSE)。",
        "solution_en": "(y - Xw)<sup>T</sup>(y - Xw).",
        "solution_cn": "(y - Xw)<sup>T</sup>(y - Xw)。"
    },
    {
        "topic": "Mean Absolute Error (LR Q2)",
        "question_en": "Expression for Mean Absolute Error.",
        "question_cn": "平均绝对误差的表达式。",
        "solution_en": "1/N ∑ |y<sub>i</sub> - [X]<sub>i:</sub>w|.",
        "solution_cn": "1/N ∑ |y<sub>i</sub> - [X]<sub>i:</sub>w|。"
    },
    {
        "topic": "Gradients (LR Q3)",
        "question_en": "Differentiate SSE and MAE wrt w.",
        "question_cn": "对 SSE 和 MAE 关于 w 求导。",
        "solution_en": "<b>SSE grad</b>: -2X<sup>T</sup>(y - Xw).<br/><b>MAE grad</b>: -1/N ∑ [X]<sub>i:</sub> sgn(y<sub>i</sub> - [X]<sub>i:</sub>w).",
        "solution_cn": "<b>SSE 梯度</b>：-2X<sup>T</sup>(y - Xw)。<br/><b>MAE 梯度</b>：-1/N ∑ [X]<sub>i:</sub> sgn(y<sub>i</sub> - [X]<sub>i:</sub>w)。"
    },
    {
        "topic": "Likelihood vs SSE (LR Q4)",
        "question_en": "Show maximizing likelihood with Gaussian noise is equivalent to minimizing SSE.",
        "question_cn": "证明在具有高斯噪声的情况下最大化似然等同于最小化 SSE。",
        "solution_en": "Gaussian Likelihood includes term exp(-SSE). Maximizing log-likelihood involves maximizing -SSE, which is equivalent to Minimizing SSE.",
        "solution_cn": "高斯似然包含 exp(-SSE) 项。最大化对数似然涉及最大化 -SSE，这等同于最小化 SSE。"
    },
    {
        "topic": "Design Matrix (LR Q5)",
        "question_en": "Design matrix for 3rd order polynomial with inputs 2, 3, 4, 6, 8.",
        "question_cn": "输入为 2, 3, 4, 6, 8 的 3 阶多项式的设计矩阵。",
        "solution_en": "Rows are [1, x, x<sup>2</sup>, x<sup>3</sup>].<br/>E.g., row 1: [1, 2, 4, 8].",
        "solution_cn": "行是 [1, x, x<sup>2</sup>, x<sup>3</sup>]。<br/>例如，第 1 行：[1, 2, 4, 8]。"
    },
    {
        "topic": "L2 Regularization (LR Q6)",
        "question_en": "What to add to cost function for L2 regularization?",
        "question_cn": "为了 L2 正则化，需要在成本函数中添加什么？",
        "solution_en": "Add λw<sup>T</sup>w (penalty on squared weights).",
        "solution_cn": "添加 λw<sup>T</sup>w （对权重平方的惩罚）。"
    },
    {
        "topic": "L1 Regularization (LR Q7)",
        "question_en": "What to add for L1 regularization?",
        "question_cn": "为了 L1 正则化，需要添加什么？",
        "solution_en": "Add λ ∑ |w<sub>i</sub>| (penalty on absolute weights). Promotes sparsity.",
        "solution_cn": "添加 λ ∑ |w<sub>i</sub>| （对权重绝对值的惩罚）。促进稀疏性。"
    },
    {
        "topic": "Gaussian Process Covariance (GP Q1)",
        "question_en": "Exponential kernel k(x,x')=e<sup>-|x-x'|/10</sup>. Train: (1,2), (3,4). Test: 2. Compute k<sub>*f</sub> and K<sub>ff</sub>.",
        "question_cn": "指数核 k(x,x')=e<sup>-|x-x'|/10</sup>。训练点：(1,2), (3,4)。测试点：2。计算 k<sub>*f</sub> 和 K<sub>ff</sub>。",
        "solution_en": "k<sub>*f</sub> = [k(2,1), k(2,3)] ≈ [0.90, 0.90].<br/>K<sub>ff</sub> = [[k(1,1), k(1,3)], [k(3,1), k(3,3)]] ≈ [[1, 0.82], [0.82, 1]].<br/>Posterior mean = k<sub>*f</sub> K<sup>-1</sup> y ≈ 2.99.",
        "solution_cn": "k<sub>*f</sub> = [k(2,1), k(2,3)] ≈ [0.90, 0.90].<br/>K<sub>ff</sub> = [[k(1,1), k(1,3)], [k(3,1), k(3,3)]] ≈ [[1, 0.82], [0.82, 1]].<br/>后验均值 = k<sub>*f</sub> K<sup>-1</sup> y ≈ 2.99。"
    },
    {
        "topic": "GP Definition (GP Q4)",
        "question_en": "Define Gaussian Process.",
        "question_cn": "定义高斯过程。",
        "solution_en": "A stochastic process where every finite collection of random variables has a multivariate normal distribution.",
        "solution_cn": "一种随机过程，其中每个有限的随机变量集合都服从多元正态分布。"
    },
    {
        "topic": "Uncertainty in Lengthscale (GP Q5)",
        "question_en": "How to handle uncertainty in lengthscale?",
        "question_cn": "如何处理长度尺度的不确定性？",
        "solution_en": "<b>Bayesian approach</b>: Place a hyperprior on the lengthscale and integrate it out (marginalize), or approximate by sampling from the hyperprior and averaging predictions.",
        "solution_cn": "<b>贝叶斯方法</b>：如果对长度尺度设置超先验并将其积分掉（边缘化），或者通过从超先验采样并平均预测结果来近似。"
    },
    {
        "topic": "Kernel Trick (Kernel Q1)",
        "question_en": "Review shape of XX<sup>T</sup> vs X<sup>T</sup>X. Which is easier to invert?",
        "question_cn": "回顾 XX<sup>T</sup> 与 X<sup>T</sup>X 的形状。哪一个更容易求逆？",
        "solution_en": "If N (data points) > D (features), X<sup>T</sup>X (DxD) is smaller/easier. If D >> N, XX<sup>T</sup> (NxN) is smaller. Kernel trick uses NxN Gram matrix.",
        "solution_cn": "如果 N (数据点) > D (特征)，则 X<sup>T</sup>X (DxD) 更小/更容易。如果 D >> N，则 XX<sup>T</sup> (NxN) 更小。核技巧使用 NxN Gram 矩阵。"
    }
]

part2_data = [
    {
        "topic": "PART 2: ADVANCED",
        "question_en": "SECTION HEADER",
        "question_cn": "第二部分：高阶内容",
        "solution_en": "SECTION HEADER",
        "solution_cn": "SECTION HEADER"
    },
    {
        "topic": "Bernoulli Distribution (Q2.1)",
        "question_en": "Write the Bernoulli distribution equations for P(Y=1) and P(Y=0), and combine them into a single equation P(Y=y).",
        "question_cn": "写出 P(Y=1) 和 P(Y=0) 的伯努利分布方程，并将它们合并为一个方程 P(Y=y)。",
        "solution_en": "P(Y=1) = π, P(Y=0) = 1-π.<br/>Combined: P(Y=y) = π<sup>y</sup> (1-π)<sup>1-y</sup>.",
        "solution_cn": "P(Y=1) = π, P(Y=0) = 1-π。<br/>合并后：P(Y=y) = π<sup>y</sup> (1-π)<sup>1-y</sup>。"
    },
    {
        "topic": "Log-Likelihood (Q2.4)",
        "question_en": "Given independent samples x<sub>i</sub> with outcomes y<sub>i</sub>, write the likelihood L and the negative log-likelihood.",
        "question_cn": "给定具有结果 y<sub>i</sub> 的独立样本 x<sub>i</sub>，写出似然 L 和负对数似然。",
        "solution_en": "Likelihood L = ∏ p(x<sub>i</sub>; y<sub>i</sub>).<br/>Negative log-likelihood = -∑ log p(x<sub>i</sub>; y<sub>i</sub>).",
        "solution_cn": "似然 L = ∏ p(x<sub>i</sub>; y<sub>i</sub>)。<br/>负对数似然 = -∑ log p(x<sub>i</sub>; y<sub>i</sub>)。"
    },
    {
        "topic": "Logistic Regression Optimization",
        "question_en": "Derive the derivative of the log-probability for logistic regression using π(x<sub>i</sub>) = Sigmoid(w<sup>T</sup> x<sub>i</sub>).",
        "question_cn": "使用 π(x<sub>i</sub>) = Sigmoid(w<sup>T</sup> x<sub>i</sub>) 推导逻辑回归对数概率的导数。",
        "solution_en": "Log-prob involves y<sub>i</sub> log π + (1-y<sub>i</sub>) log(1-π). Sigmoid derivative is π(1-π).<br/>Result is complex but solvable with gradient descent (iterative).",
        "solution_cn": "对数概率涉及 y<sub>i</sub> log π + (1-y<sub>i</sub>) log(1-π)。Sigmoid 导数是 π(1-π)。<br/>结果复杂，但可用梯度下降（迭代）求解。"
    },
    {
        "topic": "Auto-differentiation (Q3.2)",
        "question_en": "What are the adjoints for reverse mode vs forward mode auto-differentiation?",
        "question_cn": "反向模式与前向模式自动微分的伴随变量（adjoints）分别是什么？",
        "solution_en": "<b>Reverse mode</b>: Adjoints v&#772;<sub>i</sub> = ∂Output / ∂v<sub>i</sub> (Propagates gradient backwards).<br/><b>Forward mode</b>: Adjoints v&#775;<sub>i</sub> = ∂v<sub>i</sub> / ∂Input (Propagates derivatives forwards).",
        "solution_cn": "<b>反向模式</b>：伴随变量 v&#772;<sub>i</sub> = ∂输出 / ∂v<sub>i</sub> （向后传播梯度）。<br/><b>前向模式</b>：伴随变量 v&#775;<sub>i</sub> = ∂v<sub>i</sub> / ∂输入 （向前传播导数）。"
    },
    {
        "topic": "Neural Networks - Hidden Layers (Q4.3)",
        "question_en": "Why do we use hidden layers in neural networks?",
        "question_cn": "为什么我们在神经网络中使用隐藏层？",
        "solution_en": "They allow learning non-linear decision boundaries and hierarchical features. Without them, NN is just a linear model.",
        "solution_cn": "它们允许学习非线性决策边界和分层特征。如果没有它们，神经网络就只是一个线性模型。"
    },
    {
        "topic": "NN Dimensions (Q4.6)",
        "question_en": "For images of size 30x45 and 5 classes, what is the input size for the first layer (if flattened) and output size?",
        "question_cn": "对于尺寸为 30x45 的图像和 5 个类别，第一层的输入尺寸（如果展平）和输出尺寸是多少？",
        "solution_en": "Input: 30 × 45 = 1350 units.<br/>Output: 5 units (one-hot encoding).",
        "solution_cn": "输入：30 × 45 = 1350 个单元。<br/>输出：5 个单元（独热编码）。"
    },
    {
        "topic": "CNN Output Size (Q5.2)",
        "question_en": "Calculate CNN output size. Image N=28, Filter F=5, Padding P=2, Stride S=1. Also for S=2.",
        "question_cn": "计算 CNN 输出尺寸。图像 N=28，滤波器 F=5，填充 P=2，步幅 S=1。以及 S=2 的情况。",
        "solution_en": "O = (N - F + 2P)/S + 1.<br/>S=1: (28-5+4)/1 + 1 = 28.<br/>S=2: (28-5+4)/2 + 1 = 14.5 -> 14 (floor).",
        "solution_cn": "O = (N - F + 2P)/S + 1。<br/>S=1: (28-5+4)/1 + 1 = 28。<br/>S=2: (28-5+4)/2 + 1 = 14.5 -> 14 (向下取整)。"
    },
    {
        "topic": "CNN Architecture (Q5.3)",
        "question_en": "Suggest a simple CNN architecture for 30x45 RGB images with 5 classes.",
        "question_cn": "为具有 5 个类别的 30x45 RGB 图像建议一个简单的 CNN 架构。",
        "solution_en": "Input(30x45x3) -> Conv(F=7) -> ReLU -> Conv(F=5, S=3) -> ReLU -> FC(600) -> Output(5).",
        "solution_cn": "输入(30x45x3) -> 卷积(F=7) -> ReLU -> 卷积(F=5, S=3) -> ReLU -> 全连接(600) -> 输出(5)。"
    },
    {
        "topic": "PCA Optimization (Q6.5)",
        "question_en": "What is the optimisation criterion for the first principal component u<sub>1</sub>?",
        "question_cn": "第一主成分 u<sub>1</sub> 的优化标准是什么？",
        "solution_en": "Maximize variance: u<sub>1</sub><sup>T</sup> C u<sub>1</sub> subject to ||u<sub>1</sub>||=1.<br/>Equivalent to minimising reconstruction error.",
        "solution_cn": "最大化方差：u<sub>1</sub><sup>T</sup> C u<sub>1</sub>，约束条件为 ||u<sub>1</sub>||=1。<br/>等同于最小化重构误差。"
    },
    {
        "topic": "Auto-encoders (Q6.6/6.7)",
        "question_en": "Describe Auto-encoder shape and use for dimensionality reduction.",
        "question_cn": "描述自动编码器的形状及其在降维中的用途。",
        "solution_en": "Hourglass shape: Encoder shrinks input to latent space (bottleneck); Decoder expands back. For reduction, use only the Encoder.",
        "solution_cn": "沙漏形状：编码器将输入缩小到潜在空间（瓶颈）；解码器将其展开。对于降维，仅使用编码器。"
    },
    {
        "topic": "K-Means Failures (Q7.3)",
        "question_en": "When does K-means clustering fail?",
        "question_cn": "K-means 聚类何时失效？",
        "solution_en": "Non-spherical clusters (e.g., moons), different variances/densities, or significant outliers.",
        "solution_cn": "非球形聚类（例如月牙形），不同的方差/密度，或显著的异常值。"
    },
    {
        "topic": "Normalized Cut (Q7.5)",
        "question_en": "Define Normalized Cut (Ncut) between sets A and B.",
        "question_cn": "定义集合 A 和 B 之间的归一化割 (Normalized Cut) 。",
        "solution_en": "Ncut(A,B) = Cut(A,B)/Vol(A) + Cut(A,B)/Vol(B).<br/>Normalized by volume (total degrees), encouraging balanced clusters.",
        "solution_cn": "Ncut(A,B) = Cut(A,B)/Vol(A) + Cut(A,B)/Vol(B)。<br/>按体积（总度数）归一化，鼓励平衡的聚类。"
    },
    {
        "topic": "Naive Bayes Assumption (Q8.2)",
        "question_en": "What is the key assumption for Naive Bayes classifier?",
        "question_cn": "朴素贝叶斯分类器的关键假设是什么？",
        "solution_en": "Features are conditionally independent given the class label.",
        "solution_cn": "在给定类别标签的情况下，特征是条件独立的。"
    },
    {
        "topic": "ELBO (Q8.7)",
        "question_en": "Explain the Evidence Lower Bound (ELBO).",
        "question_cn": "解释证据下界 (ELBO)。",
        "solution_en": "A lower bound on the log-evidence (log p(x)). Maximizing ELBO minimizes KL divergence between approximate posterior and true posterior.",
        "solution_cn": "对数证据 (log p(x)) 的下界。最大化 ELBO 可最小化近似后验与真实后验之间的 KL 散度。"
    }
]

combined_data = part1_data + part2_data

with open('revision_questions.json', 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)

print(f"JSON file created: revision_questions.json with {len(combined_data)} items.")
