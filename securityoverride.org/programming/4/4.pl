#!/usr/bin/perl -w
use WWW::Mechanize;
use strict;

&main();

sub main{
	my ($agent,$content,$length,$distance);
	
	$agent = WWW::Mechanize->new();
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
	$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	$agent->click();
	
	$agent->get("http://securityoverride.org/challenges/programming/4/");
	$content = $agent->content;
	$content=~m/<code style='white-space:nowrap'>\s+(.+?)\s+/;

	$length = $1;
	#$length = 3;
	print "Länge = $length\n";

	#Calculating the shortest distance with ((2*$length)**2)+length**2
	$distance = int(sqrt(((2*$length)**2)+($length**2)));
	
	$agent->form_name("submitform");
	$agent->set_fields(string=>$distance);
	$agent->click();
}
