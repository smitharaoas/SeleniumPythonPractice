import os

import pytest
import pytest_html
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions



def pytest_addoption(parser):
    parser.addoption("--browserName",action="store",default ="firefox",help ="to select browser")


@pytest.fixture
def browser_driver(request):

    browser = request.config.getoption("--browserName")
    if browser == "chrome":
        print(browser)
        options = ChromeOptions()
        options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
        })
        print(options.experimental_options)
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-save-password-bubble")
        driver = webdriver.Chrome(options=options)
    elif browser=="firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    elif browser=="ie":
        options = EdgeOptions()
        driver = webdriver.Edge(options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()



# -------------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser_driver")
        if driver:
            # Make sure the screenshots directory exists
            screenshot_dir = os.path.abspath("reports/screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_name = f"{item.name}.png"
            screenshot_path = os.path.join(screenshot_dir, screenshot_name)
            driver.save_screenshot(screenshot_path)

            # Attach to HTML report
            if hasattr(item.config, "_html"):
                extra = getattr(rep, "extra", [])
                # Use base64-encoded image (important for self-contained HTML)
                with open(screenshot_path, "rb") as image_file:
                    import base64
                    encoded = base64.b64encode(image_file.read()).decode("utf-8")
                html = f'<div><img src="data:image/png;base64,{encoded}" alt="screenshot" style="width:600px;height:auto;" onclick="window.open(this.src)" /></div>'
                extra.append(pytest_html.extras.html(html))
                rep.extras = extra

# Needed for pytest-html to recognize the plugin and allow screenshots
def pytest_configure(config):
    config._html = config.pluginmanager.getplugin("html")
