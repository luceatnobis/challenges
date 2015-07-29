#!/usr/bin/perl -w
use Date::Calc qw(:all);
use WWW::Mechanize;
use strict;

&main();

sub main{
	my ($agent,$content,$solutionString);
	my (@days);
	my %nrToDay = (1=>"Monday",2=>"Tuesday",3=>"Wednesday",4=>"Thursday",5=>"Friday",6=>"Saturday",7=>"Sunday");
	my %nrToMon = ("January"=>1,"Febuary"=>2,"March"=>3,"April"=>4,"May"=>5,"June"=>6,"July"=>7,"August"=>8,
				   "September"=>9,"October"=>10,"November"=>11,"December"=>12);
	
	$agent = WWW::Mechanize->new();
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
	$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	$agent->click();
	
	$agent->get("http://securityoverride.org/challenges/programming/9/");
	$content = $agent->content;
	$content=~m#<code style='white-space:nowrap'>\s+(.+?)<#;
	my @dates = split(/;\s?/,$1);
	foreach(@dates){
		$_=~m/(.+?) (\d+?), (\d+)/;
		my ($month, $day, $year) = ($1,$2,$3);
		push(@days,$nrToDay{Day_of_Week($year,$nrToMon{$month},$day)});
	}
	foreach(@days){
		print $_."\n";
	}
	$solutionString = join("; ",@days);
	$agent->form_name("submitform");
	$agent->set_fields(string=>$solutionString);
	$agent->click();
}
