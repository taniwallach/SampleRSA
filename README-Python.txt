Needed
	pip install pycryptodome

# =========================================================================

Run the following to get a signature:
	python3 gen-sig-pkcs1_padding.py

# =========================================================================

Sample output:
--------------

Timestamp being encrypted: 1708003923
The signature is below:
oy48m047bVZ1TMwMKn2bFvtRUoXErJvcLbQu741Ht1MhROT0qnGcA6JphMCzSru278l/VjQrJjDJf6riGNZa6pXxKu94bxamk0T9WOR+5ko6moxu9qtZdKg2LsBQ1KbHApOHAe3HD75jDP99809p5f0qKk4ZEvadefnc1qQ4h5xD+4tfZswH4mdWRo/MI+TcY0G8JHrAGOjGR9TwglGmU0i0MLWOLVqe5O/k4U1p02rTfrkq+OIZ/X/MSnb7VjC4vZx6Cu3ldgwMjIbhpgpaI8OVdm5y1i75/B6j5XDyjjBp3l6fD3WRVA1gNU9FX2VBTYuRgqNtcUuARFFz18loTt+jN7GgpPbIfqwPDE0DH/4RkKcfmsWvCe7/DHrwryZxozZLv9SdSUcPErVQTdjF5KNHktGhYub+DafidJCob+GjvdRmkNyx/L+3/qXYB+PZteT8xoYj90N3ihRN/vO3sPnlHzvXh/f7VVVhzPY0p83+4KZ+Qo3JpJeBclMIQhQx

# =========================================================================

Run the following to test a signature:
        python3 check-sig-pkcs1_padding.py "PUT-THE-SIG-TO-TEST-HERE"

Sample run:
-----------
        python3 check-sig-pkcs1_padding.py "oy48m047bVZ1TMwMKn2bFvtRUoXErJvcLbQu741Ht1MhROT0qnGcA6JphMCzSru278l/VjQrJjDJf6riGNZa6pXxKu94bxamk0T9WOR+5ko6moxu9qtZdKg2LsBQ1KbHApOHAe3HD75jDP99809p5f0qKk4ZEvadefnc1qQ4h5xD+4tfZswH4mdWRo/MI+TcY0G8JHrAGOjGR9TwglGmU0i0MLWOLVqe5O/k4U1p02rTfrkq+OIZ/X/MSnb7VjC4vZx6Cu3ldgwMjIbhpgpaI8OVdm5y1i75/B6j5XDyjjBp3l6fD3WRVA1gNU9FX2VBTYuRgqNtcUuARFFz18loTt+jN7GgpPbIfqwPDE0DH/4RkKcfmsWvCe7/DHrwryZxozZLv9SdSUcPErVQTdjF5KNHktGhYub+DafidJCob+GjvdRmkNyx/L+3/qXYB+PZteT8xoYj90N3ihRN/vO3sPnlHzvXh/f7VVVhzPY0p83+4KZ+Qo3JpJeBclMIQhQx"

Sample output:
--------------

The decrypted data is: 1708003923

# =========================================================================

Test the same signature with PHP:

	php -f ./check-sig-pkcs1_padding.php "oy48m047bVZ1TMwMKn2bFvtRUoXErJvcLbQu741Ht1MhROT0qnGcA6JphMCzSru278l/VjQrJjDJf6riGNZa6pXxKu94bxamk0T9WOR+5ko6moxu9qtZdKg2LsBQ1KbHApOHAe3HD75jDP99809p5f0qKk4ZEvadefnc1qQ4h5xD+4tfZswH4mdWRo/MI+TcY0G8JHrAGOjGR9TwglGmU0i0MLWOLVqe5O/k4U1p02rTfrkq+OIZ/X/MSnb7VjC4vZx6Cu3ldgwMjIbhpgpaI8OVdm5y1i75/B6j5XDyjjBp3l6fD3WRVA1gNU9FX2VBTYuRgqNtcUuARFFz18loTt+jN7GgpPbIfqwPDE0DH/4RkKcfmsWvCe7/DHrwryZxozZLv9SdSUcPErVQTdjF5KNHktGhYub+DafidJCob+GjvdRmkNyx/L+3/qXYB+PZteT8xoYj90N3ihRN/vO3sPnlHzvXh/f7VVVhzPY0p83+4KZ+Qo3JpJeBclMIQhQx"

Sample output:
--------------

The decrypted data is: 1708003923

# =========================================================================

Test the same signature with Perl:

	php -f ./check-sig-pkcs1_padding.php "oy48m047bVZ1TMwMKn2bFvtRUoXErJvcLbQu741Ht1MhROT0qnGcA6JphMCzSru278l/VjQrJjDJf6riGNZa6pXxKu94bxamk0T9WOR+5ko6moxu9qtZdKg2LsBQ1KbHApOHAe3HD75jDP99809p5f0qKk4ZEvadefnc1qQ4h5xD+4tfZswH4mdWRo/MI+TcY0G8JHrAGOjGR9TwglGmU0i0MLWOLVqe5O/k4U1p02rTfrkq+OIZ/X/MSnb7VjC4vZx6Cu3ldgwMjIbhpgpaI8OVdm5y1i75/B6j5XDyjjBp3l6fD3WRVA1gNU9FX2VBTYuRgqNtcUuARFFz18loTt+jN7GgpPbIfqwPDE0DH/4RkKcfmsWvCe7/DHrwryZxozZLv9SdSUcPErVQTdjF5KNHktGhYub+DafidJCob+GjvdRmkNyx/L+3/qXYB+PZteT8xoYj90N3ihRN/vO3sPnlHzvXh/f7VVVhzPY0p83+4KZ+Qo3JpJeBclMIQhQx"

Sample output:
--------------

The decrypted data is: 1708003923

