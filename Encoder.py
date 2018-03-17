import hashlib
import os
from ui import *

def enc(cargo,kind):
    #--------------------------------------------------------------------------- [Alphabet]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', ';',
                '\\', ':', '"', '|', ',', '.', '/', '<', '>', '?',"'",' ','0','1','2','3','4','5','6','7','8','9']
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
            print_red('Menu > Encrypt > Import File > Error!')
            print_purple1('---------------------------------------------------------------------')
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
                print_purple2('Menu > Encrypt > Import File >')
                print_red('Attention!!')
                print_purple1('---------------------------------------------------------------------')
                print ("We have detected"),
                print_blue2(counter)
                print(','),
                print_red2('\\n')
                print('in your text. change it to'),
                print_red('\\N')
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
                print_purple1('Menu > Encrypt > Import File > Set encryption key')
                print_purple1('---------------------------------------------------------------------')
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
                print_purple1('Menu > Encrypt > Import File > Set encryption key > Set name')
                print_purple1('---------------------------------------------------------------------')
                name = input('Enter a name for encrypted file\n>> ')
                if ".txt" not in name:
                    name = name + '.txt'
                saveFile = open(name,"w")
                saveFile.write(str(encryptedFile))
                saveFile.close()
                os.system('clear')
                print_green('Menu > Encrypt > Import File > Set encryption key > Set name > Done! ')
                print_purple1('---------------------------------------------------------------------')
                note = input('The encrypted file created. press Enter to go menu.')


    elif kind == 'text':
        #--------------------------------------------------------------------------- [alphatext]
        alphatext = ""
        for letter in cargo:
            if letter in alphabet:
                alphatext = alphatext + str(alphabet.index(letter))
        #--------------------------------------------------------------------------- [password -> sha256]
        os.system('clear')
        print_purple1('Menu > Encrypt > Import Text > Set encryption key')
        print_purple1('---------------------------------------------------------------------')
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
        print_green('Menu > Encrypt > Import Text > Set encryption key > Done!')
        print_purple1('---------------------------------------------------------------------')
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
            print_purple1('Menu > Decrypt > Import File > Error')
            print_purple1('---------------------------------------------------------------------')
            note = input('File Not Found! hit Enter to go menu.')
            fileState = False
        if fileState == True:
            #---------------------------------------------------------------------------[Enter Secret key]
            os.system('clear')
            print_purple1('Menu > Decrypt > Import File > Enter encryption key')
            print_purple1('---------------------------------------------------------------------')
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
                print_green('Menu > Decrypt > Import File > Enter encryption key > Done!')
                print_purple1('---------------------------------------------------------------------\n')
                for part in decryptedFile:
                    print(part)
                print('\n')
                note = input('Its decrypted file text. hit Enter to go menu.')
            except:
                os.system('clear')
                print_red('Menu > Decrypt > Import File > Enter encryption key > Error!')
                print_purple1('---------------------------------------------------------------------')
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
        print_purple1('Menu > Decrypt > Import Text > Enter encryption key')
        print_purple1('---------------------------------------------------------------------')
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
            print_red('Menu > Decrypt > Import Text > Enter encryption key > Error!')
            print_purple1('---------------------------------------------------------------------')
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
            print_green('Menu > Decrypt > Import Text > Enter encryption key > Done!')
            print_purple1('---------------------------------------------------------------------')
            print('This is your decrypted text, hit Enter to go menu.\n')
            print(decryptedText)
            note = input('')
        except:
            os.system('clear')
            print_red('Menu > Decrypt > Import Text > Enter encryption key > Error!')
            print_purple1('---------------------------------------------------------------------')
            print('Decrypting fail >_<!')
            print('''Tips:
            1. Secret code is incorrect
            2.Encrypted text has been manipulated!''')
            note = input('')


while True:
    os.system('clear')
    print_purple1('Menu')
    print_purple1('---------------------------------------------------------------------')
    chose = input('[1]Encrypt  [2]Decrypt  [3]Help & About  [4]Exit\n>>  ')

    if chose in ['ENCRYPT','encrypt','Encrypt','1']:
        while True:
            os.system('clear')
            print_purple1('Menu > Encrypt')
            print_purple1('---------------------------------------------------------------------')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = input('>> ')

            if   chose == '1':
                os.system('clear')
                print_purple1('Menu > Encrypt > Import File')
                print_purple1('---------------------------------------------------------------------')
                filename = input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    enc(filename,'file')
                    break
            elif chose == '2':
                os.system('clear')
                print_purple1('Menu > Encrypt > Import Text')
                print_purple1('---------------------------------------------------------------------')
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
            print_purple1('Menu > Decrypt')
            print_purple1('---------------------------------------------------------------------')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = input('>> ')
            if chose == '1':
                os.system('clear')
                print_purple1('Menu > Decrypt > Import File')
                print_purple1('---------------------------------------------------------------------')
                filename = input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    dec(filename,'file')
                    break
            elif chose == '2':
                os.system('clear')
                print_purple1('Menu > Decrypt > Import Text')
                print_purple1('---------------------------------------------------------------------')
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
        print_purple1('Menu > Help & About')
        print_purple1('---------------------------------------------------------------------')
        print('''Its a simple program to Encrypt & Decrypt Texts & Text Files
you can use it to encrypt secret messages. also you can encrypt all
your passwords with this program and then save them where you want.''')
        print('Trust it. powered by SHA256!'),
        print_red2('created by My own')
        print('2019.Jun.08')
        print_red2('>>')
        print_blue('Github: Github.com/ccxa')
        print_red2('>>')
        print_purple1('---------------------------------------------------------------------')
        note=input('')
    elif chose == '4':
        os.system('clear')
        exit()
    else:
        print('>> Invalid Input !')
