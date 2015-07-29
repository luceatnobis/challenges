#!/usr/bin/perl -w
use strict;


&main();

sub main{
	my (%hash);

	open(TABLE,"<table");
	foreach(<TABLE>){
		chomp;
		$_=~m#(\d+):(.)#;
		$hash{$1}=$2;
	}
	close(TABLE);
	open(HASH,"<numbers");
	foreach(<HASH>){
		chomp;
		print $hash{$_};
	}
	print "\n";
}
