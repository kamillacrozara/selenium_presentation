#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: search_download_searchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Search tab on the Search/Download page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCSearchDownloadSearchTab(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
    
    def test_t_c_search_download_search_tab(self):
        self.driver.get(self.base_url + "/search.php?simple")
        
        try: self.assertEqual("SAMATE Reference Dataset", self.driver.title)
        except AssertionError as e: self.verificationErrors.append(" Wrong title on page %s" %(self.base_url + "/search.php?simple"))

        common_ui_tests.testSRDBanner(self, self.driver, self.verificationErrors)
        common_ui_tests.testSRDMenu(self, self.driver, self.verificationErrors)
        common_ui_tests.testFooter(self, self.driver, self.verificationErrors)
        common_ui_tests.testTestDownloadMenu(self, self.driver, self.verificationErrors)
       
        try: self.assertEqual("Number (Test case ID):", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div/label/span/strong").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Number (Test case ID):' not found on page %s" %(self.base_url + "/search.php?simple"))
        try: self.assertEqual("Description contains:", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[2]/label/span/strong").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Description contains:' not found on page %s" %(self.base_url + "/search.php?simple"))
        try: self.assertEqual("Author:", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[3]/label/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Author:' not found on page %s" %(self.base_url + "/search.php?simple"))
        try: self.assertEqual("Contributor:", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[4]/label/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Contributor:' not found on page %s" %(self.base_url + "/search.php?simple"))
        try: self.assertEqual("Bad / Good / Mixed:", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[5]/label/span/acronym").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Bad / Good / Mixed:' not found on page %s" %(self.base_url + "/search.php?simple"))
        try: self.assertEqual("Language:", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[6]/label/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Language:' not found on page %s" %(self.base_url + "/search.php?simple"))
        try: self.assertEqual("Type of Artifact:", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[7]/label/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Type of Artifact:' not found on page %s" %(self.base_url + "/search.php?simple"))
        try: self.assertEqual("Status:", self.driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[8]/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Status:' not found on page %s" %(self.base_url + "/search.php?simple"))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
