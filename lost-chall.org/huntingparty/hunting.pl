#!/usr/bin/perl
use strict;
use warnings;

&main();

sub main{
	my (%lines);	

	open my $hunting, "<huntingparty.txt" or die "Can't find file huntingparty.txt";
	
	foreach(<$hunting>){
		chomp;
		$lines{$_} = 1;
	}
	while(my($key, $value) = each(%lines)){
		print "$key => $value$/";
	}
}
