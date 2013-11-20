#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements in the More Downloads page
"""

from selenium import webdriver
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCMoreDownloads(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c_more_downloads(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'More Downloads')]").click()
        time.sleep(2)
        self.assertEqual("SAMATE Reference Dataset :: Around the Samate Reference Dataset", driver.title)
        
        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)

        try: self.assertEqual("More downloads from the Samate Reference Dataset", driver.find_element_by_xpath("//div[@id='content']/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Download the Full Manifest", driver.find_element_by_xpath("//div[@id='boxes']/table/tbody/tr/td/div/div/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Manifest generation", driver.find_element_by_xpath("//div[@id='boxes']/table/tbody/tr[2]/td/div/div/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Weaknesses and Code complexities", driver.find_element_by_xpath("//div[@id='boxes']/table/tbody/tr/td[2]/div/div/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
