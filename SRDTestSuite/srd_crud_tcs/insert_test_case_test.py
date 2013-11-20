#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: insert_test_case_test.py
Author: Kamilla H. Crozara
Description:    
    This test verifies if is possible insert test cases correctly. 
"""
from selenium import webdriver
import unittest, time, os
#from srd_sd_tcs.common_sd_methods import common_sd_methods

"""This class inserts test cases using the options in the dict dropdown_options"""
class InsertTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        #config = {}
        #execfile("srd_test_suite.conf", config)
        #self.base_url = config["BASE_URL"]
        self.base_url = "http://129.6.58.118/i-SRD-4.3"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

    def test_submit_test_case(self):
    	driver = self.driver

        dropdown_options =  {'languages' : ["Python", "Java", "C"], 
                            'flawed' : ["Bad", "Good", "Mixed"],
                            'artifact' : ["Source Code", "Binary", "Pseudo Code"],
                            'type_flaw' : ["----+ CWE-180: Incorrect Order", "----+ CWE-209: Information Leak Error", "----+ CWE-209: Information Leak Error"],
                            'ccplx' : ["memory access", "pointer", "memory location"]
                            }
        self.login_srd()
        
        i = 0
        #3 is the size of the dropdown_options lists
        while i < 3:
            #inserting test cases
            driver.get(self.base_url + "/submit.php")
            el = driver.find_element_by_xpath("//select[@name='flawed[]']")
            self.select_option_dropdow(el, dropdown_options.get('flawed')[i])

            el = driver.find_element_by_xpath("//select[@name='languages[]']")
            self.select_option_dropdow(el, dropdown_options.get('languages')[i])

            el = driver.find_element_by_xpath("//select[@name='typesofartefacts[]']")
            self.select_option_dropdow(el, dropdown_options.get('artifact')[i])

            driver.find_element_by_xpath("//input[@name='input']").clear()
            driver.find_element_by_xpath("//input[@name='input']").send_keys("Selenium automated tests")
            driver.find_element_by_xpath("//input[@name='output']").clear()
            driver.find_element_by_xpath("//input[@name='output']").send_keys("Selenium automated tests")
            driver.find_element_by_xpath("//textarea[@name='description']").clear()
            driver.find_element_by_xpath("//textarea[@name='description']").send_keys("Selenium automated tests")

            driver.find_element_by_xpath("//input[@name='file_1']").send_keys(os.getcwd() + "/example_files/numfiles_samevalue_light_test.py")

            el = driver.find_element_by_xpath("//select[@name='typesofflaws_1[]']")
            self.select_option_dropdow(el, dropdown_options.get('type_flaw')[i])

            el = driver.find_element_by_xpath("//select[@name='ccplx_1[]']")
            self.select_option_dropdow(el, dropdown_options.get('ccplx')[i])

            driver.find_element_by_xpath("//input[@name='Submit']").click()
            time.sleep(3)

            #searching test cases
            driver.get(self.base_url + "/search.php?extended&tree")

            driver.find_element_by_xpath("//input[@name='description']").clear()
            driver.find_element_by_xpath("//input[@name='description']").send_keys("Selenium")

            el = driver.find_element_by_xpath("//select[@name='flawed[]']")
            self.select_option_dropdow(el, dropdown_options.get('flawed')[i])

            el = driver.find_element_by_xpath("//select[@name='languages[]']")
            self.select_option_dropdow(el, dropdown_options.get('languages')[i])

            el = driver.find_element_by_xpath("//select[@name='typesofartifacts[]']")
            self.select_option_dropdow(el, dropdown_options.get('artifact')[i])

            el = driver.find_element_by_xpath("//select[@id='flaw_sel']")
            self.select_option_dropdow(el, dropdown_options.get('type_flaw')[i])

            el = driver.find_element_by_xpath("//select[@id='complex_sel']")
            self.select_option_dropdow(el, dropdown_options.get('ccplx')[i])

            driver.find_element_by_xpath("//input[@name='Submit']").click()
            time.sleep(3)

            try: self.assertEqual(dropdown_options.get('languages')[i], driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[4]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(dropdown_options.get('artifact')[i], driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[5]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))
            try: self.assertEqual(dropdown_options.get('type_flaw')[i], driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[2]/td[8]").text)
            except AssertionError as e: self.verificationErrors.append(str(e))

            i += 1 

    """This method selects the option opt_text in the dropdown element"""
    def select_option_dropdow(self, element, opt_text):
        for option in element.find_elements_by_tag_name('option'):
            if option.text == opt_text:
                option.click() 

    def login_srd(self):
    	self.driver.get(self.base_url + "/login.php")
        self.driver.find_element_by_id("login").send_keys("kamilla")
        self.driver.find_element_by_id("pass").send_keys("123456")
        self.driver.find_element_by_name("submit").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

