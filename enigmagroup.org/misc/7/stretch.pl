#!/usr/bin/perl
use strict;
use warnings;

&main();

sub main{
	my $text = "admin";
	my $addendum = 'x';

	$text .= " " until length($text) == 32;
	$text .= $addendum;
	print $text."\n";
}
