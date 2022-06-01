
from selenium.webdriver.common.by import By
from behave import *


class Loginpage:

    def __init__(self,driver):
        self.driver = driver

    Username = (By.NAME, "userNameOrEmail")
    Password = (By.NAME, "password")
    Loginbutton = (By.XPATH, "//button[@type='submit']")


    def usernameoremail(self):
        return self.driver.find_element(*Loginpage.Username)


    def password(self):
        return self.driver.find_element(*Loginpage.Password)


    def loginbutton(self):
        return self.driver.find_element(*Loginpage.Loginbutton)

