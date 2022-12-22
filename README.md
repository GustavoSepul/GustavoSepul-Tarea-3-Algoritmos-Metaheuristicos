# Tarea-3-Algoritmos-Metahuristicos
## Problema de la mochila con optimizacion extrema
### El ***problema de la mochila***, es un problema de optimización combinatorio, es decir, que buscará la mejor solución entre un conjunto finito de posibles soluciones, el cual desarrollaremos implementando el método ***Extremal Optimization*** en Python.

## Programas utilizados 

* [GitHub Desktop](https://desktop.github.com/) - Herramienta para tener los repositorios en la nube y mantener las versiones.
* [Visual Studio Code](https://visualstudio.microsoft.com/es/) - IDE y editor para la creación del Algoritmo.

## Instalación
* La versión utilizada para python será [3.10.7](https://www.python.org/downloads/).
* Se necesitara instalar la libreria [numpy](https://numpy.org/) en la IDE que se este trabajando con el siguiente código:
 ```
 pip install numpy
 ```
 * Se necesitara instalar la libreria [pandas](https://pandas.pydata.org/) en la IDE que se este trabajando con el siguiente código:
 ```
 pip install pandas
 ```
 * Para bajar el programa haga click en el siguiente [Link](https://github.com/GustavoSepul/Tarea-3-Algoritmos-Metaheuristicos/archive/refs/heads/main.zip)

## Ejecución del programa

- Para ejecutar el codigo se debe ejecutar el siguiente comando: 
```
python ./mochila.py Seed Número_Iteraciones Tau Archivo_entrada >> Archivo_Salida
```
- Donde:
    - ***Seed***, el cuál sera un número real randomico mayor a 0.
    - ***Número_Iteraciones***, el cuál sera un número entero a criterio del usuario.
    - ***Tau***, el cuál sera un número real.
    - ***Archivo_entrada***, nombre del archivo con los valores y pesos de prueba (Prueba1.txt).
    - ***Archivo_Salida***, nombre del archivo con la solución encontrada (Solucion1.txt).

## Ejemplo
```
python.exe .\mochila.py 30 200 1.4 Prueba1.txt >> Tabla1.csv
```


## Resultados
- Los resultados se guardan en un archivo csv con los siguientes datos:
```
Numero de Elementos 50
Capacidad 99748
Valor optimo 396225
Semilla, Iteraciones, Mejor valor encontrado
0 195 396225.0
1 136 396225.0
2 200 381795.0
3 200 364382.0
4 40 396225.0
5 200 374130.0
6 200 381795.0
7 137 396225.0
8 62 396225.0
9 107 396225.0
10 200 379196.0
11 200 364382.0
12 200 367807.0
13 80 396225.0
14 115 396225.0
15 200 376931.0
16 200 381795.0
17 70 396225.0
18 200 367807.0
19 79 396225.0
20 200 381795.0
21 69 396225.0
22 72 396225.0
23 35 396225.0
24 117 396225.0
25 200 379196.0
26 200 365206.0
27 130 396225.0
28 77 396225.0
29 200 381795.0

```



### Autores
* Diego Araneda Hidalgo - daranedah@ing.ucsc.cl
* Gustavo Sepulveda Ocampo - gsepulvedao@ing.ucsc.cl
* Javier Victoriano Rivas - jvictoriano@ing.ucsc.cl
