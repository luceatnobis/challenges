#!/usr/bin/perl
use Math::BigInt;
use warnings;
use strict;

&main();

sub main{
	my @big = split("",Math::BigInt->new(17)->bpow(39)->bpow(11));
	my $result;

	for(0..$#big){
		if(0==($_%33)){
			$result .= $big[$_];
		}
	}
	print $result."\n";
}
