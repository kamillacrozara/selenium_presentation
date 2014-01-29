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
import unittest

class TCMoreDownloadsTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
    
    def test_more_downloads_tab(self):
        self.driver.get(self.base_url + "/around.php")

        try: self.assertEqual("SAMATE Reference Dataset :: Around the Samate Reference Dataset", self.driver.title)
        except AssertionError as e: self.verificationErrors.append(" Wrong title on page %s" %(self.base_url + "/around.php"))

        common_ui_tests.testSRDBanner(self, self.driver, self.verificationErrors)
        common_ui_tests.testSRDMenu(self, self.driver, self.verificationErrors)
        common_ui_tests.testFooter(self, self.driver, self.verificationErrors)

        try: self.assertEqual("Download the Full Manifest", self.driver.find_element_by_xpath("//div[@id='boxes']/table/tbody/tr/td/div/div/h2").text)
        except AssertionError as e: self.verificationErrors.append("Section 'Download the Full Manifest' does not exist on page %s" %(self.base_url + "/around.php"))
        try: self.assertEqual("Weaknesses and Code complexities", self.driver.find_element_by_xpath("//div[@id='boxes']/table/tbody/tr/td[2]/div/div/h2").text)
        except AssertionError as e: self.verificationErrors.append("Section 'Weaknesses and Code complexities' does not exist on page %s" %(self.base_url + "/around.php"))
        try: self.assertEqual("Manifest generation", self.driver.find_element_by_xpath("//div[@id='boxes']/table/tbody/tr[2]/td/div/div/h2").text)
        except AssertionError as e: self.verificationErrors.append("Section 'Manifest generation' does not exist on page %s" %(self.base_url + "/around.php"))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
