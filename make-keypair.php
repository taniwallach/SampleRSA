<?php

require __DIR__ . '/vendor/autoload.php';

use phpseclib3\Crypt\PublicKeyLoader;
use phpseclib3\Crypt\RSA;

$private = RSA::createKey(3072);

$public = $private->getPublicKey();

#echo $public->toString('PKCS1') . PHP_EOL;
#echo $private->toString('PKCS1') . PHP_EOL;

file_put_contents('testing-private.key',$private->toString('PKCS1') . "\n");

file_put_contents('testing-public.key',$public->toString('PKCS1') . "\n");

?>

