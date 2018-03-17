import hashlib
import os

def prLightPurple(text):
    print("\033[36m{}\033[00m".format(text))
def prLightPurple2(text):
    print("\033[36m{}\033[00m".format(text)),
def prBlue(text):
    print("\033[34m{}\033[00m".format(text))
def prBlue2(text):
    print("\033[34m{}\033[00m".format(text)),
def prRed(text):
    print("\033[91m{}\033[00m" .format(text))
def prRed2(text):
    print("\033[91m{}\033[00m" .format(text)),
def prGreen(text):
    print("\033[32m{}\033[00m" .format(text))

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
            prRed('Menu > Encrypt > Import File > Error!')
            prLightPurple('---------------------------------------------------------------------')
            note = raw_input('File Not Found! hit Enter to go menu.')

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
                prLightPurple2('Menu > Encrypt > Import File >')
                prRed('Attention!!')
                prLightPurple('---------------------------------------------------------------------')
                print ("We have detected"),
                prBlue2(counter)
                print(','),
                prRed2('\\n')
                print('in your text. change it to'),
                prRed('\\N')
                print('Otherwise it considered as Enter button and navigate words to next line.')
                note = raw_input('')
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
                prLightPurple('Menu > Encrypt > Import File > Set encryption key')
                prLightPurple('---------------------------------------------------------------------')
                sk = raw_input("input an secret key in order to encrypt file\n>> ")
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
                prLightPurple('Menu > Encrypt > Import File > Set encryption key > Set name')
                prLightPurple('---------------------------------------------------------------------')
                name = raw_input('Enter a name for encrypted file\n>> ')
                if ".txt" not in name:
                    name = name + '.txt'
                saveFile = open(name,"w")
                saveFile.write(str(encryptedFile))
                saveFile.close()
                os.system('clear')
                prGreen('Menu > Encrypt > Import File > Set encryption key > Set name > Done! ')
                prLightPurple('---------------------------------------------------------------------')
                note = raw_input('The encrypted file created. press Enter to go menu.')


    elif kind == 'text':
        #--------------------------------------------------------------------------- [alphatext]
        alphatext = ""
        for letter in cargo:
            if letter in alphabet:
                alphatext = alphatext + str(alphabet.index(letter))
        #--------------------------------------------------------------------------- [password -> sha256]
        os.system('clear')
        prLightPurple('Menu > Encrypt > Import Text > Set encryption key')
        prLightPurple('---------------------------------------------------------------------')
        sk = raw_input('Set a secret key in order to encrypt text\n>> ')
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
        prGreen('Menu > Encrypt > Import Text > Set encryption key > Done!')
        prLightPurple('---------------------------------------------------------------------')
        print('This is your encrypted text:')
        print(encryptedText)
        note = raw_input('press Enter to go menu.')

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
            prLightPurple('Menu > Decrypt > Import File > Error')
            prLightPurple('---------------------------------------------------------------------')
            note = raw_input('File Not Found! hit Enter to go menu.')
            fileState = False
        if fileState == True:
            #---------------------------------------------------------------------------[Enter Secret key]
            os.system('clear')
            prLightPurple('Menu > Decrypt > Import File > Enter encryption key')
            prLightPurple('---------------------------------------------------------------------')
            sk = raw_input("Enter files encryption key to decrypt it.\n>> ")
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
                prGreen('Menu > Decrypt > Import File > Enter encryption key > Done!')
                prLightPurple('---------------------------------------------------------------------\n')
                for part in decryptedFile:
                    print(part)
                print('\n')
                note = raw_input('Its decrypted file text. hit Enter to go menu.')
            except:
                os.system('clear')
                prRed('Menu > Decrypt > Import File > Enter encryption key > Error!')
                prLightPurple('---------------------------------------------------------------------')
                print('Decrypting fail >_<!')
                print('''Tips:
                1. Secret code is incorrect
                2.Encrypted file has been manipulated!''')
                note = raw_input('')

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
        prLightPurple('Menu > Decrypt > Import Text > Enter encryption key')
        prLightPurple('---------------------------------------------------------------------')
        sk = raw_input('Import secret key in order to decrypt your text\n>> ')
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
            prRed('Menu > Decrypt > Import Text > Enter encryption key > Error!')
            prLightPurple('---------------------------------------------------------------------')
            print('Decrypting fail >_<!')
            print('''Tips:
            1. Secret code is incorrect
            2.Encrypted text has been manipulated!''')
            note = raw_input('')

        try:
            for r in range(0,len(alphatext)//3):
                letter = alphatext[0:3]
                decryptedText = decryptedText + alphabet[int(letter)]
                alphatext = alphatext[3:]
            os.system('clear')
            prGreen('Menu > Decrypt > Import Text > Enter encryption key > Done!')
            prLightPurple('---------------------------------------------------------------------')
            print('This is your decrypted text, hit Enter to go menu.\n')
            print(decryptedText)
            note = raw_input('')
        except:
            os.system('clear')
            prRed('Menu > Decrypt > Import Text > Enter encryption key > Error!')
            prLightPurple('---------------------------------------------------------------------')
            print('Decrypting fail >_<!')
            print('''Tips:
            1. Secret code is incorrect
            2.Encrypted text has been manipulated!''')
            note = raw_input('')


while True:
    os.system('clear')
    prLightPurple('Menu')
    prLightPurple('---------------------------------------------------------------------')
    chose = raw_input('[1]Encrypt  [2]Decrypt  [3]Help & About  [4]Exit\n>>  ')

    if chose in ['ENCRYPT','encrypt','Encrypt','1']:
        while True:
            os.system('clear')
            prLightPurple('Menu > Encrypt')
            prLightPurple('---------------------------------------------------------------------')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = raw_input('>> ')

            if   chose == '1':
                os.system('clear')
                prLightPurple('Menu > Encrypt > Import File')
                prLightPurple('---------------------------------------------------------------------')
                filename = raw_input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    enc(filename,'file')
                    break
            elif chose == '2':
                os.system('clear')
                prLightPurple('Menu > Encrypt > Import Text')
                prLightPurple('---------------------------------------------------------------------')
                text = raw_input('Import Text, or leave it empty to Cancel.\n>> ')
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
            prLightPurple('Menu > Decrypt')
            prLightPurple('---------------------------------------------------------------------')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = raw_input('>> ')
            if chose == '1':
                os.system('clear')
                prLightPurple('Menu > Decrypt > Import File')
                prLightPurple('---------------------------------------------------------------------')
                filename = raw_input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    dec(filename,'file')
                    break
            elif chose == '2':
                os.system('clear')
                prLightPurple('Menu > Decrypt > Import Text')
                prLightPurple('---------------------------------------------------------------------')
                text = raw_input('Import Text, or leave it empty to Cancel.\n>> ')
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
        prLightPurple('Menu > Help & About')
        prLightPurple('---------------------------------------------------------------------')
        print('''Its a simple program to Encrypt & Decrypt Texts & Text Files
you can use it to encrypt secret messages. also you can encrypt all
your passwords with this program and then save them where you want.''')
        print('Trust it. powered by SHA256!'),
        prRed2('created by My own')
        print('2019.Jun.08')
        prRed2('>>')
        prBlue('Github: Github.com/ccxa')
        prRed2('>>')
        prLightPurple('---------------------------------------------------------------------')
        note=raw_input('')
    elif chose == '4':
        os.system('clear')
        exit()
    else:
        print('>> Invalid Input !')
