#!/usr/bin/perl
use strict;
use warnings;

&main();

sub main{
	my ($fh);
	open($fh,"<file");
	my $string = <$fh>;
	$string=~s/[A-Z]//g;
	print length($string)."\n";
}
