#!/usr/bin/perl -w
use Math::BigFloat;
use strict;

&main();

sub main{
	Math::BigFloat->accuracy(5003);
	my $bigNum = Math::BigFloat->new(13155187)->bdiv(13417);
	print "$bigNum\n";
}
