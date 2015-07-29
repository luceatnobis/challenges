#!/usr/bin/perl -w
use Math::BaseCalc;
use strict;

&main();

sub main{
	my $baseCalc = new Math::BaseCalc(digits=>[0,1]);
	open(LINE1,"<data1");
	open(LINE2,"<data2");

	chomp(my $line1 = <LINE1>);
	chomp(my $line2 = <LINE2>);

	close(LINE1);
	close(LINE2);

	$line1=~s/[^01]//g;
	$line2=~s/[^01]//g;
	my @line1 = split(/(.{8})/,$line1);
	my @line2 = split(/(.{8})/,$line2);;

	foreach(0..$#line1){
		next if $line1[$_] eq "";
		my ($decLine1,$decLine2) = ($baseCalc->from_base($line1[$_]),$baseCalc->from_base($line2[$_]));
		my $resChar = chr($decLine1^$decLine2);
		print $resChar;
	}
	print "\n";
}
