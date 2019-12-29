<?php
$pid=$_POST["pid"];
$f = fopen("all/comment.json", "r");
while(!feof($f)){
	$line=fgets($f);
	if(strpos($line,"\"pid\":"."\"".$pid)!==false){
		echo $line."@,~";
	}
}
?>