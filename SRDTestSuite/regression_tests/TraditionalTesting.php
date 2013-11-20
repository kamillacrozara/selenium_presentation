<?php
/*
File: TraditionalTesting.php
Author: Eric Rosenberg
Created: 7/2/2013
Description:	
	TraditionalTesting.php querys a page record its HTML. The record becomes a snapshot of the website. Later, the script can be run again without the generate option (-g) to compare the current website to the existing record. The comparision is done with a diff and the output is saved to a file inside the Proposed subdirectory of TraditionalTestingOutput. This file is name diffOutput.txt. 

	Syntax: php TraditionalTesting.php [-g] [-u] http://samate.nist.gov/ngSRD/ *.xml

	Note: [-g] is used to generate a record or snapshot. [-u] and its following url are used to override the URL that the scripts querys.
*/

include('CommandLineHandling.php');
include('Utilities.php');

$testingDirectory = basename($argv[0], ".php") .'Output';
$queries = array(); //Array of queries to reference later. filename.html => http://example.com/script.php?param1=0

if(!$generate)
	checkExpected($testingDirectory);

// Build the active directory 
$activeDirectory = $testingDirectory . '/' .($generate ? 'Expected' : 'Proposed');
if(file_exists($activeDirectory))
	exec("rm -r $activeDirectory");
if(!mkdir($activeDirectory, 0775, true)){
	echo "ERROR: Failed to build Active Directory.\n";
	die;
}

//Run queries
//$xmlFileOutputs = runQueries($xmlFiles, $url, &$queries);

//Process all output
if(!$generate){
	$numberOfChanges = 0;
	$expectedDirectory = $testingDirectory . '/Expected';
	$reportLog = '';
}

file_put_contents($activeDirectory . '/ReadMe.txt', "Files come from: $subdirectory");
$countTotal = count($xmlFiles);
$counter = 0;
foreach ($xmlFiles as $filename){
	$query = '';

	$file = basename($filename, '.xml') . '.html';
	$proposedFile = $activeDirectory . '/' . $file;

	if(!$generate)
		$expectedFile = $expectedDirectory . '/' . $file;

	file_put_contents($proposedFile, getOutput($url, realpath($filename), '', &$query));

	if(!$generate){
		$reportLog .= $separationLine;
		$reportLog .= "File: $file\n";
		$reportLog .= "Query: $query\n";
		$differences = shell_exec('diff -B ' .realpath($expectedFile) . ' ' .realpath($proposedFile) .'| cat -v');
		if(!$differences == ''){
			$numberOfChanges++;
			$reportLog .="$differences\n";
		}else $reportLog .="Exact Match\n";
		$reportLog .= $separationLine;
	}
	$counter++;
	system('echo "Progress: ' . intval(100 * ($counter / $countTotal)) .'%"');
	system('echo "\033[2A"');
}
system('echo');
system('echo');
if(!$generate){
	echo "Found: \t\t\t\t$numberOfChanges files with differences.\n";
	file_put_contents($activeDirectory  .'/diffOutput.txt', $reportLog);
	echo "File With Details Created: \t$activeDirectory/diffOutput.txt\n";
}else
	echo "Generation Completed\n";

/*
	Output 	=> returns the Expected directory
*/
function checkExpected(){
	global $testingDirectory;
	if(file_exists("$testingDirectory/Expected"))
		return true;
	echo "ERROR: No Expected Directory Found.\n";
	die;
}

?>