# Qianyu 的 Kaggle 使用指南

Kaggle 是数据科学和机器学习平台，主要用来寻找数据、参加预测竞赛、运行 Notebook、阅读他人的实验，以及展示项目成果。[官方入门文档](https://www.kaggle.com/docs/)

## 和我们项目的关系

| 阶段 | Kaggle 的用途 | 需要留下的记录 |
| --- | --- | --- |
| 第 1 周 | 账号与个人主页准备；实验在 Mac 本地运行 | 个人主页链接 |
| 第 2 周 | 获取糖尿病预测等项目的数据；参考公开实验思路 | 数据来源链接、参考来源、自己的实验结果 |
| 第 3 周 | Titanic 与 House Prices 的真实预测提交 | 每个竞赛至少 2 次提交、每次分数与改动、提交截图 |
| 第 6 周 | Dog Breed 图像分类竞赛 | 至少 1 次提交、截图、Top-1/Top-5 指标 |

以上提交次数来自本地归档任务书，并非 Kaggle 平台对所有用户的统一要求。

## 竞赛怎样工作

1. 查看竞赛问题、数据说明、评价指标、提交格式和规则。
2. 加入竞赛并接受规则后，下载数据。规则的接受由你在 Kaggle 页面完成。
3. 用带有答案的训练数据建立模型。在本地划分验证数据，检查模型效果。
4. 为竞赛提供的测试数据生成预测。竞赛测试集通常没有公开的答案。
5. 按要求导出 CSV，提交给 Kaggle。平台使用隐藏答案计算分数并展示到排行榜。
6. 改进特征或模型，再次提交，记录版本、分数和改动。

可以在本地电脑或 Kaggle Notebook 中建立模型，再提交预测文件。[Kaggle 官方竞赛说明](https://www.kaggle.com/docs/competitions-setup)

## 我们会参加的项目

- [Titanic](https://www.kaggle.com/competitions/titanic)：根据乘客信息预测是否生还；提交文件包含 `PassengerId` 和 `Survived`。
- [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)：根据房屋信息预测售价。
- [Dog Breed](https://www.kaggle.com/competitions/dog-breed-identification)：狗品种图像分类，后续周次使用。

例如，Titanic 中一行预测可以是：

```csv
PassengerId,Survived
892,0
```

这是提交格式示例，不是我们已经完成的预测结果。完整提交要覆盖竞赛测试集。[Titanic 官方说明](https://www.kaggle.com/c/titanic)

## 本地工作安排

- 数据放进各周的 `data/raw/`；清洗后的数据放进 `data/processed/`。
- 实验代码、图表和报告保存在本地项目目录。
- 第三周的预测 CSV 放进 `Week03_Kaggle_Tabular/submissions/`。
- 提交截图放进 `Week03_Kaggle_Tabular/kaggle_submission_screenshots/`。
- 将每次提交对应的模型、特征、验证分数、Kaggle 分数和文件名记入实验记录。

公开 Notebook 可以帮助理解方法；使用他人的思路或代码时，应记录来源并说明自己的修改。排行榜分数和本地验证结果都需要记录，以便解释改进是否有效。

## 账号记录

姓名：Qianyu。

注册状态：用户于 2026-10-13 确认已完成注册。

Kaggle 用户名：待填写。

个人主页链接：待填写。

本地安装了 Kaggle 命令行工具。账号授权、竞赛规则接受、数据下载和预测提交在使用相应功能时再处理。
