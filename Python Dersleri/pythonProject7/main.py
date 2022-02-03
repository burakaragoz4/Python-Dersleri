from selenium.webdriver.common.by import By
from instagramUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "karagoz9920@hotmailcom"
password = "09180918Burak"
browserProfile = webdriver.ChromeOptions()
browser = webdriver.Chrome('chromedriver.exe', chrome_options=browserProfile)
browser.maximize_window()
browser.get("https://www.instagram.com/accounts/login/")

usernameInput = browser.findElement(By.name("username")).sendKeys(username);

passwordInput = browser.findElement(By.name("password")).sendKeys(password);
passwordInput.send_keys(Keys.ENTER)

time.sleep(2)


