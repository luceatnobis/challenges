#!/usr/bin/perl
use strict;
use warnings;
use Math::NumSeq::Fibbinary;


&main();

sub main{
	my $seq = Math::NumSeq::Fibbinary->new ();

	print $seq->ith(2973).$/;
}
