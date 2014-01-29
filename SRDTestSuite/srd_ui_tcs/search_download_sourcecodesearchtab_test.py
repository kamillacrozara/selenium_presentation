#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: search_download_sourcecodesearchtab_test.py
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
        self.maxDiff = None

    def test_t_c_search_download_source_code_search(self):
        
        self.driver.get(self.base_url + "/search.php?code")
        
        try: self.assertEqual("SAMATE Reference Dataset", self.driver.title)
        except AssertionError as e: self.verificationErrors.append(" Wrong title on page %s" %(self.base_url + "/search.php?code"))

        common_ui_tests.testSRDBanner(self, self.driver, self.verificationErrors)
        common_ui_tests.testSRDMenu(self, self.driver, self.verificationErrors)
        common_ui_tests.testFooter(self, self.driver, self.verificationErrors)
        common_ui_tests.testTestDownloadMenu(self, self.driver, self.verificationErrors)
       
        try: self.assertEqual("File contains:", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'File contains:' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("File name:", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[2]/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'File name:' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("File size (bytes):", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'File size (bytes):' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("Number of files:", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[4]/span").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Number of files:' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("Exact", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div/acronym").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Exact' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("Contains", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div/acronym[2]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Contains' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("Regex", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[2]/acronym").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Regex' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("min", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/span[2]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'min' for 'File size' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("max", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[3]/span[3]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'max' for 'File size' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("min", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[4]/span[2]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'min' for 'Number of files' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("max", self.driver.find_element_by_xpath("//div[@id='search_Code']/form/div[4]/span[3]").text)
        except AssertionError as e: self.verificationErrors.append("Field 'max' for 'Number of files' not found on page %s" %(self.base_url + "/search.php?code"))
        try: self.assertEqual("Search in source code engine", self.driver.find_element_by_xpath("//div[@id='info_search_code']/h2").text)
        except AssertionError as e: self.verificationErrors.append("Field 'Search in source code engine' not found on page %s" %(self.base_url + "/search.php?code"))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
