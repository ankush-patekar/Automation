from pages.dashboard_page import DashboardPage
from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators
import time
import pytest


class TestDashboard:
    @pytest.fixture(autouse=True)
    def _setup_pages(self, browser, login):
        self.dashboard_page = DashboardPage(browser)
        self.base_page = BasePage(browser)

    def test_create_dashboard(self):
        self.base_page.click(DashboardLocators.CREATEDASHBOARD, 5)
        self.base_page.click(DashboardLocators.ADDWIDGET, 5)
        time.sleep(1)
        self.dashboard_page.click_display_as()
        time.sleep(1)
        self.dashboard_page.click_widget_name()
        self.dashboard_page.click_submit_button()
        time.sleep(2)
        self.dashboard_page.enter_dashboard_name()
        time.sleep(3)
        self.dashboard_page.click_save_button()
        time.sleep(2)

    def test_create_dashboard1(self):
        self.base_page.click(DashboardLocators.CREATEDASHBOARD, 2)


