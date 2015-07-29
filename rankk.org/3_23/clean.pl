#!/usr/bin/perl
use strict;
use warnings;

&main();

sub main{
	my(@oldFiles);

	@oldFiles = <txt/*>;
	open(ALL,">all");
	foreach my $fileName(@oldFiles){
		open(OLD,"<$fileName");
		foreach(<OLD>){
			$_=~s/\x0d\x0a//g;
			print ALL $_."\n";
		}
		close(OLD);
	}
}
