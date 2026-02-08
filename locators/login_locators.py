from selenium.webdriver.common.by import By


class LoginLocators:
    
    CONTINUE = (By.XPATH, "//button[@type='submit']")
    USERNAME = (By.XPATH, "//input[@name='email']")
    PASSWORD = (By.XPATH, "//input[@name='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

