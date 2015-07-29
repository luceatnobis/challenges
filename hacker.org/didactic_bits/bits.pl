#!/usr/bin/perl
use Math::BaseCalc;
use strict;
use warnings;

&main();

sub main{
	
	my $base = new Math::BaseCalc(digits=>[0,1]);

	open(DATEI,"<string");
	chomp(my $string = <DATEI>);
	close(DATEI);

	$string=~s/a/0/g;
	$string=~s/b/1/g;

	foreach(split(/(.{8})/,$string)){
		next if $_ eq "";	
		print chr($base->from_base($_));
	}
	print "\n";
}
