from playwright.sync_api import BrowserContext, expect

class InvoiceListPage:
    URL = 'https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/account'
    LOGOUT_BUTTON = '.btn[href=/logout]'
    FIRST_INVOICE_LINK = '.row [href="/invoice/0"]'

    def __init__(self, browser_context: BrowserContext):
        self.browser_context = browser_context
        self.page = self.browser_context.pages[0]

    def is_in_page(self):
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(self.URL)

    def click_logout(self):
        self.page.click(self.LOGOUT_BUTTON)

    def click_first_invoice(self):
        self.page.click(self.FIRST_INVOICE_LINK)