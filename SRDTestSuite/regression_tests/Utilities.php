<?php
/*
File: Utilities.php
Author: Eric Rosenberg
Created: 7/2/2013
Description:	
	Utilities.php is a collection of functions that Testings scripts may utilize. 

	Note: Utilities.php is meant to be included by Testings scripts not run standalone.
*/

/*
	$baseURL 				=>	contains a valid URL in which the $xmlFile can query
	$xmlFile 				=>	has valid testcase structure
	$hardCodedParameters 	=>	is a string of additional parameters to add to XML query(can be empty)
	Output 					=>	returns the contents of the generated Query
*/
function getOutput($baseURL, $xmlFile, $hardCodedParameters, &$query = ''){
	$actualURL = $baseURL . getURLQuery($xmlFile) . $hardCodedParameters;
    $opts = array(
      'http'=>array(
        'method'=>"GET",
        'header'=>"Accept-language: en\r\n" .
                  "User-Agent: Mozilla/5.0\r\n"
      )
    );
    $query = $actualURL;
	return file_get_contents($actualURL, false, stream_context_create($opts));
}

/*
	$xmlFile 	=>	has valid testcase structure
	Output 		=>	returns string containing Query extension
*/
function getURLQuery($xmlFile){
	if($xmlFile == "")	return "";
	$xmlFile = simplexml_load_file($xmlFile);
	$data = array();
	foreach ($xmlFile->Parameter as $parameter)
		$data[(string)$parameter['id']] = (string)$parameter;
	$query = http_build_query($data);
	if($query == false && count($xmlFile->Parameter) > 0){
		echo "ERROR: Failed to build query. Most likely something wrong with XML File.\n";
		die;
	}
	return $xmlFile->URL . '?' . $query;
}

?>