from BasePage import BasePage


class OfficePage(BasePage):
    UPLOADING_REPORTS_LOCATOR = "//a[@class='sidebar-menu__link'][@href='/ecab/vkr2.php']"

    def go_to_uploading_report_page(self):
        self.click_element(self.UPLOADING_REPORTS_LOCATOR)