from time import sleep

from selenium.webdriver.common.by import By

from bbs.test_case.page_obj.base import Page


class login(Page):
    url = '/base/login'

    login_username_loc = (By.ID, "username")
    login_password_loc = (By.ID, "pwd")
    login_button_loc = (By.CSS_SELECTOR, ".ant-btn")

    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    def user_login(self, username="admin", password="123456"):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    def user_login_success(self):
        return self.find_element(By.XPATH, "//span[3]/span[2]").text
