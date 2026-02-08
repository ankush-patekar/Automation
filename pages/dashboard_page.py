from pages.base_page import BasePage
from locators.dashboard_locators import DashboardLocators
import random


class DashboardPage(BasePage):

    def click_add_widget(self):
        self.click(DashboardLocators.ADDWIDGET, 2)

    def click_display_as(self):
        self.click(DashboardLocators.DSIPLAYAS, 2)

    def click_widget_name(self):
        self.click_dynamic_text(DashboardLocators.WIDGETNAME, "Metric")

    def click_submit_button(self):
        self.click(DashboardLocators.buttonSubmit, 2)

    def enter_dashboard_name(self):
        suffix = random.randint(1000, 9999)
        self.type(DashboardLocators.dashboardName, f"Ankush_{suffix}")

    def click_save_button(self):
        self.click(DashboardLocators.saveDashboard, 2)
        # self.wait("2")
