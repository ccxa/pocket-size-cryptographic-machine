import hashlib
import os

import values
from ui import *

def enc(cargo,kind):
    #--------------------------------------------------------------------------- [Alphabet]
    alphabet = values.enc_alphabet
    n = 0
    while n < 100:
        alphabet.insert(0,0)
        n+=1
    if kind == 'file' :
        #----------------------------------------------------------------------- [Reading file]
        fileState = False
        try:
            file = open(cargo,"r").read()
            file = file.split("\n")
            if '' in file:
                file.remove("")
            fileState = True
        except IOError:
            os.system('clear')
            print_colorful('Menu > Encrypt > Import File > Error!', 'red')
            print_colorful('---------------------------------------------------------------------', 'purple')
            note = input('File Not Found! hit Enter to go menu.')

        if fileState == True:
            counter = 0
            flag = False
            for part in file:
                print(part)
                if '\\n' in part:
                    counter = counter + part.count('\\n')
                    flag = True

            if flag == True:
                os.system('clear')
                print_colorful('Menu > Encrypt > Import File >', 'purple2')
                print_colorful('Attention!!', 'red')
                print_colorful('---------------------------------------------------------------------', 'purple')
                print_colorful(counter, 'blue2')
                print(','),
                print_colorful('\\n', 'red2')
                print('in your text. change it to'),
                print_colorful('\\N', 'red')
                print('Otherwise it considered as Enter button and navigate words to next line.')
                note = input('')
            else:
                #----------------------------------------------------------------------- [doc to alphafile]
                alphafile = ""
                for part in file:
                    for letter in part:
                        if letter in alphabet:
                            alphafile = alphafile + str(alphabet.index(letter))
                    alphafile = alphafile + str(alphabet.index('\\')) + str(alphabet.index('n'))
                #----------------------------------------------------------------------- [password > sha256]
                os.system('clear')
                print_colorful('Menu > Encrypt > Import File > Set encryption key', 'blue')
                print_colorful('---------------------------------------------------------------------', 'purple')
                sk = input("input an secret key in order to encrypt file\n>> ")
                sha = hashlib.sha256()
                sha.update(sk.encode('utf-8'))
                sha = sha.hexdigest()
                #----------------------------------------------------------------------- [sha256 -> alphasha]
                alphasha = ""
                for l in sha:
                    alphasha = alphasha + str(alphabet.index(l))
                #----------------------------------------------------------------------- [Create Encrypted File]
                encryptedFile = int(alphasha) * int(alphafile)
                os.system('clear')
                print_colorful('Menu > Encrypt > Import File > Set encryption key > Set name', 'blue')
                print_colorful('---------------------------------------------------------------------', 'purple')
                name = input('Enter a name for encrypted file\n>> ')
                if ".txt" not in name:
                    name = name + '.txt'
                saveFile = open(name,"w")
                saveFile.write(str(encryptedFile))
                saveFile.close()
                os.system('clear')
                print_colorful('Menu > Encrypt > Import File > Set encryption key > Set name > Done! ', 'green')
                print_colorful('---------------------------------------------------------------------', 'purple')
                note = input('The encrypted file created. press Enter to go menu.')


    elif kind == 'text':
        #--------------------------------------------------------------------------- [alphatext]
        alphatext = ""
        for letter in cargo:
            if letter in alphabet:
                alphatext = alphatext + str(alphabet.index(letter))
        #--------------------------------------------------------------------------- [password -> sha256]
        os.system('clear')
        print_colorful('Menu > Encrypt > Import Text > Set encryption key', 'blue')
        print_colorful('---------------------------------------------------------------------', 'purple')
        sk = input('Set a secret key in order to encrypt text\n>> ')
        sha = hashlib.sha256()
        sha.update(sk.encode('utf-8'))
        sha = sha.hexdigest()
        #--------------------------------------------------------------------------- [sha256 -> alphasha]
        alphasha = ""
        for l in sha:
            alphasha = alphasha + str(alphabet.index(l))
        #--------------------------------------------------------------------------- [generate encryptedText]
        encryptedText = int(alphasha) * int(alphatext)
        os.system('clear')
        print_colorful('Menu > Encrypt > Import Text > Set encryption key > Done!', 'green')
        print_colorful('---------------------------------------------------------------------', 'purple')
        print('This is your encrypted text:')
        print(encryptedText)
        note = input('press Enter to go menu.')

