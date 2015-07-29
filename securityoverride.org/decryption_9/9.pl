#!/usr/bin/perl -w
use WWW::Mechanize;
use strict;

&main();

sub main{
	my ($agent,$content,$length,$distance);
	#open(DATEI,"+>table");

	$agent = WWW::Mechanize->new();
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
	$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	$agent->click();
	
	foreach(32..127){	#7bit ascii
		my $probe = chr($_).chr($_);

		$agent->get("http://securityoverride.org/challenges/decryption/9/");
		$agent->form_number(2);
		$agent->set_fields(enc=>$probe);
		$agent->click();
		$agent->content=~m#\x0A(\d+128)(\d+)\x0A#;
		my $line =  "$1:".chr($_)."\n$2:".chr($_)."\n";
		print $line;
	}			
}
