####################
# Name:event vendor module
# Description: To do some operation
# Author: Alex herbert
# Date: 23-05-2022
####################
# Library use #
import time
import os
import sys
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObject.Popupwindow import Popupwindow
from PageObject.event_contract_tab import Event_contract_tab
from PageObject.eventdiarypage import eventdiarypage
from PageObject.login_page import Loginpage
from Testdata.datareadwritefile import Datareadfile, usernamepass, passwordpass, datawritefail, loggedinpass
from Utilities.BaseClass import Baseclass


@allure.severity(allure.severity_level.NORMAL)
class TestEpo(Baseclass):
    @allure.description('To enter the valid username')
    def test_TC_02_username(self):
        log = self.loggerdemo()
        datareadusername = Datareadfile.username
        loginpage = Loginpage(self.driver)
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.presence_of_element_located((By.NAME, "userNameOrEmail")))
        loginpage.usernameoremail().send_keys(datareadusername)
        usernamepass()

    @allure.description('To enter the valid password')
    def test_Test_03_password(self):
        loginpage = Loginpage(self.driver)
        datareadpwd = Datareadfile.password
        loginpage.password().send_keys(datareadpwd)
        passwordpass()


    try:
        @allure.description('only login when entered a valid password')
        def test_TC_04_login_button(self):
            loginpage = Loginpage(self.driver)
            loginpage.loginbutton().click()
            time.sleep(5)
    except Exception as e:
        def test_failedcase(self):
            allure.attach(self.driver.get_screenshot_as_png(), name="testfailedscreen",
                        attachment_type=AttachmentType.PNG)
            msg2 = datawritefail()
            self.driver.close()
    finally:
        @allure.description('Once logged in successfully to take a screenshot')
        def test_TC_05_screen_shot(self):
            allure.attach(self.driver.get_screenshot_as_png(), name="testscreenshot",
                      attachment_type=AttachmentType.PNG)

    @allure.description('To close the popup window')
    def test_TC_06_popup_window(self):
        popupwindow = Popupwindow(self.driver)
        popupwindow.popup().click()

    @allure.description('when successfully logged in to check the title for confirmation')
    def test_TC_07_logged_conformation(self):
        title1 = self.driver.title
        if title1 == "Event Plan On":
            print("logged in successfully")
            msg1 = loggedinpass()
        else:
            msg2 = datawritefail()

    @allure.description('To click the desired event')
    def test_TC_08_event_diary(self):
        eventdiary = eventdiarypage(self.driver)
        time.sleep(3)
        eventdiary.eventdiarytask().click()

    @allure.description('To click the respective module')
    def test_TC_09_event_contract_tab(self):
        event_contract = Event_contract_tab(self.driver)
        time.sleep(4)
        event_contract.Event_contract_tab().click()
        time.sleep(4)

    def test_TC_10_add_contract(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@ptooltip="New Contract"]').click()
        time.sleep(3)
        self.driver.find_element_by_id('contractName').send_keys('organizer1')
        time.sleep(3)
        self.driver.find_element_by_xpath('//a[@ptooltip="Contract Template"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//app-contract-modal[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/p-dropdown[1]/div[1]/div[3]').click()
        time.sleep(3)
        ele = self.driver.find_elements_by_xpath('//div[@class="ui-dropdown-items-wrapper"]//ul//p-dropdownitem')
        iter1 = -1
        for names in ele:
            iter1 = iter1 + 1
            text1 = names.text
            print(text1)
            if text1 == "Sample Speaker Agreement":
                self.driver.find_elements_by_xpath('//li[@class="ui-dropdown-item ui-corner-all"]//span')[iter1].click()
                time.sleep(3)
                break
        self.driver.find_element_by_xpath('//button[contains(text(), "Apply")]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Assign Tags"]').send_keys('contract')
        time.sleep(6)
        actions = ActionChains(self.driver)
        dd_click = self.driver.find_element_by_xpath('//app-contract-modal[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/p-scrollpanel[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/p-multiselect[1]/div[1]/div[3]')
        actions.double_click(dd_click).perform()
        time.sleep(3)
        ele2 = self.driver.find_elements_by_xpath('//div[@class="ui-multiselect-items-wrapper"]//ul//p-multiselectitem')
        iter2 = -1
        for names2 in ele2:
            iter2 = iter2 + 1
            text2 = names2.text
            print(text2)
            if text2 == "Ryan Fond  (Vendor)":
                self.driver.find_elements_by_xpath('//li[@class="ui-multiselect-item ui-corner-all"]//div[1]//div[1]')[iter2].click()
                time.sleep(3)
                break
        time.sleep(6)
        self.driver.find_element_by_xpath('//a[@class="ui-multiselect-close ui-corner-all"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//span[contains(text(), " Create Contract")]').click()
        time.sleep(3)

    def test_TC_11_preview(self):
        time.sleep(3)
        ele3 = self.driver.find_elements_by_xpath('//table[@class="table qtTable valign tblmt-1 cf"]//tbody//tr//td[1]')
        iter3 = -1
        for names3 in ele3:
            iter3 = iter3 + 1
            text3 = names3.text
            print(text3)
            if text3 == "Sample Speaker Agreement":
                self.driver.find_elements_by_xpath('//span[@ptooltip="Preview"]')[iter3].click()
                time.sleep(3)
                break
        allure.attach(self.driver.get_screenshot_as_png(), name="preview",
                      attachment_type=AttachmentType.PNG)
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Back')]").click()
        time.sleep(3)

    def test_TC_11_edit_contract(self):
        time.sleep(3)
        ele4 = self.driver.find_elements_by_xpath('//table[@class="table qtTable valign tblmt-1 cf"]//tbody//tr//td[1]')
        iter4 = -1
        for names4 in ele4:
            iter4 = iter4 + 1
            text4 = names4.text
            print(text4)
            if text4 == "Sample Speaker Agreement":
                self.driver.find_elements_by_xpath('//span[@ptooltip="Edit"]')[iter4].click()
                time.sleep(3)
                break
        self.driver.find_element_by_xpath('//input[@placeholder="Assign Tags"]').send_keys('sample')
        time.sleep(3)
        self.driver.find_element_by_id('contractName').clear()
        time.sleep(3)
        self.driver.find_element_by_id('contractName').send_keys('organizer1')
        time.sleep(3)
        self.driver.find_element_by_xpath('//span[contains(text(), "Update Contract")]').click()
        time.sleep(3)


    def test_TC_12_delete_contract(self):
        time.sleep(3)
        ele5 = self.driver.find_elements_by_xpath('//table[@class="table qtTable valign tblmt-1 cf"]//tbody//tr//td[1]')
        iter5 = -1
        for names5 in ele5:
            iter5 = iter5 + 1
            text5 = names5.text
            print(text5)
            if text5 == "organizer1":
                self.driver.find_elements_by_xpath('//span[@ptooltip="Delete"]')[iter5].click()
                time.sleep(3)
                break
        self.driver.find_element_by_xpath('//button[contains(text(), "Delete")]').click()
        time.sleep(3)



































        








