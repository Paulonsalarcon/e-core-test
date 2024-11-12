from behave import then
from playwright.sync_api import sync_playwright

@then('Invoice Details Page is open')
def step_then_invoice_details_page_is_open(context):
    context.invoice_details_page.wait_until_page_loaded()

@then('Hotel Name must be "{hotel_name}"')
def step_then_hotel_must_be(context, hotel_name):
    context.invoice_details_page.validate_hotel_name(hotel_name)

@then('Invoice Date must be "{invoice_date}"')
def step_then_invoice_date_must_be(context, invoice_date):
    context.invoice_details_page.validate_invoice_date(invoice_date)

@then('Due Date must be "{due_date}"')
def step_then_due_date_must_be(context, due_date):
    context.invoice_details_page.validate_due_date(due_date)

@then('Invoice Number must be "{invoice_number}"')
def step_then_invoice_number_must_be(context, invoice_number):
    context.invoice_details_page.validate_invoice_number(invoice_number)

@then('Booking Code must be "{booking_code}"')
def step_then_booking_code_must_be(context, booking_code):
    context.invoice_details_page.validate_booking_code(booking_code)

@then('Customer Details must be "{customer_details}"')
def step_then_customer_details_must_be(context, customer_details):
    context.invoice_details_page.validate_customer_details(customer_details)

@then('Room must be "{room}"')
def step_then_room_must_be(context, room):
    context.invoice_details_page.validate_room(room)

@then('Check In must be "{check_in}"')
def step_then_check_in_must_be(context, check_in):
    context.invoice_details_page.validate_check_in(check_in)

@then('Check Out must be "{check_out}"')
def step_then_check_out_must_be(context, check_out):
    context.invoice_details_page.validate_check_out(check_out)

@then('Total Stay Count must be "{total_stay_count}"')
def step_then_total_stay_count_must_be(context, total_stay_count):
    context.invoice_details_page.validate_total_stay_count(total_stay_count)

@then('Total Stay Amount must be "{total_stay_amount}"')
def step_then_total_stay_amount_must_be(context, total_stay_amount):
    context.invoice_details_page.validate_total_stay_amount(total_stay_amount)

@then('Deposit Now must be "{deposit_now}"')
def step_then_deposit_now_must_be(context, deposit_now):
    context.invoice_details_page.validate_deposit_now(deposit_now)

@then('Tax & VAT must be "{tax_vat}"')
def step_then_tax_vat_must_be(context, tax_vat):
    context.invoice_details_page.validate_tax_vat(tax_vat)

@then('Total Amount must be "{total_amount}"')
def step_then_total_amount_must_be(context, total_amount):
    context.invoice_details_page.validate_total_amount(total_amount)

@then('the invoice details must be')
def step_then_invoice_details_must_be(context):
    # Extract the expected values from the data table
    for row in context.table:
        context.invoice_details_page.validate_hotel_name(row['HotelName'])
        context.invoice_details_page.validate_invoice_date(row['InvoiceDate'])
        context.invoice_details_page.validate_due_date(row['DueDate'])
        context.invoice_details_page.validate_invoice_number(row['InvoiceNumber'])
        context.invoice_details_page.validate_booking_code(row['BookingCode'])
        context.invoice_details_page.validate_customer_details(row['CustomerDetails'])
        context.invoice_details_page.validate_room(row['Room'])
        context.invoice_details_page.validate_check_in(row['CheckIn'])
        context.invoice_details_page.validate_check_out(row['CheckOut'])
        context.invoice_details_page.validate_total_stay_count(row['TotalStayCount'])
        context.invoice_details_page.validate_total_stay_amount(row['TotalStayAmount'])
        context.invoice_details_page.validate_deposit_now(row['DepositNow'])
        context.invoice_details_page.validate_tax_vat(row['Tax&VAT'])
        context.invoice_details_page.validate_total_amount(row['TotalAmount'])