#!/usr/bin/perl -w
use strict;

&main();

sub main{
	foreach my $k(1..9){
		foreach my $s(1..9){
			if(($k+($s.$k)) eq $k.$s){
				print $k.$s."\n";
			}
		}
	}
}
