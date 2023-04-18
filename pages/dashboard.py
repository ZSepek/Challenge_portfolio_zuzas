import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    contact_dev_xpath = "//*[text()='Dev team contact']"
    add_player_xpath = "//*[text()='Add player']"
    back_to_report_one_xpath = "//*/div[4]/div/div/a/button"
    back_to_report_two_xpath = "//*/div[5]/div/div/a/button"
    last_created_player_xpath = "//*/div[3]/div/div/a[1]/button"
    last_update_player_xpath = "//*/a[2]/button"
    last_created_match_xpath = "//*/a[3]/button"
    last_update_match_xpath = "//*/a[4]/button"
    menu_main_xpath = "//*[text()='Main page']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl'
    expected_title = "Scouts panel"

    pass

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title