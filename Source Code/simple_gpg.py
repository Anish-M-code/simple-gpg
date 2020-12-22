# flag=imp
# [THIS IS A STABLE RELEASE]
# [ VERSION 8.1 ]

# Simple_Gpg
# Copyright (C) 2018-2020 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

''' 
This project was developed by M.Anish as way to learn python3 programming during 1st semester and has improved it ever since. 
Though care has been taken to avoid bugs, bugs may exist.

'''

import os
import hashlib
import platform
import sys

#Function to remove a file if it exists.
def r(f):
   if os.path.exists(f):
      os.remove(f)

#Function to detect if required tools/package is present on local host or not.
def detect(cmd,web,snam,pkg):
    
        if platform.system().lower()=='windows':
              os.system('cls')
              if os.system(cmd+'>chk')!=0:
                print('\nPlease wait opening '+snam +' website in your browser!\nYou Have to download and install it.\n')
                os.system(' start '+web)
                
        else:
         if os.system(cmd+'>chk')!=0:    
           print('\nError:'+pkg+' is not installed in default directory in your device!')
           x=input('\nPress any key to exit...')
           r('chk')
           sys.exit()
        r('chk')

#Function to Detect gpg tool on local host. 
def gpg():
   detect('gpg --version','https://gpg4win.org','gpg4win','Gnupg')

#Throw error if no output file is generated when output file is expected after an operation involving Asymmetric Cryptography.
def serr(file):
    chkfl(file,'o')
    with open(file,'r') as f:
      f.seek(0,2)
      if f.tell()==0:
          print('\nYou may not have appropriate administrative access\n or There are no OPENPGP keys to display!\n')
          print('\n<-----Task Ended----->\n')
          x=input('\nPress to continue...')
          f.close()
          os.remove(file)
          main()
          sys.exit()

      f.seek(0)

 #Throw error if no output file is generated when output file is expected after an operation.       
def err(file):
    chkfl(file,'o')
    with open(file,'r') as f:
      f.seek(0,2)
      if f.tell()==0:
          print('\nYou may have given incorrect input!\n')
          print('\n<-----Task Failed!----->\n')
          f.close()
          os.remove(file)
          main()
          sys.exit()

      f.seek(0)
    
#Function to pause the program.
def pause():
    s=input('\nPress any key to continue...\n')
    main()

 #Function to check if a file exists or not and throw errors according to use case.   
def chkfl(file,p):
    if os.path.isfile(file)==False:
        if p.lower()=='i':
            print('\nERROR: FILE NOT FOUND!\n')
            pause()
        else:
            print('\nIncorrect Input or Output error!\n')
 
#Function to notify user that task has started. 
def start():
    print('\n<-----Task Started----->\n')

#Function to notify user that task has ended.    
def end():
    print('\n<-----Task Completed----->\n')

#Function to Catch errors before passing input to process()
def cmd():
    while 1:
     try:
      z=input('\nEnter command:')
      break
     except KeyboardInterrupt:
      print('Key Board Interrupt Error!')
      pause()
      sys.exit()
     except EOFError:
      print('Unknown Error!')
      pause()
      sys.exit()
    process(z)
    
#Alias for start()   
def tsks():
    start()
    
#Alias for end()
def tske():
    end()

#Function to notify user that given task failed.
def tskf():
    print('\n<-----Task Failed !----->\n')
    
