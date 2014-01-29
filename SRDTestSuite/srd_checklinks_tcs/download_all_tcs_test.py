#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: download_all_tcs_test.py
Author: Kamilla H. Crozara
Description:    
    This test go to each page in the SRD and check if 
    the download link is working properly. Also verify
    if the direct download link of all test cases in SRD
    is working
"""
from selenium import webdriver
import unittest
import requests

class DownloadAllTcs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]

        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

    """This method verifies the download links of all test cases in a page 
    For each page of test cases (using the default visualization with 20 test cases per page) 
    verifies the link "Download all test cases on the page"""
    def test_download_all_tcs_on_page(self):
        i = 20
        j = 1
        while (i < 88720):
            #take the response of the request to download all the test cases on a given page
            resp = requests.head(self.base_url + "/view.php?count=20&action=zip-page&first=%s&sort=asc" %i)
            try: 
                self.assertEqual(resp.status_code, 200)
            except AssertionError as e: self.verificationErrors.append("Could not download all the test cases on page %s" %i)
            i += 20
            j += 1
            
    """This method verifies the direct download link of all test cases in SRD"""
    def test_download_all_tcs_on_srd(self):
        resp = requests.head(self.base_url + "/archive/current.zip")
        try: self.assertEqual(resp.status_code, 200)
        except AssertionError as e: self.verificationErrors.append("Link to download all the test cases in SRD does not work.")
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()