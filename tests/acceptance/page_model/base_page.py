from tests.acceptance.locators.base_page import BasePageLocators
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import sys

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    @staticmethod
    def browser():
        options = webdriver.ChromeOptions()
        browser_string = sys.argv[-1].strip().lower()
        if browser_string == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_string == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_string == 'opera':
            options = webdriver.Opera()

        URL = 'http://127.0.0.1:4444/wd/hub' # selenium hub url
        try:
            # options = Options()
            options.add_argument('--headless')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-gpu")
            options.add_argument("--remote-debugging-port=0") #9222
            options.add_argument("--screen-size=1200x800")
            options.add_argument('--disable-dev-shm-usage')
            return webdriver.Remote(command_executor=URL, desired_capabilities=options.to_capabilities())
            # return webdriver.Remote("http://127.0.0.1:4446/wd/hub", DesiredCapabilities.CHROME, options=options)
            return webdriver.Chrome()
        except:
            return None

    @property
    def url(self):
        return "http://127.0.0.1:5000"

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)
