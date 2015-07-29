#!/usr/bin/perl -w
use strict;

&main();

sub main{
	foreach my $penis(-1000..1000){
		my $lowerpenis = $penis--;
		if(($penis & $lowerpenis) == 0){
			print $penis."\n";
		}
	}
}
