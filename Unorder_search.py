# -*- coding: utf-8 -*-

def search_number(numbers_list, number_to_find, low, high):
    
    if low > high:
        return False

    mid = (high + low) / 2
    if numbers_list[mid] == number_to_find:
        return True
    elif numbers_list[mid] > number_to_find:
        return search_number(numbers_list, number_to_find, low, mid -1)
    else:
        return search_number(numbers_list, number_to_find, mid + 1, high) 


if __name__ == '__main__':
    unorder_numbers_list = [12, 24, 35, 47, 58, 61, 72, 83, 39, 11, 31, 25, 30, 9, 22, 26, 27, 49, 33, 37, 44, 110]
    numbers_list = sorted(unorder_numbers_list)
    number_to_find = int(raw_input('Cual es el Numero que deseas Buscar: '))
    
    result = search_number(numbers_list, number_to_find, 0, len(numbers_list) - 1)

    if result == True:
        print('El Numero Sí esta en la lista!')
    else:
        print("El numero No esta en la lista")