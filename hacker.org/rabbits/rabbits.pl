#!/usr/bin/perl
use strict;
use warnings;
use Math::BigInt;

&main();

sub main{
	print &fib(4)."\n";
}

sub fib{
	my($a,$b,$n,$sum);
	$n=$_[0];
	$a=Math::BigInt->new(0);
	$b=Math::BigInt->new(1);

	for (my$i=1;$i<=$n;$i++){
		$sum=Math::BigInt->new(Math::BigInt->new($a)->badd($b));
		$a=Math::BigInt->new($b);
		$b=Math::BigInt->new($sum);
	}
	return $b;
}
