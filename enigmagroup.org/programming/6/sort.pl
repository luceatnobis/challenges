#!/usr/bin/perl
use warnings;
use strict;

&main();

sub main{
	open(DATEI,"<keywords") or die "file not found";
	open(SORTED,">sorted");
	foreach(<DATEI>){
		chomp;
		my $sorted = join('',sort split("",$_));
		$sorted=~s/\s//g;
		print SORTED "$_:$sorted\n";
	}
	close(SORTED);
	close(DATEI);
}
