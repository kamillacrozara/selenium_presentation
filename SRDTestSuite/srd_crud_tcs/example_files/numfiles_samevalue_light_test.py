#!/usr/bin/python
# -*- coding: utf-8 *-*
from selenium import webdriver
import unittest, time, re
from srd_sd_tcs.common_sd_methods import common_sd_methods
##@package srd_light_tcs
# Package with automated Search/Download tab tests using 
# Selenium Webdriver

##@file numfiles_samevalue_light_test.py
# @brief Test Cases searching different values in the min and max number 
# of files fields of the Extended Search tab
# @ingroup suite_light_tcs
##@brief This class executes tests related to the Number of Files field on Source Code Search tab
class  NumFilesSameValueLightTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True

        self.maxDiff = None

    ##@brief This method verifies the results of searchers for the same values to min and max field            
    def test_srd_sd_numfiles_light_tc_same_values(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?code")
        #11 is the max number of files in a test case
        i = 0
        while True: 
            j = 0
            testCase = 2
            #send the same value for max and min
            driver.find_element_by_xpath("//input[@name='minFiles']").send_keys("%s" %i)
            driver.find_element_by_xpath("//input[@name='maxFiles']").send_keys("%s" %i)
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
                        try: self.assertTrue(i==1)
                        except AssertionError as e: self.verificationErrors.append(("Number of files is not the same as %s " %i))
                    else:
                        try: self.assertEqual(i, int(numOfFiles))
                        except AssertionError as e: self.verificationErrors.append(("Number of files is not the same as %s " %i))
                    
                    j += 1
                    testCase += 1
                    driver.back()
                driver.back() 

            if (i == 11):
            	break
            i += 11  

    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main(buffer=True)
