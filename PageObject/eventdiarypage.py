from selenium.webdriver.common.by import By


class eventdiarypage:
    def __init__(self, driver):
        self.driver = driver

    task1 = (By.XPATH, '//div//div[@class="owl-item active"][1]//div[1]//div[1]//div[1]//div[2]//div[1]//h4//a')

    def eventdiarytask(self):
        return self.driver.find_element(*eventdiarypage.task1)