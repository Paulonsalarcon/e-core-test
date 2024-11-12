from playwright.sync_api import BrowserContext
from config import config

class InvoiceDetailsPage:
    URL_PATTERN = 'invoice'
    HOTEL_NAME_SELECTOR = 'h4'
    INVOICE_DATE_SELECTOR = 'xpath=//*[text()="Invoice Date:"]/parent::*'
    DUE_DATE_SELECTOR = 'xpath=//*[text()="Due Date:"]/parent::*'
    INVOICE_NUMBER_SELECTOR = 'h6'
    BOOKING_CODE_SELECTOR = 'xpath=//*[text()="Booking Code"]/following-sibling::*'
    CUSTOMER_DETAILS_SELECTOR = 'xpath=//*[text()="Customer Details"]/following-sibling::div'
    ROOM_SELECTOR = 'xpath=//*[text()="Room"]/following-sibling::*'
    CHECK_IN_SELECTOR = 'xpath=//*[text()="Check-In"]/following-sibling::*'
    CHECK_OUT_SELECTOR = 'xpath=//*[text()="Check-Out"]/following-sibling::*'
    TOTAL_STAY_COUNT_SELECTOR = 'xpath=//*[text()="Total Stay Count"]/following-sibling::*'
    TOTAL_STAY_AMOUNT_SELECTOR = 'xpath=//*[text()="Total Stay Amount"]/following-sibling::*'
    DEPOSIT_NOW_SELECTOR = 'xpath=//*[text()="Billing Details"]/following::table/tbody//td[1]'
    TAX_VAT_SELECTOR = 'xpath=//*[text()="Billing Details"]/following::table/tbody//td[2]'
    TOTAL_AMOUNT_SELECTOR = 'xpath=//*[text()="Billing Details"]/following::table/tbody//td[3]'

    def __init__(self, browser_context: BrowserContext):
        self.browser_context = browser_context
        self.page = self.browser_context.pages[0]

    def wait_until_page_loaded(self):
        tab_is_open = False
        timeout = config.TIMEOUT
        timer = timeout
        
        #Defining listener for new tab
        def on_new_page(new_page):
            new_page.bring_to_front()
        
        self.browser_context.on("page", on_new_page)

        #Wait until new tab is open
        while not tab_is_open and timer > 0:
            for page in self.browser_context.pages:
                if self.URL_PATTERN in page.url:
                    page.bring_to_front()
                    self.page = page
                    tab_is_open = True
            timer = timer - config.TIME_STEP
            page.wait_for_timeout(config.TIME_STEP)

        self.page.wait_for_load_state('load')
        assert self.URL_PATTERN in self.page.url, f"URL '{self.page.url}' does not contain '{self.URL_PATTERN}'"

    #Generic field validator
    def validate_field(self, selector, expected_value):
        actual_value = self.page.locator(selector).text_content()
        assert expected_value in actual_value, f"Expected {expected_value}, but got {actual_value}"

    def validate_hotel_name(self, expected_value):
        self.validate_field(self.HOTEL_NAME_SELECTOR, expected_value)

    def validate_invoice_date(self, expected_value):
        self.validate_field(self.INVOICE_DATE_SELECTOR, expected_value)

    def validate_due_date(self, expected_value):
        self.validate_field(self.DUE_DATE_SELECTOR, expected_value)

    def validate_invoice_number(self, expected_value):
        self.validate_field(self.INVOICE_NUMBER_SELECTOR, expected_value)

    def validate_booking_code(self, expected_value):
        self.validate_field(self.BOOKING_CODE_SELECTOR, expected_value)

    def validate_customer_details(self, expected_value):
        self.validate_field(self.CUSTOMER_DETAILS_SELECTOR, expected_value)

    def validate_room(self, expected_value):
        self.validate_field(self.ROOM_SELECTOR, expected_value)

    def validate_check_in(self, expected_value):
        self.validate_field(self.CHECK_IN_SELECTOR, expected_value)

    def validate_check_out(self, expected_value):
        self.validate_field(self.CHECK_OUT_SELECTOR, expected_value)

    def validate_total_stay_count(self, expected_value):
        self.validate_field(self.TOTAL_STAY_COUNT_SELECTOR, expected_value)

    def validate_total_stay_amount(self, expected_value):
        self.validate_field(self.TOTAL_STAY_AMOUNT_SELECTOR, expected_value)

    def validate_deposit_now(self, expected_value):
        self.validate_field(self.DEPOSIT_NOW_SELECTOR, expected_value)

    def validate_tax_vat(self, expected_value):
        self.validate_field(self.TAX_VAT_SELECTOR, expected_value)

    def validate_total_amount(self, expected_value):
        self.validate_field(self.TOTAL_AMOUNT_SELECTOR, expected_value)
