# -*- coding: utf-8 -*-
"""
El propósito de este trabajo es recoger información sobre la influencia del 
estrés en el rendimiento académico. 
1. NUNCA 2. RARA VEZ 3. A VECES 4. CASI SIEMPRE 5. SIEMPRE
EVALUACIÓN: 
    5 – 19 nivel de estrés Bajo 
    20 - 39 niveles de estrés Medio 
    40 - 50 niveles de estrés Alto"""

import json
import os

class creador:
    
    def crearExamen(self):
        preguntasFinales = {}
        pregunta = []
        informacion = {}
        salida,indice,inciso = 0
        print('\nEl programa tiene como objetivo crear examenes. ')
        print('\nSin embargo, lo importante es ofrecerle al estudiante retroalimenación cuando se equivoque en alguna pregunta')
        print('\nPor lo tanto, te pedimos que ingreses una retroalimentacion que sea bastante general.')
        informacion['Asignatura']=input('Nombre de la asignatura: ')
        informacion['Examen'] = input('Nombre del examen: ')
        preguntasFinales['Info'] = informacion
        while(salida == 0):
            pregunta.clear()
            indice += 1
            pregunta.append(input('Pregunta: '))
            while(inciso < 3):
                pregunta.append('-'+input('Inciso: '))
                if(inciso == 2):
                    pregunta.append(int(input('Inciso correcto: ')))
                inciso +=1
            preguntasFinales['Pregunta '+str(indice)] = pregunta.copy()
            if(indice >= 3):
                print('\n¿Deseas añadir otra pregunta?\n\t1.Si\n\t2.No')
                dec = int(input())
                if(dec == 2):
                    salida = 1
            elif(indice == 10):
                salida = 1
                print('\nHaz alcanzado el limite de las preguntas\n')
            inciso = 0
        with open('Prueba.json', 'a') as outfile:
            json.dump(preguntasFinales, outfile)
            
        print(preguntasFinales)
    
    def testEstres(self):
        preguntas = []
        finalizado1,final,indice1 = 0
        contador = 1
        nombre = ''
        
        for examen in os.listdir():
            if examen.endswith(".json"):
                if(examen == 'Test_estres.json'):
                    nombre = examen
        file = open(nombre)
        data =json.load(file)
        
        while(contador < len(data.items())):
            preguntas.append(data['Pregunta '+str(contador)])
            contador+=1
        
        while(finalizado1 == 0):
            print(str(indice1+1)+'. '+preguntas[indice1])
            """El ciclo va a servir para desplegar todas las preguntas y,
            a su vez, va a servir para poder elegir la opción correcta"""
            respuesta=int(input('Seleccion: \n'))
            final = final + respuesta
            indice1+=1
            if(len(preguntas) == indice1):
                finalizado1=1
        if(final >= 5 and final <= 19):
            print('Estres bajo')
        elif(final >= 20 and final <= 39):
            print('Estres medio')
        elif(final >= 40 and final <= 50):
            print('Estres alto')
        file.close()