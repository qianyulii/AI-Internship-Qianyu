# 项目环境与启动方式

环境方案：uv 管理 Python 3.12，使用项目内 `.venv/` 隔离依赖；版本通过 `uv.lock` 固定。

项目位置：`/Users/leohome/AI-Internship-Qianyu`。

## 工具分工

| 工具 | 用途 |
| --- | --- |
| Python + NumPy + SciPy | 编程、数组运算、科学计算 |
| pandas | 读取 CSV、清洗与分析表格 |
| Matplotlib + Seaborn | 绘制实验图表 |
| scikit-learn | 分类、回归、聚类、模型评价 |
| PyTorch | Tensor 运算、自动求导和自定义模型训练 |
| JupyterLab + ipykernel | 交互式 Notebook 与项目执行内核 |
| Kaggle CLI | 后续数据下载和提交的命令行入口 |

当前环境覆盖第一至三周的核心任务。图像训练和本地大模型在对应周次添加相应工具。

## 启动 JupyterLab

在终端中运行：

```bash
cd /Users/leohome/AI-Internship-Qianyu
./scripts/start-jupyter.sh
```

JupyterLab 会显示本地浏览器访问地址。Notebook 内核选择 **Python (Qianyu AI)**，对应此项目 `.venv/bin/python`。在终端按 `Control+C` 可停止服务。

## 运行脚本

```bash
cd /Users/leohome/AI-Internship-Qianyu
uv run --locked python your_script.py
```

也可以在终端激活环境：

```bash
source /Users/leohome/AI-Internship-Qianyu/.venv/bin/activate
```

## 重建和新增依赖

```bash
cd /Users/leohome/AI-Internship-Qianyu
uv sync --locked
uv run --locked python -m ipykernel install --sys-prefix --name qianyu-ai --display-name "Python (Qianyu AI)"
```

新增项目依赖时使用 `uv add 包名`，让依赖声明和锁定文件保持同步。`requirements.txt` 是额外导出的固定版本清单，供使用 pip 的环境复现。

## 环境检查

```bash
cd /Users/leohome/AI-Internship-Qianyu
uv run --locked python scripts/check_environment.py
```

该检查验证 Python 版本与架构、核心库导入、PNG 绘图、Iris/Diabetes 数据加载，以及项目 Jupyter 内核路径。当前安装版本和检查结果保存在 `docs/environment-status.json`。

参考：[uv 项目管理](https://docs.astral.sh/uv/guides/projects/)、[uv 与 Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/)。

## VS Code 内核选择

项目内核已注册到用户级 Jupyter 目录。Notebook 右上角选择：

**Select Another Kernel → Jupyter Kernels → Qianyu AI (.venv / Python 3.12.12)**。

如果列表未更新，先保存 Notebook，再运行命令面板中的 `Developer: Reload Window`。

Python 版本号不能唯一确定运行环境。此项目使用的解释器路径是：

```text
/Users/leohome/AI-Internship-Qianyu/.venv/bin/python
```

uv 的基础 Python 同样显示 3.12.12，其依赖与项目虚拟环境分开。项目所需的 scikit-learn 和 ipykernel 已安装在 `.venv` 中。

需要在其他电脑重新注册这个内核时，在项目根目录运行：

```bash
uv run --locked python -m ipykernel install --user --name qianyu-ai-project --display-name "Qianyu AI (.venv / Python 3.12.12)"
```