def dec(cargo,kind):
    #---------------------------------------------------------------------------[Alphabet]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ';',
                '\\', ':', '"', '|', ',', '.', '/', '<', '>', '?',"'",' ','0','1','2','3','4','5','6','7','8','9']
    n = 0
    while n < 100:
        alphabet.insert(0,0)
        n+=1
    if kind == 'file':
        #----------------------------------------------------------------------- [read encryptedFile]
        fileState = False
        try:
            file = open(cargo,"r").read()
            file = file.split("\n")
            if "" in file:
                file.remove("")
            fileState = True
        except IOError:
            os.system('clear')
            print_colorful('Menu > Decrypt > Import File > Error', 'red')
            print_colorful('---------------------------------------------------------------------', 'purple')
            note = input('File Not Found! hit Enter to go menu.')
            fileState = False
        if fileState == True:
            #---------------------------------------------------------------------------[Enter Secret key]
            os.system('clear')
            print_colorful('Menu > Decrypt > Import File > Enter encryption key', 'blue')
            print_colorful('---------------------------------------------------------------------', 'purple')
            sk = input("Enter files encryption key to decrypt it.\n>> ")
            sha = hashlib.sha256()
            sha.update(sk.encode('utf-8'))
            sha = sha.hexdigest()
            alphasha = ""
            for l in sha:
                alphasha = alphasha + str(alphabet.index(l))
            #---------------------------------------------------------------------------[Decrypt -> Alphafile]
            try:
                for r in range(0,len(file)):
                    Alphafile = int(file[r]) / int(alphasha)
                    Alphafile = str(Alphafile)
                    decryptedFile = ""
                    for r in range(0,len(Alphafile)//3):
                        letter = Alphafile[0:3]
                        decryptedFile = decryptedFile + alphabet[int(letter)]
                        Alphafile = Alphafile[3:]

                decryptedFile = decryptedFile.split('\\n')
                if '' in decryptedFile:
                    decryptedFile.remove('')
                os.system('clear')
                print_colorful('Menu > Decrypt > Import File > Enter encryption key > Done!', 'green')
                print_colorful('---------------------------------------------------------------------\n', 'purple')
                for part in decryptedFile:
                    print(part)
                print('\n')
                note = input('Its decrypted file text. hit Enter to go menu.')
            except:
                os.system('clear')
                print_colorful('Menu > Decrypt > Import File > Enter encryption key > Error!', 'red')
                print_colorful('---------------------------------------------------------------------', 'purple')
                print('Decrypting fail >_<!')
                print('''Tips:
                1. Secret code is incorrect
                2.Encrypted file has been manipulated!''')
                note = input('')

    elif kind == 'text':
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ';',
                    '\\', ':', '"', '|', ',', '.', '/', '<', '>', '?',"'",' ','0','1','2','3','4','5','6','7','8','9']
        n = 0
        while n < 100:
            alphabet.insert(0,0)
            n+=1
        os.system('clear')
        print_colorful('Menu > Decrypt > Import Text > Enter encryption key', 'blue')
        print_colorful('---------------------------------------------------------------------', 'purple')
        sk = input('Import secret key in order to decrypt your text\n>> ')
        sha = hashlib.sha256()
        sha.update(sk.encode('utf-8'))
        sha = sha.hexdigest()
        alphasha = ''
        for l in sha:
            alphasha = alphasha + str(alphabet.index(l))

        try:
            alphatext = int(cargo) / int(alphasha)
            alphatext = str(alphatext)
            decryptedText = ''
        except ValueError:
            os.system('clear')
            print_colorful('Menu > Decrypt > Import Text > Enter encryption key > Error!', 'red')
            print_colorful('---------------------------------------------------------------------', 'purple')
            print('Decrypting fail >_<!')
            print('''Tips:
            1. Secret code is incorrect
            2.Encrypted text has been manipulated!''')
            note = input('')

        try:
            for r in range(0,len(alphatext)//3):
                letter = alphatext[0:3]
                decryptedText = decryptedText + alphabet[int(letter)]
                alphatext = alphatext[3:]
            os.system('clear')
            print_colorful('Menu > Decrypt > Import Text > Enter encryption key > Done!', 'green')
            print_colorful('---------------------------------------------------------------------', 'purple')
            print('This is your decrypted text, hit Enter to go menu.\n')
            print(decryptedText)
            note = input('')
        except:
            os.system('clear')
            print_colorful('Menu > Decrypt > Import Text > Enter encryption key > Error!', 'red')
            print_colorful('---------------------------------------------------------------------', 'purple')
            print('Decrypting fail >_<!')
            print('''Tips:
            1. Secret code is incorrect
            2.Encrypted text has been manipulated!''')
            note = input('')


while True:
    os.system('clear')
    print_colorful('Menu', 'blue')
    print_colorful('---------------------------------------------------------------------', 'purple')
    chose = input('[1]Encrypt  [2]Decrypt  [3]Help & About  [4]Exit\n>>  ')

    if chose in ['ENCRYPT','encrypt','Encrypt','1']:
        while True:
            os.system('clear')
            print_colorful('Menu > Encrypt', 'blue')
            print_colorful('---------------------------------------------------------------------', 'purple')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = input('>> ')

            if   chose == '1':
                os.system('clear')
                print_colorful('Menu > Encrypt > Import File', 'blue')
                print_colorful('---------------------------------------------------------------------', 'purple')
                filename = input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    enc(filename,'file')
                    break
            elif chose == '2':
                os.system('clear')
                print_colorful('Menu > Encrypt > Import Text', 'blue')
                print_colorful('---------------------------------------------------------------------', 'purple')
                text = input('Import Text, or leave it empty to Cancel.\n>> ')
                if text == '':
                    os.system('clear')
                    break
                else:
                    enc(text,'text')
                    break
            elif chose == '3':
                break
            else:
                print('Invalid!')
    elif chose in ['DECRYPT','decrypt','Decrypt','2'] :
        while True:
            os.system('clear')
            print_colorful('Menu > Decrypt', 'blue')
            print_colorful('---------------------------------------------------------------------', 'purple')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = input('>> ')
            if chose == '1':
                os.system('clear')
                print_colorful('Menu > Decrypt > Import File', 'blue')
                print_colorful('---------------------------------------------------------------------', 'purple')
                filename = input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    dec(filename,'file')
                    break
            elif chose == '2':
                os.system('clear')
                print_colorful('Menu > Decrypt > Import Text', 'blue')
                print_colorful('---------------------------------------------------------------------', 'purple')
                text = input('Import Text, or leave it empty to Cancel.\n>> ')
                if text == '':
                    break
                else:
                    dec(text,'text')
                    break
            elif chose == '3':
                break
            else:
                print('Invalid!')
    elif chose in ['HELP','help','Help','3']:
        os.system('clear')
        print_colorful('Menu > Help & About', 'blue')
        print_colorful('---------------------------------------------------------------------', 'purple')
        print('''Its a simple program to Encrypt & Decrypt Texts & Text Files
you can use it to encrypt secret messages. also you can encrypt all
your passwords with this program and then save them where you want.''')
        print('Trust it. powered by SHA256!'),
        print_colorful('created by My own', 'red2')
        print('2019.Jun.08')
        print_colorful('>>', 'red2')
        print_colorful('Github: Github.com/ccxa', 'blue')
        print_colorful('>>', 'red2')
        print_colorful('---------------------------------------------------------------------', 'purple')
        note=input('')
    elif chose == '4':
        os.system('clear')
        exit()
    else:
        print('>> Invalid Input !')
