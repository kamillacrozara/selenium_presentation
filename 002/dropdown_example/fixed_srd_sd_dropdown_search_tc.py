from selenium import webdriver
import unittest

class GeneratedSrdSdDropdownSearchTc(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://samate.nist.gov/SRD"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_generated_srd_sd_dropdown_search_tc(self):
        driver = self.driver
        driver.get(self.base_url + "/search.php?simple")

        driver.find_element_by_name("description").clear()
        driver.find_element_by_name("description").send_keys("buffer")

        ##fixed selection of dropdown options
        el = driver.find_element_by_xpath("//select[@name='flawed[]']")
        self.select_option_dropdow(el, "Bad")

        el = driver.find_element_by_xpath("//select[@name='languages[]']")
        self.select_option_dropdow(el, "Java")

        el = driver.find_element_by_xpath("//select[@name='typesofartifacts[]']")
        self.select_option_dropdow(el, "Source Code")

        driver.find_element_by_name("Submit").click()
        self.assertEqual("SAMATE Reference Dataset :: View all test cases", driver.title)
    
    def select_option_dropdow(self, element, opt_text):
        for option in element.find_elements_by_tag_name('option'):
            if option.text == opt_text:
                option.click() 
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
