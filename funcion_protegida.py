# -*- coding:utf-8 -*-

def protected(funcion_decoradora):

    def wrapper(password):

        if password == 'platzi':
            return funcion_decoradora()
        else:
            print('Contrasena es incorrecta')
    return wrapper

@protected
def protected_function():
    print('Tu contrasena es correcta.')


if __name__ == '__main__':
    password = str(raw_input('Ingresa tu Contrasena: '))
    protected_function(password)