#!/usr/bin/perl
use WWW::Mechanize;

use warnings;
use strict;

&main();

sub main{
	my ($agent,$content,$solutionString);
	my (@words);
	my (%values);

	open(SORTED,"<sorted");
	foreach(<SORTED>){
		chomp;
		$_=~m#(.+?):(.+)#;
		$values{$2}=$1;
	}
	close(SORTED);	

	$agent = WWW::Mechanize->new;
	$agent->get("http://www.hackthissite.org");
	$agent->form_number(1);
	$agent->set_fields(username=>$ARGV[0],password=>$ARGV[1]);
	$agent->click();
	$agent->get("https://www.hackthissite.org/missions/programming/");
	$content = $agent->get("http://www.hackthissite.org/missions/prog/1/")->content;
	print $content."\n";
	while($content=~m#<td><li>(.+?)</li></td> </tr>#g){
		push(@words,$values{join("",sort(split("",$1)))});
	}
	$solutionString = join(",",@words);
	$agent->form_name("submitform");
	$agent->set_fields("solution"=>$solutionString);
	$agent->click();
	print $solutionString."\n";
}
