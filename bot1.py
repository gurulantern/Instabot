from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser


    def login(self, username, password):
        """Logs into the insta with terracottatoy"""
        username_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.findElement(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def login(self, username, password):
        """Logs into the insta with terracottatoy"""
        username_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='username']")
        password_input = self.browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        sleep(5)

    def go_to_login_page(self):
        self.browser.find_element(By.XPATH, "//a[text()='Log in']").click()
        sleep(2)
        return LoginPage(self.browser)

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("<your username>", "<your password>")

    errors = browser.find_element(By.CSS_SELECTOR, '#error_message')
    assert len(errors) == 0

browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
home_page.login("terracottatoy", "ouroboros")

browser.close()