#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: view_testcase_148803_page_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of a specific test case page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCViewTestCase148803Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
    

    def test_t_c_view_test_case148803_page(self):
        driver = self.driver
        driver.get(self.base_url + "/view_testcase.php?tID=148803")

        try: self.assertEqual("SAMATE Reference Dataset :: TestCase 148803", self.driver.title)
        except AssertionError as e: self.verificationErrors.append(" Wrong title on page %s" %(self.base_url + "/around.php"))

        common_ui_tests.testSRDBanner(self, self.driver, self.verificationErrors)
        common_ui_tests.testSRDMenu(self, self.driver, self.verificationErrors)
        common_ui_tests.testFooter(self, self.driver, self.verificationErrors)

        try: self.assertEqual("Downloads: ", driver.find_element_by_xpath("//div[@id='content']/div/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Downloads:' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//img[@alt='Download this Test Case #148803']"))
        try: self.assertEqual("Back to the previous page", driver.find_element_by_xpath("//div[@id='content']/h1/a").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Back to the previous page' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Test Case ID", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Test Case ID' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Bad / Good / Mixed", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[2]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Bad / Good / Mixed' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Author", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[3]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Author' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Associated test case", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[4]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Associated test case' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Contributor", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[5]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Contributor' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Language", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[6]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Language' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Type of test case", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[7]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Type of test case' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Input string", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[9]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Input string' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Expected Output", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[10]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Expected Output' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Instructions", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[11]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Instructions' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Submission date", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[12]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Submission date' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Description", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[13]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Description' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Filename", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Filename' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Flaw", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Flaw' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("148803", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[2]/span").text)
        except AssertionError as e: self.verificationErrors.append("Field '148803' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        try: self.assertEqual("Submit a comment", driver.find_element_by_xpath("//a[contains(text(),'Submit a comment')]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Submit a comment' not found on page %s" %(self.base_url + "/view_testcase.php?tID=148803"))
        
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
