#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: download_test_suites_test.py
Author: Kamilla H. Crozara
Description:    
    This test verifies the download links of the test suites. 
"""
from selenium import webdriver
import unittest
import requests
from srd_sd_tcs.common_sd_methods import common_sd_methods

"""This class verifies the download links of all 
   test suites in  Test Suite (/testsuite.php) page"""
class DownloadTestSuites(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_download_standalone_test_suites(self):
        self.verify_link_standalone_suite("/testsuites/stonesoup/stonesoup-c-mc.zip")

        self.verify_link_standalone_suite("/testsuites/stonesoup/stonesoup-c-np.zip")

        self.verify_link_standalone_suite("/testsuites/stonesoup/stonesoup-java-inj.zip")

        self.verify_link_standalone_suite("/testsuites/stonesoup/stonesoup-java-nh.zip")

        self.verify_link_standalone_suite("/testsuites/stonesoup/stonesoup-java-td.zip")
    

    def test_archives_test_suites(self):
        self.verify_link_standalone_suite("/testsuites/juliet/Juliet_Test_Suite_v1.2_for_C_Cpp.zip")

        self.verify_link_standalone_suite("/testsuites/juliet/Juliet_Test_Suite_v1.2_for_Java.zip")

        self.verify_link_standalone_suite("/testsuites/juliet/Juliet_Test_Suite_v1.1.1_for_Java.zip")

        self.verify_link_standalone_suite("/testsuites/juliet/Juliet_Test_Suite_v1.1_for_C_Cpp.zip")

        self.verify_link_standalone_suite("/testsuites/juliet/Juliet-2010-12.c.cpp.zip")

        self.verify_link_standalone_suite("/testsuites/juliet/Juliet-2010-12.java.zip")


    def test_download_srd_suites(self):
        driver = self.driver
        numOfTestCases = self.count_srd_suites(driver)
        i = 0

        while(i < numOfTestCases):
            driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%i]/td/a" %i).click()
            common_sd_methods.assert_title(self, driver, self.verificationErrors)


    def verify_link_standalone_suite(self, file_url):
        resp = requests.head(self.base_url + file_url)
        try:
            self.assertEqual(resp.status_code, 200)
        except AssertionError as e: self.verificationErrors.append(str(e))


    def count_srd_suites(self, driver):
        i = 2
        numOfTestCases = 0

        while(True):
            try:
                driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td/a" %i)

                numOfTestCases += 1
                i += 1
            except:
                return numOfTestCases

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()