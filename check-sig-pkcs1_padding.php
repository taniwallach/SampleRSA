<?php
require __DIR__ . '/vendor/autoload.php';

use phpseclib3\Crypt\PublicKeyLoader;
use phpseclib3\Crypt\RSA;

$key = PublicKeyLoader::load(file_get_contents('testing-private.key'), $password = false)->withPadding(RSA::ENCRYPTION_PKCS1 | RSA::SIGNATURE_PKCS1);

# echo "Padding:"  . $key->getPadding() . PHP_EOL;

$myinput = $argv[1];

# echo "$myinput" . PHP_EOL;

$ciphertext = base64_decode( $myinput );

# echo "$ciphertext" . PHP_EOL;

$plaintext = $key->decrypt($ciphertext);

echo "The decrypted data is: $plaintext" . PHP_EOL;

?>

