#!/usr/bin/perl
use strict;
use warnings;

&main();

sub main{
	open my $art, "<art" or die "File not found.";
	foreach(split(/(.{100})/,<$art>)){
		next if $_ eq "";
		chomp $_;
		print $_."\n";
	}
}
