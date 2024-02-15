Needed
	phpseclib

# =========================================================================

Run the following to get a signature:
	php -f gen-sig-pkcs1_padding.php

# =========================================================================

Sample output:
--------------

Timestamp being encrypted: 1708004257
The signature is below:
Ej+4qvyMJ/T1obLxTTT+/L72FQpcA37+tR41Nl7XUBQzuDJtzJtemgCItEit5+0h3KS7/OH042BO/oOuJuoAz8vS9rd1AWnFSbbxP67qMdw6yL+/1YSxlK7Oa/L3qfVW34b8s00amApfc5ecxdgnan3UyfqsVdm2mubC0vohQqjof/2xi4SQdHEa/RqMhVyrTKcGVSaMaeNF8lWhjJRDgKxYsixPQisyLLuBkEEq5yoDegnu8iOpLAxKdTcBMfKjBqojc6rOuXJyh8m62pqY6xdazwgBVsolbIZXkD3Y1hQuZREju2xk26UOYXA4n3ohAEw9JwMkJ5KohAtABcB6/Zsc+U2FN0XqEfGH3fj/ZPvLofUFFsu5jAA+uqd9+8asvhGSds4DZpbX4B0GnryTtm5oLMILjwuD3Kfw2GBooXoLmsjUtFtjCZqopSa6nFVYeVchIeGgAj7xWNKt3emFsxZykzacWtb3cabaJvRYDe3p4Ud4pP9yjvp/UXf3eXvF

# =========================================================================

Run the following to test a signature:
	php -f check-sig-pkcs1_padding.php "PUT-THE-SIG-TO-TEST-HERE"

Sample run:
-----------
	php -f check-sig-pkcs1_padding.php "Ej+4qvyMJ/T1obLxTTT+/L72FQpcA37+tR41Nl7XUBQzuDJtzJtemgCItEit5+0h3KS7/OH042BO/oOuJuoAz8vS9rd1AWnFSbbxP67qMdw6yL+/1YSxlK7Oa/L3qfVW34b8s00amApfc5ecxdgnan3UyfqsVdm2mubC0vohQqjof/2xi4SQdHEa/RqMhVyrTKcGVSaMaeNF8lWhjJRDgKxYsixPQisyLLuBkEEq5yoDegnu8iOpLAxKdTcBMfKjBqojc6rOuXJyh8m62pqY6xdazwgBVsolbIZXkD3Y1hQuZREju2xk26UOYXA4n3ohAEw9JwMkJ5KohAtABcB6/Zsc+U2FN0XqEfGH3fj/ZPvLofUFFsu5jAA+uqd9+8asvhGSds4DZpbX4B0GnryTtm5oLMILjwuD3Kfw2GBooXoLmsjUtFtjCZqopSa6nFVYeVchIeGgAj7xWNKt3emFsxZykzacWtb3cabaJvRYDe3p4Ud4pP9yjvp/UXf3eXvF"

Sample output:
--------------

The decrypted data is: 1708004257

# =========================================================================

Test the same signature with Perl:

	perl -f check-sig-pkcs1_padding.pl "Ej+4qvyMJ/T1obLxTTT+/L72FQpcA37+tR41Nl7XUBQzuDJtzJtemgCItEit5+0h3KS7/OH042BO/oOuJuoAz8vS9rd1AWnFSbbxP67qMdw6yL+/1YSxlK7Oa/L3qfVW34b8s00amApfc5ecxdgnan3UyfqsVdm2mubC0vohQqjof/2xi4SQdHEa/RqMhVyrTKcGVSaMaeNF8lWhjJRDgKxYsixPQisyLLuBkEEq5yoDegnu8iOpLAxKdTcBMfKjBqojc6rOuXJyh8m62pqY6xdazwgBVsolbIZXkD3Y1hQuZREju2xk26UOYXA4n3ohAEw9JwMkJ5KohAtABcB6/Zsc+U2FN0XqEfGH3fj/ZPvLofUFFsu5jAA+uqd9+8asvhGSds4DZpbX4B0GnryTtm5oLMILjwuD3Kfw2GBooXoLmsjUtFtjCZqopSa6nFVYeVchIeGgAj7xWNKt3emFsxZykzacWtb3cabaJvRYDe3p4Ud4pP9yjvp/UXf3eXvF"

Sample output:
--------------

The decrypted data is: 1708004257

# =========================================================================

Test the same signature with Python:

        python3 check-sig-pkcs1_padding.py "Ej+4qvyMJ/T1obLxTTT+/L72FQpcA37+tR41Nl7XUBQzuDJtzJtemgCItEit5+0h3KS7/OH042BO/oOuJuoAz8vS9rd1AWnFSbbxP67qMdw6yL+/1YSxlK7Oa/L3qfVW34b8s00amApfc5ecxdgnan3UyfqsVdm2mubC0vohQqjof/2xi4SQdHEa/RqMhVyrTKcGVSaMaeNF8lWhjJRDgKxYsixPQisyLLuBkEEq5yoDegnu8iOpLAxKdTcBMfKjBqojc6rOuXJyh8m62pqY6xdazwgBVsolbIZXkD3Y1hQuZREju2xk26UOYXA4n3ohAEw9JwMkJ5KohAtABcB6/Zsc+U2FN0XqEfGH3fj/ZPvLofUFFsu5jAA+uqd9+8asvhGSds4DZpbX4B0GnryTtm5oLMILjwuD3Kfw2GBooXoLmsjUtFtjCZqopSa6nFVYeVchIeGgAj7xWNKt3emFsxZykzacWtb3cabaJvRYDe3p4Ud4pP9yjvp/UXf3eXvF"

Sample output:
--------------

The decrypted data is: 1708004257

