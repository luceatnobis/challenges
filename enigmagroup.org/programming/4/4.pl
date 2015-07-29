#!/usr/bin/perl
use Image::Magick;
use Math::BaseCalc;
use WWW::Mechanize;
use strict;
use warnings;

&main();

sub main{

	my ($agent,$content,$result,$username,$password,$base,$image,$buffer,$maxX,$maxY,$bytes);
	my @bytes;
	
    $agent = WWW::Mechanize->new;
	$image = Image::Magick->new;
	$base = new Math::BaseCalc(digits=>[0,1]);

    ($username,$password) = ($ARGV[0], $ARGV[1]);
    $agent->get('http://www.enigmagroup.org/');
    $agent->form_number(2);
    $agent->set_fields('user'=>"$username",passwrd=>$password);
    $agent->click();
	$agent->get("http://www.enigmagroup.org/missions/programming/4/image.php");
	$content = $agent->content;

	open(PIC,">s.png");
	print PIC $content;
	close(PIC);

	$image->Read('s.png');
	($maxX,$maxY) = ($image->Get('width'),$image->Get('height'));

	foreach my $y(0..$maxY-1){
		foreach my $x(0..$maxX-1){
			my ($r,$g,$b) = $image->GetPixel(x=>$x,y=>$y);
			$_ *= 255 for ($r,$g,$b);
			if($r+$g+$b==0){
				$buffer.="1";
			}else{
				$buffer.="0";
			}
			if (length($buffer)==8){
				push(@bytes,$buffer);
				$buffer = "";
			}
		}
	}
	foreach(@bytes){
		$buffer.=chr($base->from_base($_));
	}
	$buffer=~m/:(.+)/;
	$result = $1;
	$agent->add_header(Referer=>"http://www.enigmagroup.org/missions/programming/4/index.php");
	$agent->post("http://www.enigmagroup.org/missions/programming/4/image.php",{answer=>$result});
	print $agent->content."\n";
}
