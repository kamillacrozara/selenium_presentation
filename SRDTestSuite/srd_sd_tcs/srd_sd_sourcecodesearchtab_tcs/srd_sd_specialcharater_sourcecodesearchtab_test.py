#!/usr/bin/python
# -*- coding: utf-8 *-*
"""
File: srd_sd_specialcharacter_sourcecodesearchtab_test.py
Author: Kamilla H. Crozara
Description:    
    This tests verifies the searches by special 
    characters in fields of the Source Code Search tab
"""
from selenium import webdriver
import unittest, time, re

class SrdSdSpecialcharaterSourcecodesearchtabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        config = {}
        execfile("srd_test_suite.conf", config)
        self.base_url = config["BASE_URL"]
        self.verificationErrors = []
        self.accept_next_alert = True
        
    """This method verifies the results of the special characters searches"""
    def test_srd_sd_specialcharater_sourcecodesearchtab_tc(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?code")

        self.search_special_characters("function", "\"This sentence is wrapped in double quotes.\"")
        driver.back()
        
        self.search_special_characters("fileName", "\"This sentence is wrapped in double quotes.\"")
        driver.back()

        self.search_special_characters("function", "\"This sentence is wrapped in double quotes.\"", True)
        driver.back()
        
        self.search_special_characters("fileName", "\"This sentence is wrapped in double quotes.\"", None, True)
        driver.back()

        self.search_special_characters("function", "'single quotes'")
        driver.back()
        
        self.search_special_characters("fileName", "'single quotes'")
        driver.back()

        self.search_special_characters("function", "'single quotes'", True)
        driver.back()
        
        self.search_special_characters("fileName", "'single quotes'", None, True)
        driver.back()
        
        self.search_special_characters("function", "[square brackets]")
        driver.back()
        
        self.search_special_characters("fileName", "[square brackets]")
        driver.back()

        self.search_special_characters("function", "[square brackets]", True)
        driver.back()
        
        self.search_special_characters("fileName", "[square brackets]", None, True)
        driver.back()
        
        self.search_special_characters("function", "{curly braces}")
        driver.back()
        
        self.search_special_characters("fileName", "{curly braces}")
        driver.back()

        self.search_special_characters("function", "{curly braces}", True)
        driver.back()
        
        self.search_special_characters("fileName", "{curly braces}", None, True)
        driver.back()
        
        self.search_special_characters("function", "<angle brackets>")
        driver.back()
        
        self.search_special_characters("fileName", "<angle brackets>")
        driver.back()

        self.search_special_characters("function", "<angle brackets>", True)
        driver.back()
        
        self.search_special_characters("fileName", "<angle brackets>", None, True)
        driver.back()
        
        self.search_special_characters("function", "<!-- XML comment -->")
        driver.back()
        
        self.search_special_characters("fileName", "<!-- XML comment -->")
        driver.back()

        self.search_special_characters("function", "<!-- XML comment -->", True)
        driver.back()
        
        self.search_special_characters("fileName", "<!-- XML comment -->", None, True)
        driver.back()
        
        self.search_special_characters("function", "\"quoted\" segment & ampersand")
        driver.back()
        
        self.search_special_characters("fileName", "\"quoted\" segment & ampersand")
        driver.back()

        self.search_special_characters("function", "\"quoted\" segment & ampersand", True)
        driver.back()
        
        self.search_special_characters("fileName", "\"quoted\" segment & ampersand", None, True)
        driver.back()
        
        self.search_special_characters("function", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"")
        driver.back()
        
        self.search_special_characters("fileName", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"")
        driver.back()

        self.search_special_characters("function", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"", True)
        driver.back()
        
        self.search_special_characters("fileName", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"", None, True)
        driver.back()
        
        self.search_special_characters("function", "\\c:\\mydocs")
        driver.back()
        
        self.search_special_characters("fileName", "\\c:\\mydocs")
        driver.back()

        self.search_special_characters("function", "\\c:\\mydocs", True)
        driver.back()
        
        self.search_special_characters("fileName", "\\c:\\mydocs", None, True)
        driver.back()

        self.search_special_characters("function", "Hawai`i")
        driver.back()
        
        self.search_special_characters("fileName", "Hawai`i")
        driver.back()

        self.search_special_characters("function", "Hawai`i", True)
        driver.back()
        
        self.search_special_characters("fileName", "Hawai`i", None, True)
        driver.back()

        self.search_special_characters("function", "#20")
        driver.back()
        
        self.search_special_characters("fileName", "#20")
        driver.back()

        self.search_special_characters("function", "#20", True)
        driver.back()
        
        self.search_special_characters("fileName", "#20", None, True)
        driver.back()
        
        self.search_special_characters("function", "\\/")
        driver.back()
        
        self.search_special_characters("fileName", "\\/")
        driver.back()

        self.search_special_characters("function", "\\/", True)
        driver.back()
        
        self.search_special_characters("fileName", "\\/",  None, True)
        driver.back()

    def search_special_characters(self, input_name, characters, precision=None, regex=None):
        self.driver.find_element_by_xpath("//input[@name='%s']" %input_name).send_keys("%s" %characters)
        if precision:
            self.driver.find_element_by_xpath("(//input[@name='precision'])[2]").click()

        if regex:
            self.driver.find_element_by_xpath("//input[@name='searchNameByRegex']").click()

        self.driver.find_element_by_xpath("//input[@name='Submit']").click()
        try: self.assertEqual("SAMATE Reference Dataset :: View all test cases", self.driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
