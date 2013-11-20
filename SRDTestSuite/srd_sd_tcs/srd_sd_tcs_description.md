# SRD Search/Download Tab Test Cases

## Description ##

The [SRD Seach/Download tab Test Cases](d5/da7/a00144.html) verifies special characters input in the following tabs: [Search](http://samate.nist.gov/ngSRD/search.php?simple), 
[Extended Search](http://samate.nist.gov/ngSRD/search.php?extended) and [Source Code Search](http://samate.nist.gov/ngSRD/search.php?code). 

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

### Test 2 - Strings of over 500 characters ###

For each field insert the following text:

- I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text. I am typing in more than 500 characters of text to test whether the more than 500 characters are cut off or if they display correctly. 500 characters is a lot of text.

### Test 3 - Non-ASCII Characters in UI ###

For each field insert the following text:

 - ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå

And verify if the search is performed correctly.1


### Test 4 - Dropdown menus ###

Verify if the search works properly using the dropdown menus for "Bad/Good/Mixed", "Language" and "Type of Artifact".


### Test 5 - Search by Weakness and Code complexity ###

In Search/Download > Extended Search verify if the search by Weakness and Code Complexity works properly. 


### Test 5 - Search by date ###

In Search/Download > Extended Search verify if the search by date works properly.





