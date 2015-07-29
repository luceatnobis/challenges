#!/usr/bin/perl -w
use Image::Magick;
use Digest::MD5 qw(md5 md5_hex md5_base64);
use WWW::Mechanize;
use warnings;
use strict;

&main();

sub main{

	my($agent,$image,$frameBaseX,$frameBaseY,$solutionString);
	my(%characters);

	($frameBaseX,$frameBaseY) = (10,10);

	open(DATEI,"<finish");
	foreach(<DATEI>){
		chomp;
		$_=~m/(.):(.+)/;
		$characters{$2} = $1;
	}
	close(DATEI);
	#
	$image = Image::Magick->new();
	$agent = WWW::Mechanize->new();
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
	$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	$agent->click();
	$agent->get("http://securityoverride.org/challenges/programming/11/index.php");
	$agent->mirror("http://securityoverride.org/challenges/programming/11/php_captcha.php",'captcha.jpg');
	
	$image->Read('captcha.jpg');
	until(485<$frameBaseX){
		my ($characterHash) = ("");
		foreach my $advanceY(0..5){
			foreach my $advanceX(0..3){
				my ($readPixelX,$readPixelY) = ($frameBaseX+$advanceX,$frameBaseY+$advanceY);
				my ($r,$g,$b) = $image->GetPixel(x=>$readPixelX,y=>$readPixelY);
				$_ *= 255 for ($r,$g,$b);
				my $pixelSum = ($r+$g+$b);
				$pixelSum<610 ? $characterHash.=" " : $characterHash.='#';
			}
		}
		$frameBaseX+=5;
		$characterHash = md5_hex($characterHash);
		$solutionString.=$characters{$characterHash};
	}
	print $solutionString."\n";
	#$agent->form_name("submitform");
	#$agent->post("http://securityoverride.org/challenges/programming/11/index.php",{'string'=>$solutionString});
	#print $agent->content."\n";
}
