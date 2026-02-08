from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator, condition=EC.visibility_of_element_located):
        """Wait until element condition is met and return element"""
        return self.wait.until(condition(locator))

    def click(self, locator, timeout):
        """Wait until element is clickable and then click"""
        self.wait_for_element(locator, EC.element_to_be_clickable).click()

    def type(self, locator, text):
        """Wait until element is visible and then type"""
        self.wait_for_element(locator).send_keys(text)

    def get_text(self, locator):
        """Wait until element is visible and return text"""
        return self.wait_for_element(locator).text

    def wait_for_page_load(self):
        """Wait until page is fully loaded (DOM + AJAX)"""
        try:
            self.wait.until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            # also wait for jQuery active requests = 0 (if jQuery present)
            self.wait.until(
                lambda d: d.execute_script("return window.jQuery != undefined && jQuery.active == 0")
            )
            return True
        except TimeoutException:
            return False

    def click_dynamic_text(self, locator_template, dynamic_text):
        """
        Replace %s in locator with dynamic_text and click the element.
        """
        by, value = locator_template
        locator = (by, value % dynamic_text)

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
