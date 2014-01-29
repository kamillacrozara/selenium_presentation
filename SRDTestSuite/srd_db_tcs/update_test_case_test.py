#!/usr/bin/python
# -*- coding: utf-8 *-*
from selenium import webdriver
import unittest, time, os, re, random
from srd_sd_tcs.common_sd_methods import common_sd_methods
from common_db_test_methods import common_db_test_methods

class UpdateTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        #self.base_url = config["BASE_URL"]
        self.base_url = "http://129.6.58.118/i-SRD-4.3"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

        self.user = config["USER"]
        self.password = config["PASSWORD"]

        common_db_test_methods.login_srd(self.driver, self.base_url, self.user, self.password)
        self.insertedTestCasesID = common_db_test_methods.insert_test_cases(self.driver, self.base_url)


    """After the test case update this method goes to each test case and verify if the iformations were updated correctly"""
    def test_update_test_case(self):
        
        self.update_test_cases()

        i = 2
        for id in self.insertedTestCasesID:
            self.driver.get(self.base_url + "/view_testcase.php?tID=%s" %id)
            
            try: self.assertEqual(common_db_test_methods.dropdown_options['flawed'][i], self.driver.find_element_by_id("Flawed").text)
            except AssertionError as e: self.verificationErrors.append("Test case's type was not updated correctly." )

            try: self.assertEqual("Paul", self.driver.find_element_by_id("Author").text)
            except AssertionError as e: self.verificationErrors.append("Test case's author was not updated correctly." )

            #if the associated test cases is used, uncomend this code
            #try: self.assertEqual("168304", self.driver.find_element_by_id("Associatedtestcase").text)
            #except AssertionError as e: self.verificationErrors.append("Test case's associated test case was not updated correctly." )

            try: self.assertEqual(common_db_test_methods.dropdown_options['languages'][i], self.driver.find_element_by_id("Language").text)
            except AssertionError as e: self.verificationErrors.append("Test case's language was not updated correctly." )

            try: self.assertEqual("Updating Selenium automated tests", self.driver.find_element_by_id("Inputstring").text)
            except AssertionError as e: self.verificationErrors.append("Test case's input string was not updated correctly." )

            try: self.assertEqual("Updating Selenium automated tests", self.driver.find_element_by_id("Expectedoutputstring").text)
            except AssertionError as e: self.verificationErrors.append("Test case's expected output was not updated correctly." )

            try: self.assertEqual("Updating Selenium automated tests", self.driver.find_element_by_id("Instruction").text)
            except AssertionError as e: self.verificationErrors.append("Test case's instruction was not updated correctly." )

            try: self.assertEqual("Updating Selenium automated tests", self.driver.find_element_by_id("Description").text)
            except AssertionError as e: self.verificationErrors.append("Test case's description was not updated correctly." )

            try: self.assertEqual(re.search('\d+',common_db_test_methods.dropdown_options.get('type_flaw')[i]).group(0), re.search('\d+', self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/span").text).group(0))
            except AssertionError as e: self.verificationErrors.append("Test case's flaw was not updated correctly." )

            try: self.assertEqual("45", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/span[2]").text)
            except AssertionError as e: self.verificationErrors.append("Test case's line number was not updated correctly." )

            try: self.assertEqual(common_db_test_methods.dropdown_options.get('ccplx')[i], self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/span[3]").text)
            except AssertionError as e: self.verificationErrors.append("Test case's code complexity was not updated correctly." )

            i = i - 1


    """Goes to each test case that was inserted and update the informations. The original data is:
    
        test case 1 :   "Bad", "Python", "Source Code", "----+ CWE-180: Incorrect Order", "memory access" 
        test case 2 :   "Good", "Java", "Binary", "----+ CWE-209: Information Leak Error", "pointer"
        test case 3 :   "Mixed", "C", "Pseudo Code", "--+ CWE-506: Embedded Malicious Code", "memory location"
    """
    def update_test_cases(self):
        i = 2
        for id in self.insertedTestCasesID:
            self.driver.get(self.base_url + "/view_testcase.php?tID=%s" %id)

            self.driver.find_element_by_id("Flawed").click()
            self.driver.find_element_by_css_selector("input[type='text']").clear()
            self.driver.find_element_by_css_selector("input[type='text']").send_keys(common_db_test_methods.dropdown_options['flawed'][i])
            self.driver.find_element_by_css_selector("input[type='submit']").click()

            self.driver.find_element_by_id("Author").click()
            self.driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
            self.driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Paul")
            self.driver.find_element_by_xpath("(//input[@value='Save'])[2]").click()

            #if the associated test cases is used, uncomend this code
            #self.driver.find_element_by_id("Associatedtestcase").click()
            #self.driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
            #self.driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("168304")
            #self.driver.find_element_by_xpath("(//input[@value='Save'])[3]").click()

            self.driver.find_element_by_id("Language").click()
            self.driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
            self.driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(common_db_test_methods.dropdown_options['languages'][i])
            self.driver.find_element_by_xpath("(//input[@value='Save'])[4]").click()

            self.driver.find_element_by_id("Inputstring").click()
            self.driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
            self.driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("Updating Selenium automated tests")
            self.driver.find_element_by_xpath("(//input[@value='Save'])[5]").click()
            
            self.driver.find_element_by_id("Expectedoutputstring").click()
            self.driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
            self.driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("Updating Selenium automated tests")
            self.driver.find_element_by_xpath("(//input[@value='Save'])[6]").click()
            
            self.driver.find_element_by_id("Instruction").click()
            self.driver.find_element_by_xpath("(//input[@type='text'])[7]").clear()
            self.driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys("Updating Selenium automated tests")
            self.driver.find_element_by_xpath("(//input[@value='Save'])[7]").click()
            
            self.driver.find_element_by_id("Description").click()
            self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[13]/td[2]/form/textarea").clear()
            self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[13]/td[2]/form/textarea").send_keys("Updating Selenium automated tests")
            self.driver.find_element_by_xpath("(//input[@value='Save'])[8]").click()
            
            self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/span").click()
            el = self.driver.find_element_by_xpath("//div[@id='uniqFlawName']/span/form/select")
            common_sd_methods.select_option_dropdow(el, common_db_test_methods.dropdown_options.get('type_flaw')[i])
            self.driver.find_element_by_xpath("//img[@alt='Send']").click()

            self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/span[2]").click()
            self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/form/input").clear()
            self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/form/input").send_keys("45")
            self.driver.find_element_by_xpath("(//input[@value='Save'])[9]").click()

            self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/span[3]").click()
            el = self.driver.find_element_by_xpath("//div[@id='uniqCCplxName']/span/form/select")
            #is necessary to insert a space at the beginning of the string for this dropdown menu
            common_sd_methods.select_option_dropdow(el, (common_db_test_methods.dropdown_options.get('ccplx')[i]))
            self.driver.find_element_by_xpath("//div[@id='uniqCCplxName']/span/form/a[2]/img").click()

            i = i - 1


    def tearDown(self):
        for testCase in self.insertedTestCasesID:
            self.driver.get(self.base_url + "/remove.php?tcid=%s" %testCase)

        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()