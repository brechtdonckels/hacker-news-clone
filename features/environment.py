import os

from playwright.sync_api import sync_playwright


def before_all(context):
    """Bypass Django's async safety checks."""
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

    """Start Playwright before all scenarios."""
    context.playwright = sync_playwright().start()


def before_scenario(context, scenario):
    """Launch a new browser and page for each scenario."""
    context.browser = context.playwright.chromium.launch()
    context.page = context.browser.new_page()
    context.page.set_default_timeout(5000)


def after_scenario(context, scenario):
    """Close the browser after each scenario."""
    if hasattr(context, "page"):
        context.page.close()
    if hasattr(context, "browser"):
        context.browser.close()


def after_all(context):
    """Stop Playwright after all scenarios."""
    context.playwright.stop()

    """Enable Django's async safety checks."""
    os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "false"
