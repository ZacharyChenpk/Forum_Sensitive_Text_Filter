<?php
$url=$_POST["data"];
$s=array();
$f = fopen($url, "r");
while(!feof($f)){
	$line=fgets($f);
	if($line==""){
		break;
	}
	echo $line."@,";
}
?>