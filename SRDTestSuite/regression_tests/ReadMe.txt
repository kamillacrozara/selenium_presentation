SRD Regression Testing
Author: Eric Rosenberg
Created: 7/2/2013

Objective:		
				Test the SRD for changes.

Solution:		
				Run queries on the SRD website to generate a snapshot of the website. After manipulation to the website has occurred, run the same queries and examine differences.

Usage Guide:	
				General: 
					1)	Run "RunAll.php" with -g to create snapshot
					2)	Make changes to website or database
					3)	Run "RunAll.php" without -g to run diff
					4)	Examine changes.

				RunAll.php:
					Default execution of all tests in the terminal window. In order to add more tests, add XML file test cases to TraditionTestingXMLs and DownloadTestingXMLs.

					Syntax:
						Generate Snapshot 	=> "php RunAll.php -g"
						Run Diff 			=> "php RunAll.php"

				TraditionalTesting.php:
					This script runs similar functions as the previous regression testing scripts. It uses the Utilities.php functions to query the database and set the output as a snapshot to be compared to in the future or compares the files to a previous snapshot. After the comparison, the changes are logged in a .txt file in the output directory. 

					Syntax:
						php script.php [-g] [-u] anyValidBaseUrl *.xml

						Explanation:
							php 			=> The script is run with php
							script.php 		=> The script you wish to run
							[-g] (Optional) => Generate snapshot (Expected Directory)
							[-u] (Optional) => Base URL Override - Must be followed by valid base url (anyValidBaseUrl)
							*.xml 			=> Listing of XML files of valid testcase structure

					Example:
						1)	php TraditionalTesting.php -g -u http://samate.nist.gov/ngSRD/ TraditionalTestingXMLs/*.xml

							Explanation:
								This command will "generate" a snapshot from querying the overriden base URL "http://samate.nist.gov/ngSRD/" and the queries will be extracted from all of the XML files in "TraditionalTestingXMLs/".

						2) php TraditionalTesting.php -u http://samate.nist.gov/ngSRD/ TraditionalTestingXMLs/*.xml

							Explanation:
								This command will compare the files returned from queries to the override base URL "http://samate.nist.gov/ngSRD/" with the current expected directory. The queries will be extracted from all of the XML files in "TraditionalTestingXMLs/".

				DownloadTesting.php:
					This script uses the Utilities.php functions to query the database for a table of data, downloads the zip of testcases associated with that tables and compares the values of the two to check for consistency.

					Syntax:
						php DownloadTesting.php [-u] anyValidBase Url *.xml

					Example:
						php DownloadTesting.php -u http://samate.nist.gov/ngSRD/ DownloadTestingXMLs/SRDDownloadZIP.xml

							Explanation:
								This command will run a consistency check based on "DownloadTestingXMLs/SRDDownloadZIP.xml" on the overriden base URL "http://samate.nist.gov/ngSRD"