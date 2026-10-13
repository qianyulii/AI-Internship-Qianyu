# AI 科研实践实习任务书 v2.2

来源：[飞书原文](https://my.feishu.cn/wiki/CYRGwckoIiIBcckhkCHcTREUnzi)  
作者：张志琳 · 原文版本：v2.2 · 页面显示修改时间：8月11日修改  
本地保存时间：2026-10-11 23:40 CDT  
保存方式：从 Chrome 中可阅读的正文逐段归档，保留标题、任务、表格、代码目录和资源链接；此文件是本地快照。

> 这是一份面向你个人的 8 周实习任务书。你需要按照每周要求完成项目、提交代码、记录实验、整理报告，并在最后形成一个可以展示的 AI 项目作品集。

---

<a id="KxZfd2dd1ohqFyx9HnJcL4bBnUc"></a>

## 一、使用方式

<a id="Kxqmddci9oYdFfxWG8OcnhWnnjh"></a>

### 你需要先完成的基础准备

- [ ] 建立 GitHub 或 Gitee 个人项目仓库

- [ ] 建立 Kaggle 账号并完善个人主页

- [ ] 按周建立项目目录

- [ ] 每周按要求提交代码、图表、实验结果和报告

- [ ] 最终形成一篇完整技术文章和答辩 PPT

<a id="XbpGdRRUhonVevxLtwacw0sfnlf"></a>

### 建议仓库命名

```text
AI-Internship-你的姓名
```

<a id="WskrdoKBNo75T1xnwgLcPvH0n1b"></a>

### 建议仓库结构

```text
AI-Internship-你的姓名/
├─ README.md
├─ Week01_AI_Basic_Iris_Regression/
├─ Week02_ML_Practical_Projects/
├─ Week03_Kaggle_Tabular/
├─ Week04_LeNet_MNIST/
├─ Week05_ResNet_Transformer/
├─ Week06_DogBreed_FaceRecognition/
├─ Week07_LocalLLM_RAG/
├─ Week08_Final_Report/
└─ docs/
```

<a id="HVojdczjhoNZT6xXQEQcoFB6nYb"></a>

### 每周目录统一要求

```text
WeekXX_ProjectName/
├─ README.md
├─ notebooks/
├─ src/
├─ data_source.md
├─ results/
│  ├─ figures/
│  ├─ metrics.csv
│  └─ screenshots/
├─ error_analysis.md
├─ report.md
└─ run_log.txt
```

---

<a id="HLp3dbZW1ory4dxR4KPcLs1Hnrh"></a>

## 二、8 周任务总览

| 周次 | 核心主题 | 你需要完成的主要任务 | 周提交重点 |
| --- | --- | --- | --- |
| 第 1 周 | AI 认知、工具流、Iris 与线性回归 | GitHub/Kaggle 初始化；Iris 分类；线性回归 | 仓库链接、Kaggle 主页、2 个基础 ML 项目 |
| 第 2 周 | 传统机器学习实战 | 信用卡违约预测；糖尿病预测；2 个选做 ML 项目 | 至少 4 个 ML 项目、图表、模型对比 |
| 第 3 周 | Kaggle 表格竞赛 | Titanic；House Prices | 两个 Kaggle 项目、多模型对比、提交截图 |
| 第 4 周 | LeNet-5 论文复现 | LeNet + MNIST | PyTorch 代码、训练曲线、准确率、复现报告 |
| 第 5 周 | ResNet 复现 + Transformer 启动 | ResNet + CIFAR-10；Transformer 初读 | ResNet 实验、消融实验、Transformer 初步笔记 |
| 第 6 周 | Dog Breed + 人脸识别进阶 | Dog Breed 迁移学习；人脸识别选做 | Kaggle 提交、Top-1/Top-5、人脸识别选做 |
| 第 7 周 | Transformer + 本地大模型 + RAG | Transformer 精读；本地 LLM；RAG 论文问答 | Transformer 报告、本地模型截图、RAG Demo |
| 第 8 周 | 最终整合与答辩 | 技术文章；PPT；总仓库整理 | 最终文章、PPT、完整仓库、总实验表 |

---

<a id="XyEkdl1VGoKJ3vxbGpNcXApfnlh"></a>

## 三、项目与数据链接

<a id="GHBTdOOnqolgaDxtIuvcYrd1n72"></a>

### 1. AI 入门与工具学习

| 内容 | 链接 |
| --- | --- |
| 吴恩达 AI for Everyone | https://www.deeplearning.ai/courses/ai-for-everyone/ |
| 吴恩达 Generative AI for Everyone | https://www.deeplearning.ai/courses/generative-ai-for-everyone/ |
| 吴恩达 AI Prompting for Everyone | https://www.deeplearning.ai/courses/ai-prompting-for-everyone/ |
| Karpathy 大模型入门 | https://www.youtube.com/watch?v=zjkBMFhNj_g |

如果无法访问 YouTube，可在 B 站搜索：

```text
Andrej Karpathy 大模型入门
```

<a id="O2IpdtqTfo3G52xz0Lhc2EOJnDg"></a>

### 2. 基础机器学习项目

| 项目 | 数据链接 | 任务类型 |
| --- | --- | --- |
| Iris 鸢尾花分类 | https://archive.ics.uci.edu/dataset/53/iris | 多分类 |
| sklearn Iris 示例 | https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html | 示例参考 |
| California Housing | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html | 回归 |
| Diabetes Regression Dataset | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html | 回归 |

<a id="QxEVdIAIzowKpsxqbV9cFXPhnWd"></a>

### 3. 传统机器学习实战

| 项目 | 数据链接 | 推荐算法 |
| --- | --- | --- |
| 信用卡违约预测 | https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients | LR、DT、RF、XGBoost/LightGBM |
| 糖尿病预测 | https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database | LR、RF、XGBoost、SVM |
| 亚洲足球梯队聚类 | https://inside.fifa.com/fifa-world-ranking/men | KMeans、PCA、层次聚类 |
| 异常行为识别 | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud | Isolation Forest、One-Class SVM |
| Online Retail 用户行为 | https://archive.ics.uci.edu/dataset/352/online+retail | 用户行为分析、异常检测 |
| 学生成绩预测 | https://archive.ics.uci.edu/dataset/320/student+performance | 回归/分类、RF、XGBoost |
| 天气预测 Jena Climate | https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip | 时间序列、回归、LSTM 选做 |

<a id="UZhEdoCDmoK7GGxXNWrcWp8znWe"></a>

### 4. Kaggle 项目

| 项目 | 链接 | 要求 |
| --- | --- | --- |
| Titanic 生存预测 | https://www.kaggle.com/c/titanic | 至少 2 次提交 |
| House Prices 房价预测 | https://www.kaggle.com/c/house-prices-advanced-regression-techniques | 至少 2 次提交 |
| Dog Breed Identification | https://www.kaggle.com/c/dog-breed-identification | 至少 1 次提交 |

<a id="RqLHdjNaRovBFHxgGhacndG6nRc"></a>

### 5. 论文复现与精读

| 论文 | 链接 | 数据 |
| --- | --- | --- |
| LeNet-5 | http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf | https://yann.lecun.com/exdb/mnist/ |
| ResNet | https://arxiv.org/abs/1512.03385 | https://www.cs.toronto.edu/~kriz/cifar.html |
| Transformer | https://arxiv.org/abs/1706.03762 | 论文精读 |

<a id="HrOOduWaGoK9PcxYxKvc7nEGnVc"></a>

### 6. 人脸识别

| 内容 | 链接 |
| --- | --- |
| LFW 人脸数据集 | http://vis-www.cs.umass.edu/lfw/ |
| sklearn Olivetti Faces | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html |
| FaceNet 论文 | https://arxiv.org/abs/1503.03832 |

<a id="RuCId0EGtot04AxYuRBcZFtbn3b"></a>

### 7. 本地大模型与 RAG

| 工具 | 链接 |
| --- | --- |
| Ollama | https://ollama.com/ |
| LM Studio | https://lmstudio.ai/ |
| Chroma | https://www.trychroma.com/ |
| FAISS | https://github.com/facebookresearch/faiss |
| sentence-transformers | https://www.sbert.net/ |
| all-MiniLM-L6-v2 | https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2 |

---

<a id="HsImdZi6roJw2kxJiRZcIMiVnmf"></a>

## 四、每周任务详情

<a id="AXjFdgPR6o0jEuxR0F1c6vTHnJ0"></a>

### 第 1 周：AI 认知、工具流、Iris 与线性回归

<a id="BxRodkMaTovkxmxgNN3cBYclnwX"></a>

#### 本周目标

你需要完成 AI 基础认知、工具流搭建、GitHub/Kaggle 初始化，并完成两个基础机器学习项目。

<a id="Wu75d9z2LoncAzx0lrsccSNunWg"></a>

#### 你需要完成

- [ ] 注册 GitHub 或 Gitee

- [ ] 注册 Kaggle

- [ ] 创建个人实习总仓库

- [ ] 完成 Iris 鸢尾花分类

- [ ] 完成线性回归项目

- [ ] 记录 AI 工具使用过程

<a id="Ic4RdY0C2oU8glx7KbZcUhx8nRf"></a>

#### Iris 项目要求

- [ ] 读取 Iris 数据

- [ ] 输出数据基本信息

- [ ] 绘制类别分布图、特征散点图、相关性热力图

- [ ] 使用 Logistic Regression、KNN、Decision Tree

- [ ] 输出 Accuracy 和混淆矩阵

- [ ] 分析哪个特征对分类最有帮助

<a id="CIiNdP1tgoVtifxv73Nc5E3pnOe"></a>

#### 线性回归项目要求

- [ ] 使用 California Housing 或 Diabetes Regression 数据

- [ ] 分析目标变量分布

- [ ] 分析特征相关性

- [ ] 使用 Linear Regression

- [ ] 增加 Ridge 或 Random Forest Regressor 对比

- [ ] 输出 MSE、RMSE、MAE、R2

- [ ] 绘制真实值 vs 预测值图

<a id="FUwQdx1swonC0kxtFSXc1ogJnIf"></a>

#### 本周提交

```text
Week01_AI_Basic_Iris_Regression/
├─ README.md
├─ AI_认知与工具记录.md
├─ Iris_Classification.ipynb
├─ Linear_Regression.ipynb
├─ data_source.md
├─ results/
│  ├─ iris_confusion_matrix.png
│  ├─ iris_feature_plot.png
│  ├─ regression_pred_vs_true.png
│  └─ metrics.csv
├─ report.md
└─ run_log.txt
```

<a id="NlxkdxYJro7jV2x6J4Ccul5Xn4g"></a>

#### 本周验收标准

- [ ] GitHub/Gitee 仓库链接已提交

- [ ] Kaggle 主页链接已提交

- [ ] Iris 项目完整运行

- [ ] 线性回归项目完整运行

- [ ] 至少 6 张图

- [ ] 至少 2 个模型结果表

- [ ] 周报告不少于 1000 字

---

<a id="B5D9dG6kgobsyhxmtOdcxkgFnfb"></a>

### 第 2 周：传统机器学习实战专题

<a id="YY6sd9jl9oCmqHxt687cnepbnkT"></a>

#### 本周目标

你需要完成多个传统机器学习项目，建立分类、回归、聚类和异常检测的基本能力。

<a id="Tovad3CGzoewLUxuCuNcgk1Tns6"></a>

#### 必做项目

- [ ] 信用卡还款/违约预测

- [ ] 糖尿病预测与分析

<a id="LyzwdwQCUoyy0gxiqglcjv6LnYd"></a>

#### 选做项目，至少完成 2 个

- [ ] 聚类算法分析亚洲足球梯队

- [ ] 异常行为用户自动识别

- [ ] 学生成绩可视化与预测

- [ ] 天气数据可视化与预测

<a id="AaPldItLqoebZ7xgiRscvqHtnSf"></a>

#### 本周提交

```text
Week02_ML_Practical_Projects/
├─ Credit_Default_Prediction.ipynb
├─ Diabetes_Prediction.ipynb
├─ Optional_Project_1/
├─ Optional_Project_2/
├─ results/
│  ├─ model_comparison.csv
│  ├─ roc_curve.png
│  ├─ feature_importance.png
│  └─ optional_project_figures/
├─ report.md
└─ run_log.txt
```

<a id="CMg6diyHXo3FscxhXrccFYT8nmh"></a>

#### 本周验收标准

- [ ] 必做项目 2 个

- [ ] 选做项目至少 2 个

- [ ] 总计至少 4 个机器学习项目

- [ ] 至少 8 张图

- [ ] 至少 4 个模型对比表

- [ ] 周报告不少于 1500 字

---

<a id="E8T6dWQ86oJ1PTxryCucuB7qnLM"></a>

### 第 3 周：Kaggle 表格竞赛专题

<a id="REwddaUuyonQ7yxOaMacQOSpnCd"></a>

#### 本周目标

你需要完成 Titanic 和 House Prices 两个 Kaggle 项目，并进行多模型对比、特征工程和真实提交。

<a id="HSYzd7b0Lobhbrxj10wcbmjVnpe"></a>

#### Titanic 要求

- [ ] 完成 EDA

- [ ] 处理缺失值

- [ ] 完成 Title、FamilySize、IsAlone、Age 分箱、Fare 分箱

- [ ] 至少使用 4 个模型

- [ ] 至少完成 2 次 Kaggle 提交

- [ ] 记录每次提交分数

<a id="XGTMdxc1CogQffxsc85cV9YtnZK"></a>

#### House Prices 要求

- [ ] 完成 EDA

- [ ] 处理缺失值

- [ ] 类别变量编码

- [ ] 对 SalePrice 做 log 变换

- [ ] 至少使用 4 个模型

- [ ] 尝试模型融合

- [ ] 至少完成 2 次 Kaggle 提交

<a id="VITldcZe0o75z5x8JGocbH75nqd"></a>

#### 本周提交

```text
Week03_Kaggle_Tabular/
├─ Titanic_Advanced.ipynb
├─ House_Prices_Advanced.ipynb
├─ kaggle_submission_screenshots/
├─ results/
│  ├─ titanic_model_comparison.csv
│  ├─ house_model_comparison.csv
│  ├─ feature_engineering.md
│  └─ figures/
├─ report.md
└─ run_log.txt
```

<a id="RsH7dI9OUoiFoIxj4DfcJfmQnJh"></a>

#### 本周验收标准

- [ ] Titanic 至少 2 次 Kaggle 提交

- [ ] House Prices 至少 2 次 Kaggle 提交

- [ ] 每个项目至少 4 个模型

- [ ] 每个项目至少 5 张图

- [ ] 周报告不少于 1500 字

- [ ] 附 Kaggle 主页链接和提交截图

---

<a id="V4v2dgarCo89Gzx3s70cn61enPc"></a>

### 第 4 周：论文复现 1，LeNet-5 + MNIST

<a id="PAyWdUF5ioc6TGx1jIzc77itnJd"></a>

#### 本周目标

你需要使用 PyTorch 复现 LeNet-5 或简化版 LeNet，在 MNIST 数据集上完成 0-9 手写数字分类任务。

<a id="GzSwdhmINoZS59xkHBLc0q9tn0b"></a>

#### 你需要完成

- [ ] 阅读 LeNet 论文，整理 1-2 页笔记

- [ ] 用 PyTorch 搭建卷积层、池化层、全连接层

- [ ] 加载 MNIST 数据集

- [ ] 完成训练和测试

- [ ] 记录 loss 和 accuracy

- [ ] 测试集准确率目标达到 98% 左右

- [ ] 绘制训练 loss 曲线

- [ ] 绘制测试 accuracy 曲线

- [ ] 随机展示 10 张测试图片

- [ ] 分析至少 10 个错误分类样例

<a id="BGJrdkxZQoperHx9UrzcifJJnpb"></a>

#### 本周提交

```text
Week04_LeNet_MNIST/
├─ train.py
├─ model.py
├─ LeNet_MNIST.ipynb
├─ requirements.txt
├─ results/
│  ├─ loss_curve.png
│  ├─ accuracy_curve.png
│  ├─ prediction_examples.png
│  ├─ error_cases.png
│  └─ metrics.csv
├─ LeNet_paper_notes.md
├─ LeNet_reproduction_report.md
└─ run_log.txt
```

<a id="RAAwdVdqgogDOixTJd2c81Sxnzg"></a>

#### 本周验收标准

- [ ] 代码可运行

- [ ] 测试准确率达到 98% 左右

- [ ] 有训练曲线

- [ ] 有预测样例

- [ ] 有错误样例分析

- [ ] 复现报告不少于 1500 字

---

<a id="PH73d3St8oiwetxndHjcAuLknGb"></a>

### 第 5 周：ResNet 论文复现 + Transformer 精读启动

<a id="VaCwdDUU4owSedxSsBQcSgnbnuc"></a>

#### ResNet 要求

- [ ] 阅读 ResNet 论文

- [ ] 理解残差连接

- [ ] 实现 ResNet-18 或简化 ResNet

- [ ] 加载 CIFAR-10

- [ ] 完成训练和测试

- [ ] 对比普通 CNN 与 ResNet

- [ ] 至少做 2 个消融实验

<a id="EHAkd01hhoY5bxxbO5tcOvdGnqh"></a>

#### Transformer 初读要求

- [ ] 阅读摘要、引言、模型结构部分

- [ ] 结合老师提供的 Transformer 报告

- [ ] 整理 Transformer 结构图

- [ ] 初步解释 Self-Attention、Multi-Head Attention、Positional Encoding

<a id="SmRfdzu1ooJQhJx5GxGcfmT0nLg"></a>

#### 本周提交

```text
Week05_ResNet_Transformer/
├─ ResNet_CIFAR10.ipynb
├─ train_resnet.py
├─ model_resnet.py
├─ results/
│  ├─ cnn_vs_resnet.csv
│  ├─ ablation_study.csv
│  ├─ loss_curve.png
│  └─ accuracy_curve.png
├─ ResNet_paper_notes.md
├─ Transformer_initial_notes.md
├─ transformer_architecture_draft.png
└─ Week05_report.md
```

<a id="FzBJdkexvoit2BxBhp8cNakFnZb"></a>

#### 本周验收标准

- [ ] ResNet 代码可运行

- [ ] 有 CNN vs ResNet 对比

- [ ] 有至少 2 个消融实验

- [ ] 有 Transformer 初步笔记

- [ ] 周报告不少于 1800 字

---

<a id="XBNXdsITWoFbZZxtHvvcWZzCnfh"></a>

### 第 6 周：Dog Breed 图像识别 + 人脸识别进阶

<a id="DYzpdBZcfodJZQx0SM5cKHy0nKd"></a>

#### Dog Breed 要求

- [ ] 下载并整理图像数据

- [ ] 完成图像预处理

- [ ] 完成数据增强

- [ ] 使用 ResNet、EfficientNet、ConvNeXt 三选一

- [ ] 输出 Top-1 和 Top-5 指标

- [ ] 完成至少 1 次 Kaggle 提交

- [ ] 分析容易混淆的狗品种

<a id="JN93dBHpzorqkMxEgg4c0XbwnHf"></a>

#### 人脸识别进阶

- [ ] 加载 LFW 或 Olivetti Faces

- [ ] 展示人脸样例

- [ ] 训练一个简单分类模型

- [ ] 输出准确率和混淆矩阵

- [ ] 进阶：提取 embedding，计算人脸相似度

<a id="SHAYdggxMopnyixPJGcc83KPnsd"></a>

#### 本周提交

```text
Week06_DogBreed_FaceRecognition/
├─ Dog_Breed_Identification.ipynb
├─ Face_Recognition_Optional.ipynb
├─ kaggle_submission_screenshot.png
├─ results/
│  ├─ top1_top5_metrics.csv
│  ├─ dog_prediction_examples.png
│  ├─ dog_error_cases.png
│  ├─ face_examples.png
│  └─ face_metrics.csv
├─ report.md
└─ run_log.txt
```

<a id="GWGgdoxKMoRcnyxhBpdcngRnnTg"></a>

#### 本周验收标准

- [ ] Dog Breed 必做

- [ ] 至少完成 1 次 Kaggle 提交

- [ ] 必须使用迁移学习

- [ ] 必须有 Top-1/Top-5 指标

- [ ] 人脸识别为进阶任务，建议争取完成

- [ ] 周报告不少于 1500 字

---

<a id="WEbTdiU4noBndqxTkb2c23RRnLf"></a>

### 第 7 周：Transformer 精读 + 本地大模型部署 + RAG 项目

<a id="UHJidjAIVo3t3qxDMG1cNZnWnsg"></a>

#### Transformer 精读要求

- [ ] 完成 Transformer 论文精读

- [ ] 结合老师提供的 Transformer 报告

- [ ] 解释 Self-Attention、Q/K/V、Multi-Head Attention、Positional Encoding、Encoder、Decoder、Masked Attention、Feed Forward Network

- [ ] 画出 Transformer 架构图

- [ ] 说明 Transformer 为什么是大模型的重要基础

<a id="ZdD7dvZT3ovP7gxriT9c3iLunAg"></a>

#### 本地大模型部署要求

- [ ] 使用 Ollama 或 LM Studio

- [ ] 在本地电脑成功运行一个小模型

- [ ] 记录电脑配置

- [ ] 记录模型名称和参数量

- [ ] 截图证明模型可以对话

<a id="CHtqdaG5XosQ5GxVwLmcJdH6nOg"></a>

#### RAG 论文问答要求

- [ ] 使用至少 3 篇论文：LeNet、ResNet、Transformer

- [ ] 完成 PDF 解析

- [ ] 完成文本切分

- [ ] 完成向量化

- [ ] 建立向量库

- [ ] 实现论文问答

- [ ] 对比直接问大模型和 RAG 问答结果

<a id="AtjGdCbhZomreIxb7u4c8wKwn1e"></a>

#### 固定测试问题

1. LeNet 的核心结构是什么？

2. ResNet 的残差连接解决了什么问题？

3. Transformer 和 RNN 有什么区别？

4. Self-Attention 中 Q、K、V 分别是什么？

5. Multi-Head Attention 为什么有用？

6. Positional Encoding 的作用是什么？

7. Transformer 为什么能并行训练？

8. 三篇论文分别用了什么数据集？

9. RAG 比直接问大模型好在哪里？

10. RAG 系统失败的案例有哪些？

<a id="SeVudb3CmoC6q4xaJWQcthnQnfe"></a>

#### 本周提交

```text
Week07_LocalLLM_RAG/
├─ Transformer_reading_report.md
├─ transformer_architecture.png
├─ local_llm_screenshot.png
├─ rag_demo.py
├─ rag_notebook.ipynb
├─ papers_source.md
├─ rag_questions_answers.md
├─ direct_vs_rag_comparison.csv
├─ error_cases.md
└─ Week07_report.md
```

<a id="UQp8dDu93oPCZQx3lfecJnvQnPe"></a>

#### 本周验收标准

- [ ] Transformer 精读报告不少于 2000 字

- [ ] 本地模型成功运行

- [ ] RAG 系统能够回答固定问题

- [ ] 至少完成 10 组问答

- [ ] 有直接问模型 vs RAG 问答对比

- [ ] 有失败案例分析

---

<a id="XFyLdX0y5oadMzxbFatcMtnKnbe"></a>

### 第 8 周：最终整合、技术文章与答辩

<a id="PK44dXOgYoh0zPx3sHpcj0sznec"></a>

#### 最终提交内容

- [ ] GitHub/Gitee 总仓库链接

- [ ] Kaggle 主页链接

- [ ] Titanic 提交截图

- [ ] House Prices 提交截图

- [ ] Dog Breed 提交截图

- [ ] 所有机器学习项目代码

- [ ] LeNet 复现报告

- [ ] ResNet 复现报告

- [ ] Transformer 精读报告

- [ ] RAG 项目代码和截图

- [ ] 最终技术文章

- [ ] 答辩 PPT

- [ ] 总实验结果表

<a id="CHCDdHv3poJ7yvxJAbDctvnlnif"></a>

#### 最终文章结构

1. 项目背景

2. AI 工具与工作流

3. 传统机器学习项目

4. Kaggle 表格建模项目

5. LeNet 论文复现

6. ResNet 论文复现

7. Dog Breed 图像识别

8. Transformer 精读

9. 本地大模型与 RAG 系统

10. 实验结果汇总

11. 问题与改进

12. 总结

<a id="ALHudIqE1oifFFxDnVxcicTsn4e"></a>

#### 答辩 PPT 要求

PPT 不少于 15 页，建议结构：

1. 个人介绍

2. 实习任务总览

3. GitHub 仓库展示

4. Kaggle 主页展示

5. 传统机器学习项目展示

6. Titanic 项目展示

7. House Prices 项目展示

8. LeNet 复现展示

9. ResNet 复现展示

10. Dog Breed 项目展示

11. Transformer 精读展示

12. 本地大模型部署展示

13. RAG 系统展示

14. 总实验结果

15. 收获、不足与后续计划

---

<a id="JYtpdYBPoocDAex0znwcxuPBnyf"></a>

## 五、结业标准

<a id="Ql91d3jKroxLFQxeIBVcOaBonDb"></a>

### 合格

- [ ] 完成 GitHub/Gitee 仓库

- [ ] 完成 Kaggle 主页

- [ ] 完成至少 3 个传统机器学习项目

- [ ] 完成至少 1 个 Kaggle 项目

- [ ] 完成 LeNet 论文复现

- [ ] 提交最终报告

<a id="SLzId1lPHol8guxyFKqcKbV1nUf"></a>

### 良好

- [ ] 完成至少 5 个传统机器学习项目

- [ ] 完成 Titanic、House Prices、Dog Breed 三个 Kaggle 项目

- [ ] 完成 LeNet 和 ResNet 两篇论文复现

- [ ] 完成 Transformer 精读

- [ ] 完成本地大模型部署

- [ ] 提交最终文章和 PPT

<a id="N73rdKT8lo1jcixZhG2cRbbQneh"></a>

### 优秀

- [ ] 完成全部传统机器学习项目

- [ ] 完成全部 Kaggle 项目并有多模型对比

- [ ] 完成 LeNet、ResNet，并选做第三篇论文复现或人脸识别项目

- [ ] 完成可运行的 RAG 系统

- [ ] 最终文章结构完整、图表充分、实验详实

- [ ] 代码仓库清晰，可复现性强

---

<a id="V4iKde4BaojRKBx4oM4cPPx0nYe"></a>

## 六、特别强调

- [ ] 每周必须提交代码，不能只交截图

- [ ] 每周必须有实验结果表

- [ ] 每周必须有图表

- [ ] 每周必须写清楚数据来源

- [ ] 每周必须写清楚遇到的问题和解决方法

- [ ] 可以使用 AI 工具，但必须注明 AI 辅助内容

- [ ] 不允许直接复制 Kaggle Notebook 或 GitHub 代码却不说明来源

- [ ] 最终报告不能写成学习心得，必须写成项目型技术文章

- [ ] 如果某个项目运行失败，也需要提交失败记录、报错截图和解决尝试

- [ ] 你的最终成果应该能让别人按照 README 复现主要实验

---

<a id="KJq7dVbs4oYobAx6TXIcfL9dnFh"></a>

## 七、每周一任务通知模板

> 建议每周一上午发。作用是明确本周任务、提交时间、最低要求和优秀要求。

<a id="RCRGdue4zoekwExHMZFcvF2PnLf"></a>

### 周一通知模板

各位同学好，本周进入第 X 周任务。

本周主题：

```text
填写本周主题，例如：Kaggle 表格竞赛专题
```

本周你需要完成：

- [ ] 任务 1

- [ ] 任务 2

- [ ] 任务 3

- [ ] 任务 4

本周必须提交：

- [ ] 代码或 Notebook

- [ ] 数据来源说明

- [ ] 实验结果表

- [ ] 结果图

- [ ] 错误分析

- [ ] 周报告

- [ ] 运行日志

提交截止时间：

```text
本周日 22:00 前
```

最低要求：

```text
填写最低要求，例如至少完成 2 次 Kaggle 提交，至少 4 个模型对比。
```

优秀要求：

```text
填写优秀要求，例如完成模型融合、消融实验、错误样例分析。
```

提醒：

1. 不要只交截图，必须提交可运行代码。

2. 数据来源必须写清楚。

3. 使用 AI 工具可以，但需要注明辅助内容。

4. 遇到问题要记录解决过程。

---

<a id="OKeMdBw6XomS2WxIwqacVruGn5f"></a>

## 八、周末提交与复盘模板

> 建议周五晚上或周六上午发。作用是提醒收尾、统一提交格式、让学生做自检。

<a id="WNvjdWY4moYRAex2zQxc9EFunWg"></a>

### 周末提醒模板

各位同学好，本周任务进入收尾阶段。

请你在提交前完成以下自检：

- [ ] 代码是否可以运行

- [ ] README 是否写清楚运行方式

- [ ] data_source.md 是否写清楚数据来源

- [ ] results 文件夹是否包含图表和结果表

- [ ] report.md 是否包含实验过程、结果和分析

- [ ] error_analysis.md 是否记录错误样例或失败案例

- [ ] run_log.txt 是否记录关键训练/运行日志

- [ ] GitHub/Gitee 是否已更新

- [ ] Kaggle 项目是否已提交并截图

本周提交格式：

```text
姓名：
GitHub/Gitee 仓库链接：
Kaggle 主页链接：
本周目录链接：
本周完成项目：
关键实验结果：
遇到的问题：
下周计划：
```

本周复盘问题：

1. 本周最重要的实验结果是什么？

2. 哪个模型效果最好？为什么？

3. 哪些地方失败了？你如何处理？

4. 如果再做一版，你会优先改哪里？

5. 哪些内容是 AI 工具辅助完成的？

提交截止时间：

```text
本周日 22:00 前
```

---

<a id="P4gtdmbPjorZITxk0QzcoVcmn9d"></a>

## 九、第一天总包发布模板

各位同学好，欢迎进入 8 周 AI 科研实践实习。

这份文档是你本次实习的总任务书。请先完整浏览一遍，重点关注：

1. 8 周任务安排

2. GitHub/Gitee 仓库要求

3. Kaggle 主页和提交要求

4. 每周提交格式

5. 结业标准

第一周你需要先完成：

- [ ] 注册 GitHub/Gitee

- [ ] 注册 Kaggle

- [ ] 创建个人实习仓库

- [ ] 完成 Iris 分类项目

- [ ] 完成线性回归项目

- [ ] 提交 Week01 目录

请注意：本实习以项目产出为核心，不以观看视频和写学习心得为核心。每周都需要提交可检查、可运行、可复现的成果。
