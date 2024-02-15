#!/usr/bin/perl -w

use strict;
use warnings;

use File::Slurp;
use Crypt::OpenSSL::RSA;
use MIME::Base64;


my $base64_ciphertext = shift;

my $ciphertext = decode_base64( $base64_ciphertext );

my $key_string = read_file('testing-private.key');

my $rsa_private = Crypt::OpenSSL::RSA->new_private_key($key_string);

$rsa_private->use_pkcs1_padding();

my $plaintext = $rsa_private->decrypt( $ciphertext );

print "The decrypted data is: $plaintext\n";

exit
