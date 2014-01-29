#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_nonascii_extendedsearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searches 
    of non-ascii characters in fields of the Extended Search tab
"""
from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

class SrdSdNonasciiExtendedsearchtabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

    """This method verifies the results of the non-ascii characters searches"""
    def test_srd_sd_nonascii_extendedsearchtab_tc(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?extended")
        time.sleep(2)
        self.assertEqual("SAMATE Reference Dataset", driver.title)
        
        driver.find_element_by_xpath("//input[@name='reference']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        driver.back()
        
        driver.find_element_by_xpath("//input[@name='description']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        driver.back()
        
        driver.find_element_by_xpath("//input[@name='author']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        driver.back()
        
        driver.find_element_by_xpath("//input[@name='contributor']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        common_sd_methods.assert_title(self, driver, self.verificationErrors)
        driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
