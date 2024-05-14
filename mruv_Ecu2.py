#Programa para el calculo de MRUV
#Ecuacion de la forma Vf= Vi +- a * t


#Funciones para calcular MRUV

#imports
import math  #operaciones
#grafica
import matplotlib.pyplot as plt
import numpy as np

#Calcular Velocidad final
def velocidadFinal():
    velIni = float(input("Ingrese la velocidad inicial (m/s): "))
    if(velIni < 0):
        print("La velocidad inicial no puede ser Negativa!") 
        return 0
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if(tiempo <= 0):
       print("El tiempo no puede ser negativo o cero")
       return 0
    acel = float(input("Ingrese la aceleracion: "))
    resultado = velIni + (acel * tiempo)
    return resultado

#Funcion calcular Velocidad inicial
def velocidadInicial():
    acel = float(input("Ingrese la aceleracion: "))
    velFin= float(input("Ingrese la velocidad final (m/s): "))
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if(tiempo <= 0): #tiempo negativo o cero
       print("El tiempo no puede ser negativo o cero")
       return 0
    resultado = velFin - (acel*tiempo)
    return abs(resultado) #retornando como positivo

#Funcion calcular ACELERACION
def aceleracion():
    velFin= float(input("Ingrese la velocidad final (m/s): "))
    velIni = float(input("Ingrese la velocidad inicial (m/s): ")) 
    if(velIni < 0):
        print("La velocidad inicial no puede ser Negativa!") 
        return 0
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if(tiempo <= 0):
       print("El tiempo no puede ser negativo o cero")
       return 0
    else:
        resultado = (velFin - velIni) / tiempo
        return resultado

#Funcion para calcular el tiempo
def tiempo():
    velFin= float(input("Ingrese la velocidad final (m/s): "))
    velIni = float(input("Ingrese la velocidad inicial (m/s): ")) 
    if(velIni < 0):
        print("La velocidad inicial no puede ser Negativa!") 
        return 0
    acel = float(input("Ingrese la aceleracion: "))
    if(acel == 0):
        print("Aceleracion cero Invalido: calculo MRUV")
        return 0 
    else: 
        resultado = (velFin - velIni) / acel
        resultado = abs(resultado) # tiempo:como resultado positivo
        resultadoRedondeo = math.ceil(resultado) #redondeo
        resultadoRedondeo = abs(resultadoRedondeo) # tiempo:como resultado positivo
        return resultado,resultadoRedondeo   

#Funcion para grafica
def grafica():
    velocidadInicial = float(input("Ingrese la velocidad inicial: "))
    aceleracion = float(input("Ingrese la aceleracion: "))    
    tiempo= np.arange(0.0, 10.0)
    desplazamiento = (velocidadInicial*tiempo)+((aceleracion*((tiempo)**2))/2)
    velocidadFinal = velocidadInicial+(aceleracion*tiempo)
    fig, ax = plt.subplots(2)
    ax[0].plot(desplazamiento)
    ax[1].plot(velocidadFinal)
    ax[0].set(ylabel = "Desplazamiento")
    ax[1].set(ylabel = "Velocidad", xlabel = "Tiempo")
    fig.suptitle("Analisis del cuerpo en MRUV")
    fig.savefig("MRUV")
    plt.show()

    
    
# Menu de Opciones
def menu():
    print("** ::::::::::::::::::::::::: **")
    print("::       Calculo de MRUV - Ecuacion 2    ::")
    print("** ::::::::::::::::::::::::: **")
    print("-------------------------------")
    print("| Calcular la velocidad final:            ->  1   |")
    print("| Calcular la velocidad inicial:    ->  2   |")
    print("| Calcular la aceleracion:          ->  3   |")
    print("| Calcular el tiempo     :          ->  4  |")
    print("| Presentar las graficas en funcion del tiempo -> 5")
    print("| Salir:                            ->  s   |")
    print("-----------------------------------")
    print("** ::::::::::::::::::::::::: **")
    print("\n")

#Opcion seleccionada
def opciones():
   opcion = input("Seleccione una Opción... ")
   return opcion

def errorOperacion():
    regresar = input("¿Quiere realizar una nueva operación [S/N]? ")
    return regresar

while True:
    menuOpciones = menu() #mostrar menu de opciones
    opc = opciones() 

    #opcion para salir 
    if opc =='s':
        print("Saliendo...")
        break

    #Opcion para Calcular la velocidad final
    elif opc == '1':
        print("\n")
        print("** Calculo de la velocidad final **")                 
        resultadoVelocidadFinal = velocidadFinal()        
        print("La distancia es: " + str(velocidadFinal) + " m/s")
        nuevaOperacion = errorOperacion() 

    #Opcion para Calcular la velocidad inicial
    elif opc == '2':
        print("\n")
        print("** Calculo de la velocidad inicial **")                 
        resultadoVelIni = velocidadInicial()        
        print("La velocidad inicial es: " + str(resultadoVelIni) + "m/s")
        nuevaOperacion = errorOperacion()        

    #Opcion para Calcular la aceleracion
    elif opc == '3':
        print("\n")
        print("** Calculo de la aceleracion **")                 
        resultadoAceleracion = aceleracion()        
        print("La aceleracion es de: " + str(resultadoAceleracion) + " m/s^2")
        nuevaOperacion = errorOperacion()

    #Opcion para Calcular el tiempo
    elif opc == '4':
        print("\n")
        print("** Calculo del tiempo **")                 
        resultadoTiempo,resultadoTiempoRedondeado = tiempo()        
        print("El tiempo es de: " + str(resultadoTiempo) + " s")
        print("Redondeado igual a : " + str(resultadoTiempoRedondeado) + " s")
        nuevaOperacion = errorOperacion()

    #Opcion para grafica en funcion del tiempo
    elif opc == '5':
        print("\n")
        print("**Graficas en funcion del tiempo**")
        grafica()
        nuevaOperacion = errorOperacion()

    #Opcion incorrecta    
    else:
        print("Opción no válida")
        continue

    #Opcion para salir
    if nuevaOperacion.upper() != "S" :
        print("Saliendo...")
        break