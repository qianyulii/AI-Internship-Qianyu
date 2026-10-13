"""Check the project's installed Python, core imports, data loaders, and kernel."""
from pathlib import Path
import importlib
import importlib.metadata
import io
import json
import platform
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
expected_python = ROOT / ".venv" / "bin" / "python"
assert Path(sys.executable).absolute() == expected_python, sys.executable
assert sys.version_info[:2] == (3, 12), sys.version
assert platform.machine() == "arm64", platform.machine()
modules = {"numpy": "numpy", "pandas": "pandas", "scipy": "scipy",
           "scikit-learn": "sklearn", "matplotlib": "matplotlib",
           "seaborn": "seaborn", "jupyterlab": "jupyterlab", "ipykernel": "ipykernel"}
versions = {}
for package, module in modules.items():
    importlib.import_module(module)
    versions[package] = importlib.metadata.version(package)
# Kaggle's top-level import can request credentials; check package metadata only.
versions["kaggle"] = importlib.metadata.version("kaggle")
import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])
buffer = io.BytesIO()
fig.savefig(buffer, format="png")
assert buffer.getvalue().startswith(b"\x89PNG"), "PNG renderer failed"
plt.close(fig)
from sklearn.datasets import load_iris, load_diabetes
assert load_iris().data.shape == (150, 4)
assert load_diabetes().data.shape == (442, 10)
from jupyter_client.kernelspec import KernelSpecManager
kernel = KernelSpecManager().get_kernel_spec("qianyu-ai")
assert Path(kernel.argv[0]).absolute() == expected_python, kernel.argv
status = {"checkedAt": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
          "pythonExecutable": sys.executable, "architecture": platform.machine(),
          "packages": versions, "checks": {"imports": "passed", "PNGRendering": "passed",
          "IrisLoader": "passed", "DiabetesLoader": "passed", "JupyterKernel": "passed"},
          "kaggleAuthentication": "not configured"}
(ROOT / "docs" / "environment-status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(status, ensure_ascii=False, indent=2))
