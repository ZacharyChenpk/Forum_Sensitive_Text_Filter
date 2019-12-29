<?php
$time = time();
$Year = date("Y", $time);
$month = date("m", $time);
$day = date("d", $time);
$counter_sub = "counter.dat";
//添加
$day_cnt="day_cnt.txt";
$Date=$Year.$month.$day."\n";
if (!file_exists($day_cnt)){
	$f_day = fopen($day_cnt, "w");
	fwrite($f_day,$Date."\n");
	fclose($f_day);
}
else{
	$f_day = fopen($day_cnt, "a+");
	$rep=0;
	$count=0;
	while(!feof($f_day)){
		$count+=1;
		$line=fgets($f_day);
		if($Date==$line){
			echo "YES";
			$rep=1;
			break;
		}
	}
	echo $count;
	if($rep==0){
		fwrite($f_day, $Date);
	}
	fclose($f_day);
}
//添加结束
if (!file_exists($counter_sub)){
	$counter = 0;
	$cfile = fopen($counter_sub, "w");
	fputs($cfile,'0');
	fclose($cfile);
}
else{
	$cfile = fopen($counter_sub, "r");
	$counter = trim(fgets($cfile,10));
	fclose($cfile);
}
$counter++;
$cfile = fopen($counter_sub, "w");
fputs($cfile,$counter);
fclose($cfile);
$subject = process_input($_POST['subject']);
$dz_text = process_input($_POST['content']);

//调用python程序分析帖子是否需要过滤
unset($out1);
unset($out2);
$py1=exec("conda activate pytorch36 && python text_filter.py {$subject}",$out1,$res1);
$py2=exec("conda activate pytorch36 && python text_filter.py {$dz_text}",$out2,$res2);
$code1=(int)($out1[count($out1)-1]);
$code2=(int)($out2[count($out2)-1]);
if($code1==2 || $code2==2){
	$judge=false;
}
else{
	$judge=true;
}

$pid = $counter;
$reply_num = 0;
$myarray = array('pid'=>$pid, 'subject'=>$subject, 'dz_text'=>$dz_text, 'time'=>$time, 'reply_num'=>$reply_num);
$myjson = json_encode($myarray, JSON_UNESCAPED_UNICODE);
$newfpath = "json/";
$newfpath .= strval($Year);
$newfpath .= "/";
$newfpath .= strval($month);
if (!is_dir($newfpath)){
	$res = mkdir($newfpath, 0777, true);
	if ($res){
		echo "Directory made";
	}
	else{
		echo "Make directory failed";
	}
}
if(!is_dir("all")){
	mkdir("all",0777,true);
}
$newfname = $newfpath . "/" . strval($day) . ".json";
if($judge){
	file_put_contents($newfname, $myjson.PHP_EOL, FILE_APPEND | LOCK_EX);
	file_put_contents("all/post.json",$myjson.PHP_EOL, FILE_APPEND | LOCK_EX);
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