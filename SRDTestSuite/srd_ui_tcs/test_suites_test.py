#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Test Suites page
"""


from selenium import webdriver
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCTestSuites(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c_test_suites(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'Test Suites')]").click()
        time.sleep(2)
        self.assertEqual("SAMATE Reference Dataset", driver.title)
       
        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)

        self.assertEqual("Test Suites", driver.find_element_by_xpath("//div[@id='content']/h1").text)
        self.assertEqual("Stand-alone Suites", driver.find_element_by_xpath("//div[@id='content']/h2").text)
        self.assertEqual("SRD Suites", driver.find_element_by_xpath("//div[@id='content']/h2[2]").text)
        self.assertEqual("Archives", driver.find_element_by_xpath("//div[@id='content']/h2[3]").text)
       
       
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
