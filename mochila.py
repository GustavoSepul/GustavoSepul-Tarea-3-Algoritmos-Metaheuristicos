import numpy as np
import pandas as pd
import sys 
import time

def ruleta(n):
    aux = np.arange(1,n+1)**-Tau
    aux /= np.sum(aux)
    aux = np.cumsum(aux)
    return aux

def calcular_valor(n,datos,sol):
    aux = 0
    for i in range(n):
        aux += (datos[i][0]) * sol[i]
    return aux

def factibilidad(n,datos,sol):
    aux = 0
    for i in range(n):
        aux += (datos[i][1]) * sol[i]
    if(aux <= c):
        return True
    else:
        return False


if len(sys.argv) == 5: #python.exe .\mochila.py 30 200 1.4 .\Prueba1.txt >>Tabala1.csv
    Seed = int(sys.argv[1])
    Iteraciones = int(sys.argv[2])
    Tau = float(sys.argv[3])
    Archivo_entrada = str(sys.argv[4])
    # print('Semilla: ', Seed)
    # print('Numero iteraciones: ', Iteraciones)
    # print('Tau: ', Tau)
    # print('Matriz: ', Archivo_entrada)

    if(Seed < 0):
        print("Error: La cantidad de semillas debe ser positiva\nIngrese una cantidad de semillas positivo")
        sys.exit(0)
    if(Iteraciones < 1):
        print("Error: El número de iteraciones debe ser mayor a 1\nIngrese un número de iteraciones mayor a 1")
        sys.exit(0)
    if(Tau < 0 or Tau > 3):
        print("Error: El valor de Tau debe ser entre 0 y 3\nIngrese un valor de Tau entre 0 y 3")
        sys.exit(0)
else:
    print("Error: Los datos ingresados no son validos, ingrese los datos de la siguiente manera:")
    print("python.exe .\mochila.py Seed Número_Iteraciones Tau Archivo_Entrada")
    sys.exit(0)

#Lectura y conversion de los datos de prueba
datos = pd.read_table(Archivo_entrada, header=None, skiprows=5, sep=",", names=range(4), engine='python')
datos = datos.drop(columns=3)
datos = datos.drop(index=(len(datos)-1),axis=0)
datos = datos.drop(columns =0,axis=1).to_numpy()

datos2 = pd.read_table(Archivo_entrada, header = None,delim_whitespace=True, skiprows=1, nrows=3, engine='python')
datos2 = datos2.drop(columns =0,axis=1).to_numpy()

n = datos2[0][0]
c = datos2[1][0]
z = datos2[2][0]
print("Numero de Elementos",n)
print("Capacidad",c)
print("Valor optimo",z)
print("Semilla,","Iteraciones,","Mejor valor encontrado")


#Inicio del proceso para cada semilla
for x in range(Seed):
    
#Inicializacion semilla
    np.random.seed(x)
    
#Generacion solucion inicial 
    solucion = np.random.randint(2, size=n)
    mejor_solucion = np.zeros(n,dtype=int)

#Evaluar factibiidad solucion inicial
    factible = factibilidad(n,datos,solucion)
    if(factible == True):
        mejor_solucion = solucion
    else:
        mejor_solucion = solucion
        mejor_solucion = np.zeros(n,dtype=int)

#calcular valor de la solucion 
    mejor_valor = calcular_valor(n,datos,mejor_solucion)
    generacion = 0
    
#Inicio ciclo para para solucion de cada semilla
    while generacion<Iteraciones and mejor_valor<z:
        
#Creacion arreglo fitness
        fitness = np.zeros((n,2))
        fitness[:, 0] = datos[:, 0]/datos[:, 1]
        fitness[:, 1] = [k for k in range(n)] 
        ordenado = np.zeros((n,2))
        
#Creacion arreglo fitness ordenado si la solucion es factible
        if(factible == True):
            ordenado = np.zeros((n,2))
            for i in range(n):  
                if solucion[i] == 0: 
                    ordenado[i][0]= fitness[i][0]  
                    ordenado[i][1]= fitness[i][1]     
            ordenado = np.delete(ordenado, np.where(ordenado[:, 0] == 0)[0], axis=0)
            ordenado = ordenado[ordenado[:, 0].argsort()]
            ordenado=ordenado[::-1]
        else:
            ordenado = np.zeros((n,2))
            for i in range(n):  
                if solucion[i] == 1: 
                    ordenado[i][0]= fitness[i][0]  
                    ordenado[i][1]= fitness[i][1]     
            ordenado = np.delete(ordenado, np.where(ordenado[:, 0] == 0)[0], axis=0)
            ordenado = ordenado[ordenado[:, 0].argsort()]

#Creacion arreglo ruleta segun fitness ordenado
        rulet = ruleta(np.shape(ordenado)[0])
        
#Girar ruleta y seleccionar
        aux2=0
        rand = np.random.rand()
        i=0
        seleccionado = 0
        for i in range(0, np.shape(ordenado)[0]):
            if rand > rulet[i]:
                aux2 = i
        seleccionado = aux2       


#Evaluar si la solucion en la posicion seleccionada es cero o uno y reemplazarla por el contrario
        if(int(solucion[int(ordenado[seleccionado][1])]) == 0):
            solucion[int(ordenado[seleccionado][1])] = 1
        else:
            solucion[int(ordenado[seleccionado][1])] = 0

#Calcular valor de la solucion
        valor = calcular_valor(n,datos,solucion)
        
#Evaluar factibilidad de la solucion
        factible = factibilidad(n,datos,solucion)

#Evaluar si la solucion es factible y si el valor de la solucion es mejor que el mejor valor 
        if (valor>mejor_valor and factible==True):
            mejor_solucion = solucion
            mejor_valor = valor
        
        generacion+=1

    print(x+1,generacion,int(mejor_valor))
    # print(generacion)
    # print("Mejor Solucion: ",mejor_solucion)
    # print(mejor_valor)