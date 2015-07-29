#!/usr/bin/perl -w
use strict;

&main();

sub main{
	my $longest="";
	open(DATEI,"<pi1000000.txt");
	chomp(my $pi = <DATEI>);
	close(DATEI);
	
	my @sequences = split("9",$pi);
	foreach(@sequences){
		next if $_ eq "";
		if(length($longest)<length($_)){
			$longest = $_;
		}
	}
	print $longest."\n";
}
