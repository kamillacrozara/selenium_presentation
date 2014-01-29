#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_query_date_extendedsearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searches by date on Extended Search tab
"""
from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

class SrdSdQuerydateExtendedSearchTabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

    """This method verifies the results of the searches 
       by date on the "Extended Search" tab"""
    def test_srd_sd_query_date_extendedsearchtab_tc(self):
        driver = self.driver

        #on date tests
        driver.get(self.base_url + "/search.php?extended")
        driver.find_element_by_xpath("//input[@name='date']").send_keys("10/21/2005")
        driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[3]/input").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_query_date_on_date(driver, numOfTestCases, "2005-10-21")

        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_query_date_on_date(driver, numOfTestCases, "2005-10-21")

        driver.get(self.base_url + "/search.php?extended")
        driver.find_element_by_xpath("//input[@name='date']").send_keys("05/22/2013")
        driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[3]/input").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_query_date_on_date(driver, numOfTestCases, "2013-05-22")

        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_query_date_on_date(driver, numOfTestCases, "2013-05-22")

        #before date tests
        driver.get(self.base_url + "/search.php?extended")
        driver.find_element_by_xpath("//input[@name='date']").send_keys("10/21/2005")
        driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[2]/input").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_query_date_before_date(driver, numOfTestCases, "2005-10-21")

        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_query_date_before_date(driver, numOfTestCases, "2005-10-21")

        driver.get(self.base_url + "/search.php?extended")
        driver.find_element_by_xpath("//input[@name='date']").send_keys("05/22/2013")
        driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[2]/input").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_query_date_before_date(driver, numOfTestCases, "2013-05-22")

        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_query_date_before_date(driver, numOfTestCases, "2013-05-22")

        #after date tests
        driver.get(self.base_url + "/search.php?extended")
        driver.find_element_by_xpath("//input[@name='date']").send_keys("10/21/2005")
        driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[4]/input").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_query_date_after_date(driver, numOfTestCases, "2005-10-21")

        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_query_date_after_date(driver, numOfTestCases, "2005-10-21")

        driver.get(self.base_url + "/search.php?extended")
        driver.find_element_by_xpath("//input[@name='date']").send_keys("05/22/2013")
        driver.find_element_by_xpath("//div[@id='cleaner_1']/span/label[4]/input").click()
        driver.find_element_by_xpath("//input[@name='Submit']").click()
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_query_date_after_date(driver, numOfTestCases, "2013-05-22")

        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_query_date_after_date(driver, numOfTestCases, "2013-05-22")
        

    def verify_query_date_on_date(self, driver, numOfTestCases, date):
        i = 2
        while(i < numOfTestCases):
            testCaseID = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]" %i).text
            try: self.assertEqual(date, driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[3]" %i).text)
            except AssertionError as e: self.verificationErrors.append("Date is not the same as %s in test case %s" %(date, testCaseID))
            i +=1

    def verify_query_date_before_date(self, driver, numOfTestCases, date):
        i = 2
        while(i < numOfTestCases):
            testCaseID = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]" %i).text
            try: self.assertTrue(date >= driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[3]" %i).text)
            except AssertionError as e: self.verificationErrors.append("Date is not before %s in test case %s" %(date, testCaseID))
            i +=1

    def verify_query_date_after_date(self, driver, numOfTestCases, date):
        i = 2
        while(i < numOfTestCases):
            testCaseID = driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]" %i).text
            try: self.assertTrue(date <= driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[3]" %i).text)
            except AssertionError as e: self.verificationErrors.append("Date is not after %s in test case %s" %(date, testCaseID))
            i +=1

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()