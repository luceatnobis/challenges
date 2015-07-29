#!/usr/bin/perl
use Image::Magick;
use warnings;
use strict;

&main();

sub main{
	my $image = Image::Magick->new;
	$image->Read("greenline.png");

	foreach(0..85){
		my ($r,$g,$b) = $image->GetPixel(x=>$_,y=>0);
		$_ *= 255 for ($r,$g,$b);
		print chr($g);
	}
	print "\n";
}
