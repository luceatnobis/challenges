#!/usr/bin/perl -w
use strict;

&main();

sub main{
	my $text = 'Rwfwcvttw ufriifyg dws jjbhwooqm ezu iwsh';
	$text=~s/ //g;
	my $xorKey = 'enc';

	$xorKey .= 'enc' until(length($text) <= length($xorKey));

	my @splitKey = split("",$xorKey);
	my @splitText = split("",$text);

	foreach(0..$#splitText){
		my $xor1 = ord($splitText[$_]);
		my $xor2 = ord($splitKey[$_]);
		my $result = chr($xor1 | $xor2);
		print "$result";
	}
	print "\n";
}
