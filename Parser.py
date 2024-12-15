import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from LoginPage import LoginPage
from MainPage import MainPage

from dotenv import load_dotenv
import os

from OfficePage import OfficePage
from UploadingReportPage import UploadingReportPage

URL = "https://omgtu.ru/"
HW_FILE_PATH = "C:\\Users\\user\\PycharmProjects\\parserhw\\hw.pdf"


SUBJECT_NAME = "Языки информационного обмена"

if not os.path.exists(HW_FILE_PATH):
    raise FileNotFoundError(f"Файл не найден: {HW_FILE_PATH}")

firefox_options = Options()
driver = webdriver.Firefox(options=firefox_options)

load_dotenv()

username = os.getenv("OMGTU_LOGIN")
password = os.getenv("OMGTU_PASSWORD")

driver.get(URL)

main_page = MainPage(driver)

main_page.go_to_login_page()

login_page = LoginPage(driver)

login_page.login(username=username,password=password)

office_page = OfficePage(driver)

office_page.go_to_uploading_report_page()

uploading_report_page = UploadingReportPage(driver)

uploading_report_page.upload_hw(file_path=HW_FILE_PATH,subject_name=SUBJECT_NAME)

time.sleep(300)
driver.quit()


