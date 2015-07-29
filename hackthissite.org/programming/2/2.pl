#!/usr/bin/perl
use Text::Morse;
use WWW::Mechanize;
use Image::Magick;
use warnings;
use strict;

&main();

sub main{
	my ($agent,$counter,$last,$image,$morse,$solutionString);
	($counter,$last) = (0,0);

	$morse = new Text::Morse;
	$image = Image::Magick->new;

	$agent = WWW::Mechanize->new;
	$agent->get("https://www.hackthissite.org");
	$agent->form_number(1);
	$agent->set_fields(username=>$ARGV[0],password=>$ARGV[1]);
	$agent->click();
	$agent->get("https://www.hackthissite.org/missions/prog/2/");
	$agent->mirror("https://www.hackthissite.org/missions/prog/2/PNG",'PNG.png');	

	$image->Read('PNG.png');

	foreach my $y(0..29){
		#print "New line\n";
		foreach my $x (0..99){
			my ($r,$g,$b) = $image->GetPixel(x=>$x,y=>$y);
			$_ *= 255 for ($r,$g,$b);
			if($r == 255){
				$solutionString .= chr($counter - $last);
				$last = $counter;
			}
			$counter++;
		}
	}
	$solutionString =  $morse->Decode($solutionString);
		
	$agent->post("https://www.hackthissite.org/missions/prog/2/index.php",{solution=>$solutionString});
	print $solutionString."\n";
}
