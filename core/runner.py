# runner.py
from playwright.sync_api import sync_playwright

def run_automation(search_term: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # ✅ Use DuckDuckGo instead of Google
        page.goto("https://duckduckgo.com/")
        page.wait_for_selector("input[name='q']")
        page.fill("input[name='q']", search_term)
        page.keyboard.press("Enter")

        # Wait for results to load
        page.wait_for_selector("a.result__a")

        # Extract results
        results = page.query_selector_all("a.result__a")
        output = f"<h1>DuckDuckGo Search Results for '{search_term}'</h1><ul>"
        for link in results[:10]:
            href = link.get_attribute("href")
            title = link.inner_text()
            output += f"<li><a href='{href}'>{title}</a></li>"
        output += "</ul>"

        browser.close()
        return output