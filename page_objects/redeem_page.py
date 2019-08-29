from selenium.common.exceptions import TimeoutException

from page_objects.base_elements.base_page import BasePage
from page_objects.base_elements.base_page_elements import InputElement, BaseElement


class CodeInput(InputElement):
    selector = '#shift_code_input'


class RedeemButton(BaseElement):
    selector = '#shift_code_check'


class RedeemPlatformButton(BaseElement):
    selector = '#new_archway_code_redemption > input.submit_button.redeem_button'


class RedeemResult(BaseElement):
    selector = '#code_results'


class RedeemPage(BasePage):
    fail_phrases = ['This SHiFT code has expired',
                    'This code is not available for your account',
                    'Unexpected error occurred']

    code_input = CodeInput()
    redeem_button = RedeemButton()
    redeem_platform_button = RedeemPlatformButton()
    redeem_results = RedeemResult()

    def redeem(self, code):
        self.code_input.clear()
        self.code_input = code
        self.redeem_button.click()
        while True:
            redeem_text = self.redeem_results.text
            if redeem_text == 'Please wait':
                self.driver.implicitly_wait(1)
            elif redeem_text in self.fail_phrases:
                return
            else:
                break
        try:
            self.redeem_platform_button.click()
        except TimeoutException:
            pass
