#!/usr/bin/perl -w
use strict;
use LWP::UserAgent;

&main();

sub main{
	my $agent = LWP::UserAgent->new(max_redirect=>0);
	my $content = $agent->get("http://www.hacker.org/challenge/misc/one.php")->content;	

	
}
