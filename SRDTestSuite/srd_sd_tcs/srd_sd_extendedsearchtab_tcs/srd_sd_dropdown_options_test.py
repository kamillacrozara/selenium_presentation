#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_dropdown_options_test.py
Author: Kamilla H. Crozara
Description:    
    This tests to verifies the searches using all
    the dropdown menus options
"""

from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

"""This class executes tests with the dropdown menus options 
    on the "Extended Search" tab"""
class SrdSdDropDownSearchTabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True

    """Verifies the results of searches using the dropdown menus"""
    def test_srd_sd_dropdown_tc(self):
        driver = self.driver
        
        driver.get(self.base_url + "/search.php?simple")
        el = driver.find_element_by_xpath("//select[@name='flawed[]']")
        common_sd_methods.select_option_dropdow(el, "Bad")

        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_flawed_element(driver, numOfTestCases, "Bad test case")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_flawed_element(driver, numOfTestCases, "Bad test case")

        driver.get(self.base_url + "/search.php?simple")
        el = driver.find_element_by_xpath("//select[@name='flawed[]']")
        common_sd_methods.select_option_dropdow(el, "Good")

        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_flawed_element(driver, numOfTestCases, "Good test case")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_flawed_element(driver, numOfTestCases, "Good test case")

        driver.get(self.base_url + "/search.php?simple")            
        el = driver.find_element_by_xpath("//select[@name='flawed[]']")
        common_sd_methods.select_option_dropdow(el, "Mixed")

        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_flawed_element(driver, numOfTestCases, "Mixed test case")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_flawed_element(driver, numOfTestCases, "Mixed test case")

        driver.get(self.base_url + "/search.php?simple")            
        el = driver.find_element_by_xpath("//select[@name='languages[]']")
        common_sd_methods.select_option_dropdow(el, "C")

        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_language_element(driver, numOfTestCases, "C")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_language_element(driver, numOfTestCases, "C")

        driver.get(self.base_url + "/search.php?simple")            
        el = driver.find_element_by_xpath("//select[@name='languages[]']")
        common_sd_methods.select_option_dropdow(el, "Java")

        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_language_element(driver, numOfTestCases, "Java")
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_language_element(driver, numOfTestCases, "Java")

        driver.get(self.base_url + "/search.php?simple")            
        el = driver.find_element_by_xpath("//select[@name='languages[]']")
        common_sd_methods.select_option_dropdow(el, "C++")

        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_language_element(driver, numOfTestCases, "C++")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_language_element(driver, numOfTestCases, "C++")

        driver.get(self.base_url + "/search.php?simple")            
        el = driver.find_element_by_xpath("//select[@name='languages[]']")
        common_sd_methods.select_option_dropdow(el, "PHP")
        
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_language_element(driver, numOfTestCases, "PHP")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_language_element(driver, numOfTestCases, "PHP")

        driver.get(self.base_url + "/search.php?simple")      
        el = driver.find_element_by_xpath("//select[@name='typesofartifacts[]']")
        common_sd_methods.select_option_dropdow(el, "Source Code")      
        
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_artifact_element(driver, numOfTestCases, "Source Code")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_artifact_element(driver, numOfTestCases, "Source Code")

        driver.get(self.base_url + "/search.php?simple")      
        el = driver.find_element_by_xpath("//select[@name='typesofartifacts[]']")
        common_sd_methods.select_option_dropdow(el, "Mix Of Artifact")   
        
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_artifact_element(driver, numOfTestCases, "Mix Of Artifact")
        
        if common_sd_methods.go_last_page(driver):
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
            self.verify_artifact_element(driver, numOfTestCases, "Mix Of Artifact")

    def go_last_page(self, driver):
        try:
            driver.find_element_by_xpath("//a[contains(text(),'Last')]").click()
            time.sleep(5)
            return True
        except:
            return None
        
    def verify_language_element(self, driver, numOfTestCases, language):
        i = 2
        while(i < numOfTestCases):
            try: self.assertEqual(language, driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%i]/td[4]" %i).text) 
            except AssertionError as e: self.verificationErrors.append(str(e))
            i +=1

    def verify_flawed_element(self, driver, numOfTestCases, testCaseType):
        i = 2
        while(i < numOfTestCases):
            try: self.assertEqual(testCaseType, driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[9]/a/img" %i).get_attribute('alt')) 
            except AssertionError as e: self.verificationErrors.append(str(e))
            i +=1

    def verify_artifact_element(self, driver, numOfTestCases, artifactType):
        i = 2
        while(i < numOfTestCases):
            try: self.assertEqual(artifactType, driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[5]" %i).text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            i +=1
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()