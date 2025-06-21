import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class UserPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_new_user(self):
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[3]/div/div[1]/div/button").click()

    def create_user(self, name, email):
        self.driver.find_element(By.NAME, "name").send_keys(name)
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys("1234567890")
        dropdown = Select(self.driver.find_element(By.XPATH, "//*[@id='key-0']/div"))
        dropdown.select_by_visible_text("Index Universal Life (IUL)")
        self.driver.find_element(By.ID, "agentId-0").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div[2]/form/div[3]/button[1]").click()
        time.sleep(5)
