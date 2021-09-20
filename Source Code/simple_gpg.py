
# Simple_gpg
# Copyright (c) 2021 ANISH M < aneesh25861@gmail.com >

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

''' 
This project was developed by M.Anish as way to learn python3 programming during 1st semester and has improved it ever since. 
Though care has been taken to avoid bugs, bugs may exist.

'''

import os
import hashlib
import platform
import sys
import subprocess

#Function to detect if required tools/package is present on local host or not.
def detect(cmd,web,snam,pkg):
    
        if platform.system().lower()=='windows':
              if subprocess.run(cmd.split(),stdout=subprocess.DEVNULL).returncode!=0:
                print('\nPlease wait opening '+snam +' website in your browser!\nYou Have to download and install it.\n')
                from webbrowser import open
                open(web)
                
        else:
         if subprocess.run(cmd.split(),stdout=subprocess.DEVNULL).returncode != 0:    
           print('\nError:'+pkg+' is not found! Please install it before running this program again :( ')
           x=input('\nPress any key to exit...')
           sys.exit()

#Function to Detect gpg tool on local host. 
def gpg():
   detect('gpg --version','https://gpg4win.org','gpg4win','Gnupg')

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
    if os.path.isfile(file) is False:
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
      output=subprocess.run(['gpg','--print-md',algo,feed],capture_output = True)
      buff=output.stdout.decode()
      with open(algo+'.txt','w') as f:
          f.write(buff)
      print(buff.rstrip())
      err(algo+'.txt')
      end()
      hcmd()
          
   #Function to compute sha3 hashes of files using hashlib. 
  def sha3(file,txt):
      start()
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
      elif x.lower() in ('c','close'):
          sys.exit()
      else:
            print('Incorrect choice, Enter choice which is a number in\n1,2,3,4,5,6')
            i=input('\nPress any key to continue')
            choice()

  print('-----Hash-Calculator-----')
  file=input('\nEnter FileName:')
  chkfl(file,'i')
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
        print('\nChoose Hash Algorithm:\n1)sha1 \n2)sha256\n3)sha512 (Recommended)')
        x=input('\nEnter Hash algorithm:')
        if x.lower()=='sha256' or x=='2':
            digest='sha256'
        elif x.lower()=='sha512' or x=='3':
            digest='sha512'
        else:
            digest='sha1'
        subprocess.run(['gpg','-o',out,'--s2k-mode','3','--s2k-count','65011712','--s2k-digest',digest,'--cipher-algo',algo,'-c',file]).stdout
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
        elif x.lower() in ('c','close'):
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
    subprocess.run(['gpg','-o',outfile,'-d',file]).stdout
    err(outfile)
    end()
    main()

