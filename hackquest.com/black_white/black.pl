#!/usr/bin/perl -w
use strict;

&main();

sub main{
	open(DATEI,"1234.php") or die "file not found";
	foreach(<DATEI>){
		chomp;
		$_=~s/\x09/1/g;
		$_=~s/\x20/0/g;
		print $_."\n";
	}	
}
