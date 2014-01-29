#!/usr/bin/python
# -*- coding: utf-8 *-*

"""
File: common_sd_methods.py
Author: Kamilla H. Crozara
Description:    
    Common methods related to the Search/Download tab tests.
"""
def assert_title(self, driver, verificationErrors):
    try: self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
    except AssertionError as e: verificationErrors.append(str(e))

def assert_search_result(self, driver, verificationErrors):
	try: self.assertEqual("View/Download\nDownloads:     \n\nThere is no such test case in the database! Back to the previous page", driver.find_element_by_xpath("//div[@id='content']").text)
	except AssertionError as e: verificationErrors.append(str(e))
	try: self.assertEqual("Back to the previous page", driver.find_element_by_xpath("//a[contains(text(),'Back to the previous page')]").text)
	except AssertionError as e: verificationErrors.append(str(e))

"""This method counts the number of test cases in a given page"""
def count_test_cases_in_page(driver):
    i = 2
    numOfTestCases = 0

    while(True):
        try:
            driver.find_element_by_xpath("//div[@id='content']/form/table/tbody/tr[%s]/td[2]/a" %i)
            numOfTestCases += 1
            i += 1
        except:
            return numOfTestCases


def go_last_page(driver):
        try:
            driver.find_element_by_xpath("//a[contains(text(),'Last')]").click()
            time.sleep(5)
            return True
        except:
            return None


"""This method selects the option opt_text in the dropdown element"""
def select_option_dropdow(element, opt_text):
    for option in element.find_elements_by_tag_name('option'):
        if option.text == opt_text:
            option.click()

if __name__ == '__main__':
	main()
