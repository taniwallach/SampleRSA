<?php

require __DIR__ . '/vendor/autoload.php';

use phpseclib3\Crypt\PublicKeyLoader;
use phpseclib3\Crypt\RSA;

$key = PublicKeyLoader::load(file_get_contents('testing-public.key'), $password = false)->withPadding(RSA::ENCRYPTION_PKCS1 | RSA::SIGNATURE_PKCS1);

# echo "Padding:"  . $key->getPadding() . PHP_EOL;

# echo "$key" . PHP_EOL;

$mytime = time();

echo "Timestamp being encrypted: $mytime" . PHP_EOL;

$sig1 = $key->encrypt( $mytime );

#echo "$sig1" . PHP_EOL;
$sig2 = base64_encode( $sig1 );

echo "The signature is below:" . PHP_EOL;

echo "$sig2" . PHP_EOL;

?>

