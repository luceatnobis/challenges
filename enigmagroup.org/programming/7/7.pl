#!/usr/bin/perl -w
use WWW::Mechanize;
use HTTP::Cookies;
use strict;
use warnings;

&main();

sub main{
	my ($agent,$company,$department,$info,$totalBudget,$username,$password,$result);
	($username,$password) = ($ARGV[0], $ARGV[1]);	

	$agent = WWW::Mechanize->new;

	$agent->get('http://www.enigmagroup.org/');
	$agent->form_number(2); 
	$agent->set_fields('user'=>"$username",passwrd=>$password);
	$agent->click();
	$agent->get("http://www.enigmagroup.org/missions/programming/7/index.php");
	
	$agent->content=~m#from the (.+?) department#;
	$department = $1;
	$agent->content=~m#Company:  (.+?)<br /><br />(.+?)<br /><br /><br /><br /><br /><br />#;
	($company,$info) = ($1,$2);
	$info=~s/ D/\nD/g;
	foreach my $line (split("\n",$info)){
		next unless $line=~/$department/;
		$line=~/(\d+)/;
		$result+=$1;
	}
	my $getString = "company=>$company,department=>$department,total=>$result";
	$agent->post("http://www.enigmagroup.org/missions/programming/7/submit.php",{
		company=>$company,department=>$department,total=>$result});
}
