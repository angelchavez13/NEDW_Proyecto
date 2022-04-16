"""
El programa mostrará el examen de opción multiple
"""
import time

class examen:    
    def opcionMultiple(self,nombre,asignatura,numero):
        respuestas = []
        tiempo = []
        finalizado1 = 0
        finalizado2 = 0
        indice1 = 0
        indice2 = 0
        salida = ''
        preguntas = [['Pregunta de prueba','1.XD','2.OLV','3.SUS',3],
                     ['Pregunta de prueba 2','1.Tilin','2.Ete sech','3.SUS',1]]
        #examenFinal = open("Transacciones.txt","a")
        print('\nNombre del examen: '+nombre)
        print('\nAsignatura: '+asignatura)
        print('\nNumero total de preguntas: '+str(numero))
        print('\n\nExamen de opción multiple')
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
        return respuestas,tiempo
        #examenFinal.close() 
        
    """
    La funcion solucion va a mostrar el resultado que obtuvo el alumno en el examen,
    ademas de que va a mostrar el tiempo que se tomo cada persona al resolver cada
    pregunta
    """
    def solucion(self,respuestas,tiempo):
        print('\nEl resultado del examen es el siguiente: \n')
        for i in range(len(respuestas)):
            print(respuestas[i]+'. Tiempo: '+tiempo[i]+' segundos\n')
