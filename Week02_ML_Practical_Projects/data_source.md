# 数据来源

| 数据集 | 原始来源链接 | 获取日期 | 获取方式 | 使用文件/版本 |
| --- | --- | --- | --- | --- |
| Default of Credit Card Clients（信用卡违约） | [UCI 350](https://archive.ics.uci.edu/dataset/350/default+of+credit+card+clients) | 2026-11-01 | UCI 官方 API 提供的 CSV，保存本地后读取 | `data/raw/credit_default_uci350.csv`；变量说明 `data/raw/uci350_metadata.json` |

## 数据说明

- 样本数：30,000；原始表共 25 列（ID、23 个特征、目标 Y）。
- Notebook 根据官方变量说明将特征列 X1–X23 改成可读名称，将 Y 改为 `default_next_month`；原始 CSV 保留不变。
- 目标：1 = 违约，0 = 未违约。未违约 23,364 条（77.88%），违约 6,636 条（22.12%）。
- ID 仅作为记录编号，不纳入特征。当前只完成导入，尚未划分训练集和测试集。
- 导入检查：未发现缺失值；特殊数值编码仍需在后续 EDA 中检查。
- 官方 CSV：https://archive.ics.uci.edu/static/public/350/data.csv
- CSV SHA-256：`45bcf4df62ff2e237a74eb155cabfb4bbbc171219a0637daef44fdad07503dd0`。
- 引用：Yeh, I. (2009). Default of Credit Card Clients. UCI Machine Learning Repository. https://doi.org/10.24432/C55S3H
- 许可：CC BY 4.0；使用时注明来源。