#Function which generates hash outputs using gpg and hashlib for files given as input.   
def hashcall():
  print()
  
  #Function to generate hashes of files using gpg.
  def output(feed,algo):
      start()
      os.system('gpg --print-md '+algo+' '+feed)
      os.system('gpg --print-md '+algo+' '+feed+'>'+algo+'.txt')
      err(algo+'.txt')
      end()
      hcmd()
          
   #Function to compute sha3 hashes of files using hashlib. 
  def sha3(file,txt):
      start()
      if platform.python_version().lower()<'3.6.0':
        print('\nSorry, This function will not work for this platform!\n')
        tskf()
        pause()
      limit=1024
      if txt=='256':
        v=hashlib.sha3_256()
      else:
        v=hashlib.sha3_512()
      with open(file,'rb+') as f:
          buff=f.read(limit)
          v.update(buff)
          while len(buff)>0:
              buff=f.read(limit)
              v.update(buff)
      d=str(v.hexdigest())
      print(d)
      if txt=='256':
        with open(file+'_sha3_256.txt','w') as k:
            k.write(d)
        err(file+'_sha3_256.txt')
      else:
        with open(file+'_sha3_512.txt','w') as k:
            k.write(d)
        err(file+'_sha3_512.txt')
      end()
      hcmd()

  #Menu to select Hash Algorithms.
  def choice():
      print('\nFollowing Hash Algorithms are supported:-')
      print('1)md4\n2)md5\n3)Ripemd160\n4)SHA1\n5)SHA224\n6)SHA256\n7)SHA384\n8)SHA512\n9)SHA3_256\n10)SHA3_512\n')
      print('\nSHA2 and SHA3 are considered secure,rest insecure!\n')
      hcmd()
  
  #Function which loads appropriate function based on User Selection of Supported hashes.  
  def hcmd():
      while 1:
       try:
         x=input('\nEnter command:')
         break
       except KeyboardInterrupt:
          print('Keyboard Interrupt Error!')
          pause()
          
       except EOFError:
          print('Unknown Error!')
          pause()
          
      if x=='1':
          output(file,'md4')
      elif x=='2':
          output(file,'md5')
      elif x=='3':
          output(file,'ripemd160')
      elif x=='4':
          output(file,'sha1')
      elif x=='5':
          output(file,'sha224')
      elif x=='6':
          output(file,'sha256')
      elif x=='7':
          output(file,'sha384')
      elif x=='8':
          output(file,'sha512')
      elif x=='9':
          sha3(file,'256')
      elif x=='10':
          sha3(file,'512')
      elif x=='mm':
          main()
      elif x=='sm':
          hashcall()
      elif x.lower()=='c' or x.lower()=='close':
          sys.exit()
      else:
            print('Incorrect choice, Enter choice which is a number in\n1,2,3,4,5,6')
            i=input('\nPress any key to continue')
            choice()

  print('-----Hash-Calculator-----')
  
  file=input('\nEnter FileName:')
  chkfl(file,'i')
  f=open(file,'rb+')
  choice()

#Function which deals with Symmetric Cryptography in FNv8.
def ciphercall():
    print()
    
    #Function for encrypting files with given cipher.
    def output(file,algo):
        start()
        out=input('\nEnter Output FileName:')
        if out=='':
            out=file+'.gpg'
        print('\nChoose Hash Algorithm:\n1)default(recommended)\n2)sha256\n3)sha512')
        x=input('\nEnter Hash algorithm:')
        if x.lower()=='sha256' or x=='2':
            digest='--s2k-digest-algo sha256 '
        elif x.lower()=='sha512' or x=='3':
            digest='--s2k-digest-algo sha512 '
        else:
            digest=''
        os.system('gpg -o '+out+' --s2k-mode 3 --s2k-count 65000000 '+digest+'--cipher-algo '+algo+' -c '+file)
        end()
        main()

    #Function to select supported ciphers.
    def choice():
        print('\nFollowing Symmetric Encryption Algorithms are supported:-')
        print('\n1)IDEA\n2)3DES\n3)CAST5\n4)BLOWFISH\n5)AES128\n6)AES192\n7)AES256\n8)TWOFISH\n9)CAMELLIA128\n10)CAMELLIA192\n11)CAMELLIA256\n')
        ecmd()
        
    #Function to load appropriate functions based on user selection to encrypt files.    
    def ecmd():
        x=input('\nEnter choice:')
        if x=='1':
            output(file,'idea')
        elif x=='2':
            output(file,'3des')
        elif x=='3':
            output(file,'cast5')
        elif x=='4':
            output(file,'blowfish')
        elif x=='5':
            output(file,'aes')
        elif x=='6':
            output(file,'aes192')
        elif x=='7':
            output(file,'aes256')
        elif x=='8':
            output(file,'twofish')
        elif x=='9':
            output(file,'camellia128')
        elif x=='10':
            output(file,'camellia192')
        elif x=='11':
            output(file,'camellia256')
        elif x.lower()=='mm':
            main()
        elif x.lower()=='sm':
            ciphercall()
        elif x.lower()=='c' or x.lower()=='close':
            sys.exit()
        else:
            print('Incorrect choice!')
            x=input()
            ecmd()
            
    print('\n<-----Symmetric-Encryptor----->\n')    
    file=input('\nEnter FileName for Encryption:')
    chkfl(file,'i')
    choice()

#Function to decrypt encrypted files.
def decrypt():
    file=input('Enter Filename:')
    chkfl(file,'i')
    outfile=input('Enter Output file:')
    if len(outfile)==0:
       outfile=file[:len(file)-4]
    start()
    os.system('gpg -d '+file+'>'+outfile)
    err(outfile)
    end()
    main()

