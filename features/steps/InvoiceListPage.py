from behave import given, when, step, then

@then("Invoice List Page must be open")
def step_invoice_list_page_is_open(context):
    context.invoice_list_page.is_in_page()

@when("user clicks in first invoice details")
def step_click_first_invoice_details(context):
    context.invoice_list_page.click_first_invoice()