import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AgentControlPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_agent_controls(self):
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div[3]/ul/li[1]/a")

    def search_user(self, name):
        dropdown = Select(self.driver.find_element(By.XPATH, "//*[@id='type']/div"))
        dropdown.select_by_visible_text("Digital Leads Agents")
        self.driver.find_element(By.ID, "search-input").clear()
        self.driver.find_element(By.ID, "search-input").send_keys(name)
        self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[3]/div/div[2]/div[2]/button").click()
        time.sleep(5)

    def validate_search_result(self, name):
        rows = self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[3]/div/div[3]")
        return any(name in row.text for row in rows)

    def click_view_digital_leads(self, name):
        rows = self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[3]/div/div[3]")
        for row in rows:
            if name in row.text:
                row.find_element(By.LINK_TEXT, "View Digital Leads").click()
                break