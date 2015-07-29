#!/usr/bin/perl
use warnings;
use strict;

sub main{
	print &calc(50)."\n";;
}
sub calc{
	my $depth = @_;
	return 1 if $depth == 0;
	my $cc = &calc($depth - 1);
	return $cc + ($depth % 7) + (((($cc ^ $depth) % 4) == 0) ? 1 : 0);
}
&main();
