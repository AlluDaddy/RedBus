from nntplib import GroupInfo
import pytest
from testcases import Secondfile
from base.base import *
from utilities.utils import *
from ddt import ddt, data, file_data, unpack
import softest



@ddt
@pytest.mark.usefixtures("setup")
class TestMain(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.sf = Secondfile.Second(self.driver)
        self.ut = Utils()

    @data(*Utils.read_data_from_excel("C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\Red_bus\\testdata\\travel.xlsx",
                                      "Sheet1"))
    @unpack
    


    
    def test_first(self, going_from, going_to, data_of_journey):
        "Launches the pages and pass the arguments From , Destination and Date of Journey."
        # self.sf.from_to_date(going_from, going_to, data_of_journey)
        self.sf.from_to_date(going_from, going_to, str(data_of_journey))
        # print("Data is inserted")
        sleep_time(self, 2)
        "It handles the search button and Advertisements."
        self.sf.search_button()
        # print("searching")
        sleep_time(self, 5)

        self.driver.refresh()
        # print("page is refresh")
        sleep_time(self, 5)
        try:
            self.sf.add_close_btn()
        # print("Advertisement is close")
        except:
            pass

        "It Scrolls the page to End of the Page."
        self.sf.page_scroll()

        "Selected the bus and select the deck."
        self.sf.seats_button()
        sleep_time(self, 5)
