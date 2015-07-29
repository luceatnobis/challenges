#!/usr/bin/perl -w
use WWW::Mechanize;
use HTTP::Cookies;
use Image::Magick;
use strict;
use warnings;

&main();

sub main{
	my ($agent,$image,$username,$password,$result);
	($username,$password) = ($ARGV[0], $ARGV[1]);	

	$agent = WWW::Mechanize->new;
	$image = Image::Magick->new;

	$agent->get('http://www.enigmagroup.org/');
	$agent->form_number(2); 
	$agent->set_fields('user'=>"$username",passwrd=>$password);
	$agent->click();
	$agent->get("http://www.enigmagroup.org/missions/programming/3/image.php");
	open(BILD,">picture.jpg");
	print BILD $agent->content;
	close(BILD);

	$image->Read("picture.jpg");
	my($r,$g,$b) = $image->GetPixel(x=>0,y=>0);
	$_ *= 255 for ($r,$g,$b);
	undef $image;

	$agent->post("http://www.enigmagroup.org/missions/programming/3/image.php",
				{color=>"$r;$g;$b",submit=>1});
	print $agent->content."\n";
}
