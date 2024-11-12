from playwright.sync_api import BrowserContext

class LoginPage:
    URL = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/"
    USERNAME_FIELD = "input[name=username]"
    PASSWORD_FIELD = "input[name=password]"
    LOGIN_BUTTON = "#btnLogin"
    ERROR_MESSAGE = ".alert"

    def __init__(self, browser_context: BrowserContext):
        self.browser_context = browser_context
        self.page = self.browser_context.pages[0]

    def open(self):
        self.page.goto(self.URL)

    def set_username(self, username: str):
        self.page.fill(self.USERNAME_FIELD, username)

    def set_password(self, password: str):
        self.page.fill(self.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.page.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        return self.page.text_content(self.ERROR_MESSAGE)

    def login(self, username: str, password: str):
        self.open()
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
