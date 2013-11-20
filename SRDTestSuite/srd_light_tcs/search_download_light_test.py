#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: search_download_light_test.py
Author: Kamilla H. Crozara
Description:    
    This test searches for special characters and non-asccii characters 
    in the fields on Search/Download tab
"""
from selenium import webdriver
import unittest, time, re

"""This class executes tests inserting different types 
   charactes in the fields on the Search/Download tab"""
class SearchDownloadLightTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        
        self.verificationErrors = []
        self.accept_next_alert = True
        
        self.maxDiff = None

    def test_search_download_light(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")

        driver.find_element_by_xpath("//a[contains(text(),'Search / Download')]").click()
        driver.find_element_by_xpath("//input[@name='reference']").send_keys("\"This sentence is wrapped in double quotes.\"")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        self.assert_title(driver)
        driver.back()

        driver.find_element_by_xpath("//input[@name='contributor']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        self.assert_title(driver)
        driver.back()

        driver.find_element_by_xpath("//a[contains(text(),'Extended Search')]").click()
        driver.find_element_by_xpath("//input[@name='reference']").send_keys("\"This sentence is wrapped in double quotes.\"")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        self.assert_title(driver)
        driver.back()

        driver.find_element_by_xpath("//input[@name='contributor']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        self.assert_title(driver)
        driver.back()

        driver.find_element_by_xpath("//a[contains(text(),'Source Code Search')]").click()
        driver.find_element_by_xpath("//input[@id='function']").send_keys("\"This sentence is wrapped in double quotes.\"")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        self.assert_title(driver)
        driver.back()

        driver.find_element_by_xpath("//input[@id='fileName']").send_keys(u"ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå")
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        time.sleep(2)
        self.assert_title(driver)

    def assert_title(self, driver):
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(buffer=True)
