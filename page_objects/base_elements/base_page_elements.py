from abc import ABC

from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 20


class BaseElement:
    def selector(self):
        raise NotImplementedError

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        self.driver = obj.driver
        driver = obj.driver
        WebDriverWait(driver, TIMEOUT).until(
            lambda driver: driver.find_element_by_css_selector(self.selector))
        return driver.find_element_by_css_selector(self.selector)


class InputElement(BaseElement, ABC):

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, TIMEOUT).until(
            lambda driver: driver.find_element_by_css_selector(self.selector))
        print('found element')
        driver.find_element_by_css_selector(self.selector).clear()
        driver.find_element_by_css_selector(self.selector).send_keys(value)

