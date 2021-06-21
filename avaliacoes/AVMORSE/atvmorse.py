def para_codigo_morse(text):
    codigo = { 'a':'.-', 'b':'-...',
                        'c':'-.-.', 'd':'-..', 'e':'.',
                        'f':'..-.', 'g':'--.', 'h':'....',
                        'i':'..', 'j':'.---', 'k':'-.-',
                        'l':'.-..', 'm':'--', 'n':'-.',
                        'o':'---', 'p':'.--.', 'q':'--.-',
                        'r':'.-.', 's':'...', 't':'-',
                        'u':'..-', 'v':'...-', 'w':'.--',
                        'x':'-..-', 'y':'-.--', 'z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-', ' ':'|'}

    morse_codigo = ""

    for x in text:
        morse_codigo += codigo[x.lower()]

    return morse_codigo

text = input("Digite o texto para ser convertido a morse: ")
print(para_codigo_morse(text))
