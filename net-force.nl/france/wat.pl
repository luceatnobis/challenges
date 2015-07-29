#!/usr/bin/perl -w
use strict;

&main();

sub main{
	my @clear 	= split("","thesecretpasswordforthechallengepageisthekeyweused");
	my @cipher	= split("","vychxqxyrrrqhpcxxdqirwxqnujnvlvxdgackjrwxyksuglqtw");

	foreach my $i(0..$#clear){
		print $i.":".ord($clear[$i]).":".ord($cipher[$i])."\n";
	}
}
