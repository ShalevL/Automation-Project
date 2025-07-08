# interface/cli.py
import argparse
from core.runner import run_automation
from core.batch import run_batch
from reports.generator import generate_report
from utils.time import timestamped_filename

def run_cli():
    parser = argparse.ArgumentParser(description="Automate and report browser tasks")
    parser.add_argument("--query", type=str, help="Single search query")
    parser.add_argument("--file", type=str, help="File containing multiple search queries")
    parser.add_argument("--report", type=str, default=None, help="Optional output report filename")

    args = parser.parse_args()

    if args.file:
        run_batch(args.file)
    elif args.query:
        print(f"Running automation for: {args.query}")
        html = run_automation(args.query)
        filename = args.report or timestamped_filename(args.query, extension="html")
        generate_report(html, f"data/output/{filename}")
        print(f"Saved report to: data/output/{filename}")
    else:
        print("❌ Please provide either --query or --file")