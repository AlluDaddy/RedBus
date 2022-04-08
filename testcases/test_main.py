import pytest
from testcases import Secondfile
from base.base import *
from utilities.utils import *

@pytest.mark.usefixtures("setup")
class TestMain:

    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sf = Secondfile.Second(self.driver)
        self.ut = Utils()

    def test_first(self):
        "Launches the pages and pass the arguments From , Destination and Date of Journey."
        self.sf.from_to_date("Bangalore", "Hyderabad", "30")
        # print("Data is inserted")
        sleep_time(self, 2)

    def test_search(self):
        "It handles the search button and Advertisements."
        self.sf.search_button()
        # print("searching")
        sleep_time(self, 5)
        self.driver.refresh()
        # print("page is refresh")
        sleep_time(self, 5)
        # try:
        self.sf.add_close_btn()
        # print("Advertisement is close")
        # except:
        #     pass

    def test_page_scroll(self):
        # assert False
        "It Scrolls the page to End of the Page."
        self.sf.page_scroll()
        # print("page is scrolled")

    def test_seat_selection(self):
        "Selected the bus and select the deck."
        self.sf.seats_button()
        # print("Seats are selecting")
        sleep_time(self, 5)
