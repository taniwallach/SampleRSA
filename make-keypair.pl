#!/usr/bin/perl -w

use strict;
use warnings;

use Crypt::OpenSSL::Random;
use Crypt::OpenSSL::RSA;

my $rsa_key = Crypt::OpenSSL::RSA->generate_key(3072);

open( KEYFILE, "> testing-public.key");
print KEYFILE $rsa_key->get_public_key_string();
close( KEYFILE );

open( KEYFILE, "> testing-private.key");
print KEYFILE $rsa_key->get_private_key_string();
close( KEYFILE );

