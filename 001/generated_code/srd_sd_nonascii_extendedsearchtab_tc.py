#!/usr/bin/python
# -*- coding: utf-8 *-*
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class SrdSdNonasciiExtendedsearchtabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://samate.nist.gov/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_srd_sd_nonascii_extendedsearchtab_tc(self):
        driver = self.driver
        driver.get(self.base_url + "/ngSRD/view.php")
        driver.find_element_by_xpath("//a[contains(text(),'SRD Home')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Search / Download')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Extended Search')]").click()
        try: self.assertEqual("SAMATE Reference Dataset", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//input[@name='reference']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        try: self.assertEqual("Test Case ID", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Description", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[7]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Weakness", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[8]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_xpath("//input[@name='description']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        try: self.assertEqual("View/Download\nDownloads:     \n\nThere is no such test case in the database! Back to the previous page", driver.find_element_by_xpath("//div[@id='content']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Back to the previous page", driver.find_element_by_link_text("Back to the previous page").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_xpath("//input[@name='author']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        try: self.assertEqual("View/Download\nDownloads:     \n\nThere is no such test case in the database! Back to the previous page", driver.find_element_by_xpath("//div[@id='content']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Back to the previous page", driver.find_element_by_link_text("Back to the previous page").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_xpath("//input[@name='contributor']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        try: self.assertEqual("View/Download\nDownloads:     \n\nThere is no such test case in the database! Back to the previous page", driver.find_element_by_xpath("//div[@id='content']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Back to the previous page", driver.find_element_by_link_text("Back to the previous page").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.get(self.base_url + "")
    
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
