#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_weakness_extendedsearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searches by weakness on Extended Search tab
"""
from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

class SrdSdWeaknessExtendedSearchTabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True

    """This method verifies the results of searches by weakness"""
    def test_srd_sd_weakness_extendedsearchtab_tc(self):
        driver = self.driver

        driver.get(self.base_url + "/search.php?extended&tree")
        el = driver.find_element_by_xpath("//select[@id='flaw_sel']")
        common_sd_methods.select_option_dropdow(el, "--+ CWE-843: Access of Resource Using Incompatible Type (Type Confusion)")
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_weakness(driver, numOfTestCases, "CWE-843: Access of Resource Using Incompatible Type (Type Confusion)")
 
        driver.get(self.base_url + "/search.php?extended&tree")
        el = driver.find_element_by_xpath("//select[@id='flaw_sel']")
        common_sd_methods.select_option_dropdow(el, "--+ CWE-835: Loop with Unreachable Exit Condition (Infinite Loop)")
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_weakness(driver, numOfTestCases, "CWE-835: Loop with Unreachable Exit Condition (Infinite Loop)")

        driver.get(self.base_url + "/search.php?extended&tree")
        el = driver.find_element_by_xpath("//select[@id='flaw_sel']")
        common_sd_methods.select_option_dropdow(el, "--+ CWE-506: Embedded Malicious Code")
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_weakness(driver, numOfTestCases, "CWE-506: Embedded Malicious Code")

        driver.get(self.base_url + "/search.php?extended&tree")
        el = driver.find_element_by_xpath("//select[@id='flaw_sel']")
        common_sd_methods.select_option_dropdow(el, "--+ CWE-170: Improper Null Termination")
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_weakness(driver, numOfTestCases, "CWE-170: Improper Null Termination")

        driver.get(self.base_url + "/search.php?extended&tree")
        el = driver.find_element_by_xpath("//select[@id='flaw_sel']")
        common_sd_methods.select_option_dropdow(el, "--+ CWE-336: Same Seed in PRNG")
        numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)
        self.verify_weakness(driver, numOfTestCases, "CWE-336: Same Seed in PRNG")

    def get_page(self, driver, url):
        driver.get(self.base_url + url)
        time.sleep(2)


    def verify_weakness(self, driver, numOfTestCases, weaknessType):
        i = 2
        while(i < numOfTestCases):
            try: self.assertEqual(weaknessType, driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[8]" %i).text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            i +=1

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()