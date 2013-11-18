#!/usr/bin/python
# -*- coding: utf-8 *-*

##@package srd_checklinks_tcs
# Package with tests of all download links in SRD. 

##@file download_each_tc_test.py
# @brief Test Cases to verify all the download links in the SRD
# @ingroup suite_srd_ckecklinks
from selenium import webdriver
import unittest
import requests

##@brief This class executes checks all the download links in SRD
class DownloadEachTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True


    ##@brief This method goes to each Test Case in the SRD and verifies the link "Download this Test Case #".
    def test_download_each_tc(self):
        i = 0
        driver = self.driver
        #for each page in SRD
        while (i < 88720):
            j = 2
            #self.open_page(i)
            driver.get(self.base_url + "/view.php?count=20&first=%s&sort=asc" %i)
            #try to go in each tc and download it
            while (j < 22):
                try:
                    tcID = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j).text
                except Exception, e:
                    tcID = 0

                if(tcID):
                    #the comma in the end of the string is just a little
                    #trick to have the "ok" message on the same line. It works!
                    #print ("tcID = %s..." %tcID),
                    resp = requests.head(self.base_url + "/view.php?reference=%s&action=zip-selected" %tcID)
                    try: 
                        self.assertEqual(resp.status_code, 200)
                        #print "ok status code = " + str(resp.status_code)
                    except AssertionError as e: self.verificationErrors.append(str(e))
                j += 1 
            i+=20
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()