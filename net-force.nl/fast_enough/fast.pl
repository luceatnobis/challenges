#!/usr/bin/perl -w
use WWW::Mechanize;
use strict;

&main();

sub main{
	my($agent,$answer,$number);

	$agent = WWW::Mechanize->new;
	$agent->get("http://net-force.nl/challenge/level602/prog2.php");
	$agent->content=~m#You will need this number '(\d+)'#;
	$number = $1;

	$answer = ($number * 3 + 2) - 250;
	$agent->get("http://net-force.nl/challenge/level602/prog2.php?solution=$answer");
	print $agent->content."\n";
}
