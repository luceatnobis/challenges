#!/usr/bin/perl -w
use strict;
use warnings;

&main();

sub main{
	open(DATEI,"<list") or die "KEENE LISTE JUNG";
	my $pi = <DATEI>;
	close(DATEI);

	print index($pi,"12345678")."\n";
}
