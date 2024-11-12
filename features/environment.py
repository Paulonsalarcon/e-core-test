from playwright.sync_api import sync_playwright
from pages import login_page, invoice_details_page, invoice_list_page

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browsers = {
        "chromium": context.playwright.chromium.launch(headless=True),
        "firefox": context.playwright.firefox.launch(headless=True)
    }
    context.browser_name = None
    context.browser_context = None
    context.page = None
    context.login_page = None
    context.invoice_list_page = None
    context.invoice_details_page = None

def before_scenario(context, scenario):
    for browser_name, browser in context.browsers.items():
        context.browser_name = browser_name
        context.browser_context = browser.new_context()
        context.page = context.browser_context.new_page()
        context.login_page = login_page.LoginPage(context.browser_context)
        context.invoice_list_page = invoice_list_page.InvoiceListPage(context.browser_context)
        context.invoice_details_page = invoice_details_page.InvoiceDetailsPage(context.browser_context)

def after_scenario(context, scenario):
    for page in context.browser_context.pages:
        page.close()

def after_all(context):
    for browser in context.browsers.values():
        browser.close()
    context.playwright.stop()
