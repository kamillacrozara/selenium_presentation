#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_bigstring_sourcecodesearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searches by 
    big strings in fields of the Source Code Search tab
"""

from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

class SrdSdBigstringSourcecodesearchtabTc(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

    def test_srd_sd_bigstring_sourcecodesearchtab_tc(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?code")
        
        driver.find_element_by_xpath("//input[@id='function']").send_keys("I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text.")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        
        driver.back()
        
        driver.find_element_by_xpath("//input[@id='function']").send_keys("I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text.")
        driver.find_element_by_xpath("(//input[@name='precision'])[2]").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        
        driver.back()
        
        driver.find_element_by_xpath("//input[@id='fileName']").send_keys("I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text.")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        
        driver.back()
        
        driver.find_element_by_xpath("//input[@id='fileName']").send_keys("I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text.")
        driver.find_element_by_xpath("//input[@name='searchNameByRegex']").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        
        driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
