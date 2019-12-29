<?php
$filename=$_POST["file"];
$pid=$_POST["pid"];
$f = fopen($filename, "r");
$cnt=1;
while(!feof($f)){
	$line=fgets($f);
	if($cnt==(int)$pid){
		echo $line;
		break;
	}
	$cnt+=1;
}
?>