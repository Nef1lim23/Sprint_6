from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    def current_url(self):
        return self.driver.current_url

    @staticmethod
    def format_locators(locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method, locator
