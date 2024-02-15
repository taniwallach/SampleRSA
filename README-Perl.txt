Needed
	File::Slurp
	Crypt::OpenSSL::RSA
	MIME::Base64

# =========================================================================

Run the following to get a signature:
	perl -f gen-sig-pkcs1_padding.pl

# =========================================================================

Sample output:
--------------

Timestamp being encrypted: 1708004067
The signature is below:
p4+Z2k8GaF5I7XgD8TjoaVq4iHNLN38bmM7NAN3qnGnCFt4evPvy2C/P7u2G4gLZHlCNMhWqi9p1hGiWvanzmxKP8mpBAWzt4so6bNGuW67BddzdZtWxfZPqznE5J4hd8cKadS/yKn/Hacvc96NYoRasuY9ehCzDWKLUOYWymhAV9EFgBIKSSTCA+eMQDQQu5yKxZnbT3smCCedKs2JNrqTDpCLxrN1p9+88cIRcnOIfKuT34siWEWspE4eeRo9mYfIw+0GFSxfXzIYJC4NNCiYiIUBkyEcXI2gaNpHdXwhc2xlh8xiL1RdWHGz/pcQroAo83TD1rBbglYYgBA1ab4me6Hozq+wlDJxlb/3UGYec5EdxnceYWZ3Zq0sky1W7ugLX9aGJXRzPqjXbj3aAx5Ff6iC0E8wWaUGjlj8zjyk3gtE1038sNmDiJi2TZt5ofX9FYskbi2xOED6g9zqXWdVFC/FnylCX6CR9FZDDj6XYOf5hrCu+3qIZLzyeZAUi 

# =========================================================================

Run the following to test a signature:
	perl -f check-sig-pkcs1_padding.pl "PUT-THE-SIG-TO-TEST-HERE"

Sample run:
-----------
	perl -f check-sig-pkcs1_padding.pl "p4+Z2k8GaF5I7XgD8TjoaVq4iHNLN38bmM7NAN3qnGnCFt4evPvy2C/P7u2G4gLZHlCNMhWqi9p1hGiWvanzmxKP8mpBAWzt4so6bNGuW67BddzdZtWxfZPqznE5J4hd8cKadS/yKn/Hacvc96NYoRasuY9ehCzDWKLUOYWymhAV9EFgBIKSSTCA+eMQDQQu5yKxZnbT3smCCedKs2JNrqTDpCLxrN1p9+88cIRcnOIfKuT34siWEWspE4eeRo9mYfIw+0GFSxfXzIYJC4NNCiYiIUBkyEcXI2gaNpHdXwhc2xlh8xiL1RdWHGz/pcQroAo83TD1rBbglYYgBA1ab4me6Hozq+wlDJxlb/3UGYec5EdxnceYWZ3Zq0sky1W7ugLX9aGJXRzPqjXbj3aAx5Ff6iC0E8wWaUGjlj8zjyk3gtE1038sNmDiJi2TZt5ofX9FYskbi2xOED6g9zqXWdVFC/FnylCX6CR9FZDDj6XYOf5hrCu+3qIZLzyeZAUi"

Sample output:
--------------

The decrypted data is: 1708004067

# =========================================================================

Test the same signature with PHP:

	php -f check-sig-pkcs1_padding.php "p4+Z2k8GaF5I7XgD8TjoaVq4iHNLN38bmM7NAN3qnGnCFt4evPvy2C/P7u2G4gLZHlCNMhWqi9p1hGiWvanzmxKP8mpBAWzt4so6bNGuW67BddzdZtWxfZPqznE5J4hd8cKadS/yKn/Hacvc96NYoRasuY9ehCzDWKLUOYWymhAV9EFgBIKSSTCA+eMQDQQu5yKxZnbT3smCCedKs2JNrqTDpCLxrN1p9+88cIRcnOIfKuT34siWEWspE4eeRo9mYfIw+0GFSxfXzIYJC4NNCiYiIUBkyEcXI2gaNpHdXwhc2xlh8xiL1RdWHGz/pcQroAo83TD1rBbglYYgBA1ab4me6Hozq+wlDJxlb/3UGYec5EdxnceYWZ3Zq0sky1W7ugLX9aGJXRzPqjXbj3aAx5Ff6iC0E8wWaUGjlj8zjyk3gtE1038sNmDiJi2TZt5ofX9FYskbi2xOED6g9zqXWdVFC/FnylCX6CR9FZDDj6XYOf5hrCu+3qIZLzyeZAUi"

Sample output:
--------------

The decrypted data is: 1708004067

# =========================================================================

Test the same signature with Python:

        python3 check-sig-pkcs1_padding.py "p4+Z2k8GaF5I7XgD8TjoaVq4iHNLN38bmM7NAN3qnGnCFt4evPvy2C/P7u2G4gLZHlCNMhWqi9p1hGiWvanzmxKP8mpBAWzt4so6bNGuW67BddzdZtWxfZPqznE5J4hd8cKadS/yKn/Hacvc96NYoRasuY9ehCzDWKLUOYWymhAV9EFgBIKSSTCA+eMQDQQu5yKxZnbT3smCCedKs2JNrqTDpCLxrN1p9+88cIRcnOIfKuT34siWEWspE4eeRo9mYfIw+0GFSxfXzIYJC4NNCiYiIUBkyEcXI2gaNpHdXwhc2xlh8xiL1RdWHGz/pcQroAo83TD1rBbglYYgBA1ab4me6Hozq+wlDJxlb/3UGYec5EdxnceYWZ3Zq0sky1W7ugLX9aGJXRzPqjXbj3aAx5Ff6iC0E8wWaUGjlj8zjyk3gtE1038sNmDiJi2TZt5ofX9FYskbi2xOED6g9zqXWdVFC/FnylCX6CR9FZDDj6XYOf5hrCu+3qIZLzyeZAUi"

Sample output:
--------------

The decrypted data is: 1708004067

