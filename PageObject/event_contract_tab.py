from selenium.webdriver.common.by import By


class Event_contract_tab:

    def __init__(self, driver):
        self.driver = driver

    event_contract_tab = (By.XPATH, '//div[@class="event-menu-nw"]//span[1]//ul//li[12]//a')

    def Event_contract_tab(self):
        return self.driver.find_element(*Event_contract_tab.event_contract_tab)