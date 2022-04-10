import os
from datetime import datetime
from py.xml import html
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.redbus.in/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.close()


def pytest_html_report_title(report):
    report.title = "RedBus report"


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    ''' modifying the summary in pytest environment'''

    prefix.extend([html.h1("Auto Selecting Trip.")])
    summary.extend([html.h3("It takes input from User. ")])
    postfix.extend([html.h3("Data can be extracted from other files.")])


def pytest_html_results_table_header(cells):
    # del cells[1]
    cells.insert(0, html.th('Time', class_='sortable time', col='time'))
    cells.insert(2, html.th("Test name"))
    cells.insert(3, html.th('Description'))
    cells.insert(4, html.th('Duration'))
    cells.insert(5, html.th('URL'))
    cells.pop()
    cells.pop()
    cells.pop()


def pytest_html_results_table_row(report, cells):
    del cells[1]
    cells.insert(0, html.td(datetime.utcnow(), class_='col-time'))
    # cells.insert(1, html.td(report.tag))
    cells.insert(2, html.td(report.test_name))
    cells.insert(3, html.td(report.test_description))
    # cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("https://www.redbus.com"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            from os import getcwd
            report_directory = getcwd
            file_name = report.nodeid.replace("::", "_")[27:] + ".png"
            destination_file = os.path.join(report_directory, "reports.html")
            driver.save_screenshot(destination_file)
            if file_name:
                htm = '<div><img src="%s" alt="screenshot" style="width:300px; height:"400px" onclick="window.open(' \
                      'this.src)" align="right" </div>' % file_name
            extra.append(pytest_html.extras.html(htm))
        report.extra = extra
    testcase = str(item.function.__doc__)
    report.test_description = testcase
    c = str(item.function.__name__)[5:].title()
    c = c.replace("_", " ")
    report.test_name = c

    
