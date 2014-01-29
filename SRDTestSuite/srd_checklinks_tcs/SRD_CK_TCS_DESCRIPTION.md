# SRD Checklinks Test Cases

	## Description ##

	The SRD Checklinks Test Cases verifies all the download links in SRD. These tests takes around 14 hours to run.

	### download_selected_tcs_test.py - Verify the download link of selected test cases ###

		For each page of test cases (using the default visualization with 20 test cases per page) select 
		10 tests cases and verify the response of the link "Download the selected Test Cases".

	### download_all_tcs_test.py - Verify the download links of all test cases in a page ###
		
		For each page of test cases (using the default visualization with 20 test cases per page) verify the link "Download all test cases on the page".

	### download_all_tcs_test.py - Verify the direct download link of all test cases in SRD ###
		
		Verify the request to download all the tests cases in the SRD.

	### download_each_tc_test.py - Verify the download links of each test cases in  SRD ###
		
		Go to each Test Case in the SRD and verify the link "Download this Test Case #".

	### download_test_suites_test.py - Verify the links of all files in the Test Suite page ###
		
		Go to the Test Suite page and verify the links for Stand-alone Suites, SRD Suites and Archives.


