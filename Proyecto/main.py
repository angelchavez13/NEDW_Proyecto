# -*- coding: cp1252 -*-
"""
Proyecto. Examenes de opción multiple
"""

import examen as ex

class principal:    
    def main(self):
        nombre = ''
        asignatura = ''
        numero = ''
        salida = 0
        print('\t\t\tElaborador de ex�menes.')
        while(salida == 0):
            print('\t\t\t\nMenu\n1. Crear examen\n2. Realizar examen\n3. Salir\n')
            opcion = int(input('Selecciona una opci�n: '))
            
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
                print('\nOpci�n no valida\n')
        print('\nSaliendo del programa')

prin = principal()
prin.main()
