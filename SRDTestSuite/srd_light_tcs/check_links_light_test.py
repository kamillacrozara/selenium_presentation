#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: check_links_light_test.py
Author: Kamilla H. Crozara
Description:    
    This test is a light version to verify the download links in the SRD
"""
from selenium import webdriver
import unittest, requests

"""This test executes light checks is some pages of the SRD"""
class CheckLinksLightTest(unittest.TestCase):
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
       For pages 20, 44370 and 88720 (using the default visualization with 
       20 test cases per page) verifies the link "Download all test cases on the page"."""
    def test_download_all_tcs_on_page(self):
        i = 20
        j = 1
        while True:
            url = self.base_url + ("/view.php?count=20&action=zip-page&first=%s&sort=asc" %i)
      
            resp = requests.head(url)
            try: 
                self.assertEqual(resp.status_code, 200)
            except AssertionError as e: self.verificationErrors.append("The link to download all test cases does not work on page %s" %i)
            if (i == 88720): 
            	break
            i += 44350
            j += 1

    """This method goes to each Test Case on pages 20, 
       44370 and 88720 in the SRD and verifies the link 
       "Download this Test Case."""
    def test_download_each_tc(self):
        i = 0
        driver = self.driver
        #for each page in SRD
        while True:
            j = 2
            driver.get(self.base_url + "/view.php?count=20&first=%s&sort=asc" %i)
            #try to go in each tc page and download it
            while (j < 22):
                try:
                    tcID = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j).text
                except Exception, e:
                    tcID = 0

                if(tcID):
                    resp = requests.head(self.base_url + "/view.php?reference=%s&action=zip-selected" %tcID)
                    try: 
                        self.assertEqual(resp.status_code, 200)
                    except AssertionError as e: self.verificationErrors.append("Could not download the test case %s on page %i" %(tcID, i))
                j += 1 
            if (i == 88720): 
                break
            i+=44360

    """This method verifies the download link of selected test cases. 
       For pages 20, 44370 and 88720 of test cases (using the default 
       visualization with 20 test cases per page) selects 10 tests cases 
       and verify the link "Download the selected Test Cases"."""
    def test_download_selected_tcs(self):
        i = 0
        specialCharacter = "%5B%5D"
        driver = self.driver
        while True:
            download_url = "/view.php?count=20zip"
            j = 2
            driver.get(self.base_url + "/view.php?count=20&first=%s&sort=asc" %i)
            while (j < 20):
                try:
                    elementNumber = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %j).text
                except Exception, e:
                    elementNumber = 0

                if(elementNumber):
                    download_url = download_url + ("&zipTestCasesList%s=%s" %(specialCharacter, elementNumber))
                j += 2

            resp = requests.head(self.base_url + download_url)
            try: 
                self.assertEqual(resp.status_code, 200)
            except AssertionError as e: self.verificationErrors.append("Could not download the selected test cases on page %s" %i)
            if (i == 88720): 
                break
            i+=44360

    """This method verifies the direct download link of all test cases in SRD"""
    def test_download_all_tcs_on_srd(self):
        resp = requests.head(self.base_url + "/archive/current.zip")
        try: self.assertEqual(resp.status_code, 200)
        except AssertionError as e: self.verificationErrors.append("Error trying to download all the tcs on SRD using the direct link. " + str(e))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    unittest.main()