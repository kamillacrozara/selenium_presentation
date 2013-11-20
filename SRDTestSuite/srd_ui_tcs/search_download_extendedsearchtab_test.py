#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Extended Search tab on the Search/Download page
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCSearchDownloadExtendedSearchTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_t_c_search_download_extended_search_tab(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'Search / Download')]").click()
        driver.find_element_by_xpath("//a[contains(@href, 'search.php?extended')]").click()
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
        try: self.assertEqual("Language:\nAny...\nC\nC++\nJava\nAda\nPHP\nPython\nC#", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[6]").text.encode("utf-8"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Language:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[6]/label/span").text.encode("utf-8"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Type of Artifact:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[7]/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Status:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[8]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Weakness:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[9]/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Code complexity:", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[10]/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Query Date:\n(Format: M/d/Y)\nYou can use the calendar (next icon).", driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[11]/fieldset/label/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//div[@id='viewForm']/form/table/tbody/tr/td/div[12]/span/input"))
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
        try: self.assertEqual("", driver.find_element_by_xpath("//span[@id='dateChooser']/div/span/img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Any", driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Before", driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("On", driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("After", driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[4]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Click here if experiencing some trouble with the JavaScript trees.", driver.find_element_by_xpath("//a[contains(@href, 'search.php?extended&tree')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Weakness", driver.find_element_by_xpath("//div[@id='selection_flaw_codeq']/ul/li/a").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Code Complexity", driver.find_element_by_xpath("//div[@id='selection_flaw_codeq']/ul/li[2]/a").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Any...", driver.find_element_by_xpath("//div[@id='FlawTree']/div[2]/div/span/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='FlawTree']/div[2]/div/img").click()
        try: self.assertEqual("CWE-843: Access of Resource Using Incompatible Type (Type Confusion)", driver.find_element_by_xpath("//div[@id='FlawTree']/div[2]/div/div/div/span/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("CWE-533: Info Leak Server Log", driver.find_element_by_xpath("//div[@id='FlawTree']/div[2]/div/div/div[28]/span/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='FlawTree']/div[2]/div/img").click()
        try: self.assertEqual("Help", driver.find_element_by_xpath("//div[@id='content']/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Information about the current search engine", driver.find_element_by_xpath("//div[@id='content']/h2[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
       
        
        driver.find_element_by_xpath("//span[@id='dateChooser']/div/span/img").click()
        driver.find_element_by_xpath("//span[@id='dateChooser']/div/div/div/table/tbody/tr/td/table/tbody/tr/td").click()
        driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[2]/input").click()
        driver.find_element_by_xpath("//div[@id='viewForm']/form/table/tbody/tr/td/div[12]/span/input").click()
        try: self.assertEqual("View/Download", driver.find_element_by_xpath("//div[@id='content']/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
