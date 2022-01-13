import sys
import ui
import values
import graphy

args = sys.argv

# If there is only one argument other than 'Encode.py' file name
if len(args) == 2:

    if args[1] in ['-h', '--help']:
        print(values.help_message)

    # If mentioned argument was incorrect
    else:
        print(values.invalid_arg)

# If there are more than two argument, extra args will be ignored
elif len(args) > 2:

    # Encrypting text directly
    if args[1] == "-e" and args[2] == "-t":
        _text = input("Enter text to encrypt:\n>> ")
        secret = input("Enter a secret to encrypt string:\n>> ")
        graphy.enc(_text, secret, 'text')

    # Encrypting file by its path
    elif args[1] == "-e" and args[2] == "-f":
        try:
            file_path = args[3]
            secret = input("Enter a secret to encrypt string:\n>> ")
            graphy.enc(file_path, secret, "file")
        except IndexError:
            ui.print_colorful("Error! Input path: -f <file_path>")

    # Decrypting text directly
    elif args[1] == "-d" and args[2] == "-t":
        _text = input("Enter encrypted text to decrypt:\n>> ")
        secret = input("Enter secret to decrypt the data:\n>> ")
        graphy.dec(_text, secret, 'text')

    # Decrypting file by its path
    elif args[1] == "-d" and args[2] == "-f":
        try:
            file_path = args[3]
            secret = input("Enter a secret to decrypt file:\n>> ")
            graphy.dec(file_path, secret, "file")
        except IndexError:
            ui.print_colorful("Error! Input path: -f <file_path>")

    # If those arguments where incorrect
    else:
        print(values.invalid_arg)

# If there is no argument other than 'Encoder.py'
else:
    print(values.invalid_arg)
