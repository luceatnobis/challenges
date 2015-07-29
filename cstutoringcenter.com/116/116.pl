#!/usr/bin/perl
use strict;
use warnings;

my %pages;

&main();

sub main{
	
	my $bigSum = 0;

	&setPages(100,150);
	&setPages(25,28);
	&setPages(8,14);
	&setPages(113,120);
	&setPages(1);
	&setPages(8,81);
	&setPages(47,48);
	&setPages(99,109);
	&setPages(149,102);
	&setPages(66,34);
	&setPages(5);
	&setPages(123,125);
	&setPages(80,87);

	foreach(1..200){
		next unless exists $pages{$_};
		$bigSum++;
	}
	print $bigSum.$/;
}

sub setPages{
	if(@_ == 1){
		$pages{$_[0]} = 1;
	}else{
		my ($low, $high) = @_;
		return unless $low<$high;
		foreach($low..$high){
			$pages{$_} = 1;
		}
	}
}
