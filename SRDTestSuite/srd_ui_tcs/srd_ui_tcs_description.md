# SRD User Interface Test Cases

## Description

The [SRD User Interface Test Cases](da/ddb/a00145.html) verifies the user interface elements for each page in SRD.

### Test 1 - Basic elements ###

For each page the following basic elements are verified:
	- Page title
	- SRD menu
	- Sections title
	- Footer


### Test 2 - View/Download page ###

For the View/Download page the following elements are verified:
	- Table titles
	- The sort "Test Case by ID"
	- "Results" text
	- "Download" label
	- Download options
	- Pagination options
	- "Go to page" input
	- "Go to page" going to page "64"
		- Page number
		- Links to page "63" and "65"
		- Table titles
	- Pagination option in footer
	- Selector "Number of Test Cases per page:"


### Test 3 - Test Case page: ###

For the Test Case page the following elements are verified:
	- "Back to the previous page" option
	- Titles in test case description table
	- The "Download" label
	- Download option
	- "Status" button
	- Bad / Good / Mixed "button"
	- "Filename" link to download the source code
	- The Flaw tree (CWE tree)
	- "Submmit a comment" link
	- If exists, verify comments
	- The source code section (if exists, verify tables)

### Test 4 - Search/Download page: ###

For the Search/Download page the following elements are verified:
	- Tabs in Search/Download menu
	- For each tab, verify input labels, search button and menus drop down
	- If exists, verify the link "Click here if experiencing some trouble with the JavaScript trees."
	- The search
