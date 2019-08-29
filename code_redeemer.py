from typing import Dict

from selenium import webdriver

from page_objects.login_page import LoginPage
from page_objects.redeem_page import RedeemPage

REWARDS_PAGE_URL = 'https://shift.gearboxsoftware.com/rewards'


class CodeRedeemer:
    def __init__(self, game) -> None:
        self.driver = webdriver.Chrome()
        self.game = game

        super().__init__()

    def run(self):
        self.open_shift_page()
        self.perform_login()
        for code in self._parse_codes():
            self.redeem_code(code.strip())

    def open_shift_page(self):
        self.driver.get(REWARDS_PAGE_URL)

    def perform_login(self):
        login_page = LoginPage(self.driver)
        credentials = self._parse_credentials()
        login_page.login(**credentials)

    def redeem_code(self, code):
        redeem_page = RedeemPage(self.driver)
        redeem_page.redeem(code)

    @staticmethod
    def _parse_credentials() -> Dict:
        with open('.credentials') as f:
            credentials = {}
            for line in f:
                k, v = line.split('=')
                credentials[k] = v.strip()
        return credentials

    def _parse_codes(self):
        with open(f'codes/{self.game}_codes.txt') as f:
            return f.readlines()
