import numpy as np
import pandas as pd
import sys 
import time

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
    if(Iteraciones <= 1):
        print("Error: El número de iteraciones debe ser mayor a 1\nIngrese un número de iteraciones mayor a 1")
        sys.exit(0)
else:
    print("Error: Los datos ingresados no son validos, ingrese los datos de la siguiente manera:")
    print("python.exe .\mochila.py Seed Número_Iteraciones Tau Archivo_Entrada")
    sys.exit(0)


np.random.seed(Seed)


datos = pd.read_table(Archivo_entrada, header = None,delim_whitespace=True, skiprows=5, skipfooter=0, engine='python')
datos = datos.drop(columns=3)
datos = datos.drop(columns =0,axis=1).to_numpy()

datos2 = pd.read_table(Archivo_entrada, header = None,delim_whitespace=True, skiprows=1, nrows=3, engine='python')
datos2 = datos2.drop(columns =0,axis=1).to_numpy()
print(datos)
n = datos2[0][0]
c = datos2[1][0]
z = datos2[2][0]
print(n)
print(c)
print(z)

while True:
    mejor_solucion = np.random.randint(2, size=n)
    aux = 0
    for i  in range(n):
        aux += datos[i][1]*mejor_solucion[i]
    print(aux)
    if(aux <= c):
        break
