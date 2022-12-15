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

def calcular_peso(n,datos,sol):
    aux = 0
    for i in range(n):
        aux += (datos[i][1]) * sol[i]
    return aux

def factibilidad(n,datos,sol):
    if(calcular_peso(n,datos,sol) <= c):
        return True
    else:
        return False


if len(sys.argv) == 5:
    Seed = int(sys.argv[1])
    Iteraciones = int(sys.argv[2])
    Tau = float(sys.argv[3])
    Archivo_entrada = str(sys.argv[4])
    print('Semilla: ', Seed)
    print('Numero iteraciones: ', Iteraciones)
    print('Tau: ', Tau)
    print('Matriz: ', Archivo_entrada)

    if(Seed < 0):
        print("Error: El número de la semilla debe ser positivo\nIngrese un número de semilla positivo")
        sys.exit(0)
    if(Iteraciones < 1):
        print("Error: El número de iteraciones debe ser mayor a 1\nIngrese un número de iteraciones mayor a 1")
        sys.exit(0)
else:
    print("Error: Los datos ingresados no son validos, ingrese los datos de la siguiente manera:")
    print("python.exe .\mochila.py Seed Número_Iteraciones Tau Archivo_Entrada")
    sys.exit(0)


np.random.seed(Seed)


datos = pd.read_table(Archivo_entrada, header=None, skiprows=5, sep=",", names=range(4), engine='python')
datos = datos.drop(columns=3)
datos = datos.drop(index=(len(datos)-1),axis=0)
datos = datos.drop(columns =0,axis=1).to_numpy()

datos2 = pd.read_table(Archivo_entrada, header = None,delim_whitespace=True, skiprows=1, nrows=3, engine='python')
datos2 = datos2.drop(columns =0,axis=1).to_numpy()
# print(datos)
n = datos2[0][0]
c = datos2[1][0]
z = datos2[2][0]
# print(n)
# print(c)
# print(z)

solucion = np.random.randint(2, size=n)
# print(solucion)
print(solucion)


factible = factibilidad(n,datos,solucion)
if(factible == True):
    mejor_solucion = solucion
else:
    mejor_solucion = solucion
    mejor_solucion = np.zeros(n,dtype=int)

#funcion fitness
fitness = datos[:, 0]/datos[:, 1]
# print(fitness)
fitness = np.sort(fitness)

# fitness2 = np.zeros((n,2))
# for j in range(n):
#     fitness2[j][0] = datos[j][0]/datos[j][1]
#     fitness2[j][1] = j
# print(fitness2)


mejor_valor = calcular_valor(n,datos,mejor_solucion)
# print(mejor_solucion)

generacion = 0
while generacion<Iteraciones:
    rulet = ruleta(n)
    aux2=0
    rand = np.random.rand()
    # print(rulet)
    i=0
    for i in range(0, n):
        if rand > rulet[i]:
            aux2 = i
    seleccionado = aux2        
    # print(seleccionado)
    if(solucion[seleccionado] == 0):
        solucion[seleccionado] = 1
        aux3 = 0
        for i  in range(n):
            aux3 += (datos[i][1])*solucion[i]
        if(aux3 <= c):
            solucion[seleccionado] = 0
    else:
            solucion[seleccionado] = 0
            
    valor = calcular_valor(n,datos,solucion)
    factible = factibilidad(n,datos,solucion)
    if (valor>mejor_valor):
        mejor_solucion = solucion
        mejor_valor = calcular_valor(n,datos,mejor_solucion)
    generacion+=1

print(mejor_solucion)
print(mejor_valor)