#!/usr/bin/perl -w
use strict;
use LWP::UserAgent;

my%stringTable=(
                "<html><body>\nback later" => 1
               );
&main();

sub main{
    my($agent,$content,$response);
    $agent=LWP::UserAgent->new();

    while(1){
        $response=$agent->get("http://www.hacker.org/challenge/misc/minuteman.php");
        $content=$response->content;
        #print $content."\n";       
        unless (exists $stringTable{$content}){
			open(DATEI,">solution");
            print $content."\n";
			print DATEI $content."\n";
			close(DATEI);
            system("date");
        }
        sleep(20);
    }
}

