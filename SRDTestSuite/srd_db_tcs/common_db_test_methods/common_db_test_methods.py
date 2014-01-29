#!/usr/bin/python
# -*- coding: utf-8 *-*

import unittest, time, os, re, random
from srd_sd_tcs.common_sd_methods import common_sd_methods


dropdown_options = {'languages' : ["Python", "Java", "C"], 
                    'flawed' : ["Bad", "Good", "Mixed"],
                    'artifact' : ["Source Code", "Binary", "Pseudo Code"],
                    'type_flaw' : ["----+ CWE-180: Incorrect Order", "----+ CWE-209: Information Leak Error", "--+ CWE-506: Embedded Malicious Code"],
                    'ccplx' : ["memory access", "pointer", "memory location"]
                    }


def insert_test_cases(driver, base_url):
    insertedTestCasesID = []

    i = 0
    #3 is the size of the dropdown_options lists
    while i < 3:
        #inserting test cases
        driver.get(base_url + "/submit.php")
        el = driver.find_element_by_xpath("//select[@name='flawed[]']")
        common_sd_methods.select_option_dropdow(el, dropdown_options.get('flawed')[i])

        el = driver.find_element_by_xpath("//select[@name='languages[]']")
        common_sd_methods.select_option_dropdow(el, dropdown_options.get('languages')[i])

        el = driver.find_element_by_xpath("//select[@name='typesofartefacts[]']")
        common_sd_methods.select_option_dropdow(el, dropdown_options.get('artifact')[i])

        driver.find_element_by_xpath("//input[@name='input']").clear()
        driver.find_element_by_xpath("//input[@name='input']").send_keys("Selenium automated tests")
        driver.find_element_by_xpath("//input[@name='output']").clear()
        driver.find_element_by_xpath("//input[@name='output']").send_keys("Selenium automated tests")
        driver.find_element_by_xpath("//textarea[@name='description']").clear()
        driver.find_element_by_xpath("//textarea[@name='description']").send_keys("Selenium automated tests")

        #if true, include zip files using the 'Directory' tab
        #if i == 2:
        #    driver.find_element_by_xpath("//a[contains(text(),'Directory')]").click()
        #    driver.find_element_by_xpath("//input[@name='archive']").send_keys(os.getcwd() + "/srd_db_tcs/example_files/example_files.zip")
        #    driver.find_element_by_xpath("//a[contains(text(),'Files')]").click()
        #else:
        driver.find_element_by_xpath("//input[@name='file_1']").send_keys(os.getcwd() + "/srd_db_tcs/example_files/example_file_selenium.py")    


        driver.find_element_by_xpath("//input[@name='lines_1']").clear()
        driver.find_element_by_xpath("//input[@name='lines_1']").send_keys(str(random.randint(10, 80)))

        el = driver.find_element_by_xpath("//select[@name='typesofflaws_1[]']")
        common_sd_methods.select_option_dropdow(el, dropdown_options.get('type_flaw')[i])

        el = driver.find_element_by_xpath("//select[@name='ccplx_1[]']")
        common_sd_methods.select_option_dropdow(el, dropdown_options.get('ccplx')[i])

        driver.find_element_by_xpath("//input[@name='Submit']").click()

        time.sleep(3)

        try: insertedTestCasesID.append(re.search('\d+', driver.find_element_by_xpath("//div[@id='okay']").text).group(0))
        except AssertionError as e: verificationErrors.append("Could not find the test case ID!")

        i += 1

    return insertedTestCasesID


"""This method selects the option opt_text in the dropdown element"""
def select_option_dropdow(element, opt_text):
    for option in element.find_elements_by_tag_name('option'):
        if option.text == opt_text:
            option.click() 


def login_srd(driver, base_url, user, password):
    driver.get(base_url + "/login.php")
    driver.find_element_by_id("login").send_keys(user)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_name("submit").click()
