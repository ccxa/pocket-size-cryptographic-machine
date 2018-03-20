import os
import values
from ui import *
import graphy


while True:
    os.system('clear')
    print_colorful('Menu', 'blue')
    print_colorful('-' * 69, 'purple')
    chose = input('[1]Encrypt  [2]Decrypt  [3]Help & About  [4]Exit\n>>  ')

    if chose in ['ENCRYPT', 'encrypt', 'Encrypt', '1']:
        while True:
            os.system('clear')
            print_colorful('Menu > Encrypt', 'blue')
            print_colorful('-' * 69, 'purple')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = input('>> ')

            if chose == '1':
                os.system('clear')
                print_colorful('Menu > Encrypt > Import File', 'blue')
                print_colorful('-' * 69, 'purple')
                filename = input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    graphy.enc(filename, 'file')
                    break
            elif chose == '2':
                os.system('clear')
                print_colorful('Menu > Encrypt > Import Text', 'blue')
                print_colorful('-' * 69, 'purple')
                text = input('Import Text, or leave it empty to Cancel.\n>> ')
                if text == '':
                    os.system('clear')
                    break
                else:
                    graphy.enc(text, 'text')
                    break
            elif chose == '3':
                break
            else:
                print('Invalid!')
    elif chose in ['DECRYPT', 'decrypt', 'Decrypt', '2']:
        while True:
            os.system('clear')
            print_colorful('Menu > Decrypt', 'blue')
            print_colorful('-' * 69, 'purple')
            print('[1]Import File  [2]Input Text  [3]Cancel')
            chose = input('>> ')
            if chose == '1':
                os.system('clear')
                print_colorful('Menu > Decrypt > Import File', 'blue')
                print_colorful('-' * 69, 'purple')
                filename = input('Import File name, or leave it empty to Cancel.\n>> ')
                if filename == '':
                    break
                else:
                    graphy.dec(filename, 'file')
                    break
            elif chose == '2':
                os.system('clear')
                print_colorful('Menu > Decrypt > Import Text', 'blue')
                print_colorful('-' * 69, 'purple')
                text = input('Import Text, or leave it empty to Cancel.\n>> ')
                if text == '':
                    break
                else:
                    graphy.dec(text, 'text')
                    break
            elif chose == '3':
                break
            else:
                print('Invalid!')
    elif chose in ['HELP', 'help', 'Help', '3']:
        os.system('clear')
        print_colorful('Menu > Help & About', 'blue')
        print_colorful('-' * 69, 'purple')
        print(values.about)
        print('Trust it. powered by SHA256!'),
        print_colorful('created by My own', 'red2')
        print('2019.Jun.08')
        print_colorful('>>', 'red2')
        print_colorful('Github: Github.com/ccxa', 'blue')
        print_colorful('>>', 'red2')
        print_colorful('-' * 69, 'purple')
        note = input('')
    elif chose == '4':
        os.system('clear')
        exit()
    else:
        print('>> Invalid Input !')
