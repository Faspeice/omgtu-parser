import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages import OfficePage, MainPage, LoginPage, UploadingReportPage

from exceptiions import PageException

SUBJECT_NAME = "Языки информационного обмена"

if __name__ == "__main__":
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)
    try:
        load_dotenv()
        username = os.getenv("OMGTU_LOGIN")
        password = os.getenv("OMGTU_PASSWORD")
        url = os.getenv("URL")
        hw_file_path = os.getenv("HW_FILE_PATH")

        if not os.path.exists(hw_file_path):
            raise FileNotFoundError(f"Файл не найден: {hw_file_path}")

        driver.get(url)

        main_page = MainPage(driver)

        main_page.go_to_login_page()

        login_page = LoginPage(driver)

        login_page.login(username=username, password=password)

        office_page = OfficePage(driver)

        office_page.go_to_uploading_report_page()

        uploading_report_page = UploadingReportPage(driver)

        uploading_report_page.upload_hw(file_path=hw_file_path, subject_name=SUBJECT_NAME)

        time.sleep(300)
    except PageException as e:
        print("Something get wrong with pages")
        print(e.__str__())
    finally:
        driver.quit()
