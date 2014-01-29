#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: srd_home_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Home page
"""

from selenium import webdriver
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCSRDHome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
    
    def test_t_c_s_r_d_home(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        common_ui_tests.testSRDBanner(self, self.driver, self.verificationErrors)
        common_ui_tests.testSRDMenu(self, self.driver, self.verificationErrors)
        common_ui_tests.testFooter(self, self.driver, self.verificationErrors)
        time.sleep(2)
        try: self.assertEqual("SAMATE Reference Dataset", driver.title)
        except AssertionError as e: self.verificationErrors.append(" Wrong title on page %s" %(self.base_url + "/index.php")) 
       
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
