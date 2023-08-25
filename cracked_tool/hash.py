import hashlib
from colorama import init, Fore
import pyfiglet
import argparse

### Colors
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
reset = Fore.RESET

### Banner
ascii_banner = pyfiglet.figlet_format("BruteForce - HASH")
print(ascii_banner)

def check_hash(key, wordlist, type):
     for word in wordlist:
          cript = type(word.encode())
          if cript.hexdigest() == key:
               print (f'{green}Hash located as: {word}{reset}')
               exit(1)

parser = argparse.ArgumentParser(description='Cracker of hash')

parser.add_argument("-k","--hash" , help="Informe hash to be cracked", required=True)
parser.add_argument("-w","--wordlist" , help="Informe wordlist to be used",required=True)
args = parser.parse_args()

key = args.hash

print('#'*40)
print("Preparing list. Please wait !!!")
print('#'*40)

### Preparing wordlist 
arq = args.wordlist
with open(arq,'r', errors='ignore') as f:
    name = f.read()
    letter = name.splitlines()

### Choosing type of the hash
choice = input('Choice type of hash: ')
hash_name = ['blake2b','blake2s','md5','sha1','sha224','sha256','sha384','sha3_224','sha3_256','sha3_384','sha3_512','sha512']
if choice == 'blake2b':
    quebra = hashlib.blake2b
elif choice == 'blake2s':
    quebra = hashlib.blake2s
elif choice == 'md5':
    quebra = hashlib.md5
elif choice == 'sha1':
     quebra = hashlib.sha1
elif choice == 'sha224':
     quebra = hashlib.sha224
elif choice == 'sha384':
     quebra = hashlib.sha384
elif choice == 'sha3_224':
     quebra = hashlib.sha3_224
elif choice == 'sha3_256':
     quebra = hashlib.sha3_256
elif choice == 'sha3_384':
     quebra = hashlib.sha3_384
elif choice == 'sha3_512':
     quebra = hashlib.sha3_512
elif choice == 'sha512':
     quebra = hashlib.sha512
else:
    print (f'{red}Hash {choice} unknown. {reset}Options available:\n{green}{hash_name}{reset}')
    exit(1)

### Calling function
check_hash(key,letter,quebra)
print (f'\n{red}Hash {key} not found in list\n{reset}')