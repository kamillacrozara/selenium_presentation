# SRD Light Test Suite

## Description ##

	The SRD Light Test Suite verifies the basic funcionalities of the SRD.


	### search_download_light_test.py - Verify basic search with special characters ###

		- Verifies the search with special characters for some fields in Search/Download page.


	### numfiles_maxvalue_light_test.py, numfiles_maxvalue_light_test.py and numfiles_samevalue_light_test.py - 
		Verify the max and min search of "Source Code Search" tab ###

		- Verify the search for boundary values on the "Number of files" field.


	### check_links_light_test.py - Verify the download link of selected test cases ###

		- For pages 20, 44370 and 88720 (using the default visualization with 20 test cases per page) select 
			10 tests cases and verifies the link "Download the selected Test Cases".


	### check_links_light_test.py - Verify the download links of all test cases in a page ###
		
		- For pages 20, 44370 and 88720 (using the default visualization with 20 test cases per page) verifies the link 	"Download all test cases on the page".


	### check_links_light_test.py - Verify the direct download link of all test cases in SRD ###
		
		- Verifies the request to download all the tests cases in the SRD.


	### check_links_light_test.py - Verify the download links of some test cases in  SRD###
		
		- Goes to each Test Case on pages 20, 44370 and 88720 in the SRD and verifies the link "Download this Test Case #".
