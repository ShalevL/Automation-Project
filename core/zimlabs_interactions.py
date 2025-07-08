from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime

def timestamped_filename(prefix="zimlabs", ext="html"):
    return f"{prefix}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.{ext}"

def generate_report(title: str, steps: list[str], report_path: str):
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial;
            background: #f5f7fa;
            color: #333;
            padding: 2em;
        }}
        h1 {{ color: #004080; }}
        ul {{ line-height: 1.8em; }}
        li {{ margin-bottom: 8px; }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <ul>
""")
        for step in steps:
            f.write(f"<li>{step}</li>\n")
        f.write("</ul></body></html>")

def interact_with_zimlabs_site():
    output_dir = Path("data/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    steps = []
    report_path = output_dir / timestamped_filename()

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://zimlabs.zim.com/")
            page.wait_for_load_state("networkidle")
            steps.append("✅ Opened zimlabs.zim.com homepage")

            try:
                explore_btn = page.locator("//a[contains(text(), 'Explore All')]")
                if explore_btn.is_visible():
                    explore_btn.click()
                    steps.append("✅ Clicked 'Explore All'")
                else:
                    steps.append("⚠️ 'Explore All' button not visible")
            except Exception as e:
                steps.append(f"❌ Failed to click 'Explore All': {type(e).__name__}")

            try:
                page.mouse.wheel(0, 1000)
                steps.append("✅ Scrolled down the page")
            except Exception as e:
                steps.append(f"⚠️ Scroll failed: {type(e).__name__}")

            browser.close()

    except Exception as e:
        steps.append(f"❌ General error: {type(e).__name__} - {e}")

    finally:
        generate_report("ZIM Labs Automation Report", steps, str(report_path))
        print(f"📄 Report saved to: {report_path}")

if __name__ == "__main__":
    interact_with_zimlabs_site()