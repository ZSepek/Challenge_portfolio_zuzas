from pages.base_page import BasePage

class Match_form(BasePage):
    my_team_input_xpath = "//*[@name='myTeam']"
    enemy_team_input_xpath = "//*[@name='enemyTeam']"
    my_team_score_input_xpath = "//*[@name='myTeamScore']"
    enemy_score_input_xpath = "//*[@name='enemyTeamScore']"
    shirt_color_input_xpath = "//*[@name='tshirt']"
    time_played_input_xpath = "//*[@name='timePlayed']"
    web_match_input_xpath = "//*[@name='webMatch']"
    rating_input_xpath = "//*[@name='rating']"
    league_input_xpath = "//*[@name='league']"
    number_input_xpath = "//*[@name='number']"
    general_input_xpath = "//*[@name='general']"
    submit_button_xpath = "//*[@type='submit']"

    pass
