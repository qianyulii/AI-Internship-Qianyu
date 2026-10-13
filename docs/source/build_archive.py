"""Build offline reading copies from the captured, rendered Feishu document."""
from __future__ import annotations

import hashlib
import html
import json
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = Path(__file__).resolve().parents[1]
SOURCE = BASE / "source" / "feishu-dom-snapshot.json"
data = json.loads(SOURCE.read_text())
nodes = {n["id"]: n for n in data["nodes"]}
roots = sorted((n for n in nodes.values() if n["parentType"] == "page"), key=lambda n: int(n["id"]))


class Element:
    def __init__(self, tag="root", attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Element):
                yield from child.walk()

    def text(self):
        return "".join(c.text() if isinstance(c, Element) else c for c in self.children)


class Tree(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.root = Element()
        self.stack = [self.root]
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        el = Element(tag, attrs)
        self.stack[-1].children.append(el)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(el)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                self.stack = self.stack[:i]
                return

    def handle_data(self, text):
        self.stack[-1].children.append(text)


def clean(text):
    return re.sub(r"[\u200b-\u200f\u2060-\u206f\ufeff]", "", text).strip()


def lines(source):
    tree = Tree(source).root
    return [clean(e.text()) for e in tree.walk() if "ace-line" in e.attrs.get("class", "").split()]


def linked(text):
    return re.sub(r"https?://[^\s<>]+", lambda m: '<a href="' + html.escape(m[0], quote=True) + '" target="_blank" rel="noopener noreferrer">' + m[0] + "</a>", html.escape(text))


def table_rows(node):
    rows = []
    for row in Tree(node["html"]).root.walk():
        if row.tag != "tr":
            continue
        cells = []
        for cell in row.children:
            if not isinstance(cell, Element) or cell.tag not in {"td", "th"}:
                continue
            captured = nodes.get(cell.attrs.get("data-block-id"))
            source = captured["html"] if captured else ""
            text = " / ".join(t for t in lines(source) if t) if source else clean(cell.text())
            assert text, f"Unloaded table cell in block {node['id']}"
            cells.append(text)
        if cells:
            rows.append(cells)
    assert rows, f"Empty table {node['id']}"
    return rows


def render(selected):
    md, web, toc = [], [], []
    for node in selected:
        kind, ident = node["type"], node["record"]
        text = "\n".join(t for t in lines(node["html"]) if t)
        if kind == "divider":
            md.append("---")
            web.append("<hr>")
        elif not text and kind != "table":
            continue
        elif kind.startswith("heading"):
            level = int(kind[-1])
            md.append(f'<a id="{ident}"></a>\n\n' + "#" * level + " " + text)
            web.append(f'<h{level} id="{ident}">{html.escape(text)}</h{level}>')
            if level <= 3:
                toc.append((level, ident, text))
        elif kind == "code":
            code_lines = [(int(e.attrs["data-line-num"]), clean(e.text())) for e in Tree(node["html"]).root.walk() if "data-line-num" in e.attrs]
            numbers = [x[0] for x in code_lines]
            assert numbers == list(range(1, max(numbers) + 1)), f"Missing code lines: {node['id']}"
            text = "\n".join(t for _, t in code_lines)
            md.append("```text\n" + text + "\n```")
            web.append("<pre><code>" + html.escape(text) + "</code></pre>")
        elif kind == "table":
            rows = table_rows(node)
            md.append("\n".join(["| " + " | ".join(c.replace("|", "\\|") for c in rows[0]) + " |", "| " + " | ".join("---" for _ in rows[0]) + " |"] + ["| " + " | ".join(c.replace("|", "\\|") for c in r) + " |" for r in rows[1:]]))
            web.append('<div class="table-wrap"><table>' + "".join("<tr>" + "".join(f"<{('th' if i == 0 else 'td')}>" + linked(c) + f"</{('th' if i == 0 else 'td')}>" for c in row) + "</tr>" for i, row in enumerate(rows)) + "</table></div>")
        elif kind == "todo":
            md.append("- [ ] " + text)
            web.append('<div class="task"><span aria-hidden="true">☐</span><span>' + linked(text) + "</span></div>")
        elif kind == "ordered":
            order = next((clean(e.text()) for e in Tree(node["html"]).root.walk() if "order" in e.attrs.get("class", "").split()), "1.")
            md.append(order + " " + text)
            web.append('<div class="task"><span>' + html.escape(order) + "</span><span>" + linked(text) + "</span></div>")
        elif kind == "quote_container":
            md.append("> " + text.replace("\n", "\n> "))
            web.append("<blockquote>" + linked(text) + "</blockquote>")
        else:
            assert kind == "text", f"Unexpected block type: {kind}"
            md.append(text)
            web.append("<p>" + linked(text).replace("\n", "<br>") + "</p>")
    return "\n\n".join(md) + "\n", "\n".join(web), toc


saved_local = datetime.fromisoformat(data["savedAt"].replace("Z", "+00:00")).astimezone(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M %Z")
meta_md = f"来源：[飞书原文]({data['url']})  \n作者：{data['author']} · 原文版本：v2.2 · 页面显示修改时间：{data['displayedModified']}  \n本地保存时间：{saved_local}  \n保存方式：从 Chrome 中可阅读的正文逐段归档，保留标题、任务、表格、代码目录和资源链接；此文件是本地快照。\n"

CSS = """
:root{color-scheme:light;--ink:#253344;--accent:#146a65;--paper:#fff;--edge:#dce5e3}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font:16px/1.85 -apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;color:var(--ink);background:#f3f6f5}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}aside{position:fixed;top:0;bottom:0;width:280px;padding:28px 22px;overflow:auto;border-right:1px solid var(--edge);background:#edf3f1}
aside .brand{font-size:18px;font-weight:650;margin-bottom:12px}aside a{display:block;font-size:13px;line-height:1.6;padding:5px 0}.sub{padding-left:14px!important;color:#5b6a72}
main{max-width:1120px;margin:0 auto 0 280px;padding:54px 64px 100px;background:var(--paper);min-height:100vh}h1{font-size:32px;line-height:1.4;letter-spacing:-.4px}h2{font-size:25px;margin-top:60px;border-bottom:1px solid var(--edge);padding-bottom:12px}h3{font-size:21px;margin-top:40px}h4{font-size:17px;margin:28px 0 12px;color:var(--accent)}h2,h3,h4{scroll-margin-top:26px}
.meta{font-size:13px;color:#64747b;margin:20px 0 32px}.scope{padding:22px 25px;background:#eaf4ef;border-left:4px solid var(--accent);border-radius:4px;margin:28px 0}.scope p{margin:8px 0}.tag{font-size:12px;letter-spacing:1px;color:var(--accent);font-weight:700}
.task{display:flex;gap:11px;margin:7px 0}.task>span:first-child{min-width:18px;color:#6b837c}pre{background:#f4f7f6;border:1px solid var(--edge);border-radius:8px;padding:20px;overflow:auto;font:13px/1.7 Menlo,Consolas,monospace;white-space:pre}blockquote{margin:25px 0;padding:10px 22px;border-left:3px solid #abc6bd;color:#53666c}hr{border:0;border-top:1px solid var(--edge);margin:40px 0}
.table-wrap{overflow:auto;margin:22px 0}table{border-collapse:collapse;width:100%;font-size:14px;line-height:1.65}td,th{border:1px solid var(--edge);padding:12px;min-width:95px;vertical-align:top;text-align:left;overflow-wrap:anywhere}th{background:#ecf3ef;font-weight:600}td a{font-size:12px}footer{margin-top:50px;font-size:12px;color:#78888d}
@media(max-width:950px){aside{position:static;width:auto;max-height:260px;border:0;border-bottom:1px solid var(--edge)}main{margin:0;padding:30px 24px}h1{font-size:26px}}
@media print{aside{display:none}body{background:white}main{margin:0;max-width:none;padding:0}pre,table,.scope{break-inside:avoid}a{color:inherit}.meta{font-size:10px}h2,h3,h4{break-after:avoid}}
"""


def page(title, body, toc, scope=""):
    nav = ''.join(f'<a class="{("sub" if level == 3 else "")}" href="#{ident}">{html.escape(text)}</a>' for level, ident, text in toc)
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><aside><div class="brand">CASIA · 科研任务</div><a href="AI-科研实践实习任务书-v2.2.html">完整任务书</a><a href="前三周-查阅版.html">前三周查阅版</a><hr>{nav}</aside>
<main><div class="tag">本地归档 · v2.2</div><h1>{html.escape(title)}</h1><div class="meta">作者：{html.escape(data['author'])} · {html.escape(data['displayedModified'])}<br>保存于 {saved_local} · <a href="{data['url']}">查看飞书原文</a><br>正文从 Chrome 逐段归档；本地副本不自动同步。</div>{scope}{body}<footer>资源链接保留原文地址；资源内容未随任务书下载。浏览器可搜索全文或打印为 PDF。</footer></main></body></html>'''


full_md, full_html, full_toc = render(roots)
(BASE / "AI-科研实践实习任务书-v2.2.md").write_text("# " + data["title"] + "\n\n" + meta_md + "\n" + full_md)
scope_notice = '<div class="scope"><strong>当前工作范围：原任务书第 1–3 周</strong><p>按你的安排，在下周（2026-10-12 至 2026-10-18）开展这三周的内容。此处保留原文的周次。</p><p><a href="前三周-查阅版.html">打开前三周查阅版 →</a></p></div>'
(BASE / "AI-科研实践实习任务书-v2.2.html").write_text(page(data["title"], full_html, full_toc, scope_notice))

scope_nodes = [n for n in roots if int(n['id']) < 827 or 869 <= int(n['id']) < 901 or 915 <= int(n['id']) < 1030 or 1255 <= int(n['id']) < 1269]
scope_md, scope_html, scope_toc = render(scope_nodes)
summary_md = """## 当前范围与最低验收要求

按你的安排，下周（2026-10-12 至 2026-10-18）开展原任务书第 1–3 周的内容。下表是查阅摘要，具体要求见后面的原文摘录。

| 原文周次 | 主要内容 | 最低验收要求 |
| --- | --- | --- |
| 第 1 周 | AI 基础与工具记录、Iris 分类、线性回归 | 至少 6 张图、2 个模型结果表；报告不少于 1000 字；提交仓库与 Kaggle 主页链接 |
| 第 2 周 | 信用卡违约预测、糖尿病预测；4 个选做项目中至少选 2 个 | 总计至少 4 个项目、8 张图、4 个模型对比表；报告不少于 1500 字 |
| 第 3 周 | Titanic、House Prices | 每项至少 4 个模型、5 张图、2 次 Kaggle 提交；报告不少于 1500 字；附主页链接和提交截图 |

下面保留基础准备、每周通用目录、相关资源表、第 1–3 周全文要求和全局注意事项。资源表沿用原文，其中 Dog Breed 属于后续周次。完整八周安排和通知/复盘模板见 [完整任务书](AI-科研实践实习任务书-v2.2.md)。

---
"""
summary_html = '<div class="scope"><strong>下周范围 · 2026-10-12 至 2026-10-18</strong><p>原任务书第 1–3 周。以下保留基础准备、通用目录、相关资源表、三周任务与验收要求及全局注意事项。</p><p>第 1 周：AI 基础、Iris、线性回归。至少 6 张图、2 个结果表，报告 ≥1000 字。</p><p>第 2 周：2 个必做 + 至少 2 个选做。至少 8 张图、4 个模型对比表，报告 ≥1500 字。</p><p>第 3 周：Titanic、House Prices。每项至少 4 个模型、5 张图、2 次 Kaggle 提交，报告 ≥1500 字。</p><p>资源表沿用原文，其中 Dog Breed 属于后续周次。</p></div>'
(BASE / "前三周-查阅版.md").write_text("# 前三周查阅版\n\n" + meta_md + "\n" + summary_md + "\n" + scope_md)
(BASE / "前三周-查阅版.html").write_text(page("前三周查阅版", scope_html, scope_toc, summary_html))

checks = {
    "originalBlockIdRange": [798, 1376],
    "missingOriginalBlockIds": sorted(set(range(798, 1377)) - {int(i) for i in nodes}),
    "capturedNodeCount": len(nodes),
    "topLevelBlockCount": len(roots),
    "tableCount": sum(n['type'] == 'table' for n in roots),
    "tableCellCount": sum(len(row) for n in roots if n['type'] == 'table' for row in table_rows(n)),
    "codeBlockCount": sum(n['type'] == 'code' for n in roots),
    "weekHeadings": [clean(n['text']) for n in roots if n['type'].startswith('heading') and re.match(r'第 \d 周', clean(n['text']))],
    "lastScroll": data['passes'][-1]['scroll'],
    "sourceSha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "files": {p.name: {"bytes": p.stat().st_size, "sha256": hashlib.sha256(p.read_bytes()).hexdigest()} for p in BASE.iterdir() if p.suffix in {'.md', '.html'}},
}
assert not checks['missingOriginalBlockIds']
assert len(checks['weekHeadings']) == 8
(BASE / "source" / "archive-manifest.json").write_text(json.dumps({"title": data['title'], "sourceUrl": data['url'], "savedAt": data['savedAt'], "savedLocalTime": saved_local, "checks": checks}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(checks, ensure_ascii=False, indent=2))
