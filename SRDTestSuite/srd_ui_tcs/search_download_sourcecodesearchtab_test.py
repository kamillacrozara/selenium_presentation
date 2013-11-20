#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Source Code Search tab on the Search/Download page
"""
from selenium import webdriver
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCSearchDownloadSourceCodeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_t_c_search_download_source_code_search(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'Search / Download')]").click()
        driver.find_element_by_xpath("//a[contains(text(),'Source Code Search')]").click()
        time.sleep(2)
        self.assertEqual("SAMATE Reference Dataset", driver.title)
       
        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)
       
        common_ui_tests.testTestDownloadMenu(self, driver, self.verificationErrors)
      
        try: self.assertEqual("File contains:", driver.find_element_by_xpath("//div[@id='search_Code']/form/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("File name:", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[2]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("File size (bytes):", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Number of files:", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[4]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[5]/span/input").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Exact", driver.find_element_by_xpath("//div[@id='search_Code']/form/div/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Contains", driver.find_element_by_xpath("//div[@id='search_Code']/form/div/acronym[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Regex", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[2]/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("min", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("max", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/span[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("min", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[4]/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("max", driver.find_element_by_xpath("//div[@id='search_Code']/form/div[4]/span[3]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Search in source code engine", driver.find_element_by_xpath("//div[@id='info_search_code']/h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
       
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
        driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/input").send_keys("300")
        driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/input[2]").send_keys("800")
        driver.find_element_by_xpath("//div[@id='search_Code']/form/div[4]/input[2]").send_keys("10")
        driver.find_element_by_xpath("//div[@id='search_Code']/form/div[5]/span/input").click()
        try: self.assertEqual("View/Download", driver.find_element_by_xpath("//div[@id='content']/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
