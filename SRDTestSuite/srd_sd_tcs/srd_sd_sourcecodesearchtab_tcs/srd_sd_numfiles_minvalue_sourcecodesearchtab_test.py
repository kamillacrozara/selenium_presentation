#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_numfiles_minvalue_sourcecodesearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searches different values in the min number 
    of files field of the Extended Search tab
"""

from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods

class SrdSdNumfilesMinValueSourceCodeSearchtabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        self.maxDiff = None

    """This method verifies the results of searchers for values from 0 to 11 in the min field"""
    def test_srd_sd_numfiles_light_tc_max_value(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?code")
        #11 is the max number of files in a test case
        for i in range(12): 
            j = 0
            testCase = 2
            #send value for min field
            driver.find_element_by_xpath("//input[@name='minFiles']").send_keys("%s" %i)
            driver.find_element_by_xpath("//input[@name='Submit']").click()
            time.sleep(2)
            #count the number of test cases per search
            numOfTestCases = common_sd_methods.count_test_cases_in_page(driver)

            if (numOfTestCases == 0):
                driver.back()
            else:
                while(j < numOfTestCases):
                    driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %testCase).click()
                    time.sleep(2)
                    fileString = driver.find_element_by_xpath("//div[@id='content']/table/tbody/tr[14]/td[2]").text
                    
                    try:
                        numOfFiles = re.search('\d+', re.search('The test case contains \d+ files.', fileString).group(0)).group(0)
                    except:
                        numOfFiles = 1
                    
                    if(numOfFiles == 1):
                        try: self.assertTrue(int(numOfFiles) >= i)
                        except AssertionError as e: 
                            self.verificationErrors.append(("Number of files is not >= then %s " %i) + str(e))
                    else:
                        try: self.assertTrue(int(numOfFiles) >= i)
                        except AssertionError as e: 
                            self.verificationErrors.append(("Number of files is not >= then %s " %i) +str(e))
                    j += 1
                    testCase += 1
                    driver.back()
                driver.back()
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
