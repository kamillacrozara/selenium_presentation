#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_code_complexity_extendedsearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searchs using non-ascii 
    strings in fields of the Extended Search tab
"""
from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

class SrdSdCodeComplexityExtendedSearchTabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_srd_sd_code_complexity_extendedsearchtab_tc(self):
        ccplx = ["address alias level", "array address complexity", "array address complexity", 
                 "array length/limit complexity", "asynchronous", "bound violation",
                 "buffer address type", "container", "data type", "index alias level",
                 "local control flow", "loop complexity", "loop structure", "memory access", 
                 "memory location", "None/Other", "overflow magnitude", "overflow type", "pointer" 
                ]

        for i in range(len(ccplx)):
            self.driver.get(self.base_url + "/search.php?extended&tree")      
            el = self.driver.find_element_by_xpath("//select[@id='complex_sel']")
            common_sd_methods.select_option_dropdow(el, ccplx[i])  
            self.driver.find_element_by_xpath("//input[@name='Submit']").click()
            common_sd_methods.assert_title(self, self.driver, self.verificationErrors)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()