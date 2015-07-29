#!/usr/bin/perl -w
use WWW::Mechanize;
use strict;

&main();

sub main{
	my ($agent,$content,$normalForm,$solutionString,$small,$big,$k1,$k2);
	my @factors;

	$agent = WWW::Mechanize->new();
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
	$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[19);
	$agent->click();
	
	$agent->get("http://securityoverride.org/challenges/programming/6/");
	$content = $agent->content;
	$content=~m/<code style='white-space:nowrap'>\x0A(.+?)\s+</;

	$normalForm = $1;
	$normalForm=~m#(\d+)x \+ (\d+)#g;
	($small,$big) = ($1,$2);
	@factors = &factors($big);

	foreach my $a (@factors){
		my $quit = 0;
		foreach my $b (@factors){
			if($a+$b==$small){
				($k1,$k2) = ($a,$b);
				$quit = 1;
			}
		}
		last if $quit==1;
	}
	$solutionString = "(x+$k1)(x+$k2)";
	$agent->form_name("submitform");
	$agent->set_fields(string=>$solutionString);
	$agent->click();
}
sub factors{
	die unless defined $_[0];
	my ($n) = @_;
	my @factors;
	
	foreach(1..$n/2){
		if($n%$_==0){
			push(@factors,$_);
		}
	}
	return @factors;
}
