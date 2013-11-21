#!/usr/bin/python
# -*- coding: utf-8 *-*
from selenium import webdriver
import unittest

class SrdSdNonasciiExtendedsearchtabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://samate.nist.gov/SRD"
        self.verificationErrors = []
    
    def test_srd_sd_nonascii_extendedsearchtab_tc(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?extended")
        try: self.assertEqual("SAMATE Reference Dataset", driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        driver.find_element_by_xpath("//input[@name='reference']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        driver.back()
        
        driver.find_element_by_xpath("//input[@name='description']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        driver.back()
        
        driver.find_element_by_xpath("//input[@name='author']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        driver.back()
        
        driver.find_element_by_xpath("//input[@name='contributor']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
        driver.back()
    
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
