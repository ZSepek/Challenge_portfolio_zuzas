from pages.base_page import BasePage


class AddAPlayer(BasePage)
    add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = "Add player"

    pass

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.add_a_player_url) == self.expected_title