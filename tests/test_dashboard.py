from pages.dashboard_page import DashboardPage
from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators
import time


def test_create_dashboard(browser, login):
    dashboard_page = DashboardPage(browser)
    base_page = BasePage(browser)

    base_page.click(DashboardLocators.CREATEDASHBOARD, 5)
    base_page.click(DashboardLocators.ADDWIDGET, 5)
    time.sleep(1)
    dashboard_page.click_display_as()
    time.sleep(1)
    dashboard_page.click_widget_name()
    dashboard_page.click_submit_button()
    dashboard_page.enter_dashboard_name()
    time.sleep(3)
    dashboard_page.click_save_button()
    time.sleep(3)

