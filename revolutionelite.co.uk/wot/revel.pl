#!/usr/bin/perl
use warnings;
use strict;
use WWW::Mechanize;
use MIME::Base64;

sub main{
	my ($base64String, $challUrl, $hash, $loginUrl, $username, $password, $mech, $response);
	my (%dict);
	($username, $password) = ($ARGV[0], $ARGV[1]);
	$loginUrl = "http://sabrefilms.co.uk/revolutionelite/login.php";
	$challUrl = "http://sabrefilms.co.uk/revolutionelite/broken-captcha.php";
	$mech = WWW::Mechanize->new();
	$mech->get($loginUrl);
	$mech->form_name("login");
	$mech->set_fields(username => $username, password => $password, submit => "login");
	$mech->click();

	open(my $fh, "<dict");
	foreach(<$fh>){
		chomp;
		$_=~m#(.+?):(.+)#;
		$dict{$2} = $1;
	}
	print "Read dict$/";
	
	$response = $mech->get($challUrl)->content;
	$response =~ m#<img src="casefiles/case15/(.+?)\.png#;
	$base64String = reverse($1);
	$hash = reverse(decode_base64($base64String));
	my $clearText = $dict{$hash};
	$mech->form_name("chall");
	$mech->set_fields(challengesol => $clearText, submit => "submit");
	$mech->click();
}

&main();
