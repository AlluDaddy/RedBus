import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utils import *


def sleep_time(self, tme):
    time.sleep(tme)


class BaseDriver:
    log = Utils.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return "
            "pageLength;")
        match = False
        while not match:
            lastCount = pageLength
            sleep_time(self, 0.5)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return "
                "pageLength;")
            if lastCount == pageLength:
                match = True
        self.log.warning("Destination location is entered.")
        sleep_time(self, 4)

    def js_click(self, locator_type, locator, ind):
        b = self.driver.find_elements(locator_type, locator)
        print(len(b))
        self.driver.execute_script("arguments[0].click();", b[ind])

    def wait_presence_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
