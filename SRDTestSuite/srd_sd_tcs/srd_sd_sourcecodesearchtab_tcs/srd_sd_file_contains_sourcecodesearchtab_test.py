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
        #self.base_url = "http://samate.nist.gov/SRD"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
        self.fileNames = []

    """This method verifies the results of searchers using the field 'File Contains'"""
    def test_srd_sd_file_contains_sourcecodesearchtab(self):

        key_words = ["null", "string", "memory", 
                     "buffer", "stack", "heap", 
                     "integer", "race", "error", 
                     "switch", "break", "pointer",
                     "CWE", "injection", "command"]

        

        for word in key_words:
            self.driver.get(self.base_url + "/search.php?code")
            self.driver.find_element_by_xpath("//input[@id='function']").send_keys(word)
            self.driver.find_element_by_xpath("//input[@name='Submit']").click()
            foundTestCases = common_sd_methods.count_test_cases_in_page(self.driver)
            j = 2
            found_word = None

            while j < (foundTestCases+2):
                testCaseID = self.driver.find_element_by_xpath(("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j)).text
                self.driver.find_element_by_xpath(("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j)).click()

                #try to find the word on the first tab
                if(re.search(word, self.driver.find_element_by_xpath("//div[@id='code']").text, re.IGNORECASE)):
                    found_word = True
                #search for the word on the other tabs
                else:
                    i = 1
                    while(True):
                        try:
                            driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div[%s]/span" %(i+1)).click()
                        except:
                            break
                        
                        if(re.search(word, driver.find_element_by_css_selector("div[id='tab%s']" %i).text, re.IGNORECASE)):
                                found_word = True
                                
                        i +=1

                try: self.assertTrue(found_word)
                except AssertionError as e: self.verificationErrors.append(("Source code doesn't have the term '%s' searched but the test case %s still apearing in the results" %(word, testCaseID)))
                
                j += 1
                self.driver.back()

    
    def find_word_in_source_code(self, word):
        i = 1
        numLines = 0

        while(True):
            try:
                re.search(word , self.driver.find_element_by_xpath("//div[@id='code']/table/tbody/tr[2]/td/div/ol/li[%s]" %i).text)
                i += 1
                return True
            except:
                return None



    def count_test_cases_in_page(self, driver):
        i = 2
        numOfTestCases = 0

        while(True):
            try:
                driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %i)
                numOfTestCases += 1
                i += 1
            except:
                return numOfTestCases   

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
