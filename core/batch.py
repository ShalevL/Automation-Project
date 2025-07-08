# core/batch.py
import os
from core.runner import run_automation
from reports.generator import generate_report
from utils.time import timestamped_filename

def run_batch(file_path: str, output_dir: str = "data/output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(file_path, "r", encoding="utf-8") as f:
        queries = [line.strip() for line in f if line.strip()]

    for query in queries:
        print(f"\n🔍 Running for: '{query}'")
        try:
            html = run_automation(query)
            filename = timestamped_filename(query, extension="html")
            output_path = os.path.join(output_dir, filename)
            generate_report(html, output_path)
            print(f"✅ Saved: {output_path}")
        except Exception as e:
            print(f"❌ Failed on '{query}': {type(e).__name__} - {e}")