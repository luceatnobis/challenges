#!/usr/bin/perl -w
use Math::BaseCalc;
use strict;
use warnings;

&main();

sub main{
	my $base = new Math::BaseCalc(digits=>[0,1,2,3,4,5,6]);
	my $number = "28679718602997181072337614380936720482949";
	print $base->to_base($number)."\n";
}
