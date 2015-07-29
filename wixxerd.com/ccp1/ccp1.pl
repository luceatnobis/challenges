#!/usr/bin/perl
use warnings;
use strict;
use MIME::Base64;

&main();

sub main{
	open my $fh, "<data" or die "File not found";

	chomp(my $b64End = <$fh>);
	close($fh);

	my $decoded = decode_base64($b64End);
	print $decoded.$/;
}
