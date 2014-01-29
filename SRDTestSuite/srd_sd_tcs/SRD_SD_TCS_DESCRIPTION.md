# SRD Search/Download Tab Test Cases

## Description ##

	- Verifies special characters input in the following tabs: Search, Extended Search and Source Code Search;
	- Verifies the query date search on the Extended Search tab;
	- Verifies the weakness search on the Extended Search tab;
	- Verifies the search by File Size on the Source Code Search tab;
	- Verifies the search by Number of Files on the Source Code Search tab;
	- Verifies the search by File Name on the Source Code Search tab;
	- Verifies if the search works properly using the dropdown menus for "Bad/Good/Mixed", "Language" and "Type of Artifact";
	- Verifies the search by File Contais on the Source Code Search tab.


## Common tests for all tabes ##

	### Test 1 - ASCII Special Characters in UI ###

		For each field insert the following values:

			 - "This sentence is wrapped in double quotes."
			 - 'single quotes'
			 - [square brackets]
			 - {curly braces}
			 - <angle brackets>
			 - \<!-- XML comment --\>
			 - "quoted" segment & ampersand
			 - "A "quoted" segment; & (entity); wrapped in quotes"
			 - \\c:\\mydocs
			 - Hawai`i
			 - #20
			 - \/

			 - For the File Size and Number of files search verify the following numbers:
				- -99999
				- 999999

			And verifies if the search is performed correctly.

	### Test 2 - Strings of over 500 characters ###

	For each field insert the following text:

		- I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text.

		And verifies if the search is performed correctly.

	### Test 3 - Non-ASCII Characters in UI ###

		For each field insert the following text:

			- ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå

			And verifies if the search is performed correctly.



## Additional Tests ##

	### srd_sd_extendedsearchtab_tcs/srd_sd_dropdown_options_test.py - Dropdown menus ###

		- Verifies if the search works properly using the dropdown menus for "Bad/Good/Mixed", 
		  "Language" and "Type of Artifact".

	### srd_sd_extendedsearchtab_tcs/srd_sd_weakness_extendedsearchtab_test.py - 
		Search by Weakness and Code complexity on tab "Extended Search"  ###

		- In Search/Download > Extended Search the test verifies if the search by Weakness and Code Complexity works properly.

	### srd_sd_extendedsearchtab_tcs/srd_sd_query_date_extendedsearchtab_test.py - 
		Search by date on tab "Extended Search"  ###

		- In Search/Download > Extended Search the test verifies if the search by date works properly.


	### srd_sd_sourcecodesearchtab_tcs/srd_sd_file_contains_sourcecodesearchtab_test.py - 
		Execute tests using the field "File Contains" on tab "Source code Search"  ###

		- In Search/Download > Extended Search the test verifies if the search by "File contains" works properly.


	### srd_sd_sourcecodesearchtab_tcs/srd_sd_filename_sourcecodesearchtab_test.py - 
		Execute tests using the field "File Name" on tab "Source code Search"  ###

		- In Search/Download > Extended Search the test verifies if the search by "File name" works properly.


	### srd_sd_sourcecodesearchtab_tcs/srd_sd_filesize_minvalue_sourcecodesearchtab_test.py - 
		Execute tests using the fields "File Size" and "Number of files" on tab "Source code Search"  ###

		In Search/Download > Extended Search the test inserts boundarie values in the files "File Size" and "Number of files". 




