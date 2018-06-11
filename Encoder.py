import sys
import ui
import values
import graphy

args = sys.argv

if args[1] in ['-h', '--help']:
    print(values.help_message)

elif args[1] == "-e" and args[2] == "-t":
    _text = input("Enter text to encrypt:\n>> ")
    secret = input("Enter a secret to encrypt string:\n>> ")
    graphy.enc(_text, secret, 'text')

elif args[1] == "-e" and args[2] == "-f":
    try:
        file_path = args[3]
        secret = input("Enter a secret to encrypt string:\n>> ")
        graphy.enc(file_path, secret, "file")
    except IndexError:
        ui.print_colorful("Error! Input path: -f <file_path>")

elif args[1] == "-d" and args[2] == "-t":
    _text = input("Enter encrypted text to decrypt:\n>> ")
    secret = input("Enter secret to decrypt the data:\n>> ")
    graphy.dec(_text, secret, 'text')

elif args[1] == "-d" and args[2] == "-f":
    try:
        file_path = args[3]
        secret = input("Enter a secret to decrypt file:\n>> ")
        graphy.dec(file_path, secret, "file")
    except IndexError:
        ui.print_colorful("Error! Input path: -f <file_path>")
