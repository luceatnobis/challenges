<?
	
	$xorKey = "";
	$craftedXor = "";
	$decodedCookie = "";

	$cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=";
	$array = array("showpassword" => "no", "bgcolor" => "#ffffff");
	$craftedArray = array("showpassword" => "no", "bgcolor" => "#ffffff");
	$craftedJson = json_encode($craftedArray);
	
	$b64d = base64_decode($cookie);
	$json = json_encode($array);

	echo $cookie."\n";
	echo strlen($b64d)."\n";
	echo strlen($json)."\n";
	
	for($i=0;$i<strlen($b64d);$i++){
		#echo $json[$i]."\n";
		$xorKey .= ($b64d[$i] ^ $json[$i]);
	}
	$xorkey = "qw8J";
	for($i=0;$i<strlen($b64d);$i++){
		$craftedXor .= $craftedJson[$i] ^ $xorKey[$i % strlen($xorKey)];
	}
	echo base64_encode($craftedXor)."\n";
?>
