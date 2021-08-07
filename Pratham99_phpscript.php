<?php

$name = "Prathamesh Bobale";
$email = "gmsbin02.prathamesh.bobale@gnkhalsa.edu.in";
$biostack = "Genomics/Software/Transcriptomics";
$slack_username = "Pratham99";
$twitter_handle = "pbobale99";
${$slack_username} = "Pratham99";
${$twitter_handle} = "pbobale99";


$hamming_distance = 0;	
$str1 = str_split($slack_username);
$str2 = str_split($twitter_handle);
$hammin_distance = 0;
$length = count($str2);
for($i=0;$i<$length;$i++){
	if($str1[$i] != $str2[$i]){
	$hamming_distance++;}}

echo ("$name,$email,@${$slack_username},$biostack,@${$twitter_handle},$hamming_distance");

?>