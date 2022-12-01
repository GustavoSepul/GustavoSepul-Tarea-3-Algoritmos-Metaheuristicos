import numpy as np
import pandas as pd
import sys 
import time

if len(sys.argv) == 4:
    Seed = int(sys.argv[1])
    Iteraciones = int(sys.argv[2])
    Tau = float(sys.argv[3])
    print('Semilla: ', Seed)
    print('Numero iteraciones: ', Iteraciones)
    print('Tau: ', Tau)

    if(Seed < 0):
        print("Error: El número de la semilla debe ser positivo\nIngrese un número de semilla positivo")
        sys.exit(0)
    if(Iteraciones <= 1):
        print("Error: El número de iteraciones debe ser mayor a 1\nIngrese un número de iteraciones mayor a 1")
        sys.exit(0)
else:
    print("Error: Los datos ingresados no son validos, ingrese los datos de la siguiente manera:")
    print("python.exe .\Reinas.py Seed Número_Iteraciones Tau Archivo_Entrada")
    sys.exit(0)


np.random.seed(Seed)
mejor_solucion = np.arange(0,5)
print(mejor_solucion)