#Function to Handle Asymmetric Cryptography.
def cipher2call():

    #Function to check if a public key exists with given email address.
    def icheck(z):
     count=0
     var=subprocess.run(['gpg','--list-keys'],capture_output=True)
     for x in var.stdout.decode().split():
         if z in x:
            count=1
            break

     if count==0:
        print('Email address not found in database!')
        tskf()
        pause()
        cipher2call()
      
    #Function to pause the program till user presses a key.    
    def wait():
      x=input('\nPress any key to continue...\n')
  
    #Basic Function to check if entered email address is valid or not using basic syntax checks.
    def inpt():
        x=input('Enter email address in public key:')
        if x[-1] in ('@','.'):
            return False
        for i in ('@','.'):
            if i not in x:
                return False
        return x
        
    #Function to throw error if email address is found with wrong syntax.    
    def chk(x):
        if x is False:
            print('\nEntered value is not an email address!\n')
            x=input('Press any key to continue...')
            cipher2call()
    
    #Function to import an OPENPGP public key.
    def imports():
        file=input('\nEnter OPENPGPkey( public key / Secret key ) Filename:')
        chkfl(file,'i')
        print('\n<-----Importing Key----->\n')
        subprocess.run(['gpg','--import',file]).stdout
        end()
        wait()
        cipher2call()
     
    #Function to encrypt all files in given folder using asymmetric cryptography.     
    def bulk_encrypt_asymmetric():
        tsks()
        name=inpt()
        chk(name)
        icheck(name)
        if len(subprocess.run(['gpg','--list-secret-keys'],capture_output=True).stdout) == 0:
                print("Error: It seems you havenot generated a openpgp keypair!")
                pause()
                cipher2call()
                sys.exit()
        print('\nWARNING!:All files in the folder will be permanently ')
        print('Encrypted and cannot be decrypted at any cost so keep a')
        print('copy of those files before you proceed!\n')
        fname=input("Enter Folder Name:")
        if os.path.exists(fname):
           if os.path.isdir(fname):
              os.chdir(fname)
              for unit in os.listdir():
                  if os.path.isfile(unit):
                     subprocess.run(['gpg','-se','-r',name,unit]).stdout
                     os.remove(unit)
           tske()
           cipher2call()
               
        else:
           print("Folder doesn't exist!")
        tskf()
        pause()
        cipher2call()

    #Function to encrypt all files in given folder using aes256 and sign it with asymmetric cryptography.
    def bulk_encrypt_symmetric():
        tsks()
        if len(subprocess.run(['gpg','--list-secret-keys'],capture_output=True).stdout) == 0:
            print("Error: It seems you havenot generated a openpgp keypair!")
            pause()
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
                     subprocess.run(['gpg','--s2k-mode','3','--s2k-count','65011712','--s2k-digest','sha512','--cipher-algo','aes256','-sc',unit]).stdout
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
        subprocess.run(['gpg','-o',name+'_publickey.asc','-a','--export',name]).stdout
        err(name+'_publickey.asc')
        end()
        wait()
        cipher2call()
        
     #Function to list all OPENPGP public keys on local host.   
    def listkeys():
        print('\n<-----Public Keys in this computer----->\n')
        x=subprocess.run(['gpg','--fingerprint'],capture_output=True)
        if len(x.stdout) == 0:
            print('\nThere are no OPENPGP keys to display!\n')
        else:
            print(x.stdout.decode())
        end()
        wait()
        cipher2call()
     
     #Function to list all OPENPGP secret keys on local host.     
    def secretkeys():
        print('\n<------secret keys in this computer----->\n')
        x=subprocess.run(['gpg','--list-secret-keys'],capture_output=True)
        if len(x.stdout) == 0:
            print('\nThere are no OPENPGP Secret keys to display!\n')
        else:
            print(x.stdout.decode())
        end()
        wait()
        cipher2call()
     
     #Function to Export OPENPGP secret keys.     
    def exportsecrets():
        key=inpt()
        chk(key)
        icheck(key)
        print('\n<-----Exporting Secret keys----->\n')
        subprocess.run(['gpg','-o',key+'_secretkey.asc','-a','--export-secret-key',key]).stdout
        err(key+'_secretkey.asc')
        end()
        wait()
        cipher2call()

    #Function to generate an OPENPGP key pair.
    def keygen():
        print('\n<-----Generating OpenPGP keypair----->\n')
        print('\nWarning!:\n\nAlways give your name and email address, \nboth unique for each key else this program will fail.\n')
        subprocess.run(['gpg','--cert-digest-algo','sha512','--expert','--full-gen-key']).stdout
        end()
        wait()
        cipher2call()
    
    #Function to delete a given OPENPGP public key based on email address.
    def delkeys():
        print('\n<-----Deleting Public Key----->\n')
        x=inpt()
        chk(x)
        icheck(x)
        subprocess.run(['gpg','--delete-key',x]).stdout
        end()
        wait()
        cipher2call()
    
    #Function to delete a given OPENPGP secret key based on email address.
    def delsecrets():
        print('\n<-----Deleting Secret Key----->\n')
        x=inpt()
        chk(x)
        icheck(x)
        subprocess.run(['gpg','--delete-secret-key',x]).stdout
        end()
        wait()
        cipher2call()

    #Function to generate revocation Certificate based on email address.
    def revoke():
        print('\n<-----Generating Revocation Certificate----->\n')
        x=inpt()
        chk(x)
        icheck(x)
        subprocess.run(['gpg','-o','revoke.asc','--gen-revoke','-a',x])
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
            bulk_encrypt_asymmetric()
        elif x=='11':
            bulk_encrypt_symmetric()  
        elif x.lower()=='mm':
            main()
        elif x.lower() in ('c','close'):
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
    elif z.lower() in ('close','c'):
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
 


