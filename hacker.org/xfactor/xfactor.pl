#!/usr/bin/perl
use Math::BigInt; 
use strict;
use warnings;

&main();

sub main{
	#my $prime = "7393913335919140050521110339491123405991919445111971";
	my $prime = "3453454435";
	my @factors = &fac($prime);
	print "$_\n" for @factors;
}

sub fac{
    my $n = Math::BigInt->new($_[0]);
    my $number = Math::BigInt->new($n);
    my $factor = Math::BigInt->new(2);
	my@factors;
    #foreach my $factor(2..$n){
	until($factor->bcmp($n)==1){
		print $factor."\n";
        last if $number->bcmp(1)==0;
        if($number%$factor==0) {
            $number->bdiv($factor);
            push(@factors,$factor);
            redo;
        }
		$factor->binc();
    }
    return @factors;
}

