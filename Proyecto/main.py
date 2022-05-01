# -*- coding: cp1252 -*-
"""
Proyecto. Examenes de opcion multiple
"""

import examen as ex
import time

class principal:    
    def main(self):
        seleccion = 0
        salida = 0
        print('\t\t\tElaborador de examenes.')
        while(salida == 0):
            print('\t\t\t\t\tMenu\n1. Docente\n2. Estudiante\n3. Salida')
            seleccion = int(input('Selecciona una opcion: '))
            if(seleccion == 1):
                principal().docente()
            elif(seleccion == 2):
                principal().estudiante()
            elif(seleccion == 3):
                print('\n\nSaliendo del programa\n\n')
                salida = 1
            else:
                print('\n\nOpcion no valida\n\n')
    
    def docente(self):
        respuestas = []
        tiempo = []
        nombre = ''
        asignatura = ''
        numero = ''
        salida = 0
        while(salida == 0):
            print('\n\t\t\tMenu del docente\n1. Crear examen\n2. Realizar examen\n3. Ressultados\n4. Regresar\n')
            opcion = int(input('Selecciona una opcion: '))
            
            if(opcion == 1):
                nombre = input('Nombre del examen: ')
                asignatura = input('Nombre de la asignatura: ')
                numero = int(input('Numero total de preguntas: '))
            elif(opcion == 2):
            #En esta opcion se debe de crear primero un examen, de lo contrario se
            #mostrara un mensaje al usuario diciendole esto. Además, se va a mostrar
            #que se tomo para realizar el examen; el resultado estara en segundos.
                if(nombre == '' or asignatura == '' or numero == ''):
                    print('\nPrimero debes de crear un examen para poder acceder\n')
                else:
                    inicio=time.time()
                    respuestas,tiempo = ex.examen().opcionMultiple(nombre,asignatura,numero)
                    fin=time.time()
                    print('\nTiempo en que se resolvio el examen: '+str(int(fin-inicio))+' segundos')
            elif(opcion == 3):
            #Esta opcion va a mostrar el resultado del examen. En caso de que no se
            #tenga ninguna respuesta se va a mandar un mensaje al usuario
                if(len(respuestas) == 0):
                    print('\nNo hay ninguna respuesta\n')
                else:
                    ex.examen().solucion(respuestas,tiempo)
            elif(opcion == 4):
                salida = 1
            else:
                print('\nOpcion no valida\n')
        print('\nRegresando al menu principal\n')
    
    def estudiante(self):
        respuestas = []
        salida = 0
        while(salida == 0):
            print('\n\t\t\tMenu del estudiante\n1. Crear examen\n2. Realizar examen\n3. Ressultados\n4. Regresar\n')
            opcion = int(input('Selecciona una opcion: '))
            
            if(opcion == 1):
                nombre = input('Nombre del examen: ')
                asignatura = input('Nombre de la asignatura: ')
                numero = int(input('Numero total de preguntas: '))
            elif(opcion == 2):
            #En esta opcion se debe de crear primero un examen, de lo contrario se
            #mostrara un mensaje al usuario diciendole esto. Además, se va a mostrar
            #que se tomo para realizar el examen; el resultado estara en segundos.
                if(nombre == '' or asignatura == '' or numero == ''):
                    print('\nPrimero debes de crear un examen para poder acceder\n')
                else:
                    inicio=time.time()
                    respuestas,tiempo = ex.examen().opcionMultiple(nombre,asignatura,numero)
                    fin=time.time()
                    print('\nTiempo en que se resolvio el examen: '+str(int(fin-inicio))+' segundos')
            elif(opcion == 3):
            #Esta opcion va a mostrar el resultado del examen. En caso de que no se
            #tenga ninguna respuesta se va a mandar un mensaje al usuario
                if(len(respuestas) == 0):
                    print('\nNo hay ninguna respuesta\n')
                else:
                    ex.examen().solucion(respuestas,tiempo)
            elif(opcion == 4):
                salida = 1
            else:
                print('\nOpcion no valida\n')
        print('\nRegresando al menu principal\n')

prin = principal()
prin.main()
