from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class GeneratedSrdSdDropdownSearchTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://samate.nist.gov/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_generated_srd_sd_dropdown_search_tc(self):
        driver = self.driver
        driver.get(self.base_url + "SRD/view.php")
        driver.find_element_by_link_text("Search / Download").click()
        driver.find_element_by_link_text("Search").click()
        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys("buffer")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_name("Submit").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
