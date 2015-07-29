#!/usr/bin/perl
use strict;
use warnings;
use Digest::MD5;

sub main{
	my %sub = (yaq=>'a', 'xsw'=>'b', cde=>'c', vfr=>'d',bgt=>'e' ,nhz=>'f', mju=>'g',
			  ",ki"=>'h',".lo"=>'i',"-öp"=>'j','qay'=>'k',wsx=>'l',edc=>'m',
			  rfv=>'n',tgb=>'o',zhn=>'p',ujm=>'q','ik,'=>'r','ol.'=>'s','pö-'=>'t',
			  qwe=>'u',asd=>'v',yxc=>'w',rtz=>'x',fgh=>'y',vbn=>'z'
			  );
	my $md5 = Digest::MD5->new;
	open my $fh, "<4";
	my $string = <$fh>;
	while(my($key,$value) = each(%sub)){
		$string=~s/$key/$value/g;
	}
	print $string."\n";
	print Digest::MD5::md5_hex($string)."\n";
	close($fh);
}
&main();
