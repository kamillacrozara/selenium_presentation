#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Source Code Search tab on the Search/Download page
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
    
    def test_t_c_search_download_search_tab(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'Search / Download')]").click()
        driver.find_element_by_xpath("//a[contains(@href, 'search.php?simple')]").click()
        time.sleep(2)
        self.assertEqual("SAMATE Reference Dataset", driver.title)
        
        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)

        
        common_ui_tests.testTestDownloadMenu(self, driver, self.verificationErrors)
       
        
        try: self.assertEqual("Number (Test case ID):", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div/label/span/strong").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Description contains:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[2]/label/span/strong").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Author:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[3]/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Contributor:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[4]/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Bad / Good / Mixed:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[5]/label/span/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Language:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[6]/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Type of Artifact:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[7]/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Status:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[8]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Any...\nBad\nGood\nMixed", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[5]/label/span[2]/select").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Any...\nC\nC++\nJava\nAda\nPHP\nPython\nC#", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[6]/label/span[2]/select").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Any...\nSource Code\nBinary\nPseudo Code\nMix Of Artifact", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[7]/label/span[2]/select").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Candidate", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[8]/span[2]/label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Approved", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[8]/span[2]/label[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Deprecated", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[8]/span[2]/label[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//div[@id='viewForm']/form/table/tbody/tr/td/div[9]/span/input"))
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='content']/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Information about the current search engine", driver.find_element_by_xpath("//div[@id='content']/h2[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))

        common_ui_tests.testFooter(self, driver, self.verificationErrors)
        
        driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div/label/span[2]/input").send_keys("58")
        driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[9]/span/input").click()
        try: self.assertEqual("58", driver.find_element_by_xpath("//a[contains(@href, 'view_testcase.php?tID=58')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Java", driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
