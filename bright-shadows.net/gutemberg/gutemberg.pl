#!/usr/bin/perl
use warnings;
use strict;

my %freq;
open my $fh, "<gutemberg.txt" or die "Datei nicht gefunden";

foreach my $line (<$fh>){
	chomp $line;
	foreach(split("",$line)){
		$freq{$_}++;
	}
}
while(my($key,$value) = each(%freq)){
		print "$key, $value\n";
}
