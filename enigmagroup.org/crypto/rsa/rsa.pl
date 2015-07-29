#!/usr/bin/perl -w
use strict;
use warnings;
use Math::BigFloat;
use Math::BaseCalc;

&main();

sub main{
	my($base,$d,$e,$m,$n,$p,$q,$dec);
	$base = new Math::BaseCalc(digits=>[0,1]);
	($n,$e,$d)=(25777,3,1);
	($p,$q)=&fac($n);
	$m=($p-1)*($q-1);

	until(($d*$e)%$m==1){
		$d++;
	}
	#print "p=$p:q=$q:m=$m:d=$d:e=$e\n";
	
	open(DATEI,"<numbers");
	foreach my $line(<DATEI>){
		chomp $line;
		my$plain=Math::BigInt->new($line)->bmodpow($d,$n);
		$dec .= chr($plain);
	}
	close(DATEI);
	my @lines;
	foreach(split(/(.{8})/,$dec)){
		next if $_ eq "";
		print $base->from_base($_)."\n";
		push(@lines,$_);
	}
}	

sub fac{
	my$n=$_[0];
	my$number=$n;
	my@factors;
	foreach my$factor(2..$n){
		last if $number==1;
		if($number%$factor==0) {
			$number/=$factor;
			push(@factors,$factor);
			redo;
		}
	}
	return @factors;
}
