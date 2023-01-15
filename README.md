# simple-gpg
A simple Crossplatform Commandline Program Developed Using Python3 to run GNU Privacy Guard Program in safest and easiest way for beginners.

<img src="(https://user-images.githubusercontent.com/82881725/212551553-f6d50b10-9b68-4444-82f5-70667fc48bba.png">
Note: To use this program on windows please download and install gpg4win from https://gpg4win.org/ and for mac install gpgtools from https://gpgtools.org/ 

Quick Installation
------------------

To Install from [PyPI](https://pypi.org/project/simple-gpg/):

Run the following commands in Linux terminal / Windows powershell / command prompt to install:-

```
pip install simple-gpg
```
Then simply type the following command to get started :- 

```
simple-gpg
```
To run the program by directly downloading from github refer [ Instructions](/Install.md) here.

## Quick Demo

Run simple-gpg on Repl.it from here:- .[![Run on Repl.it](https://repl.it/badge/github/plibither8/2048.cpp)](https://replit.com/@AnishM9/simple-gpg#.replit)

## Features:-

1) Hash Calculator: supports Sha3_256 and sha3_512 using hashlib rest all hash algorithms using gnupg.

<img src="https://user-images.githubusercontent.com/82881725/212551628-a53a45c6-dace-430e-814f-31d0949913ef.png">

2) Individual File Encryption and Decryption using various symmetric ciphers supported by gnupg.

<img src="https://user-images.githubusercontent.com/82881725/212551709-b68d2d65-144a-4799-a827-f6fa47bc2ee7.png">

3) Asymmetric Cryptography Manager to handle Asymmetric Cryptography using gnupg.

<img src="https://user-images.githubusercontent.com/82881725/212551762-60edb3dc-f4db-4edd-8fc0-b73d599072fd.png">

4) Bulk Encryption of individual files ( Each file is individually encrypted ) using AES 256 or with a OPENPGP public key available under Asymmetric Cryptography Manager.

<img src="https://user-images.githubusercontent.com/82881725/212551812-f3a2bb2a-8fea-42d2-898c-3b84b4292b43.png">

5) Some enhancements were made , the number of iterations for hashing encryption keys were made higher for better security for symmetric file encryption and bulk encryption of individual files using aes256.

## NOTE: Like all other software this project may have bugs, though care has been taken to avoid bugs.
This mini project was done during my college 1st year to learn basics of Python Programming.
