
from BasePage import BasePage


class LoginPage(BasePage):
    LOGIN_FIELD_LOCATOR = "//input[@class='abitinput'][@name='USER_LOGIN']"
    PASSWORD_FIELD_LOCATOR = "//input[@class='abitinput'][@name='USER_PASSWORD']"
    LOGIN_BUTTON_LOCATOR = "//div[@class='abitsubmitkey'][.='войти']"

    def login(self,username,password):
        self.send_keys_to_element(self.LOGIN_FIELD_LOCATOR, username)
        self.send_keys_to_element(self.PASSWORD_FIELD_LOCATOR, password)
        self.click_element(self.LOGIN_BUTTON_LOCATOR)