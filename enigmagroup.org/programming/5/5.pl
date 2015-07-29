#!/usr/bin/perl -w
use WWW::Mechanize;
use HTTP::Cookies;
use strict;
use warnings;

&main();

sub main{
	my ($agent,$bf,$username,$password,$result);
	($username,$password) = ($ARGV[0], $ARGV[1]);	

	$agent = WWW::Mechanize->new;

	$agent->get('http://www.enigmagroup.org/');
	$agent->form_number(2); 
	$agent->set_fields('user'=>"$username",passwrd=>$password);
	$agent->click();
	$agent->get("http://www.enigmagroup.org/missions/programming/5/index.php");
	$agent->content=~m#<br />(.+?)<br /><br /><br />#;
	$bf = $1;
	
	open(BF,">bf");
	print BF $bf;
	close(BF);
	$result = `bf bf`;	

	$agent->get("http://www.enigmagroup.org/missions/programming/5/index.php?ans=$result");
	print $agent->content."\n";
}
