#!/usr/bin/perl -w
use strict;

&main();

sub main{
	open(DATEI,"<lettered");
	my $string = <DATEI>;
	close(DATEI);

	my @numbers = $string=~/(\d+)/g;

	foreach(@numbers){
		print chr($_);
	}
	print "\n";
}
