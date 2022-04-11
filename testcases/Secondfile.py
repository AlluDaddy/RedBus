from base.base import *
from selenium.webdriver.common.by import By
from base.base import BaseDriver
# import pyautogui
from selenium.webdriver.common.keys import Keys
from utilities.utils import *


class Second(BaseDriver):
    log = Utils.custom_logger()
    global SEAT_BUTTON,  VIEW_SEATS, NEXT_BUTTON, SEARCH_BUTTON
    SEAT_BUTTON = '//div[@class="button view-seats fr" and contains(text(),"View Seats")]'
    SEARCH_BUTTON = "search_btn"
    VIEW_SEATS = '//div[@class="button view-seats fr" and contains(text(),"View Seats")]'
    NEXT_BUTTON = "//tr/td[@class='next']"

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    def add_close_btn(self):
        try:
            add_close = self.driver.find_element(By.CLASS_NAME, "close")
            add_close.click()
            self.log.warning("Advertisement is closed.")
        except:
            self.log.error("Advertisement is not visible.")

    def from_to_date(self, from_, to_, date_):
        source = self.driver.find_element(By.ID, "src")
        source.send_keys(from_)
        sleep_time(self, 1)
        self.log.info("Source location is entered")
        source.send_keys(Keys.ENTER)
        # pyautogui.press("enter")
        dest = self.driver.find_element(By.ID, "dest")
        dest.send_keys(to_)
        sleep_time(self, 3)
        self.log.info("Destination location is entered.")
        dest.send_keys(Keys.ENTER)
        # pyautogui.press("enter")
        dot = self.driver.find_element(By.ID, "onward_cal")
        dot.click()
        sleep_time(self, 0.5)
        nxt_btn = self.driver.find_element_by_xpath(NEXT_BUTTON)
        nxt_btn.click()
        date_in_dot = self.driver.find_element_by_xpath("(//tr/td[contains(@class,'day') and contains(text()," + date_ + ")])[1]")
        date_in_dot.click()
        self.log.info("Date of journey is selected.")

    def search_button(self):
        self.wait_until_element_is_clickable(By.ID, SEARCH_BUTTON).click()
        self.log.warning("search button is clicked.")

    def seats_button(self):
        seat_button = self.wait_presence_elements(By.XPATH, SEAT_BUTTON)
        # print("Len", len(seat_button))
        self.js_click(By.XPATH, VIEW_SEATS, 3)
        self.log.info("Total no. of seats " + str(len(seat_button)))

