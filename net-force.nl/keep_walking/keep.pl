#!/usr/bin/perl -w
use strict;

&main();

sub main{
	my($x,$y,$ans,$prevAns)=(1,1,1,1);
	until($x == 526){
		$ans = ($x * $y + $prevAns + 3);
		$prevAns = $ans;
		$x++;$y++;
	}
	print "$ans\n";
}
