#!/usr/bin/perl -w
use Math::BaseCalc;
use strict;

&main();

sub main{
	my $string = "90 dd 3b 21 5f 23 9a 63 3f a6 ae 3c 31 64 3f 60 2e ea 3f 72 51 cf fd f0 fe";
	my $base = new Math::BaseCalc(digits=>'hex');
	
	my $paddedKey = "";
	while(length($paddedKey)<length($string)){
		$paddedKey.="secret";
	}

	while($string=~/(\w+)/g){
		my $chr =  $base->from_base($1);	
	}

}
