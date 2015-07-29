#!/usr/bin/perl
use strict;
use warnings;

&main();

sub main{
	my @vals = split("",'"><script>alert(1)</script><"');
	$_ = ord($_) for @vals;
	print join(",",@vals)."\n";
	
}
