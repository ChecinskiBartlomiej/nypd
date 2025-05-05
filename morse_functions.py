def morse_encrypt(s):
    tomorse = {
        " " : "_",
        "a" : ".-",
        "b" : "-...",
        "c" : "-.-.",
        "d" : "-..",
        "e" : ".",
        "f" : "..-.",
        "g" : "--.",
        "h" : "....",
        "i" : "..",
        "j" : ".---",
        "k" : "-.-",
        "l" : ".-..",
        "m" : "--",
        "n" : "-.",
        "o" : "---",
        "p" : ".--.",
        "q" : "--.-",
        "r" : ".-.",
        "s" : "...",
        "t" : "-",
        "u" : "..-",
        "w" : ".--",
        "v" : "...-",
        "x" : "-..-",
        "y" : "-.--",
        "z" : "--.."
    }

    word = ""
    for letter in s:
        if letter in tomorse:
            word += tomorse[letter] + " "
        else:
            word += letter + " "
    return word

def morse_decrypt(s):
    toletters = {
        "_" : " ",
        ".-" : "a",
        "-..." : "b",
        "-.-." : "c",
        "-.." : "d",
        "." : "e",
        "..-." : "f",
        "--." : "g",
        "...." : "h",
        ".." : "i",
        ".---" : "j",
        "-.-" : "k",
        ".-.." : "l",
        "--" : "m",
        "-." : "n",
        "---" : "o",
        ".--." : "p",
        "--.-" : "q",
        ".-." : "r",
        "..." : "s",
        "-" : "t",
        "..-" : "u",
        ".--" : "w",
        "...-" : "v",
        "-..-" : "x",
        "-.--" : "y",
        "--.." : "z"
    }

    word = ""
    sign = ""
    for letter in s + ' ':
        if letter == '.' or letter == '-' or letter == '_':
            sign += letter
        elif sign in toletters:
            word += toletters[sign]
            sign = ""
        else:
            word += letter
    return word
