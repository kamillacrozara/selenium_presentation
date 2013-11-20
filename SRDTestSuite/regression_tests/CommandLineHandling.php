<?php
/*
File: CommandLineHandling.php
Author: Eric Rosenberg
Created: 7/2/2013
Description:	
	CommandLineHandling.php extracts the command line arguments and displays a summary in the terminal. 

	Note: CommandLineHandling.php is meant to be included by Testings scripts not run standalone.
*/

include('Defaults.php');

//Extract Arguments - Syntax: php script.php [-g] [-u] anyValidBaseUrl *.xml
for ($i = 1; $i < count($argv); $i++)
	if($argv[$i] == '-g')
		$generate = true;
	else if($argv[$i] == '-u' && count($argv)-$i > 0){
		if(count($argv) - $i > 0 && preg_match('%[\w\d\.]+\.gov/\w%', $argv[$i+1])){
			if(strpos($argv[$i+1], "http://") !== 0)
				$argv[$i+1] = "http://" . $argv[$i+1];
			if(substr($argv[$i+1], -1) !== '/')
				$argv[$i+1] = $argv[$i+1] .'/';
			$url = $argv[$i+1];
		}else echo "\n**Failed to Override URL. Reverting to default.**\n";
	}
	else if(file_exists(realpath($argv[$i])) && pathinfo(realpath($argv[$i]), PATHINFO_EXTENSION) == 'xml')
		$xmlFiles[] = $argv[$i];

//Extract either 'SRD' or 'ngSRD'
preg_match('%\.gov/(\w+)/%', $url, $matches);
$subdirectory = (count($matches) > 0 ? $matches[1] : '');

//Make sure there are XML Files
if(count($xmlFiles) == 0){
	echo "ERROR: 0 XML Files Found";
	die;
}

echo $separationLine;
if($generate)
	echo "Generate Snapshot: \t\tTrue\n";
echo "URL: \t\t\t\t$url\n";
echo "Subdirectory: \t\t\t$subdirectory\n";
echo "Number of XML Files Found: \t" .count($xmlFiles);
echo $separationLine;

?>