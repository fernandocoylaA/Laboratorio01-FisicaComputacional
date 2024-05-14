#Programa para el calculo de MRUV
#Ecuacion de la forma d = Vo +- 1/2(a*(t^2))

#imports
import math  #operaciones

#Funciones para calcular MRUV
#Funcion calcular Distancia
def distancia():
    velIni = float(input("Ingrese la velocidad inicial (m/s): "))
    if(velIni < 0):
        print("La velocidad inicial no puede ser Negativa!") 
        return 0  
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if(tiempo <= 0):
       print("El tiempo no puede ser negativo o cero")
       return 0
    acel = float(input("Ingrese la aceleracion: ")) 
    if(acel == 0):
        print("Aceleracion cero Invalido: calculo MRUV")
        return 0
    else:              
        resultado = (velIni*tiempo) + ((acel*(tiempo**2))/2)             
        return abs(resultado) #resultado en valor absoluto 

#Funcion calcular Velocidad inicial
def velocidadInicial():
    acel = float(input("Ingrese la aceleracion: "))
    if(acel == 0):
        print("Aceleracion cero Invalido: calculo MRUV")
        return 0
    distancia = float(input("Ingrese la distancia (metros): "))
    if(distancia < 0): #distancia negativa
        print("La distancia no puede ser Negativa!") 
        return 0 
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if(tiempo <= 0): #tiempo negativo o cero
       print("El tiempo no puede ser negativo o cero")
       return 0
    else:
        resultado = (distancia-((acel/2)*tiempo**2))/tiempo
        return abs(resultado) #retornando como positivo

#Funcion calcular ACELERACION
def aceleracion():
    distancia = float(input("Ingrese la distancia (metros): "))
    if(distancia < 0): #distancia negativa
        print("La distancia no puede ser Negativa!") 
        return 0 
    velIni = float(input("Ingrese la velocidad inicial (m/s): ")) 
    if(velIni < 0):
        print("La velocidad inicial no puede ser Negativa!") 
        return 0
    tiempo = float(input("Ingrese el tiempo (segundos): "))
    if(tiempo <= 0):
       print("El tiempo no puede ser negativo o cero")
       return 0
    else:
        resultado = 2*(distancia-(velIni*tiempo))/tiempo**2
        return resultado

#Funcion para calcular el tiempo
def tiempo():
    distancia = float(input("Ingrese la distancia (metros): "))
    if(distancia < 0): #distancia negativa
        print("La distancia no puede ser Negativa!") 
        return 0 
    velIni = float(input("Ingrese la velocidad inicial (m/s): ")) 
    if(velIni < 0):
        print("La velocidad inicial no puede ser Negativa!") 
        return 0
    acel = float(input("Ingrese la aceleracion: "))
    if(acel == 0):
        print("Aceleracion cero Invalido: calculo MRUV")
        return 0
    else:        
        calculo1 = ((2*distancia)-velIni)/acel
        resultado = math.sqrt(abs(calculo1))
        resultadoRedondeo = math.ceil(resultado) #redondeo
        return resultado,resultadoRedondeo

# Menu de Opciones
def menu():
    print("** ::::::::::::::::::::::::: **")
    print("::       Calculo de MRUV - Ecuacion1::")
    print("** ::::::::::::::::::::::::: **")
    print("-------------------------------")
    print("| Calcular la distancia:            ->  1   |")
    print("| Calcular la velocidad inicial:    ->  2   |")
    print("| Calcular la aceleracion:          ->  3   |")
    print("| Calcular el tiempo     :          ->  4  |")    
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

    #Opcion para Calcular la distancia
    elif opc == '1':
        print("\n")
        print("** Calculo de la distancia **")                 
        resultadoDistancia = distancia()        
        print("La distancia es: " + str(resultadoDistancia) + "metro(s)")
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

    #Opcion incorrecta    
    else:
        print("Opción no válida")
        continue

    #Opcion para salir
    if nuevaOperacion.upper() != "S" :
        print("Saliendo...")
        break
    
    