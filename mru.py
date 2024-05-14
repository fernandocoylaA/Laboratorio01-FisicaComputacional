#Programa para el calculo de MRU

#Librerias necesarias
import matplotlib.pyplot as plt
import numpy as np

#Funciones para calcular MRU
#Funcion calcular Distancia
def distancia():
    vel = float(input("Ingrese la velocidad: "))  
    tiempo = float(input("Ingrese el tiempo: "))
    if(tiempo < 0): #tiempo negativo
      print("El tiempo no puede ser negativo")
      return 0
    return abs(vel*tiempo) #resultado en valor absoluto   

#Funcion para calcular el tiempo
def tiempo():
    dist = float(input("Ingrese la distancia: "))  
    vel = float(input("Ingrese la velocidad: "))
    if(vel==0):
        print("Velocidad no puede ser cero / division entre cero invalida")    
    return abs(dist/vel) #resultado en valor absoluto

#Funcion  para calcular la velocidad
def velocidad():
    dist = float(input("Ingrese la distancia: "))
    tiempo = float(input("Ingrese el tiempo: "))
    if(tiempo > 0): #tiempo negativo
      return abs(dist/tiempo) #resultado en valor absoluto
    print("El tiempo ingresado debe ser positivo y diferente de cero")
    return 0

#Funcion para generar la grafica de desplazamiento en funcion del tiempo
def grafica():
    vel = float(input("Ingrese la velocidad: "))
    medida = input("Ingresa la medida: km/h-> 1  o  m/s -> 2 :: ") 
    if(medida == '1'):
        vel *= (5/18) #convertir la velocidad a m/s   
    tiempo = np.arange(0.0, 10.0) # se genera un array de tiempo de 0 a 10 segundos
    desplazamiento = vel * tiempo # se calcula el desplazamiento
    fig, ax = plt.subplots() # se crea la figura y los ejes
    ax.plot(tiempo, desplazamiento) # Grafica tiempo(x) y desplazamiento(y)
    ax.set(xlabel='Tiempo', ylabel='Desplazamiento',
    title='Grafica de desplazamiento en funcion del tiempo')
    ax.grid() # se agrega una cuadrícula al gráfico
    fig.savefig("MRU") # se guarda la figura en un archivo llamado "MRU"
    plt.show() # se muestra la gráfica

# Menu de Opciones
def menu():
    print("** ::::::::::::::::::::::::: **")
    print("::       Calculo de MRU      ::")
    print("** ::::::::::::::::::::::::: **")
    print("-------------------------------")
    print("| Calcular la distancia:  ->  1   |")
    print("| Calcular el tiempo:    ->  2   |")
    print("| Calcular la velocidad: ->  3   |")
    print("| Grafica de desplazamiento en funcion del tiempo: ->  4  |")
    print("| Salir:                 ->  s   |")
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
    #Opcion para Calcular la distancia
    elif opc == '1':
        print("\n")
        print("** Calculo de la distancia **")
        #medidas en km o m
        print("Medida km(Kilometros) -> 1") 
        print("Medida m(metros) -> 2")
        medida = input("Ingresa medida: ")
        if(medida == '1'):           
            resultadoDistancia = distancia()
            print("La distancia es: " + str(resultadoDistancia) + "Kilometro(s)")
        elif(medida == '2'):            
            resultadoDistancia = distancia()
            print("La distancia es: " + str(resultadoDistancia) + "metro(s)")
        else:
            print("Opción no válida")
            continue            
        nuevaOperacion = errorOperacion()
    #Opcion Calcular Tiempo
    elif opc == '2':
        print("\n")
        print("** Calculo del tiempo **")
        #medidas en h o s
        print("Medida h(horas) -> 1") 
        print("Medida s(segundos) -> 2")
        medida = input("Ingresa medida: ")
        if(medida == '1'):
            resultadoTiempo = tiempo()
            print("El tiempo es de : " + str(resultadoTiempo) + "horas")
        elif(medida == '2'):
            resultadoTiempo = tiempo()            
            print("El tiempo es de : " + str(resultadoTiempo) + "segundos")        
        else:
            print("Opción no válida")
            continue            
        nuevaOperacion = errorOperacion()
    #Opcion calcular velocidad
    elif opc == '3':
        print("\n")
        print("**Calculo de la Velocidad**")
        #medidas en km/h o m/s
        print("Medida km/h -> 1") 
        print("Medida m/s  -> 2")
        medida = input("Ingresa medida: ")
        if(medida == '1'):
            resultadoVelocidad = velocidad()
            print("La velocidad es de : " + str(resultadoVelocidad) + "km/h")
        elif(medida == '2'):
            resultadoTiempo = tiempo()            
            print("La velocidad es de : " + str(resultadoVelocidad) + "m/s")        
        else:
            print("Opción no válida")
            continue            
        nuevaOperacion = errorOperacion()
    #Opcion Grafica de desplazamiento en funcion del tiempo
    elif opc == '4':
        print("\n")
        print("**Grafica de desplazamiento en funcion del tiempo**")
        grafica()
        nuevaOperacion = errorOperacion()
    else:
        print("Opción no válida")
        continue

    
    if nuevaOperacion.upper() != "S" :
        print("Saliendo...")
        break
