"# CNYT" 
# Calculadora de numeros imaginarios

Este proyecto es una libreria cuya funcion principal es hacer operaciones básicas con tuplas de números simulando la estructura de los numeros complejos, estas operaciones son: suma ,resta ,multiplicacion ,division ,modulo ,conjugado , Coversion a coordenadas polares y la fase de los nueros complejos

## Comenzando 

Se comienza teniendo en cuenta que las operaciones tales como la suma y la resta de complejos es igual a una suma o resta entre vectores, La diferencia con respeco a los vectores se encunetra en aplicar el algebra para determinar ciertas formulas utilizadas en la multiplicacion y la division.

La funcion del conjugado se realiza invirtiedo el signo de la parte imaginaria del numero complejo dado.

En la realizacion de las funciones restantes fue necesaria la importacion de una biblioteca math que facilitara los siguientes calculos.

Por ejemplo e la funcion modulo fue necesaria la utilizacion de la operacion raiz cuadrada.

En la funcion de cambio de cartesianas a polars y el cambio de fase fue necesario el uso de la funcion arcotangete para poder encontrar un angulo, que es necesario en el uso de estas coordenadas.

Hay que tener en cuenta que para encontrar la longitud de la recta polar es necesrio utilizar la funcion raiz, Finalmente esta funcion entregara una tupla formada por la longitud de la recta polar y el angulo de fase.

## Ejecucion de pruebas

Para la ejecucion de las pruebas automatizadas de las fuciones de la calculadora, se realizo un test de nombre testLibreria.py cuyo codigo son diversas pruebas para cada una de las funciones que demuestran su funcionamiento.

### Analisis de pruebas 

Las pruebas tienen como objetivo ser garante del funcionamiento de las diversas operaciones de la calculadora bajo cualquier situacion o entrada de numeros independientemente de su naturaleza (entero o decimal).
 
### Tipo de pruebas

testsuma = Esta prueba tiene como finalidad probar la funcion de suma.

testresta = Esta prueba tiene como finalidad probar la funcion de resta.

testmulti = Esta prueba tiene como finalidad probar la funcion de multiplicacion.

testdivisi = Esta prueba tiene como finalidad probar la funcion de division. 

testconjugado = Esta prueba tiene como finalidad probar la funcion del conjugado de numeros complejos.

testretorno = Esta prueba tiene como finalidad probar la funcion de retorno de fase.

testmodulos = Esta prueba tiene como finalidad probar la funcion del modulo de un numero complejo.

testcartesianos = Esta prueba tiene como finalidad probar la funcion de conversion a coordenadas cartesianas de un numero complejo.



## Construido con :


* [Python](https://www.python.org/) - Lenguaje de programacion


## Autores ✒

* **Cristian Camilo Forero Monroy
