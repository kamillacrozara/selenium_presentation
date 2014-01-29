#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: common_ui_tests.py
Author: Kamilla H. Crozara
Description:    
    Module with common tests that are used in most test cases 
"""
from selenium.webdriver.common.by import By

def testSRDBanner(self, driver, verificationErrors):
	try: self.assertTrue(is_element_present(self, By.CSS_SELECTOR, "area[alt=\"SAMATE Logo\"]"))
	except AssertionError as e: verificationErrors.append("Missing SAMATE logo on page %s" %self.base_url)
	try: self.assertTrue(is_element_present(self, By.CSS_SELECTOR, "area[alt=\"NIST Logo\"]"))
	except AssertionError as e: verificationErrors.append("Missing NIST logo on page %s" %self.base_url) 
	try: self.assertTrue(is_element_present(self, By.XPATH, "//img[@alt='Department of Homeland Security']"))
	except AssertionError as e: verificationErrors.append("Missing DHS logo on page %s" %self.base_url)

"""method with SRD Menu tests"""
def testSRDMenu(self, driver, verificationErrors):
	try: self.assertEqual("SRD Home", driver.find_element_by_link_text("SRD Home").text)
	except AssertionError as e: verificationErrors.append(str(e))
	try: self.assertEqual("View / Download", driver.find_element_by_link_text("View / Download").text)
	except AssertionError as e: verificationErrors.append(str(e))
	try: self.assertEqual("Search / Download", driver.find_element_by_link_text("Search / Download").text)
	except AssertionError as e: verificationErrors.append(str(e))
	try: self.assertEqual("More Downloads", driver.find_element_by_link_text("More Downloads").text)
	except AssertionError as e: verificationErrors.append(str(e))
	try: self.assertEqual("Test Suites", driver.find_element_by_link_text("Test Suites").text)
	except AssertionError as e: verificationErrors.append(str(e))

"""method with SRD page footer tests """
def testFooter(self, driver, verificationErrors):
	try: self.assertEqual(u"Information Technology Laboratory, Software and Systems Division\nPRIVACY/SECURITY ISSUES • FOIA • Disclaimer • USA.gov\nNIST is an agency of the U.S. Commerce Department".encode("utf-8"), driver.find_element_by_xpath("//div[@id='footer']/div/p/span[@class='data']").text.encode("utf-8"))
	except AssertionError as e: self.verificationErrors.append(str(e))
	try: self.assertEqual("Contact:  samate@nist.gov\nThis webpage is XHTML Strict and AA compliant.\nCreated on January 2006, last update: June 1, 2013, Version: 4.3", driver.find_element_by_xpath("//div[@id='footer']/div/p/span[@class='fieldName']").text)
	except AssertionError as e: self.verificationErrors.append(str(e))

"""method with Download Menu tests"""
def testTestDownloadMenu(self, driver, verificationErrors):
	try: self.assertEqual("Search", driver.find_element_by_xpath("//a[contains(@href, 'search.php?simple')]").text)
	except AssertionError as e: self.verificationErrors.append(str(e))
	try: self.assertEqual("Extended Search", driver.find_element_by_xpath("//a[contains(text(),'Extended Search')]").text)
	except AssertionError as e: self.verificationErrors.append(str(e))
	try: self.assertEqual("Source Code Search", driver.find_element_by_xpath("//a[contains(text(),'Source Code Search')]").text)
	except AssertionError as e: self.verificationErrors.append(str(e))

def is_element_present(self, how, what):
	try: self.driver.find_element(by=how, value=what)
	except NoSuchElementException, e: return False
	return True

if __name__ == '__main__':
	main()