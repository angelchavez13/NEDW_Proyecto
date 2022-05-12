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
import json


test = 0

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
        global test
        respuestas = []
        nombre = ''
        salida = 0
        while(salida == 0):
            print('\n\t\t\tMenu del docente\n1. Crear examen\n2. Resultados\n3. Regresar\n')
            opcion = int(input('Selecciona una opcion: '))
            
            if(opcion == 1):
                cr.creador().crearExamen()
                print('\nAplicar test de estres a los alumnos\n1. Si\n2. No')
                prueba = int(input(''))
                if(prueba == 1):
                    test = 1
                    print('\nSe aplicara el test seleccionado\n')
            elif(opcion == 2):
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
            elif(opcion == 3):
                salida = 1
            else:
                print('\nOpcion no valida\n')
        print('\nRegresando al menu principal\n')
    
    """Hará casí lo mismo que la función del profesor, solo que será para 
    el estudiante el examen y el resultado"""
    def estudiante(self):
        nombre = str(input('Nombre del estudiante: '))
        identificador = int(input('identificador: '))
        salida = 0
        
        while(salida == 0):
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
