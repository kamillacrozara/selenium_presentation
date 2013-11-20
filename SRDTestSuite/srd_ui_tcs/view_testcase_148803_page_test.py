#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: more_downloads_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the elements of a specific page in the View/Download tab
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from common_ui_tests import common_ui_tests
import unittest, time, re

class TCViewTestCase148803Page(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
    

    def test_t_c_view_test_case148803_page(self):
        driver = self.driver
        driver.get(self.base_url + "/index.php")
        driver.find_element_by_xpath("//a[contains(text(),'View / Download')]").click()
        driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr/td[2]/a/img").click()
        driver.find_element_by_xpath("//a[contains(@href, 'view_testcase.php?tID=148803')]").click()
        time.sleep(2)
        self.assertEqual("SAMATE Reference Dataset :: TestCase 148803", driver.title)
    

        common_ui_tests.testSRDMenu(self, driver, self.verificationErrors)

        try: self.assertEqual("Downloads: ", driver.find_element_by_xpath("//div[@id='content']/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//img[@alt='Download this Test Case #148803']"))
        try: self.assertEqual("Back to the previous page", driver.find_element_by_xpath("//div[@id='content']/h1/a").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Test Case ID", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Bad / Good / Mixed", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[2]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Author", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[3]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Associated test case", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[4]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Contributor", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[5]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Language", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[6]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Type of test case", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[7]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Input string", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[9]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Expected Output", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[10]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Instructions", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[11]/td/strong/acronym").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Submission date", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[12]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Description", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[13]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Filename", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Flaw", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("148803", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr/td[2]/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//div[@id='content']/table/tbody/tr/td[2]/a/img"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//div[@id='content']/table/tbody/tr[2]/td[2]/a/img"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//div[@id='content']/table/tbody/tr[2]/td[2]/a/img"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(text(),'CWE90_LDAP_Injection__listen_tcp_81_bad.java')]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(text(),'CWE90_LDAP_Injection__listen_tcp_81_base.java')]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(text(),'AbstractTestCaseBase.java')]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(text(),'IO.java')]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(text(),'AbstractTestCase.java')]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(text(),'CWE90_LDAP_Injection__listen_tcp_81a.java')]"))
        self.assertTrue(common_ui_tests.is_element_present(self, By.XPATH, "//a[contains(text(),'CWE90_LDAP_Injection__listen_tcp_81_goodG2B.java')]"))
        driver.find_element_by_css_selector("img[alt=\"(?)\"]").click()
        try: self.assertEqual("+ Root\nCWE-019: Data Handling\n    CWE-118: Improper Access of Indexable Resource (Range Error)\n       CWE-020: Insufficient Input Validation\n          CWE-074: Failure to Sanitize Data into a Different Plane (Injection)\n             CWE-090: LDAP Injection", driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[15]/td[2]/ul/li/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("CWE-090: LDAP Injection", driver.find_element_by_xpath("//div[@id='flaw_0']/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("img[alt=\"(?)\"]").click()
        try: self.assertEqual("Submit a comment", driver.find_element_by_xpath("//a[contains(text(),'Submit a comment')]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div/span").click()
        try: self.assertEqual("Filename: CWE90_LDAP_Injection__listen_tcp_81_bad.java", driver.find_element_by_xpath("//div[@id='tab0']/div/ol/li[2]/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div[2]/span").click()
        try: self.assertEqual("Filename: CWE90_LDAP_Injection__listen_tcp_81_base.java", driver.find_element_by_xpath("//div[@id='tab1']/div/ol/li[2]/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div[3]/span").click()
        try: self.assertEqual("AbstractTestCase classes.", driver.find_element_by_xpath("//div[@id='tab2']/div/ol/li[3]/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div[4]/span").click()
        try: self.assertRegexpMatches(driver.find_element_by_xpath("//div[@id='tab3']/div/ol/li[2]/div/span").text, r"^[\s\S]* @description Helper IO class$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div[5]/span").click()
        try: self.assertEqual("public abstract class AbstractTestCase extends AbstractTestCaseBase", driver.find_element_by_xpath("//div[@id='tab4']/div/ol/li[8]/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div[6]/span").click()
        try: self.assertEqual("Filename: CWE90_LDAP_Injection__listen_tcp_81a.java", driver.find_element_by_xpath("//div[@id='tab5']/div/ol/li[2]/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='mainTabContainer']/div/div[7]/span").click()
        try: self.assertEqual("Filename: CWE90_LDAP_Injection__listen_tcp_81_goodG2B.java", driver.find_element_by_xpath("//div[@id='tab6']/div/ol/li[2]/div/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        common_ui_tests.testFooter(self, driver, self.verificationErrors)
        
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
