import mechanize
import re


class DragonKnight:
    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.addheaders = [
            ("User-agent", "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0")]

        # Character stats
        self.hp = 0
        self.mp = 0
        self.tp = 0

        self.level = 0
        self.exp = 0
        self.gold = 0

        self.x_coord = 0
        self.y_coord = 0

    def login(self, username, password):
        self.browser.open("http://dragon.se7enet.com/login.php?do=login")

        self.browser.select_form(nr=0)
        self.browser.form["username"] = username
        self.browser.form["password"] = password

        response = self.browser.submit()
        self.update_stats(response.get_data())

    def is_fighting(self):
        return self.browser.geturl() == "http://dragon.se7enet.com/index.php?do=fight"

    def is_dead(self):
        return "You have died." in self.browser._response.get_data()

    def do_melee_attack(self):
        if self.is_fighting():
            self.browser.select_form(nr=1)
            response = self.browser.submit(name="fight", label="Fight")
            self.update_stats(response.get_data())

    def go_direction(self, direction="north"):
        self.browser.select_form(nr=0)
        response = self.browser.submit(name=direction.lower(), label=direction.lower().capitalize())
        self.update_stats(response.get_data())

    def go_town(self, town_id=0):
        response = self.browser.open("http://dragon.se7enet.com/index.php?do=gotown:%s" % town_id)
        self.update_stats(response.get_data())

    def get_rest(self):
        self.browser.open("http://dragon.se7enet.com/index.php?do=inn")
        self.browser.select_form(nr=1)
        response = self.browser.submit()
        self.update_stats(response.get_data())

    def do_fast_spell(self, spell_id=1):
        response = self.browser.open("http://dragon.se7enet.com/index.php?do=spell:%s" % spell_id)
        self.update_stats(response.get_data())

    def update_stats(self, html):

        # Clean the html
        html = html.replace("<blink><span class=\"highlight\"><b>*", "").replace("*</b></span></blink>", "")

        latitude_match = re.search("Latitude: (.*?)<br />", html)
        longitude_match = re.search("Longitude: (.*?)<br />", html)

        level_match = re.search("Level: (.*?)<br />", html)
        exp_match = re.search("Exp: (.*?)<br />", html)
        gold_match = re.search("Gold: (.*?)<br />", html)

        hp_match = re.search("[^ ]HP: (.*?)<br />", html)
        mp_match = re.search("MP: (.*?)<br />", html)
        tp_match = re.search("TP: (.*?)<br />", html)

        if latitude_match.group(1).endswith("N"):
            self.y_coord = int(latitude_match.group(1)[:-1])
        else:
            self.y_coord = int(latitude_match.group(1)[:-1]) * -1

        if longitude_match.group(1).endswith("E"):
            self.x_coord = int(longitude_match.group(1)[:-1])
        else:
            self.x_coord = int(longitude_match.group(1)[:-1]) * -1

        self.level = int(level_match.group(1))
        self.exp = int(exp_match.group(1).replace(",", ""))
        self.gold = int(gold_match.group(1).replace(",", ""))

        self.hp = int(hp_match.group(1))
        self.mp = int(mp_match.group(1))
        self.tp = int(tp_match.group(1))