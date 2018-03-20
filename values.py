enc_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ';',
                '\\', ':', '"', '|', ',', '.', '/', '<', '>', '?',"'",' ','0','1','2','3','4','5','6','7','8','9']

about = '''Its a simple program to Encrypt & Decrypt Texts & Text Files
you can use it to encrypt secret messages. also you can encrypt all
your passwords with this program and then save them where you want.'''

help_message = """Args guide:
[-e] means encrypting sth
[-d] means decrypting sth
[-t] text to encrypt or decrypt
[-f] file to encrypt or decrypt

Examples for encrypting text or text-file:
 
$ python3 Encoder.py -e -t
$ python3 Encoder.py -e -f '<file path to read>'"""