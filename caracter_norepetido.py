# --*-- coding:utf-8 --*--

def primer_caracter_no_repetido(secuencia_de_caracteres):
    lista = []
    for idx in secuencia_de_caracteres:
        lista += idx
    tupla = (lista)
    print(tupla)
    for idx in tupla:
        caracter = tupla.count(idx)
        if caracter == 1:
            return idx
        else:
            continue
    else:
        return '_'

if __name__ == '__main__':

    print('Revision de primer caracter no repedido en una frase!')
    print('-----*-------*-------*-------*-------*-------*------')

    secuencia_de_caracteres = str(raw_input('Digite la secuencia de Caracteres: '))
    result = primer_caracter_no_repetido(secuencia_de_caracteres)

    if result == '_':
        print('Todos los caracteres se Repiten!')
    else:
        print('El primer caracter No repetido es: {}'.format(result))


