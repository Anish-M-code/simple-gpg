# simple-gpg
A simple Crossplatform Commandline Program Developed Using Python3 to make GNU Privacy Guard Program easy to use for beginners.

<img src="https://github.com/Anish-M-code/simple-gpg/raw/master/screenshots/simplegpg.png">
Note: To use this program on windows please download and install gpg4win from https://gpg4win.org/ and for mac install gpgtools from https://gpgtools.org/ 

Quick Installation
------------------

To Install from [PyPI](https://pypi.org/project/simple-gpg/):

Run the following commands in Linux terminal / Windows powershell / command prompt to get started:-

```
pip install simple-gpg
```
Then :-

For Windows:
```
py -m simple_gpg
```
For Linux based Distributions:
```
python3 -m simple_gpg
```


## Features:-

1) Hash Calculator: supports Sha3_256 and sha3_512 using hashlib rest all hash algorithms using gnupg.

<img src="https://github.com/Anish-M-code/simple-gpg/raw/master/screenshots/hashcalc.png">

2) Individual File Encryption and Decryption using various symmetric ciphers supported by gnupg.

<img src="https://github.com/Anish-M-code/simple-gpg/raw/master/screenshots/symmetric%20encryption.png">

3) Asymmetric Cryptography Manager to handle Asymmetric Cryptography using gnupg.

<img src="https://github.com/Anish-M-code/simple-gpg/raw/master/screenshots/asymmetric%20encryption.png">

4) Bulk Encryption of individual files ( Each file is individually encrypted ) using AES 256 or with a OPENPGP public key available under Asymmetric Cryptography Manager.

<img src="https://github.com/Anish-M-code/simple-gpg/raw/master/screenshots/bulkencrypt.png">

5) Some enhancements were made , the number of iterations for hashing encryption keys were made higher for better security for symmetric file encryption and bulk encryption of individual files using aes256.

## NOTE: Like all other software this project may have bugs, though care has been taken to avoid bugs.
This mini project was done during my college 1st year to learn basics of Python Programming.
