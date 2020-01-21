# --*-- coding: utf-8 --*--
def run(numero):
    try:
        num = int(numero)
    except:
        print('****************************************')
        print('***** El numero debe ser un Entero *****')
        print('****************************************')
        return

    ciclo = range(int(num)+1)
    suma = 0
    for idx in ciclo:
        suma = suma + ciclo[idx]
    return suma

if __name__ == '__main__':
    
    while True:
        print('S U M A   R E C U R S I V A (Presione "0" para salir)')
        numero = str(input('Digite un número Entero para suma recursiva: '))
        if numero == '0':
            print('Salir')
            break
        else:
            resultado = run(numero)
            if resultado: 
                print('El total de la suma recursiva es: {}'.format(resultado))