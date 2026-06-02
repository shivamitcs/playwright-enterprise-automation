from playwright.sync_api import Page


class SynchronizationManager:
    @staticmethod
    def wait_for_page_ready(page: Page):
        page.wait_for_load_state("networkidle")
