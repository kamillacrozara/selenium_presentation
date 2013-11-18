Selenium Presentation
=====================

# Demo test cases description #

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


 ### Test 2 - Non-ASCII Characters in UI ###

For each field insert the following text:

 - ñó? ä?çíì ??/??  ??/?? Huáy?; ?? Zh?ngwén ???????? Lech Wa??sa æøå

And verify if the search is performed correctly.1