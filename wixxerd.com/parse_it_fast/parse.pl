#!/usr/bin/perl
use strict;
use warnings;
use WWW::Mechanize;

&main();

sub main{
	my ($agent,$cftoken,$cfid,$cookieRaw,$content,$headers,$username,$password,$adminFlag);

	$agent = WWW::Mechanize->new;
	
	$agent->get("http://www.wixxerd.com/challenges/coding/chal70.cfm");
	$cookieRaw = $agent->response()->header('Set-Cookie');
	$cookieRaw=~/CFID=(.+?);.+CFTOKEN=(.+?);/;
	($cfid, $cftoken) = ($1, $2);
	
	$content = $agent->content;
	$content=~s/\s//g;

	while($content=~m#<f.+?>(.+?)</.+?><.+?>(.+?)</.+?><.+?>(.+?)</.+?>#g){
		($username, $password, $adminFlag) = ($1,$2,$3);
		last if($adminFlag eq "true");
	}
	my $ansUrl = "http://wixxerd.com/challenges/coding/chal70.cfm?
		person=$username&
		password=$password&
		cfid=$cfid&
		cftoken=$cftoken
	";
	$ansUrl=~s/\s//g;
	print $agent->get($ansUrl)->content;
}
