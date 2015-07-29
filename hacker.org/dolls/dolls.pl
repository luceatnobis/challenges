#!/usr/bin/perl -w
use strict;
use warnings;

&main();

sub main{
	my $test = `file doll`;
	my $mess = `file doll`;
	while($mess eq $test){
		`mv doll doll.gz`;
		`gunzip doll.gz`;
		$mess = `file doll`;
	}
}
