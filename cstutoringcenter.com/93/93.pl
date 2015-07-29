#!usr/bin/perl
use strict;
use warnings;
use Math::BaseCalc;

&main();

sub main{
	my ($a, $b, $dist, $bigSum, $baseCalc);
	my ($aHex, $bHex);
	my (@a, @b);

	$baseCalc = new Math::BaseCalc(digits => 'hex');
	for $a (1..10000000){
		print "$a\n" if $a % 1000 == 0;
		$dist = 0;
		$b = $a - 1;
	
		$aHex = $baseCalc->to_base($a);
		$bHex = $baseCalc->to_base($b);

		$bHex = '0'.$bHex until(length($bHex)==length($aHex));
		@a = split("",$aHex);
		@b = split("",$bHex);

		foreach(0..$#a){
			if($a[$_] ne $b[$_]){
				$dist++;
			}
		}
		$bigSum += $dist;
	}
	print "$bigSum$/";
}
