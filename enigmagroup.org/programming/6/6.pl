#!/usr/bin/perl -w
use WWW::Mechanize;
use strict;
use warnings;

&main();

sub main{
	my ($agent,$username,$password,$result);
	my (@clear,%values);

	$agent = WWW::Mechanize->new;
	($username,$password) = ($ARGV[0], $ARGV[1]);	

	open(SORTED,"<sorted");
	foreach(<SORTED>){
		chomp;
		$_=~m#(.+?):(.+)#;
		$values{$2}=$1;	
	}
	close(SORTED);
	$agent->get('http://www.enigmagroup.org/');
	$agent->form_number(2); 
	$agent->set_fields('user'=>"$username",passwrd=>$password);
	$agent->click();
	$agent->get("http://www.enigmagroup.org/missions/programming/6/index.php");
	$agent->content=~m#<p class="style7">\x0A(.+?)\x0A</p#s;
	
	foreach(split("<br />\n",$1)){
		$_ =~ s# |<br />##g;
		my $sorted = join('',sort(split("",$_)));
		push(@clear,$values{$sorted});
	}
	$result = join(',',@clear);
	$agent->post("http://www.enigmagroup.org/missions/programming/6/submit.php",{anagram=>$result,submit=>"true"});
	print $agent->content."\n";
}
