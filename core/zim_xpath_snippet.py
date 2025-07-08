# zim_xpath_snippet.py
from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime

def timestamped_filename(prefix="zim_xpath", ext="png"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"{prefix}_{timestamp}.{ext}"

def interact_with_zim_xpath():
    output_dir = Path("data/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = output_dir / timestamped_filename()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.zim.com/he/")

        # Wait for the page to fully load
        page.wait_for_load_state("networkidle")

        # Accept cookies if present
        try:
            page.locator('//button[contains(text(), "I Agree")]').click(timeout=3000)
        except:
            print("✅ No cookie banner or already dismissed.")

        # Click the "שירותים" (Services) menu
        try:
            page.locator('//a[contains(text(), "שירותים")]').click()
            page.wait_for_timeout(2000)  # Wait to observe the click result
            page.screenshot(path=str(screenshot_path))
            print(f"📸 Screenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f"❌ Could not click 'שירותים': {e}")

        browser.close()

if __name__ == "__main__":
    interact_with_zim_xpath()