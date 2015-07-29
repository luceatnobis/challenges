#!/usr/bin/perl -w
use MIME::Base64;
use WWW::Mechanize;
use strict;

&main();

sub main{
	my ($agent,$content,$challHash,$testString,$testHash,$final);
	my (@splitTestString,@decodedChallHash,@decodedTestHash,@xorKeys);

 
	@splitTestString = (split("",$testString = "AAAAAAAA"));
	print "Anmeldevorgang läuft...\n";	
	$agent = WWW::Mechanize->new();
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
        $agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	$agent->click();
	print "Anmeldevorgang abgeschlossen.\n";	

	print "Exempelhash wird heruntergeladen...\n";
	$agent->get("http://securityoverride.org/challenges/decryption/8");
	$content = $agent->content;
	$content=~m/<code style='white-space:nowrap'>\s+(.+?)\s+/;
	$challHash = $1; #Wir haben nun den zu knackenden Hash. Wir werden einen Teststring schicken.
	print "Exempelhash heruntergeladen.\n";

	print "Teststring wird injiziert...\n";
	$agent->form_number(2);
	$agent->set_fields(enc=>"$testString"); #injection
	$agent->click();
	print "Teststring heruntergeladen.\n";
	$content = $agent->content;
	$content=~m#is:</b><br /><br />\x0a(.+?)\x0A#;
	$testHash = $1;
	
	#Wir vergleichen nun den testString mit der verarbeiteten Version
	@decodedTestHash = split("",decode_base64($testHash));
	@decodedChallHash = split ("",decode_base64($challHash));
	
	foreach(0..$#decodedTestHash){
		#print "$splitTestString[$_]:$decodedTestHash[$_]\n";
		my $xor1 = ord($splitTestString[$_]);
		my $xor2 = ord($decodedTestHash[$_]);
		my $result = $xor1 ^ $xor2;
		push(@xorKeys,$result);
	}
	#Wir haben nun alle Bits, mit denen ge'xor't wird
	
	foreach(0..$#decodedChallHash){
		my $xor1 = ord($decodedChallHash[$_]);
		my $xor2 = $xorKeys[$_];
		$final .= chr($xor1 ^ $xor2);
	}
	print "Problem gelöst, Lösung abgeschickt.\n";
	$agent->get("http://securityoverride.org/challenges/decryption/8");
	$agent->form_number(1);
	$agent->set_fields(hash=>$final);
	$agent->click();
	print "Challenge gelöst.\n";
}
