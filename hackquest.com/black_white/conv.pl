#!/usr/bin/perl -w
use Math::BaseCalc;
use strict;

&main();

sub main{
	my $base = new Math::BaseCalc(digits=>[0,1]);;
	open(DATEI,"<collection") or die "file not found";
	foreach(<DATEI>){
		chomp;
		print chr($base->from_base($_));	
	}
	print "\n";
}
