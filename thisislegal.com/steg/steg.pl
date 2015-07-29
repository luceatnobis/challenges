#!/usr/bin/perl -w
use strict;

&main();

sub main{
	open(DATEI,"<text");
	my $line = <DATEI>;
	close(DATEI);

	$line=~s/[^A-Z]//g;
	print $line."\n";	
}
