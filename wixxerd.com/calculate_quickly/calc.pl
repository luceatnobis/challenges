#!/usr/bin/perl
use strict;
use warnings;
use WWW::Mechanize;

&main();

sub main{
	my ($agent,$result);

	$agent = WWW::Mechanize->new;
	$agent->get("http://www.wixxerd.com/challenges/coding/chal69.cfm");

	$result = eval($agent->content);
	$agent->get("http://www.wixxerd.com/challenges/coding/chal69.cfm?answer=$result");
	print $agent->content;

}
