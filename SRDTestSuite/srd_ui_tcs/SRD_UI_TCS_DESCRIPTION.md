# SRD User Interface Test Cases

## Description

The SRD User Interface Test Cases verifies the user interface elements for each page in SRD.

### common_ui_tests.py - Basic tests used in all test cases ###

For each page the following basic elements are verified:

	- SRD Banner
	- Page title
	- SRD menu
	- Footer


### check_links_response_test.py - Check links on a given page ###
	Goes to each page listed on the configuration file and test the answer of all the 'href' elements.
	If it other than 200 a warning is raised. 


### view_download_test.py - View/Download page tests ###

For the View/Download page the following elements are verified:
	- Table titles
	- The sort "Test Case by ID"

### more_downloads_test.py - More Downloads page: ###
	- Verify if the following elements are present:
		- Download the Full Manifest
		- Weaknesses and Code complexities
		- Manifest generation

### search_download_extendedsearchtab_test.py - Search Download/Extended Search tab ###
	- Page title
	- Table titles

### search_download_searchtab_test.py - Search Download/Search tab ###
	- Page title
	- Table titles

### search_download_sourcecodesearchtab_test.py - Search Download/Source Code Search tab ###
	- Page title
	- Table titles

### srd_home_test.py - SRD Home page ###
	- Page title

### test_suites_test.py - Test Suites page ###
	- Page title
	- Table titles

### view_testcase_148803_page_test.py - Test Suites page ###
	- Page title
	- Table titles