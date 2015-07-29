#!/usr/bin/perl
use warnings;
use strict;

&main();

sub main{
	
	my(%names1, %names2);

	open my $names1, "<names1.txt" or die "Kann names1.txt nicht finden";
	open my $names2, "<names2.txt" or die "Kann names2.txt nicht finden";

	foreach(<$names1>){
		chomp;
		next if $_=~/\bname\b/;
		$_=~s/[^a-z]//g;
		next if length $_ == 0;
		$names1{$_} = 1;
	}
	foreach(<$names2>){
		chomp;
		next if $_=~/\bname\b/;
		$_=~s/[^a-z]//g;
		next if length $_ == 0;
		$names2{$_} = 1;
	}
	while(my($key, $value) = each(%names1)){
		print "$key => $value$/" if exists $names2{$key};
	}
}
