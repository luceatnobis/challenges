#!/usr/bin/perl
use Image::Magick;
use warnings;
use strict;

&main();

sub main{
	my $image = Image::Magick->new;
	$image->Read("blue.png");

	foreach my $y (0..12){
		foreach my $x (0..32){
			my ($r,$g,$b) = $image->GetPixel(x=>$x,y=>$y);
			$_ *= 255 for ($r,$g,$b);
			print chr($b);
		}
		print "\n";
	}
	print "\n";
}
