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

	($frameBaseX,$frameBaseY) = (10,10); #Obere linke Ecke des ersten Buchstabens.

	open(DATEI,"<finish"); #Das Ding hier speichert eine Datei mit dem Zeilenformat Buchstabe:md5 in einem Hash
	foreach(<DATEI>){
		chomp;
		$_=~m/(.):(.+)/;
		$characters{$2} = $1;
	}
	close(DATEI);
	
	$image = Image::Magick->new();
	
	# login Kram, wenig wichtig für uns.

	#$agent = WWW::Mechanize->new();
	#$agent->get("http://securityoverride.org");
	#$agent->form_number(1);
	#$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	#$agent->click();
	#$agent->get("http://securityoverride.org/challenges/programming/11/index.php");
	#$agent->mirror("http://securityoverride.org/challenges/programming/11/php_captcha.php",'captcha.jpg');
	
	$image->Read('captcha.jpg');
	until(485<$frameBaseX){	# Schleife über X-Werte bis zum letzten Buchstaben...da waren die Buchstabenpositionen fix
		my ($characterHash) = (""); # Hierdrin werden Zeichen gespeichert, je nachdem ob ein relevanter Pixel erkannt wurde
		foreach my $advanceY(0..5){ # Läuft über die Höhe (6) jedes Buchstaben
			foreach my $advanceX(0..3){ # Läuft über die Breite (4)  jedes Buchstaben
				my ($readPixelX,$readPixelY) = ($frameBaseX+$advanceX,$frameBaseY+$advanceY); #berechnet x und y jedes Buchstaben
				my ($r,$g,$b) = $image->GetPixel(x=>$readPixelX,y=>$readPixelY); # Speichert "Werte" in r, g und b
				$_ *= 255 for ($r,$g,$b); # Wir rechnen * 255 für jeden "Wert" um RGB Werte zu kriegen
				my $pixelSum = ($r+$g+$b); # Wir nehmen die Summe der RGB Werte um zwischen Hintergrund und Buchstabe zu unterscheiden
				$pixelSum<610 ? $characterHash.=" " : $characterHash.='#'; # Je nachdem ob die über 610 (ein willkürlicher, aber funktionierender Wert) liegt wird ein " " oder ein "#" zum Buchstabenhash zugefügt
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
