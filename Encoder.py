import sys
import values
import graphy

args = sys.argv

if args[1] in ['-h', '--help']:
    print(values.help_message)

elif args[1] == "-e":
    if args[2] == "-t":
        _text = input("Enter text to encrypt:\n>> ")
        graphy.enc(_text, 'text')
    elif args[2] == "-f":
        file_path = args[3]
        graphy.enc(file_path, "file")

elif args[1] == "-d":
    if args[2] == "-t":
        _text = input("Enter encrypted text to decrypt:\n>> ")
        graphy.dec(_text, 'text')
    elif args[2] == "-f":
        file_path = args[3]
        graphy.dec(file_path, "file")
