#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of a specific page in the View/Download tab
"""

from selenium import webdriver
from common_ui_tests import common_ui_tests
from selenium.webdriver.common.by import By
import unittest, time, re

class TCViewTestCase6Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_t_c_view_test_case6_page(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'View / Download')]").click()
        driver.find_element_by_xpath("//a[contains(@href, 'view_testcase.php?tID=6')]").click()
        time.sleep(2)
        self.assertEqual("SAMATE Reference Dataset :: TestCase 6", driver.title)
       
        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)

        try: self.assertEqual("Downloads: ", driver.find_element_by_xpath("//div[@id='content']/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//img[@alt='Download this Test Case #6']"))
        try: self.assertEqual("Back to the previous page", driver.find_element_by_xpath("//div[@id='content']/h1/a").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Test Case ID", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Bad / Good / Mixed", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[2]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Author", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[3]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Associated test case", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[4]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Contributor", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[5]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Language", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[6]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Type of test case", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[7]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Input string", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[9]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Expected Output", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[10]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Instructions", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[11]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Submission date", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[12]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Description", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[13]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Filename", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Flaw", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("6", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[2]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//div[@id='content']/table/tbody/tr/td[2]/a/img"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//div[@id='content']/table/tbody/tr[2]/td[2]/a/img"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(@href, 'testcases/000/000/006/Using_freed_memory.c')]"))
        driver.find_element_by_css_selector("img[alt=\"(?)\"]").click()
        try: self.assertEqual("+ Root\nCWE-398: Indicator of Poor Code Quality\n    CWE-416: Use After Free", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("CWE-416: Use After Free", driver.find_element_by_xpath("//div[@id='flaw_0']/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img[alt=\"(?)\"]").click()
        try: self.assertEqual("Submit a comment", driver.find_element_by_xpath("//a[contains(text(),'Submit a comment')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Using_freed_memory.c", driver.find_element_by_xpath("//div[@id='code']/table/tbody/tr/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
