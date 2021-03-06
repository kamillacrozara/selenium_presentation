#!/usr/bin/python
# -*- coding: utf-8 *-*

##@package srd_light_tcs
# Package with automated Search/Download tab tests using 
# Selenium Webdriver

##@file search_download_light_test.py
# @brief Test Cases inserting big strings in fields of the Extended Search tab
# @ingroup suite_light_tcs
from selenium import webdriver
import unittest, time, re

##@brief This class executes tests inserting special charactes in the fields on the Search/Download tab
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

    ##@brief This method verifies the results of the special characters searches
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
