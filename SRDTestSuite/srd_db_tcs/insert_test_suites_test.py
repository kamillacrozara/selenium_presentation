#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: insert_test_suites_test.py
Author: Kamilla H. Crozara
Description:    
    This test verifies if is possible insert test suites correctly. 
"""


from selenium import webdriver
import unittest, time, os, re, random
from srd_sd_tcs.common_sd_methods import common_sd_methods
from common_db_test_methods import common_db_test_methods

"""This class inserts test cases using the options in the dict dropdown_options"""
class InsertTestSuites(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        config = {}
        execfile("srd_test_suite.conf", config)
        #self.base_url = config["BASE_URL"]
        self.base_url = "http://129.6.58.118/i-SRD-4.3"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

        self.user = config["USER"]
        self.password = config["PASSWORD"]

        #login
        common_db_test_methods.login_srd(self.driver, self.base_url, self.user, self.password)


    def test_insert_test_suite(self):
    	self.driver.get(self.base_url + "/testsuite.php")

        #since it is the first login, it is not supposed have test suites
        try: self.assertEqual("You don't have any Test Suite.", self.driver.find_element_by_xpath("//div[@id='content']/div[2]/span").text)
        except AssertionError as e: self.verificationErrors.append("Found test suites associated to the test login. It is not supposed to exist tests suites on the first login.")
        
        #create a test suite
        self.driver.find_element_by_css_selector("img[alt=\"Create a new Test Suite\"]").click()
        try:
            self.assertEqual("Results: 1 Test Suites.", self.driver.find_element_by_xpath("//div[@id='content']/div[2]/span").text)
            testSuiteID = self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[2]/a").text
            testSuiteTitle = self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[4]").text
        except AssertionError as e: self.verificationErrors.append("Test suite could not be created or the number of test suites is wrong.")


        #add test cases
        self.driver.get(self.base_url + "/view.php")


        try:
            insertedTestCaseID = self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[2]/a")
            self.driver.find_element_by_xpath("//img[@alt='Add to Test Suite']").click()
            print "TITLE " + testSuiteTitle
            print ("(//a[contains(text(),'%s')])[2]" %testSuiteTitle)
            self.driver.find_element_by_xpath("(//a[contains(text(),'%s')])[2]" %testSuiteTitle).click()
        except AssertionError as e: self.verificationErrors.append("Could not insert test cases in the test suite.")


        #verify if the test cases have been added correctly
        try:
            self.driver.get(self.base_url + "/view.php?tsID=%s" %testSuiteID)
            self.assertEqual(insertedTestCaseID, self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[2]/a").text)
        except AssertionError as e: self.verificationErrors.append("Test case was not inserted correctly in the test suite.")

    
    def tearDown(self):
        self.driver.get(self.base_url + "/testsuite.php")
        self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td/input").click()
        self.driver.find_element_by_xpath("//img[@alt='Delete the Test Suite']").click()
        time.sleep(2)

    	self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
