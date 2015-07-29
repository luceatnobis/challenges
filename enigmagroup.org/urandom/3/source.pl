#!/usr/bin/perl
use strict;
use warnings;
use WWW::Mechanize;

&main();

sub main {
	my ($agent, $username, $password);

    $agent = WWW::Mechanize->new;
    $agent->get("http://ipchicken.com");
    $agent->content=~m/(\d+\.\d+\.\d+\.\d+)/;

    ($username,$password) = ($ARGV[0], $ARGV[1]);

    $agent->get('http://www.enigmagroup.org/');
    $agent->form_number(2);
    $agent->set_fields('user'=>"$username",passwrd=>$password);
    $agent->click();
    $agent->get('http://www.enigmagroup.org/missions/dev/urandom/3/');
	foreach(split("\n",$agent->content)){
		print $_."\n" unless $_ eq "";
	}
}
