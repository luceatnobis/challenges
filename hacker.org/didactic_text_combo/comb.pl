#!/usr/bin/perl
use warnings;
use strict;

sub main{
	open my $fh, "<text" or die $!;
	foreach(<$fh>){
		$_=~s/[^A-Z]//g;
		print $_;
	}
	print "\n";
}
&main();
