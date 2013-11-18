#!/usr/bin/python
# -*- coding: utf-8 *-*
from selenium import webdriver
import unittest

class SrdSdSpecialcharaterExtendedsearchtabTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://samate.nist.gov/SRD"
        self.verificationErrors = []

    def test_srd_sd_specialcharater_extendedsearchtab_tc(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?extended")
        self.assertEqual("SAMATE Reference Dataset", driver.title)
    
        self.search_special_characters("reference", "\"This sentence is wrapped in double quotes.\"")
        driver.back()
        
        self.search_special_characters("description", "\"This sentence is wrapped in double quotes.\"")
        driver.back()
        
        self.search_special_characters("author", "\"This sentence is wrapped in double quotes.\"")
        driver.back()
       
        self.search_special_characters("contributor", "\"This sentence is wrapped in double quotes.\"")
        driver.back()        

        self.search_special_characters("reference", "'single quotes'")
        driver.back()
        
        self.search_special_characters("description", "'single quotes'")
        driver.back()
        
        self.search_special_characters("author", "'single quotes'")
        driver.back()
        
        self.search_special_characters("contributor", "'single quotes'")
        driver.back()
        
        self.search_special_characters("reference", "[square brackets]")
        driver.back()
        
        self.search_special_characters("description", "[square brackets]")
        driver.back()
        
        self.search_special_characters("author", "[square brackets]")
        driver.back()
        
        self.search_special_characters("contributor", "[square brackets]")
        driver.back()
        
        self.search_special_characters("reference", "{curly braces}")
        driver.back()
        
        self.search_special_characters("description", "{curly braces}")
        driver.back()
        
        self.search_special_characters("author", "{curly braces}")
        driver.back()
        
        self.search_special_characters("contributor", "{curly braces}")
        driver.back()
        
        self.search_special_characters("reference", "<angle brackets>")
        driver.back()
        
        self.search_special_characters("description", "<angle brackets>")
        driver.back()
        
        self.search_special_characters("author", "<angle brackets>")
        driver.back()
   
        self.search_special_characters("contributor", "<angle brackets>")
        driver.back()
        
        self.search_special_characters("reference", "<!-- XML comment -->")
        driver.back()
        
        self.search_special_characters("description", "<!-- XML comment -->")
        driver.back()

        self.search_special_characters("author", "<!-- XML comment -->")
        driver.back()

        self.search_special_characters("contributor", "<!-- XML comment -->")
        driver.back()
        
        self.search_special_characters("reference", "\"quoted\" segment & ampersand")
        driver.back()
        
        self.search_special_characters("description", "\"quoted\" segment & ampersand")
        driver.back()
        
        self.search_special_characters("author", "\"quoted\" segment & ampersand")
        driver.back()
        
        self.search_special_characters("contributor", "\"quoted\" segment & ampersand")
        driver.back()
        
        self.search_special_characters("reference", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"")
        driver.back()
        
        self.search_special_characters("description", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"")
        driver.back()
        
        self.search_special_characters("author", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"")
        driver.back()
        
        self.search_special_characters("contributor", "\"A \"quoted\" segment; & (entity); wrapped in quotes\"")
        driver.back()
        
        self.search_special_characters("reference", "\\c:\\mydocs")
        driver.back()
        
        self.search_special_characters("description", "\\c:\\mydocs")
        driver.back()
        
        self.search_special_characters("author", "\\c:\\mydocs")
        driver.back()

        self.search_special_characters("contributor", "\\c:\\mydocs")
        driver.back()

        self.search_special_characters("reference", "Hawai`i")
        driver.back()
        
        self.search_special_characters("description", "Hawai`i")
        driver.back()
        
        self.search_special_characters("author", "Hawai`i")
        driver.back()

        self.search_special_characters("contributor", "Hawai`i")
        driver.back()

        self.search_special_characters("reference", "#20")
        driver.back()
        
        self.search_special_characters("description", "#20")
        driver.back()
        
        self.search_special_characters("author", "#20")
        driver.back()

        self.search_special_characters("contributor", "#20")
        driver.back()

        self.search_special_characters("reference", "\\/")
        driver.back()
        
        self.search_special_characters("description", "\\/")
        driver.back()
        
        self.search_special_characters("author", "\\/")
        driver.back()

        self.search_special_characters("contributor", "\\/")
        driver.back()

    def search_special_characters(self, input_name, characters):
        self.driver.find_element_by_xpath("//input[@name='%s']" %input_name).send_keys("%s" %characters)
        self.driver.find_element_by_xpath("//input[@name='Submit']").click()
        try: self.assertEqual("SAMATE Reference Dataset :: View all test cases", self.driver.title)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
