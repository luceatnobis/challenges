#!/usr/bin/perl -w
use strict;

&main();

sub main{
	my($c,$u,$b,$e,$d);

	foreach$c(1..9){
		foreach$u(1..9){
			foreach$b(1..9){
				foreach$e(1..9){
					foreach$d(1..9){
						my $sum = $c+$u+$b+$e+$d;
						my $string = "$c$u$b$e$d";
						if(($sum**3) eq "$string"){
							print $string."\n";
						}
					}
				}
			}
		}
	}
}
