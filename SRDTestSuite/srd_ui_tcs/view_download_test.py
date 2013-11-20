#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: more_downloads_test.py
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
    
    def test_t_c_view_download(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'View / Download')]").click()
        time.sleep(2)
        try: self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)

        self.assertTrue(common_ui_tests.is_element_present(self, By.CSS_SELECTOR, "h1"))
        try: self.assertEqual("Downloads:   ", driver.find_element_by_css_selector("span.menu-top-right").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Results:", driver.find_element_by_css_selector("strong").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.CSS_SELECTOR, "img[alt=\"Download these 88737 test cases\"]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.CSS_SELECTOR, "img[alt=\"Download all the test cases on the page\"]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.CSS_SELECTOR, "img[alt=\"Download all the test cases in the SRD\"]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.CSS_SELECTOR, "img[alt=\"Download the selected Test Cases\"]"))
        try: self.assertEqual("Pages: 1 2 3 4 5 ... >> Last\nGo to page:", driver.find_element_by_xpath("//div[@id='content']/div[2]/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='content']/div[2]/span[2]/input").clear()
        driver.find_element_by_xpath("//div[@id='content']/div[2]/span[2]/input").send_keys("64")
        driver.find_element_by_xpath("//div[@id='content']/div[2]/span[2]/input").send_keys(Keys.ENTER)
        try: self.assertEqual("Test Case ID", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Submission Date", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Language", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Type of Artifact", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[5]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Status", driver.find_element_by_css_selector("acronym[title=\"C: Candidate - A: Approved - D: Deprecated\"]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Description", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[7]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Weakness", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[8]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Bad / Good / Mixed", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[9]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]/a/img").click()
        try: self.assertEqual("148803", driver.find_element_by_xpath("//a[contains(@href, 'view_testcase.php?tID=148803')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]/a/img").click()
        try: self.assertEqual("4", driver.find_element_by_xpath("//a[contains(@href, 'view_testcase.php?tID=4')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("1 2 3 4 5 ... >> Last\nTotal of selected test cases: 88737", driver.find_element_by_xpath("//div[5]/span[@class='fieldName']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Total pages: 4437\nNumber of Test Cases per page:\n5\n10\n20\n30\n50\n100", driver.find_element_by_xpath("//div[5]/form/div/span[@class='data']").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.NAME, "setNewCountId"))
        
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
        
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
