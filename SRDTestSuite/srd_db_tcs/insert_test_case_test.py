#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: insert_test_case_test.py
Author: Kamilla H. Crozara
Description:    
    This test verifies if is possible insert test cases correctly. 
"""
from selenium import webdriver
import unittest, time, os, re, random
from srd_sd_tcs.common_sd_methods import common_sd_methods
from common_db_test_methods import common_db_test_methods

"""This class inserts test cases using the options in the dict dropdown_options"""
class InsertTestCase(unittest.TestCase):
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

        #login
        common_db_test_methods.login_srd(self.driver, self.base_url, self.user, self.password)
        
        #insert test cases
        self.insertedTestCasesID = common_db_test_methods.insert_test_cases(self.driver, self.base_url)

    def test_submit_test_case(self):
       self.search_for_tc()
       self.search_for_inserted_files()


    """Specific search for the insert test case file using the filed 'File contains' on Source Code Search tab"""
    def search_for_inserted_files(self):
        #verify if searching by a line present in the source file previously inserted the result returns the same number as the number of inserterd test cases
        self.driver.get(self.base_url + "/search.php?code")
        self.driver.find_element_by_xpath("//input[@id='fileName']").clear()
        
        #line = open(os.getcwd() + "/srd_db_tcs/example_files/example_file_selenium.py", "r").readlines()[72]
        #This line doesn't work because of some weird issue with the webdriver API
        #self.driver.find_element_by_xpath("//input[@id='function']").send_keys(unicode(line, errors='ignore'))
        
        self.driver.find_element_by_xpath("//input[@id='fileName']").send_keys("selenium")
        self.driver.find_element_by_xpath("//input[@name='Submit']").click()

        numberOfTestCases = common_sd_methods.count_test_cases_in_page(self.driver)
        
        #verify if the source file present in each test case returned as result of the search is the same as the source file previously inserted
        if numberOfTestCases > 0:
            i = 0
            while i < numberOfTestCases:
                self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %(i+2)).click()
                try: self.assertEqual("example_file_selenium.py",self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td[2]/ul/li/a").text)
                except AssertionError as e: self.verificationErrors.append("File is not the same as the inserted previously in the test case %s." %self.driver.find_element_by_xpath("//span[@id='TestCaseID']").text)
                self.driver.back()
                i += 1
        else:
            self.verificationErrors.append("Test case not found when looking for 'selenium' using the 'File Contains' search.")

    """Regular search using the test case ID and the elements in the dropdown_options dictionary"""
    def search_for_tc(self):
        i = 0
        #3 is the size of the dropdown_options lists
        while i < 3:
            self.driver.get(self.base_url + "/search.php?extended&tree")

            #take the test case ID 
            self.driver.find_element_by_xpath("//input[@name='reference']").send_keys("%s" %self.insertedTestCasesID[i])
            
            #insert keywords in the description field
            self.driver.find_element_by_xpath("//input[@name='description']").send_keys("selenium")

            #fill the dropdown menus
            el = self.driver.find_element_by_xpath("//select[@name='flawed[]']")
            common_sd_methods.select_option_dropdow(el, common_db_test_methods.dropdown_options.get('flawed')[i])

            el = self.driver.find_element_by_xpath("//select[@name='languages[]']")
            common_sd_methods.select_option_dropdow(el, common_db_test_methods.dropdown_options.get('languages')[i])

            el = self.driver.find_element_by_xpath("//select[@name='typesofartifacts[]']")
            common_sd_methods.select_option_dropdow(el, common_db_test_methods.dropdown_options.get('artifact')[i])

            el = self.driver.find_element_by_xpath("//select[@id='flaw_sel']")
            common_sd_methods.select_option_dropdow(el, common_db_test_methods.dropdown_options.get('type_flaw')[i])

            el = self.driver.find_element_by_xpath("//select[@id='complex_sel']")
            common_sd_methods.select_option_dropdow(el, common_db_test_methods.dropdown_options.get('ccplx')[i])
            
            self.driver.find_element_by_xpath("//input[@name='Submit']").click()
            time.sleep(3)   

            numberOfTestCases = common_sd_methods.count_test_cases_in_page(self.driver)

            if numberOfTestCases > 0:     
                #verify the search results
                self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[2]/a").click()
                try: self.assertEqual(self.user, self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[3]/td[2]/span").text)
                except AssertionError as e: self.verificationErrors.append("Test case not found or author is not the same when searching for author '%s'" %(self.author))

                try: self.assertEqual(common_db_test_methods.dropdown_options.get('languages')[i], self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[6]/td[2]/span").text)
                except AssertionError as e: self.verificationErrors.append("Test case not found or language is not the same when searching for language '%s'" %(common_db_test_methods.dropdown_options.get('languages')[i]))
                try: self.assertEqual(common_db_test_methods.dropdown_options.get('artifact')[i], self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[7]/td[2]/span").text)
                except AssertionError as e: self.verificationErrors.append("Test case not found or the artifact is not the same when searching for artifact '%s'" %(common_db_test_methods.dropdown_options.get('artifact')[i]))
                try: self.assertEqual(re.search('\d+', common_db_test_methods.dropdown_options.get('type_flaw')[i]).group(0), re.search('\d+', self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/span").text).group(0))
                except AssertionError as e: self.verificationErrors.append("Test case not found or the type flaw is not the same when searching for type flaw '%s'" %(common_db_test_methods.dropdown_options.get('type_flaw')[i]))
            else:
                self.verificationErrors.append("Test case not found when searching for the test cases previously inserted!")

                
            i += 1

    def tearDown(self):
        for testCase in self.insertedTestCasesID:
            self.driver.get(self.base_url + "/remove.php?tcid=%s" %testCase)

        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

