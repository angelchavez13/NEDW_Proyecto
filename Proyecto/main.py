# -*- coding: cp1252 -*-
# encoding: utf-8
"""
Universidad Nacional Autónoma de Mexico
Negocios electrónicos y desarrollo web. Grupo: 1.

Proyecto Final. Elaborador de examenes.

Integrantes del equipo:
    -Chavez Garcia Jesus Angel
    -Cruz Plata Eduargo
"""

import examen as ex
import creador as cr
import time
import os
<<<<<<< HEAD
=======
import json

>>>>>>> e2dde85b89d85f5efb918dc430415c4b895123b2

test = 0

class principal:  
    
    def main(self):
        seleccion = 0
        salida = 0
        os.system("cls")
        print('\t\t\tElaborador de examenes.')
        #Menú para mostrar que es lo que se quiere hacer
        while(salida == 0):
            print('\t\t\t\t\tMenu\n1. Docente\n2. Estudiante\n3. Salida')
            seleccion = int(input('Selecciona una opcion: '))

            #Docente
            if(seleccion == 1):
                principal().docente()

            #Estudiante
            elif(seleccion == 2):
                principal().estudiante()

            #Salida
            elif(seleccion == 3):
                print('\n\nSaliendo del programa\n\n')
                salida = 1
            else:
                print('\n\nOpcion no valida\n\n')

    #Caso de ser profesor    
    def docente(self):
        global test
        respuestas = []
        nombre = ''
        salida = 0
        #Se repite el ciclo si es que no se selecciona la opción de regresar
        
        while(salida == 0):
<<<<<<< HEAD
            os.system("cls")
            print('\n\t\t\tMenu del docente\n1. Crear examen\n2. Realizar examen\n3. Resultados\n4. Regresar\n')
=======
            print('\n\t\t\tMenu del docente\n1. Crear examen\n2. Resultados\n3. Regresar\n')
>>>>>>> e2dde85b89d85f5efb918dc430415c4b895123b2
            opcion = int(input('Selecciona una opcion: '))
            
            #CREAR EXAMEN
            if(opcion == 1):
                #Se manda a llamar a una función de creador
                cr.creador().crearExamen()
                print('\nAplicar test de estres a los alumnos\n1. Si\n2. No')
                prueba = int(input(''))
                if(prueba == 1):
                    test = 1
<<<<<<< HEAD


=======
                    print('\nSe aplicara el test seleccionado\n')
            elif(opcion == 2):
<<<<<<< HEAD
                """Se le mostrara al docente todas las personas que han realizado 
                el examen así como los resultados"""
                print('\nLas siguientes personas han respondido el examen:\n')
                indice = 1
                for examen in os.listdir():
                    if examen.__contains__('Respuestas'):
                        nombre = examen
                        print(str(indice)+'. '+nombre)
                        respuestas.append(nombre)
                        indice +=1

                eleccion = int(input('Que archivo deseas abrir: '))
                file = open(respuestas[eleccion-1])
                data =json.load(file)       
                ex.examen().solucionDocente(data)
=======
>>>>>>> e2dde85b89d85f5efb918dc430415c4b895123b2
            #En esta opcion se debe de crear primero un examen, de lo contrario se
            #mostrara un mensaje al usuario diciendole esto. Además, se va a mostrar
            #que se tomo para realizar el examen; el resultado estara en segundos.
            elif(opcion == 2):
                #If para verificar si existe un examen
                if(nombre == '' or asignatura == '' or numero == ''):
                    print('\nPrimero debes de crear un examen para poder acceder\n')

                #Si existe vamor a hacer el examen
                else:
                    inicio=time.time()
                    #Se llamara a una función en Examen para resolver el examen
                    respuestas,tiempo = ex.examen().opcionMultiple(nombre,asignatura,numero)
                    fin=time.time()
                    print('\nTiempo en que se resolvio el examen: '+str(int(fin-inicio))+' segundos')
<<<<<<< HEAD


            #Esta opcion va a mostrar el resultado del examen. En caso de que no se
            #tenga ninguna respuesta se va a mandar un mensaje al usuario
            elif(opcion == 3):
                if(len(respuestas) == 0):
                    os.system("cls")
                    print('\nNo hay ninguna respuesta\n')
                    input("")
                    os.system("cls")
                else:
                    os.system("cls")
                    ex.examen().solucion(respuestas,tiempo)
                    input("")


            #SALIDA
            elif(opcion == 4):
=======
>>>>>>> 80370c1076fcfeb72719468b0f4b373ca1e02d27
            elif(opcion == 3):
>>>>>>> e2dde85b89d85f5efb918dc430415c4b895123b2
                salida = 1
            else:
                os.system("cls")
                print('\nOpcion no valida\n')
                time.sleep(1)

    
    """Hará casí lo mismo que la función del profesor, solo que será para 
    el estudiante el examen y el resultado"""
    def estudiante(self):
<<<<<<< HEAD
        nombre = str(input('Nombre del estudiante: '))
        identificador = int(input('identificador: '))
=======
        respuestas = []
        tiempo = []
>>>>>>> 80370c1076fcfeb72719468b0f4b373ca1e02d27
        salida = 0
<<<<<<< HEAD
        #Seguirá mostrando el menú hasta presionar 3
=======
        
>>>>>>> e2dde85b89d85f5efb918dc430415c4b895123b2
        while(salida == 0):
            os.system("cls")
            print('\n\t\t\tMenu del estudiante\n1. Realizar examen\n2. Resultados\n3. Regresar\n')
            opcion = int(input('Selecciona una opcion: '))
            if(opcion == 1):
                if(test == 1):
                    estres = cr.creador().testEstres()
                else:
                    estres = 'No aplica'
                inicio=time.time()
                ex.examen().opcionMultiple(nombre,identificador,estres)
                fin=time.time()
                print('\nTiempo en que se resolvio el examen: '+str(int(fin-inicio))+' segundos')
            elif(opcion == 2):
                for examen in os.listdir():
                    if examen.__contains__(str(identificador)):
                        nombre = examen

                file = open(nombre)
                data =json.load(file)   
                ex.examen().solucionAlumno(data)
            elif(opcion == 3):
                salida = 1
            else:
                print('\nOpcion no valida\n')
        print('\nRegresando al menu principal\n')


prin = principal()
prin.main()
