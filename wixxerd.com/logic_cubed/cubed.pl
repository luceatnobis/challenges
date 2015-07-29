#!/usr/bin/perl
use warnings;
use strict;

&main();

sub main{
	my ($l,$o,$g,$i,$c) = (0,0,0,0,0,0);
	foreach $l (1..9){
		foreach $o (1..9){
			foreach $g (1..9){
				foreach $i (1..9){
					foreach $c (1..9){
						my $cubed = ($l+$o+$g+$i+$c)**3;
						if("$l$o$g$i$c" == $cubed){
							print "$l+$o+$g+$i+$c ** 3 == $cubed\n";
						}
					}
				}
			}
		}
	}
}
