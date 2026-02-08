from selenium.webdriver.common.by import By


class DashboardLocators:
    CREATEDASHBOARD = (By.XPATH, "//button[@class='ac-btn-group-item'][2]")
    ADDWIDGET = (By.XPATH, "//span[text()='Add Widget']")
    # DISPLAYAS = (By.XPATH,"//input[@type='search' and @aria-owns='widgetType_list']")
    DSIPLAYAS = (By.ID, "displayType")
    WIDGETNAME = (By.XPATH, "//span[@class='m-l-xs' and text()='%s']")
    buttonSubmit = (By.XPATH, "//button[@type='submit']")
    dashboardName = (By.XPATH, "//input[ @placeholder = 'Name']")
    saveDashboard = (By.XPATH, "//span[@class = 'ac-button-label' and text()='Save']")
