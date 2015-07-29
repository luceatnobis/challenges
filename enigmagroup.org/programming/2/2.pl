#!/usr/bin/perl -w
use WWW::Mechanize;
use HTTP::Cookies;
use strict;
use warnings;

&main();

sub main{
	my ($agent,$username,$password,$result);
        ($username,$password) = ($ARGV[0], $ARGV[1]);	

	$agent = WWW::Mechanize->new;

	$agent->get('http://www.enigmagroup.org/');
	$agent->form_number(2); 
	$agent->set_fields('user'=>"$username",passwrd=>$password);
	$agent->click();

	$agent->get("http://www.enigmagroup.org/missions/programming/2/");
	$agent->content=~/(\d+?) by (\d+?)/;
	$result = ($1*$2);

	$agent->form_number(1);
	$agent->set_fields(answer=>$result);
	$agent->click();
	print $agent->content;
}
