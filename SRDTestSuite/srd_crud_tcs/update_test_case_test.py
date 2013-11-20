#!/usr/bin/python
# -*- coding: utf-8 *-*

class UpdateTestCase(unittest.TestCase):
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


    def test_update_test_case(self):
    	driver = self.driver