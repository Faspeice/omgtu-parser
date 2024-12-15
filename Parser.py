import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from LoginPage import LoginPage
from MainPage import MainPage

from dotenv import load_dotenv
import os

from OfficePage import OfficePage

firefox_options = Options()
driver = webdriver.Firefox(options=firefox_options)

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

driver.get("https://omgtu.ru/")

main_page = MainPage(driver)

main_page.go_to_login_page()

login_page = LoginPage(driver)

login_page.login(username=username,password=password)

office_page = OfficePage(driver)

office_page.go_to_uploading_report_page()

time.sleep(300)
driver.quit()


