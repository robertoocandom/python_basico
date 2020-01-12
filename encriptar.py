# -*- coding: utf-8 -*-

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def encriptar(mensaje):
    palabras = mensaje.split(' ')
    cypher_message = []

    for palabra in palabras:
        palabra_cifrada = ''
        for letra in palabra:
            palabra_cifrada += KEYS[letra]
        cypher_message.append(palabra_cifrada)

    return ' '.join(cypher_message)

def desencriptar(mensaje):
    palabras = mensaje.split(' ')
    descifrar_mensaje = []

    
    for cifrada in palabras:
        palabra_descifrada = ''
        for letra in cifrada:

            for key, value in KEYS.items():
                if value == letra:
                    palabra_descifrada += key
        descifrar_mensaje.append(palabra_descifrada)
    return ' '.join(descifrar_mensaje)

def run():
    while True:
        command = str(raw_input('''----*----*----*----*----*----*----*----*----*
        
        Bienvenido a Criptografía, Que deseas hacer?
        
        [c]ifrar mensaje
        [d]escifrar mensaje
        [s]alir
        '''))

        if command == 'c':
            mensaje = str(raw_input('Escribe tu mensaje que deseas cifra: '))
            mensaje_cifrado = encriptar(mensaje)
            print(mensaje_cifrado)
        elif command == 'd':
            mensaje = str(raw_input('Escribe tu mensaje cifrado: '))
            mensaje_descifrado = desencriptar(mensaje)
            print(mensaje_descifrado)
        elif command == 's':
            print('salir')
            break
        else:
            print('Comando no Encontrado! Porfavor Escoja una opcion valida!')

if __name__ == '__main__':
    print('M E N S A J E S   C I F R A D O S')
    run()
