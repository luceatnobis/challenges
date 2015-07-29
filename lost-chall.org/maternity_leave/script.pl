#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Cookies;

&main();

sub main{
	my ($agent, $content, $username, $password, $response, $result);
	($username, $password) = ($ARGV[0], $ARGV[1]);
	

	$agent = LWP::UserAgent->new;
	$agent->cookie_jar(new HTTP::Cookies);
	
	$agent->post("http://lost-chall.org/login.php",{
		username => $username,
		password => $password,
		remember => 'on',
		submit 	 => 'Submit'
	});
	$response = $agent->get("http://www.lost-chall.org/maternity-leave.php");
	$content = $response->content;
        print $content;
	$content=~m#<p class="Stil1">(.+?)	  </p>#;
	$result = eval($1);
	$agent->post("http://www.lost-chall.org/maternity-leave.php",{
		solution => $result,
		submit => 'Submit'
	});
}
