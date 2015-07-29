#!/usr/bin/perl
use warnings;
use strict;

&main();

sub main{
	open my $fh, "<what" or die $!;
	chomp(my $content = <$fh>);
	close $fh;
	
	my @word=split("",$content);
	$_ = $_.length($content) for @word;	
	print join("",@word)."\n";
}
