# --*-- coding:utf-8 --*--

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = str(raw_input('Escribe el nombre del País: ')).lower()

    try:
        print('La poblacion de {} es de {} millones de personas'.format(country, countries[country]))
    except KeyError:
        print(':( Lo sentimos! No tenemos el dato de la poblacion {}!'.format(country))

