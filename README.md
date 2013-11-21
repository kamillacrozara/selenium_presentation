Selenium 
=====================

Adding real browsers to your testes.

## Requirements ##

	- Firefox web browser (www.mozilla.org) v >= 24
	- Selenium IDE (http://www.seleniumhq.org/download/) v >= 2.4.0
	- Python "selenium" package (https://pypi.python.org/pypi/selenium)
	- Python "requests" package (https://pypi.python.org/pypi/requests)

	
	Optional:

		- Chrome web browser (www.google.com/chrome/‎) v >= 29 
		- Chrome Driver (https://code.google.com/p/chromedriver/downloads/list) v >= 2.2 
	
		Installing Chrome Driver:

			Download the appropriate file: 
				Chrome Driver (http://code.google.com/p/chromedriver/downloads/list)

			And unzip the Chrome Driver in /usr/bin/google-chrome folder.


## Demo - Test cases description ##

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

		 And verify if the search is performed correctly.


	 ### Test 2 - Non-ASCII Characters in UI ###

		For each field insert the following text:

		 - ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå

		And verify if the search is performed correctly.