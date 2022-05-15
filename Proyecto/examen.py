"""
El programa mostrará el examen de opción multiple
"""
import time
import random
import os
import json

class examen:    
    
    def opcionMultiple(self,nombreAlu,identificador,estres):
        for examen in os.listdir():
                if examen.endswith(".json"):
                    if(examen == 'Prueba.json'):
                        nombre = examen
        file = open(nombre)
        data =json.load(file)
        
        for examen in os.listdir():
            if examen.endswith(".json"):
                if(examen == 'Respuestas_'+data['Info']['Examen']+'_'+str(identificador)+'.json'):
                    nombre = examen
        
        if(nombre == 'Respuestas_'+data['Info']['Examen']+'_'+str(identificador)+'.json'):
            print('\nYa has respondido este examen\n')
        else:
            respuestasFinales = {}
            informacion = {}
            respuestas = []
            finalizado1 = 0
            finalizado2 = 0
            indice1 = 0
            indice2 = 0
            contador = 0
            salida = ''
            nombre = ''
            
            informacion['Nombre'] = nombreAlu
            informacion['ID'] = identificador
            informacion['Test'] = estres
            
            respuestasFinales['Informacion'] = informacion
            
            preguntas = []
            print('\nNombre del examen: '+data['Info']['Examen'])
            print('\nAsignatura: '+data['Info']['Asignatura'])
            print('\n\nExamen de opción multiple')
            
            #La lista numeros hara que el examen se muestre diferente cada vez que alguien entre
            numeros = random.sample(range(len(data.items())-1), len(data.items())-1)
            
            while(contador < len(data.items())-1):
                preguntas.append(data['Pregunta '+str(numeros[contador]+1)])
                contador+=1
            
            while(finalizado1 == 0):
                
                respuestas.clear()
                
                print('\nPregunta '+str(indice1+1)+'.\n'+preguntas[indice1][indice2])
                respuestas.append('Pregunta '+str(indice1+1)+'. '+preguntas[indice1][indice2])
                """El ciclo va a servir para desplegar todas las preguntas y,
                a su vez, va a servir para poder elegir la opción correcta"""
                while(finalizado2 == 0):
                  indice2+=1
                  salida = preguntas[indice1][indice2]
                  if(isinstance(salida,int)):
                      inicio=time.time()
                      respuesta=int(input('Seleccion: '))
                      if(salida == respuesta):
                          fin=time.time()
                          respuestas.append(str(indice1+1)+'. Respuesta correcta')
                          respuestas.append('Tiempo en contestar: '+str(int(fin-inicio))+' segundos')
                          finalizado2 = 1
                      else:
                          fin=time.time()
                          respuestas.append(str(indice1+1)+'. Respuesta incorrecta')
                          respuestas.append('Tiempo en contestar: '+str(int(fin-inicio))+' segundos')
                          finalizado2 = 1
                  else:
                      print('\n'+preguntas[indice1][indice2])
                indice1+=1
                finalizado2 = 0
                indice2 = 0
                
                respuestasFinales['Pregunta '+str(indice1)] = respuestas.copy()
                
                if(len(preguntas) == indice1):
                    finalizado1=1
                    
            with open('Respuestas_'+data['Info']['Examen']+'_'+str(identificador)+'.json', 'a') as outfile:
                json.dump(respuestasFinales, outfile)
                    
            #examen().retroalimentacion()
            file.close()
    
        
    """
    La funcion solucion va a mostrar el resultado que obtuvo el alumno en el examen,
    ademas de que va a mostrar el tiempo que se tomo cada persona al resolver cada
    pregunta
    """
    def solucionDocente(self,data):
        contador1 = 0
        contador2 = 0
        respuestas = []
        print('\nEl estudiante con identificador '+str(data['Informacion']['ID'])+' es el siguiente.')
        print('\nTen en consideración que su resultado del test es '+data['Informacion']['Test'])
        print('\nEl resultado del examen es el siguiente: \n')
        for i in range(len(data)-1):
            respuestas = data['Pregunta '+str(i+1)]
            print(respuestas[1]+'. '+respuestas[2]+'\n')
            if(respuestas[1].__contains__('Respuesta correcta') is True):
                contador1+=1
            else:
                contador2+=1
        print('\n\n\t\tTotal correctas: '+str(contador1)+'\t\tTotal incorrectas: '+str(contador2))
    
    def solucionAlumno(self,data):
        contador1 = 0
        contador2 = 0
        print('\nEl resultado del examen es el siguiente: \n')
        for i in range(len(data)-1):
            respuestas = data['Pregunta '+str(i+1)]
            print(respuestas[1]+'. '+respuestas[2]+'\n')
            if(respuestas[1].__contains__('Respuesta correcta') is True):
                contador1+=1
            else:
                contador2+=1
        print('\n\n\t\tTotal correctas: '+str(contador1)+'\t\tTotal incorrectas: '+str(contador2))

    
    """Ofrece una pequeña retroalimentacion al terminar el examen"""
    def retroalimentacion(self):
        finalExamen=['Mucho exito','Todo saldra bien',
                     'Tomate un descanso después del examen','Escucha la musica que te gusta']
        retro = random.randint(0, len(finalExamen)-1)
        print('\n'+finalExamen[retro]+'\n')