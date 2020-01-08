<?php
$time = time();
$com_f = "all/comment.json";
$reply = process_input($_POST['content']);
unset($out1);
$py1=exec("conda activate pytorch36 && python text_filter.py {$reply}",$out1,$res1);
$code1=(int)$out1[count($out1)-1];
if($code1==2){
	$judge=false;
}
else{
 	$judge=true;
}
$pid=$_POST['pid'];
$myarray=array("pid"=>$pid,"content"=>$reply);
$myjson = json_encode($myarray, JSON_UNESCAPED_UNICODE);
if($judge){
	file_put_contents($com_f, $myjson.PHP_EOL, FILE_APPEND | LOCK_EX);
	echo "succeed";
}
else{
	echo "blocked";
}
function process_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>