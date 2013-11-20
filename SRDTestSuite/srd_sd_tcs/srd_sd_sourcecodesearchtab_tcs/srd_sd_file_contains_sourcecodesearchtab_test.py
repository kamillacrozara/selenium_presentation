#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_file_contains_sourcecodesearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searches by the file names in 
    Source Code Search tab. It takes the names of one file per test case
    and verifies if the search by file name returns only one test case
    with the correct file name.
"""

from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

class SrdSdFileContainsSourceCodeSearchtabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
        self.fileNames = []

    """This method verifies the results of searchers by filename"""
    def test_srd_sd_file_contains_sourcecodesearchtab(self):

        key_words = ["null", "string", "memory", 
                     "buffer", "stack", "heap", 
                     "integer", "race", "error", 
                     "switch", "break", "pointer",
                     "CWE", "injection", "command" ]
        
        for word in key_words:
            self.driver.get(self.base_url + "/search.php?code")
            self.driver.find_element_by_xpath("//input[@id='fileName']").send_keys(word)
            self.driver.find_element_by_xpath("//input[@name='Submit']").click()
            #must have only one test case with the same ID and the same file
            foundTestCases = common_sd_methods.count_test_cases_in_page(self.driver)
            j = 2
            while j < (foundTestCases+2):
                self.driver.find_element_by_xpath(("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j)).click()
                foundFileName = self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td[2]/ul/li/a").text
                try: self.assertTrue(re.search(foundFileName, word))
                except AssertionError as e: self.verificationErrors.append(("The search by %s using the 'file contains' field doesn't return the  is not the same in the test case page" %word))
                j += 1
                self.driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
