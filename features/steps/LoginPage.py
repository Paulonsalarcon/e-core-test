from behave import given, when, step, then

@given("user navigates to Login Page")
def step_go_to_login_page(context):
    context.login_page.open()

@when('user enters the username "{username}"')
def step_fill_username(context, username):
    context.login_page.set_username(username)

@when('user enters the password "{password}"')
def step_fill_password(context, password):
    context.login_page.set_password(password)

@when("user clicks in Login Button")
def step_click_login(context):
    context.login_page.click_login_button()

@step('user login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)
    context.invoice_list_page.is_in_page()

@then("error message '{message}' must be shown")
def step_verify_error_message(context, message):
    assert message in context.login_page.get_error_message()
