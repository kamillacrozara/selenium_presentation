#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_filename_sourcecodesearchtab_test.py
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

class SrdSdFileNameSourceCodeSearchtabTc(unittest.TestCase):
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
    def test_srd_sd_filename_sourcecodesearchtab(self):
        i = 0
        while (i < 88720):
            self.driver.get(self.base_url + "/view.php?count=20&first=%s&sort=asc" %i)
            self.grab_files_names(common_sd_methods.count_test_cases_in_page(self.driver))
            i+=20
        
        for name in self.fileNames:
            self.driver.get(self.base_url + "/search.php?code")
            self.driver.find_element_by_xpath("//input[@id='fileName']").send_keys(name)
            self.driver.find_element_by_xpath("//input[@name='Submit']").click()
            #must have only one test case with the same ID and the same file
            foundTestCases = common_sd_methods.count_test_cases_in_page(self.driver)
            if foundTestCases > 1:
                j = 2
                tcID = []
                while j < foundTestCases:
                    tcID.append(self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j).text)
                    j +=1
                try: self.assertFalse(len(tcID)!=len(set(tcID)))
                except AssertionError as e: self.verificationErrors.append(("Duplicated test cases in the search by file name %s" %name))

            self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[2]/a").click()

            #the test case file name must be the same as the file name searched
            try: self.assertEqual((self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td[2]/ul/li/a").text),  name)
            except AssertionError as e: self.verificationErrors.append(("The file name %s is not the same in the test case page" %name))

    def grab_files_names(self, numberOfTestCases):
        i = 2
        while i < numberOfTestCases:
            self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %i).click()
            time.sleep(2)
            self.fileNames.append(self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td[2]/ul/li/a").text)                    
            i += 1
            self.driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
