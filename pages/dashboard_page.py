from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_user_tab(self):
        self.driver.find_element(By.LINK_TEXT,"Users").click()