# -*- coding:utf-8 -*- 
import csv


class Contacto:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []
    
    def add(self, name, phone, email):
        contact = Contacto(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('--*--*--*--*--*--*--*--*')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))       
        print('--*--*--*--*--*--*--*--*')

    def _not_found(self):
        print('************************************************')
        print('El Usuario NO se encuentra en nuestros registros!')
        print('************************************************')

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                return contact
        else:
            self._not_found()
            return False

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow( ('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))




    def edit(self, name, phone, email):
        print('---**** Presione "Enter" si no desea modificar la Informacion! ****---')
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                name = str(raw_input('Escribe el nuevo nombre del contacto ({}): '.format(name)))
                phone = str(raw_input('Escribe el nuevo numero de Telefono: ({}): '.format(phone)))
                email = str(raw_input('Escribe el nuevo email del contacto: ({}):'.format(email)))
                if name != '':
                    contact.name = name
                if phone != '':
                    contact.phone = phone
                if email != '':
                    contact.email = email
                self._save()


def run():

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
           
            contact_book.add(row[0], row[1], row[2])


    while True:
        command = str(raw_input('''
            Que deseas Hacer?
            ---*---*---*---*---*---*---

            [A] Añadir contacto
            [C] Actualizar contacto
            [B] Buscar
            [E] Eliminar Contacto
            [L] Listar contacto
            [S] Salir        
        '''))
 
        if command == 'A':
            print('Añadiendo Contacto:')
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el numero de Telefono: '))
            email = str(raw_input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == 'C':
            print('Actualizando Contacto:')
            name = str(raw_input('Escribe el nombre del contacto que Deseas Actualizar: '))
            encontrado = contact_book.search(name)

            if encontrado:
                contact_book.edit(encontrado.name, encontrado.phone, encontrado.email)
                print('*****- Los Datos Fueron Actualizados con Exito! -*****')

        elif command == 'B':
            print('Buscando Contacto:')
            name = str(raw_input('Escribe el nombre del contacto a Buscar: '))
            contact_book.search(name)

        elif command == 'E':
            print('Eliminando Contacto:')
            name = str(raw_input('Escribe el nombre del contacto a Eliminar: '))
            
            contact_book.delete(name)
            print('El Registro de {} ha sido borrado con exito'.format(name))

        elif command == 'L':
            print('Listando los Contactos:')
            contact_book.show_all()
        elif command == 'S':
            return False
        else:
            print('Comando no Reconocido!')



if __name__ == '__main__':
    print('B I E N V E N I D O   A   L A   A G E N D A   I N T E L I G E N T E')
    run()