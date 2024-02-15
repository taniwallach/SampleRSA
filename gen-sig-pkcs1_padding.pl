#!/usr/bin/perl -w

use strict;
use warnings;

use File::Slurp;
use Crypt::OpenSSL::Random;
use Crypt::OpenSSL::RSA;
use MIME::Base64;

my $key_string = read_file('testing-public.key');

my $plaintext = time();

my $rsa_pub = Crypt::OpenSSL::RSA->new_public_key($key_string);

# use_pkcs1_padding
# use_pkcs1_oaep_padding
# use_sslv23_padding
# use_sha256_hash
# use_sha512_hash
# use_sha384_hash
#

#$rsa_pub->use_sslv23_padding(); # use_pkcs1_oaep_padding is the default

$rsa_pub->use_pkcs1_padding();

my $ciphertext = encode_base64($rsa_pub->encrypt($plaintext),'');

print "Timestamp being encrypted: $plaintext\nThe signature is below:\n";
print "$ciphertext \n\n";
exit
