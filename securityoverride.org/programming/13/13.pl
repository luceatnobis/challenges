#!/usr/bin/perl
use Image::Magick;
use WWW::Mechanize;
use warnings;
use strict;

&main();

sub main{
	my ($agent,$dump,$image,$solutionString) = (0,0,0,""); 
	my ($a,$b,$c,$d,$checkDigit) = (0,0,0,0,0);
	my (@values);
	my (%patterns);

	#reading in the patterns from the documentation
	open(PATTERNS,"<codes");
	foreach(<PATTERNS>){
		next if $_=~/#/;
		chomp;
		$_=~m/(.+):(.+)/;
		$patterns{$2} = $1;
	}
	close(PATTERNS);
	
	$image = Image::Magick->new;
	$agent = WWW::Mechanize->new;
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
	$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	$agent->click();
	$agent->get("http://securityoverride.org/challenges/programming/13/index.php");
	$agent->mirror("http://securityoverride.org/challenges/programming/13/img.php",'barcode.png');
	my $time1 = time;
	$image->Read('barcode.png');
	#long tedious reading process
	foreach my $x(0..94){
		my ($r,$g,$b) = $image->GetPixel(x=>$x,y=>0);
		$_ *= 255 for ($r,$g,$b);
		if($r+$g == 0 and $b == 255){ #blau
			$dump .= 'B';
		}elsif($r == 0 and 0<$g and 0<$b){ # türkis
			$dump .= 'T';
		}elsif($r+$g+$b == 765){ # weiss
			$dump .= '0';
		}elsif($r+$g+$b == 0){ #schwarz
			$dump .= '1';
		}
	}
	$dump = substr $dump, 1;
	foreach my $half(split("0B0B0",$dump)){
		$half=~s/^101|101$//;
		foreach(split(/(.{7})/,$half)){
			next if $_ eq "" or $_ eq "TTTTTTT";
			push(@values,$patterns{$_});
		}
	}
	foreach(0..$#values){
		if($_%2==0){
			$a += $values[$_];
		}else{
			$c += $values[$_];
		}
	}
  	$b = $a * 3;
	$d = $b + $c;
	until(($d+$checkDigit)%10 == 0){
		$checkDigit++;
	}
	$solutionString = "$d:$checkDigit";
	my $time2 = time;
	$agent->post("http://securityoverride.org/challenges/programming/13/index.php",{string=>$solutionString});
	print $solutionString."\n";
	print $time2-$time1."\n";
}
