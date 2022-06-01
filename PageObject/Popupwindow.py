from behave import *
from selenium.webdriver.common.by import By


class Popupwindow:

    def __init__(self,driver):
        self.driver = driver

    Popup = (By.XPATH, "//div[@class='header flex m-b-10']//div[1]//div[1]")


    def popup(self):
        return self.driver.find_element(*Popupwindow.Popup)