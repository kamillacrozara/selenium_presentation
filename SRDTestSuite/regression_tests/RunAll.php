<?php
/*
File: RunAll.php
Author: Eric Rosenberg
Created: 7/2/2013
Description:	
	RunAll.php executes the TraditionalTesting and DownloadTesting scripts with two options, generate and URL override. It executes these scripts with all of the XML files inside the subdirectory "TraditionalTestingXMLs" and "DownloadTestingXMLs" respectively. 

	Syntax: php RunAll.php [-g] [-u] http://samate.nist.gov/ngSRD/
	Note: all options are optional.
*/

//Arg handling
$options = '';

for ($i = 1; $i < count($argv); $i++)
	if($argv[$i] == '-g')
		$options .= '-g ';
	else if($argv[$i] == '-u'){
		if(count($argv)-$i > 0)
			$options .= '-u ' .$argv[$i+1] .' ';
		else echo "Failed to override URL - Reverting to Default.\n";
		$i++;
	}
	else echo "Failed to Process Additional Arguments.\n";

//Traditional Testing
system('php TraditionalTesting.php ' . $options .'TraditionalTestingXMLs/*.xml');

//Run Download Testing
system('php DownloadTesting.php ' . $options .'DownloadTestingXMLs/*.xml'); //Will not work 6/28/2013

//system('php DownloadTesting.php -u http://samate.nist.gov/ngSRD DownloadTestingXMLs/*.xml'); //Will work 6/28/2013

?>