import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None


def pytest_addoption(parser):
    """
    This function is used for taking command line argument from terminal
    :param parser: Browser name
    :return: {request.config.getoption("--variable name")} use this code to retrieve variable value
    """
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser_name: chrome or firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("--browser_name")
    print("welcome")
    if browser == "chrome":
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    elif browser == "firefox":
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)

    driver.implicitly_wait(15)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver  # wherever we use this setup fixture in the test class then driver will be set as ..
    # ...class variable of the test class
    yield
    driver.close()


# @pytest.mark.hookwrapper
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
