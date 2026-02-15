import os
import json
import re

# スキャン開始ディレクトリ（index.html と同じ階層）
ROOT = "."

# 除外したいファイルやフォルダ
EXCLUDE_FILES = {"index.html", "footer.html"}
EXCLUDE_DIRS = {".git", "__pycache__","9900Sample"}

# <h1> 抽出用の正規表現
H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)

def extract_h1(filepath):
    """HTML ファイルから <h1> を抽出。なければファイル名を返す。"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
        m = H1_RE.search(html)
        if m:
            return m.group(1).strip()
    except:
        pass
    # h1 が無い場合はファイル名（拡張子なし）
    return os.path.splitext(os.path.basename(filepath))[0]


pages = []

for current_dir, dirs, files in os.walk(ROOT):
    # 除外フォルダをスキップ
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

    for filename in files:
        if filename.endswith(".html") and filename not in EXCLUDE_FILES:
            # 相対パス
            rel_dir = os.path.relpath(current_dir, ROOT)
            rel_path = os.path.join(rel_dir, filename) if rel_dir != "." else filename
            rel_path = rel_path.replace("\\", "/")  # Windows対策

            # h1 タイトル抽出
            full_path = os.path.join(current_dir, filename)
            title = extract_h1(full_path)

            pages.append({
                "title": title,
                "url": rel_path
            })

# ★ URL だけでソート（フォルダ名は使わない）
pages.sort(key=lambda x: x["url"])

with open("pages.json", "w", encoding="utf-8") as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)

print("pages.json を生成しました。")

