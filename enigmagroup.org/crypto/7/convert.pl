#!/usr/bin/perl
use Math::BaseCalc;
use strict;
use warnings;

&main();

sub main{
	my ($buffer,$base);
	my (@values);
	
	$base = new Math::BaseCalc(digits=>[0,1]);
	open(DATEI,"<numbers") or die "file not found";
	foreach(<DATEI>){
		chomp;
		$buffer.=(31-$_);
		push(@values,$buffer),$buffer="" if length($buffer)==8;
	}
	foreach(0,2,4,6,8,10){
		my $val1 = $base->from_base($values[$_]);
		my $val2 = $base->from_base($values[$_+1]);
		my $xor = $val1 ^ $val2;
	}
	print "\n";
}
