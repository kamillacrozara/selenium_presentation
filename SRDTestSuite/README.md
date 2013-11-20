############################
SRD Test Suite
Author: Kamilla H. Crozara
############################

Disclaimer: 

	This software was developed at the National Institute of Standards and
	Technology by employees of the Federal Government in the course of their
	official duties. Pursuant to title 17 Section 105 of the United States
	Code this software is not subject to copyright protection and is in the
	public domain. SRDTestSuite is an experimental system. NIST assumes no
	responsibility whatsoever for its use by other parties and makes no
	guarantees, expressed or implied, about its quality, reliability, or any
	other characteristic. We would appreciate acknowledgment if the software
	is used.


Objective:
	
	Test suite to verify different aspects of the SAMATE Reference Dataset (SRD).  


Requirements:

	Webdriver and Firefox or Chrome: 

		- Firefox web browser (www.mozilla.org) v >= 24
		- Chrome web browser (www.google.com/chrome/‎) v >= 29 
		- Chrome Driver (https://code.google.com/p/chromedriver/downloads/list) v >= 2.2 
		- Python "selenium" package (https://pypi.python.org/pypi/selenium)
		- Python "requests" package (https://pypi.python.org/pypi/requests)

	
	Installing Chrome Driver:

		Download the appropriate file: Chrome Driver (http://code.google.com/p/chromedriver/downloads/list)

		And unzip the Chrome Driver in /usr/bin/google-chrome folder.


Structure:

	The SRD Test Suite is divided in different modules:

	- Light test suite with basic tests; 
	- Test suite of the Search/Download tab;
	- Test suite to check all the download links of SRD;
	- Test suite of the User Interface; 
	- Regression tests to test the SRD for changes.


Running tests: 

 	Configuring the base URL:

		The base URL to execute the tests can be modified in the srd_selenium_tests.conf file. It just need the base url between quotes (e.g. BASE_URL = "http://samate.nist.gov/SRD").

	
	To execute all tests: 

		$python run_srd_tests.py

		Explanation:

			This command executes all tests cases in the suite. It takes around 8 hours to finish the execution. 


	To execute the User Interface tests: 

		$python run_srd_tests.py ui

		Explanation:

			[ui] => argument to execute the User Interface tests. 
			For more information about these tests check the file srd_ui_tcs/srd_ui_tcs_description.md.


	To execute the Search/Download tests: 

		$python run_srd_tests.py sd

		Explanation:

			[sd] => argument to execute the Search/Download tab tests. 
			For more information about these tests check the file srd_ui_tcs/srd_sd_tcs_description.md.


	To check the download links of SRD: 

		$python run_srd_tests.py ck

		Explanation:

			[ck] => argument to check all the download links in SRD. 
			For more information about these tests check the file srd_ui_tcs/srd_ck_tcs_description.md.


	To execute the light version of tests: 

		$python run_srd_tests.py lt

		Explanation:
		
			[lt] => argument to execute basic tests to check the most important functionalities.
			For more information about these tests check the file srd_lt_tcs/srd_ck_tcs_description.md.


	To execute the Regression Tests:

	[For more information about Regression Tests check the file regression_tests/ReadMe.txt]
		
		RunAll.php:

			$python run_srd_tests.py rg RunAll.php -g

			Explanation:
				[-g] => Generate snapshot (Expected Directory)
				
				After make changes to website or database you can run "RunAll.php" without -g to run diff [$python run_srd_tests.py rg RunAll.php] and examine changes.


		TraditionalTesting.php:

			$python run_srd_tests.py rg TraditionalTesting.php [-g] [-u] anyValidBaseUrl *.xml

			Explanation:
				[-g] (Optional) => Generate snapshot (Expected Directory)
				[-u] (Optional) => Base URL Override - Must be followed by valid base url (anyValidBaseUrl)
				*.xml 			=> Listing of XML files of valid testcase structure
		

		DownloadTesting.php:

			$python run_srd_tests.py rg DownloadTesting.php [-u] [anyValidBase Url] [*.xml files directory]

			Explanation:
				[-u] (Optional) => Base URL Override - Must be followed by valid base url (anyValidBaseUrl)
				*.xml 			=> Listing of XML files of valid testcase structure