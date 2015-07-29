#!/usr/bin/perl
use warnings;
use strict;
use Image::Magick;

&main();

sub main{
	my ($image);

	$image = Image::Magick->new;
	$image->Read('note.png');

	foreach my $y(0..8){
		foreach my $x(0..47){
			my ($r, $g, $b) = $image->GetPixel(x => $x, y => $y);
			$_ *= 255 for ($r, $g, $b);
			$b == 21 ? print "0" : print "\e[1;31m1\e[0;30m"; 
			#print "x: $x, y: $y: r: $r, g: $g, b: $b\n" unless $b == 21;
		}
		print $/;
	}
}
