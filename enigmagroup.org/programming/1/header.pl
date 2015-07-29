#!/usr/bin/perl -w
use WWW::Mechanize;
use HTTP::Cookies;
use strict;
use warnings;

&main();

sub main{
	my ($agent,$content,$cookie,$ip,$username,$password);
	
	$agent = WWW::Mechanize->new;
	$agent->get("http://ipchicken.com");
	$agent->content=~m/(\d+\.\d+\.\d+\.\d+)/;
	
	($ip,$username,$password) = ($1, $ARGV[0], $ARGV[1]);

	$agent->get('http://www.enigmagroup.org/');
        $agent->form_number(1); 
        $agent->form_name("frmLogin");
        $agent->set_fields('user'=>"$username",passwrd=>$password);
	$agent->click();
	$cookie = $agent->cookie_jar; #new cookie jar
	$cookie->set_cookie(0,"mission","yes","/missions/programming/1/","enigmagroup.org"); #set mission cookie
	$agent->cookie_jar($cookie); #feed agent with new cookies
	$agent->post("http://www.enigmagroup.org/missions/programming/1/",{ip=>$ip,username=>$username});
	print $agent->content."\n";
}
