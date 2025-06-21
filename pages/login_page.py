from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "login-email").send_keys(username)
        self.driver.find_element(By.ID, "login-password").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div/div/div/div/div[3]/div/div/div/div[1]/div/div/div/form/button").click()
