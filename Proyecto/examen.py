"""
El programa mostrará el examen de opción multiple
"""
import time
import random
import os
import json

class examen:    
    def opcionMultiple(self):
        respuestas = []
        tiempo = []
        finalizado1,finalizado2,indice1,indice2 = 0
        contador = 1
        salida = ''
        nombre = ''
        for examen in os.listdir():
            if examen.endswith(".json"):
                if(examen == 'Prueba.json'):
                    nombre = examen
        file = open(nombre)
        data =json.load(file)
        preguntas = []
        print('\nNombre del examen: '+data['Info']['Examen'])
        print('\nAsignatura: '+data['Info']['Asignatura'])
        #print('\nNumero total de preguntas: '+str(numero))
        print('\n\nExamen de opción multiple')
        
        while(contador < len(data.items())):
            preguntas.append(data['Pregunta '+str(contador)])
            contador+=1
        
        while(finalizado1 == 0 or indice1 == 15):
            print('\n'+preguntas[indice1][indice2])
            """El ciclo va a servir para desplegar todas las preguntas y,
            a su vez, va a servir para poder elegir la opción correcta"""
            while(finalizado2 == 0 or indice2 == 15):
              indice2+=1
              salida = preguntas[indice1][indice2]
              if(isinstance(salida,int)):
                  inicio=time.time()
                  respuesta=int(input('Seleccion: '))
                  if(salida == respuesta):
                      fin=time.time()
                      tiempo.append(str(int(fin-inicio)))
                      respuestas.append(str(indice1+1)+'. Respuesta correcta')
                      finalizado2 = 1
                  else:
                      fin=time.time()
                      tiempo.append(str(int(fin-inicio)))
                      respuestas.append(str(indice1+1)+'. Respuesta incorrecta')
                      finalizado2 = 1
              else:
                  print('\n'+preguntas[indice1][indice2])
            indice1+=1
            finalizado2 = 0
            indice2 = 0
            if(len(preguntas) == indice1):
                finalizado1=1
        #examen().retroalimentacion()
        file.close()
        return respuestas,tiempo
    
        
    """
    La funcion solucion va a mostrar el resultado que obtuvo el alumno en el examen,
    ademas de que va a mostrar el tiempo que se tomo cada persona al resolver cada
    pregunta
    """
    def solucion(self,respuestas,tiempo):
        contador1 = 0
        contador2 = 0
        print('\nEl resultado del examen es el siguiente: \n')
        for i in range(len(respuestas)):
            print(respuestas[i]+'. Tiempo: '+tiempo[i]+' segundos\n')
            if(respuestas[i].__contains__('Respuesta correcta') is True):
                contador1+=1
            else:
                contador2+=1
        print('\n\n\t\tTotal buenas: '+str(contador1)+'\t\tTotal incorrectas: '+str(contador2))
    
    """Ofrece una pequeña retroalimentacion al terminar el examen"""
    def retroalimentacion(self):
        finalExamen=['Mucho exito','Todo saldra bien',
                     'Tomate un descanso después del examen','Escucha la musica que te gusta']
        retro = random.randint(0, len(finalExamen)-1)
        print(finalExamen[retro])