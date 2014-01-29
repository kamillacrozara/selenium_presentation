#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: test_suites_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of the Test Suites page
"""


from selenium import webdriver
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCTestSuites(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None
    
    def test_t_c_test_suites(self):
        self.driver.get(self.base_url + "/testsuite.php")
        time.sleep(2)

        try: self.assertEqual("SAMATE Reference Dataset", self.driver.title)
        except AssertionError as e: self.verificationErrors.append(" Wrong title on page %s" %(self.base_url + "/around.php"))

       
        common_ui_tests.testSRDBanner(self, self.driver, self.verificationErrors)
        common_ui_tests.testSRDMenu(self, self.driver, self.verificationErrors)
        common_ui_tests.testFooter(self, self.driver, self.verificationErrors)

        self.assertEqual("Test Suites", self.driver.find_element_by_xpath("//div[@id='content']/h1").text)
        self.assertEqual("Stand-alone Suites", self.driver.find_element_by_xpath("//div[@id='content']/h2").text)
        self.assertEqual("SRD Suites", self.driver.find_element_by_xpath("//div[@id='content']/h2[2]").text)
        self.assertEqual("Archives", self.driver.find_element_by_xpath("//div[@id='content']/h2[3]").text)

        try: self.assertEqual("Link", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Publication Date", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[2]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Title", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[3]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Version", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[4]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Description", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[5]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Contributor", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[6]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("# of Cases", self.driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[7]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Test Suite ID", self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Creation Date", self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Title", self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[3]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Description", self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[4]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Contributor", self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[5]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("# of Cases", self.driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[6]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Link", self.driver.find_element_by_xpath("//div[@id='content']/table[2]/tbody/tr/td").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Publication Date", self.driver.find_element_by_xpath("//div[@id='content']/table[2]/tbody/tr/td[2]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Title", self.driver.find_element_by_xpath("//div[@id='content']/table[2]/tbody/tr/td[3]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Version", self.driver.find_element_by_xpath("//div[@id='content']/table[2]/tbody/tr/td[4]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Description", self.driver.find_element_by_xpath("//div[@id='content']/table[2]/tbody/tr/td[5]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("Contributor", self.driver.find_element_by_xpath("//div[@id='content']/table[2]/tbody/tr/td[6]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
        try: self.assertEqual("# of Cases", self.driver.find_element_by_xpath("//div[@id='content']/table[2]/tbody/tr/td[7]").text)
        except AssertionError as e: self.verificationErrors.append("Field '' not found on page %s" %(self.base_url + "/testsuite.php"))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
