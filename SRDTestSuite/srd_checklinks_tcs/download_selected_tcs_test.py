#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: download_selected_tcs_test.py
Author: Kamilla H. Crozara
Description:    
    This test verifies the download link of selected test cases in a given page. 
"""
from selenium import webdriver
import unittest
import requests


class DownloadSelectedTcs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

    """This method verifies the download link of selected test cases. 
       For each page of test cases (using the default visualization with 
       20 test cases per page) select 10 tests cases and verifies the link 
       'Download the selected Test Cases'."""
    def test_download_selected_tcs(self):
        i = 0
        specialCharacter = "%5B%5D"
        driver = self.driver
        #for each page in SRD
        while (i < 88720):
            download_url = "/view.php?count=20zip"
            j = 2
            driver.get(self.base_url + "/view.php?count=20&first=%s&sort=asc" %i)
            
            #try to download some selected tcs
            while (j < 20):
                try:
                    elementNumber = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j).text
                except Exception, e:
                    elementNumber = 0

                #append the test case ID to the download URL 
                if(elementNumber):
                    download_url = download_url + ("&zipTestCasesList%s=%s" %(specialCharacter, elementNumber))
                j += 2

            #verify if the download URL works properly
            resp = requests.head(self.base_url + download_url)
            try: self.assertEqual(resp.status_code, 200)
            except AssertionError as e: self.verificationErrors.append("Could not download selected test cases on page %s" %i)
            i += 20
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()