#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: download_each_tc_test.py
Author: Kamilla H. Crozara
Description:    
    This class go to each test case in the SRD and check if 
    the download link is working properly.
"""
from selenium import webdriver
import unittest
import requests


class DownloadEachTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None


    """This method goes to each Test Case in the SRD 
       and verifies the link "Download this Test Case."""
    def test_download_each_tc(self):
        i = 0
        driver = self.driver
        #for each page in SRD
        while (i < 88720):
            j = 2
            #get the page using the url with the first i test cases
            driver.get(self.base_url + "/view.php?count=20&first=%s&sort=asc" %i)
            #try to go in each tc and download it
            while (j < 22):
                #take the id of each test case
                try:
                    tcID = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j).text
                except Exception, e:
                    tcID = 0

                if(tcID):
                    #and verify if it can be downloaded as expected
                    resp = requests.head(self.base_url + "/view.php?reference=%s&action=zip-selected" %tcID)
                    try: 
                        self.assertEqual(resp.status_code, 200)
                    except AssertionError as e: self.verificationErrors.append("Could not download test case %s" %tcID)
                j += 1 
            i+=20
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()