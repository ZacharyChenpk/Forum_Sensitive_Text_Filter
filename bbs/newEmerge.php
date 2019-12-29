<?php
$url=$_POST["data"];
$f = fopen($url, "r");
$num = mt_rand(1,999);
$cnt = 1;
while(!feof($f)){
	$line=fgets($f);
	if($cnt==$num){
		echo $line;
		break;
	}
	$cnt++;
}
fclose($f);
?>