#Function to Handle Asymmetric Cryptography.
def cipher2call():

    #Function to check if a public key exists with given email address.
    def icheck(z):
     count=0
     os.system('gpg --list-keys>kernel_dump.txt')
     with open('kernel_dump.txt') as f:
        for x in f.readlines():              
                 if z in x:
                    # print('found!')
                     count=1
                     break
     os.remove('kernel_dump.txt')
     if count==0:
        print('Email address not found in database!')
        tskf()
        pause()
        cipher2call()
     
    #Function to display contents of a file.
    def display(file):
        with open(file,'r') as f:
            s=f.read(1024)
            print(s)
            while len(s)>0:
                s=f.read(1024)
                print(s)
    
    #Function to pause the program till user presses a key.    
    def wait():
      x=input('\nPress any key to continue...\n')
  
    #Basic Function to check if entered email address is valid or not using basic syntax checks.
    def inpt():
        x=input('Enter email address in public key:')
        if '@' not in x:
            return False
        elif '.' not in x:
            return False
        for i in range(len(x)):
            if x[-1]=='@' or x[-1]=='.':
                    return False
        return x
        
    #Function to throw error if email address is found with wrong syntax.    
    def chk(x):
        if x==False:
            print('\nEntered value is not an email address!\n')
            x=input('Press any key to continue...')
            cipher2call()
    
    #Function to import an OPENPGP public key.
    def imports():
        file=input('\nEnter OPENPGPkey( public key / Secret key ) Filename:')
        chkfl(file,'i')
        print('\n<-----Importing Key----->\n')
        os.system('gpg --import '+file)
        end()
        wait()
        cipher2call()
     
    #Function to encrypt all files in given folder using asymmetric cryptography.     
    def rowdy():
        tsks()
        name=inpt()
        chk(name)
        icheck(name)
        os.system('gpg --list-secret-keys>tmp.txt')
        if os.path.getsize('tmp.txt')==0:
                print("Error: Either you don't have admin access \n or you havenot generated a openpgp keypair!")
                pause()
                os.remove('tmp.txt')
                cipher2call()
                sys.exit()
        os.remove('tmp.txt')
        print('\nWARNING!:All files in the folder will be permanently ')
        print('Encrypted and cannot be decrypted at any cost so keep a')
        print('copy of those files before you proceed!\n')
        fname=input("Enter Folder Name:")
        if os.path.exists(fname):
           if os.path.isdir(fname):
              os.chdir(fname)
              for unit in os.listdir():
                  if os.path.isfile(unit):
                     os.system("gpg -se -r "+name+" "+unit)
                     os.remove(unit)
                    
           tske()
           cipher2call()
               
        else:
           print("Folder doesn't exist!")
        tskf()
        pause()
        cipher2call()

    #Function to encrypt all files in given folder using aes256 and sign it with asymmetric cryptography.
    def rowdy1():
        tsks()
        os.system('gpg --list-secret-keys>tmp.txt')
        if os.path.getsize('tmp.txt')==0:
            print("Error: Either you don't have admin access \n or you havenot generated a openpgp keypair!")
            pause()
            os.remove('tmp.txt')
            cipher2call()
            sys.exit()
        
        print('\nWARNING!:All files in the folder will be permanently ')
        print('Encrypted and cannot be decrypted at any cost without the password so keep a')
        print('copy of those files before you proceed!\n')
        fname=input("Enter Folder Name:")
        if os.path.exists(fname):
           if os.path.isdir(fname):
              os.chdir(fname)
              for unit in os.listdir():
                  if os.path.isfile(unit):
                     os.system("gpg --s2k-mode 3 --s2k-count 65000000 --cipher-algo aes256 -sc  "+unit)
                     os.remove(unit)
                    
           tske()
           cipher2call()
               
        else:
           print("Folder doesn't exist!")
        tskf()
        pause()
        cipher2call()
     
     #Function to export OPENPGP public key.
    def exports():
        name=inpt()
        chk(name)
        icheck(name)
        print('\n<-----Exporting Public Key----->\n')
        os.system('gpg -a --export '+name+'>'+name+'_publickey.asc')
        err(name+'_publickey.asc')
        end()
        wait()
        cipher2call()
        
     #Function to list all OPENPGP public keys on local host.   
    def listkeys():
        print('\n<-----Public Keys in this computer----->\n')
        os.system('gpg --fingerprint>tmp.txt')
        serr('tmp.txt')
        display('tmp.txt')
        os.remove('tmp.txt')
        end()
        wait()
        cipher2call()
     
     #Function to list all OPENPGP secret keys on local host.     
    def secretkeys():
        print('\n<------secret keys in this computer----->\n')
        os.system('gpg --list-secret-keys>mp.txt')
        serr('mp.txt')
        display('mp.txt')
        os.remove('mp.txt')
        end()
        wait()
        cipher2call()
     
     #Function to Export OPENPGP secret keys.     
    def exportsecrets():
        key=inpt()
        chk(key)
        icheck(key)
        print('\n<-----Exporting Secret keys----->\n')
        os.system('gpg -a --export-secret-key '+key+'>'+key+'_secretkey.asc')
        err(key+'_secretkey.asc')
        end()
        wait()
        cipher2call()

    #Function to generate an OPENPGP key pair.
    def keygen():
        print('\n<-----Generating OpenPGP keypair----->\n')
        print('\nWarning!:\n\nAlways give your name and email address, \nboth unique for each key else this program will fail.\n')
        os.system('gpg --cert-digest-algo sha256 --expert --full-gen-key')
        end()
        wait()
        cipher2call()
    
    #Function to delete a given OPENPGP public key based on email address.
    def delkeys():
        print('\n<-----Deleting Public Key----->\n')
        x=inpt()
        chk(x)
        icheck(x)
        os.system('gpg --delete-key '+x)
        end()
        wait()
        cipher2call()
    
    #Function to delete a given OPENPGP secret key based on email address.
    def delsecrets():
        print('\n<-----Deleting Secret Key----->\n')
        x=inpt()
        chk(x)
        icheck(x)
        os.system('gpg --delete-secret-key '+x)
        end()
        wait()
        cipher2call()

    #Function to generate revocation Certificate based on email address.
    def revoke():
        print('\n<-----Generating Revocation Certificate----->\n')
        x=inpt()
        chk(x)
        icheck(x)
        os.system('gpg --gen-revoke -a '+x+'>revoke.asc')
        err('revoke.asc')
        end()
        wait()
        cipher2call()
     
    #Menu for performing Asymmetric Cryptographic Operations.     
    def choice():
        x=input('\n\nEnter command:')
        if x=='1':
            keygen()
        elif x=='2':
            imports()
        elif x=='3':
            exports()
        elif x=='4':
            exportsecrets()
        elif x=='5':
            listkeys()
        elif x=='6':
            secretkeys()
        elif x=='7':
            delkeys()
        elif x=='8':
            delsecrets()
        elif x=='9':
            revoke()
        elif x=='10':
            rowdy()
        elif x=='11':
            rowdy1()  
        elif x.lower()=='mm':
            main()
        elif x.lower()=='c'or x.lower()=='close':
            sys.exit()
        elif x.lower()=='sm':
            cipher2call()
        else:
            print('Entered Choice is incorrect, choose a number in 1,2,3, ... 11')
            wait()
            cipher2call()
    print('\n<------Asymmetric Cryptrographic Manager----->\n')
    print()
    print('Menu:-\n')
    print('\n1)Generate OPENPGP keypair.\n2)Import\n3)Export public key\n4)Export Secret key\n5)List Public Keys in this PC.\n6)List Secret keys in this PC.')
    print('7)Delete Public Key \n8)Delete Secret Key \n9)Revoke Key\n10)Bulk encrypt files in folder for a public key\n11)Bulk Sign and Symmetric encrypt files in folder\n')
         
    choice()
    cipher2call()

#Function to load appropriate functions based on User Selection.
def process(z):
    if z=='1':
        hashcall()
    elif z=='2':
        ciphercall()
    elif z=='3':
        decrypt()
    elif z=='4':
        cipher2call()
    elif z.lower()=='close'or z.lower()=='c':
        sys.exit()
    elif z.lower()=='mm':
        main()
    else:
        print('\nPlease enter a valid input,either a number from 1,2,3 or 4 or \n"mm" command\n')
        cmd()

#Display Main Menu.
def main():
  gpg()
  print('\n----- Simple-Gpg -----\n')

  print("A Crossplatform Opensource tool using gnupg for strong cryptography.")
  print('\nOS Detected:',platform.system())
  print('Python Version:',platform.python_version())
  print('Python Implementation:',platform.python_implementation())
  print('\n\nMenu:-\n\n1)Calculate Cryptographic Hash\n2)Symmetric Encryption\n3)Symmetric Decryption \n4)Asymmetric key Management.')
  cmd()
main()
 


