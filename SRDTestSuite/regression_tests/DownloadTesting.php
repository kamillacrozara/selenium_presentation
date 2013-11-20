<?php
/*
File: DownloadTesting.php
Author: Eric Rosenberg
Created: 7/2/2013
Description:	
	DownloadTesting.php querys a page to extract data about its table. After extracting, it downloads all the test cases on the page and extracts information about the downloaded file. It compares the two to check for consistency. 

	Syntax: php DownloadTesting.php [-u] http://samate.nist.gov/ngSRD/ *.xml

	Note: [-u] and the following URL are optional and yet require eachother if used.
*/

include('CommandLineHandling.php');
include('Utilities.php');

foreach ($xmlFiles as $filename){
	//Get IDs
	$IDs = array();
	preg_match_all('%view_testcase\.php\?tID=(\d+)%', getOutput($url, realpath($filename), ''), $IDs);
	$IDs = array_unique($IDs[1]);

	//Get Zip
	$zip = getOutput($url, $filename, '&action=zip-page&first=&sort=asc', $temp);
	
	if(!strpos($zip, 'testcases/'))
		echo $separationLine .'ERROR: No Zip File' .$separationLine;

	$activeDirectory = 'DownloadTestingOutput/' .basename($filename, '.xml');

	if(file_exists($activeDirectory))
		exec("rm -r $activeDirectory");
	mkdir($activeDirectory, 0755, true);

	file_put_contents("$activeDirectory/testZip.zip", $zip);
	exec("unzip -qq -d $activeDirectory $activeDirectory/testZip.zip");

	//Analyze files and IDs
	$zip = file_get_contents("$activeDirectory/"."tmp/manifest.xml");
	preg_match_all('%<testcase id=\"(\d+)\"%', $zip, $IDs2);
	echo 'Result: ' .($IDs===$IDs2[1] ? "Inconsistency" : "Consistent") ."\n\n";

	unlink("$activeDirectory/testZip.zip");
}

?>