def print_colorful(text, color):
    if color == "green":
        print("\033[34m{}\033[00m".format(text))
    elif color == "dark_green":
        print("\033[32m{}\033[00m".format(text))
    elif color == "red":
        print("\033[91m{}\033[00m".format(text))
    elif color == "blue":
        print("\033[36m{}\033[00m".format(text))

