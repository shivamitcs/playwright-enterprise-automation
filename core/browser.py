from playwright.sync_api import sync_playwright


class BrowserManager:
    def launch(self):
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(
            headless=True
        )

        context = browser.new_context()

        return playwright, browser, context
