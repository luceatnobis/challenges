#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Cookies;
use Digest::MD5;

&main();

sub main{
	my ($agent, $content, $md5, $digest, $username, $password, $response);
	($username, $password) = ($ARGV[0], $ARGV[1]);
	

	$md5 = Digest::MD5->new;
	$agent = LWP::UserAgent->new;
	$agent->cookie_jar(new HTTP::Cookies);
	
	$agent->post("http://lost-chall.org/login.php",{
		username => $username,
		password => $password,
		remember => 'on',
		submit 	 => 'Submit'
	});
	foreach(1..10000){
		$response = $agent->get("http://www.lost-chall.org/jscripts/$_.js");
		$content = $response->content;
		$digest = $md5->md5_hex($content);
		print "$_ => $digest\n";
	}
}
