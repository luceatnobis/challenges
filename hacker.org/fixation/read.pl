#!/usr/bin/perl
use Image::Magick;
use warnings;
use strict;

&main();

sub main{
	my $image = Image::Magick->new;
	$image->Read("thirdframe.gif");

	foreach my $x (0..200){
		foreach my $y (0..140){
			my ($r,$g,$b) = $image->GetPixel(x=>$x,y=>$y);
			$_ *= 255 for ($r,$g,$b);
			print "$r:$g:$b\n";
		}
	}
}
