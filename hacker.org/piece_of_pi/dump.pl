#!/usr/bin/perl
use warnings;
use strict;

&main();

sub main{
	open(DATEI,"<pi");
	my @lines = <DATEI>; 
	close(DATEI);
	
	open(DUMP,">dump");
	foreach(@lines){
		$_=~s/[^\d]//g;
		print DUMP $_;
	}
}
