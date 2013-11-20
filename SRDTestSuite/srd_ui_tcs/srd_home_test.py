#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Home page
"""

from selenium import webdriver
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCSRDHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c_s_r_d_home(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'SRD Home')]").click()
        time.sleep(2)
        try: self.assertEqual("SAMATE Reference Dataset", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))

        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)

        try: self.assertEqual("Welcome to the NIST SAMATE Reference Dataset Project", driver.find_element_by_css_selector("h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Browse, download, and search the SRD", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("How to submit test cases", driver.find_element_by_xpath("//div[@id='content']/h2[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Acknowledgments", driver.find_element_by_xpath("//div[@id='content']/h2[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Other Assurance Tool Test Collections", driver.find_element_by_xpath("//div[@id='content']/h2[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
        
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
