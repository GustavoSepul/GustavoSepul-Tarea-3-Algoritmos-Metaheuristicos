import numpy as np
import pandas as pd
import sys 
import time

def ruleta(c):
    aux = np.arange(1,c+1)**-Tau
    aux /= np.sum(aux)
    aux = np.cumsum(aux)
    return aux


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
print(solucion)
aux = 0
for i  in range(n):
    aux += (datos[i][1])*solucion[i]
# print(solucion)
if(aux <= c):
    mejor_solucion = solucion
else:
    mejor_solucion = solucion
    mejor_solucion = np.zeros(n,dtype=int)

fitness = np.zeros((n,2))
for j in range(n):
    fitness[j][0] = datos[j][0]/datos[j][1]
    fitness[j][1] = j
# print(fitness)


vector_prob = np.zeros(n)
for i in range(n):
    vector_prob[i] = (i+1)**(-Tau)
# print("PROB", vector_prob)

generacion = 0

while generacion<Iteraciones:
    # print(generacion)
    n=solucion.size
    fitOrd = np.zeros((n,2))
    for i in range(n):  
        if solucion[i] == 1:   #1
            fitOrd[i][0]= fitness[i][0]  #Agrega los fitnes de los items que no estan en mochila
            fitOrd[i][1]= fitness[i][1]   #identificador del item         
    fitOrd = np.delete(fitOrd, np.where(fitOrd[:, 0] == 0)[0], axis=0)
    fitOrd = fitOrd[fitOrd[:, 0].argsort()]
    print(fitOrd)
    rulet = ruleta(n)
    print(rulet)
    
    aux=0
    listo = False
    giro = 0.0
    giro = np.random.rand()
    while listo==False:
        if giro <= rulet[aux]:
            listo = True
        else:
            aux = aux+1  
    itemSelec = aux
    print(giro)
    print(itemSelec)
    print("a",solucion)
    if int(solucion[int(fitOrd[itemSelec][1])])==0:
        solucion[int(fitOrd[itemSelec][1])]=1
    else:
        solucion[int(fitOrd[itemSelec][1])]=0
    print("b",solucion)
    generacion+=1
# ruleta = ruleta(n)
# print(ruleta)