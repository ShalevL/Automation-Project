# core/zim_hebrew_test.py
from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime

def timestamped_filename(prefix="zim", extension="html"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{prefix}_{timestamp}.{extension}"

def interact_with_zim():
    output_dir = Path("data/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = timestamped_filename()
    output_path = output_dir / filename

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.zim.com/he/")

        page.wait_for_load_state("networkidle")

        # Accept cookie popup if shown
        try:
            page.locator("text=אני מסכים לכל").click(timeout=3000)
            print("✅ Accepted cookies.")
        except:
            print("ℹ️ No cookie banner detected.")

        # Click "שירותים" (Services)
        try:
            page.click("text=שירותים")
            page.wait_for_timeout(1500)
            print("✅ Clicked 'שירותים'.")
        except:
            print("⚠️ Could not click 'שירותים'.")

        # Optional: Click sub-menu (e.g., שירותים דיגיטליים)
        try:
            page.click("text=שירותים דיגיטליים")
            page.wait_for_timeout(1500)
            print("✅ Clicked 'שירותים דיגיטליים'.")
        except:
            print("ℹ️ Submenu not found or skipped.")

        # Save report
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(page.content())
        print(f"📄 Report saved to: {output_path.as_posix()}")

        browser.close()

if __name__ == "__main__":
    interact_with_zim()