#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: check_links_response_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the links on pages listed on the PAGES list at the config file
"""

from selenium import webdriver
from common_ui_tests import common_ui_tests
import unittest, time, re, requests

class CheckLinksResponse(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.pages = config["PAGES"]
        self.accept_next_alert = True
        self.maxDiff = None
    
    """This method goes to each page in the PAGES list and verify all the links on the given page"""
    def test_links_response(self):
        for page in self.pages:
            self.driver.get(self.base_url + page)

            #get all the elements with "href"
            elements = self.driver.find_elements_by_xpath("//*[@href]")

            for el in elements:
                #to be sure to only check webpages and not e-mail adress or something else
                if re.search("http", el.get_attribute("href")):
                    #verify the response of each link
                    resp = requests.head(el.get_attribute("href"))

                    #add a warning if the response is not 200
                    if resp.status_code is not 200:
                        self.verificationErrors.append("Check the link %s on page %s! It has returned the Status Code %s" %(el.get_attribute("href"), (self.base_url + page), resp.status_code))            

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
