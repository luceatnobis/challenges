#!/usr/bin/perl
use Math::BigFloat;
use Math::Round;
use WWW::Mechanize;
use strict;
use warnings;

&main();

sub main{
	Math::BigFloat->precision(-10);
	
	my ($agent,$content);
	my ($A,$AB,$AC,$CD) = (0,0,0,0);
	my ($AS,$BD,$BS,$PBS,$PCD,$PA) = (0,0,0,0,0,0);
	#q^
	$agent = WWW::Mechanize->new;
	$agent->get("http://securityoverride.org");
	$agent->form_number(1);
	$agent->set_fields("user_name"=>$ARGV[0],"user_pass"=>$ARGV[1]);
	$agent->click();
	$agent->get("http://securityoverride.org/challenges/programming/8/index.php");
	$content = $agent->content;
	$content=~m#Radius of A = (.+?)<br />Length of AB = (.+?)<br />Length of CD = (.+)<br />#;
	($A,$AB,$AC,$CD) = ($1,$2,$1,$3);
	
	#Wir wenden einen Pythagoras an, um AS herauszufinden.
	#AC^2 = (CD/2)^2 + AS^2 | wir formen um nach AS^2
	#AC^2 - (CD/2)^2 = AS^2
	$PCD = Math::BigFloat->new($CD)->bdiv(2)->bpow(2);
	$PA = Math::BigFloat->new($A)->bpow(2);
	$AS = Math::BigFloat->new($PA)->bsub($PCD)->bsqrt();
	
	#AS ist nun, wie erwartet, der eine Teil von AB.
	#BS = AB - AS
	$BS = Math::BigFloat->new($AB)->bsub($AS);
	$PBS = Math::BigFloat->new($BS)->bpow(2);
	$BD = Math::BigFloat->new($CD)->bdiv(2)->bpow(2)->badd($PBS)->bsqrt();
	$BD = &stround($BD,3);
	$agent->post("http://securityoverride.org/challenges/programming/8/index.php",{string=>$BD});
}

sub stround
{
    my( $number, $decimals ) = @_;
    substr( $number + ( '0.' . '0' x $decimals . '5' ), 0, $decimals + length(int($number)) + 1 );
}
