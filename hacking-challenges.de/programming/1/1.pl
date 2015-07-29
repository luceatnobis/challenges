#!/usr/bin/perl
use strict;

&main();

sub main{
	my ($zahl, $erg, $i, $x, $y) = (20, 0, 0, 0, 0);
	for($i=($zahl-10);$i<=$zahl+10;$i++){
		$erg+=$i;
		for($x=$i;$x<=$zahl+20;$x++){
			$erg+=$x;
			for($y=$x;$y<=$zahl+30;$y++){
				$erg+=$y;
			}
		}
	}
	print "$erg\n";
}
