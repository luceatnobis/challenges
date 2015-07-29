#!/usr/bin/perl
use warnings;
use strict;

&main();

sub main{
	my %words;
	open(DATEI,"<all");
	foreach(<DATEI>){
		while($_=~m/\b(\w+)\b/g){
			$words{length($1)} = $1;
		}
	}
	foreach(1..100){
		print $words{$_}."\n" if exists $words{$_};
	}
	close(DATEI);
}
