from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Instagram:
    def _init_(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath(
            "//*[@id='loginForm']/div/div[2]/div/label/input")
        time.sleep(2)


        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)


    def gir(self):
        click = self.browser.find_element_by_tag_name("//*[@type='Save Info']").click()

instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.gir()