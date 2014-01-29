#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: view_download_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the View/Download page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCViewDownload(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
    
    def test_t_c_view_download(self):
        driver = self.driver
        driver.get(self.base_url + "/view.php")
        try: self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        except AssertionError as e: self.verificationErrors.append("Wrong title on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))

        common_ui_tests.testSRDBanner(self, self.driver, self.verificationErrors)
        common_ui_tests.testSRDMenu(self, self.driver, self.verificationErrors)
        common_ui_tests.testFooter(self, self.driver, self.verificationErrors)
        
        
        try: self.assertEqual("Test Case ID", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Test Case ID' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Submission Date", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[3]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Submission Date' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Language", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[4]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Language' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Type of Artifact", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[5]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Type of Artifact' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Status", driver.find_element_by_css_selector("acronym[title=\"C: Candidate - A: Approved - D: Deprecated\"]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Status' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Description", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[7]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Description' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Weakness", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[8]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Weakness' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Bad / Good / Mixed", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[9]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Bad / Good / Mixed' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))

        
        self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]/a/img").click()
        try: self.assertEqual("148803", driver.find_element_by_xpath("//a[contains(@href, 'view_testcase.php?tID=148803')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]/a/img").click()
        try: self.assertEqual("4", driver.find_element_by_xpath("//a[contains(@href, 'view_testcase.php?tID=4')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
