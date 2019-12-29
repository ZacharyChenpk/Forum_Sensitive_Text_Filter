<?php
$time = time();
$com_f = "all/comment.json";
$reply = process_input($_POST['content']);
$pid=$_POST['pid'];
$myarray=array("pid"=>$pid,"content"=>$reply);
$myjson = json_encode($myarray, JSON_UNESCAPED_UNICODE);
file_put_contents($com_f, $myjson.PHP_EOL, FILE_APPEND | LOCK_EX);
echo "succeed";
function process_input($data)
{
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
?>