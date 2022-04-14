"""
Se utiliza la siguiente libreria para poder leer texto de un PDF.
https://github.com/jsvine/pdfplumber

Libreria para leer texto de una imagen: pip install pytesseract
"""

import examen as ex

class principal:    
    def main(self):
        nombre = ''
        asignatura = ''
        numero = ''
        salida = 0
        print('\t\t\tElaborador de exámenes.')
        while(salida == 0):
            print('\t\t\t\nMenu\n1. Crear examen\n2. Realizar examen\n3. Salir\n')
            opcion = int(input('Selecciona una opción: '))
            
            if(opcion == 1):
                nombre = input('Nombre del examen: ')
                asignatura = input('Nombre de la asignatura: ')
                numero = int(input('Numero total de preguntas: '))
            elif(opcion == 2):
                if(nombre == '' or asignatura == '' or numero == ''):
                    print('\nXD\n')
                else:
                    ex.examen().opcionMultiple(nombre,asignatura,numero)
            elif(opcion == 3):
                salida = 1
            else:
                print('\nOpción no valida\n')
        print('\nSaliendo del programa')

prin = principal()
prin.main()