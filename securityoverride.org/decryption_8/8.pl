#!/usr/bin/perl -w
use MIME::Base64;
use strict;

&main();

sub main{

	my @xorKey = (76,73,70,72,84,66,85);
	my @text = split("","ABC");	

	my $string = "";
	my @vals;

	foreach(0..$#text){
		my $char = ord($text[$_]);
		my $xor = $xorKey[$_];
		push(@vals,$xor^$char);
	}
	$string = encode_base64(join('',@vals),"\n");
	print $string;
}
