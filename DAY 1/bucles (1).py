# -*- coding: utf-8 -*-
"""Bucles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xzg34xMAOVizBJtZLsdyBBwXKaRFt24i

# Bucles

Cuando queremos hacer algo más de una vez (*iterar*) necesitamos un **bucle** y Python nos ofrece dos opciones para ello: `while` y `for`.

## Repetir con `while`

El mecanismo más sencillo en Python para repetir instrucciones es mediante la sentencia `while`. Veamos un sencillo bucle que muestra los números del 1 al 5:
"""

contador = 0
while contador <= 5:
    print(contador)
    contador = contador + 1

"""La *condición* del bucle se comprueba en cada nueva repetición. En este caso chequeamos que la variable `contador` sea menor o igual que 5. Dentro del *cuerpo* del bucle estamos incrementando esa variable en 1 unidad.

### Bucle Infinito

Si queremos repetir hasta que algo suceda, pero no estamos seguros cuándo podría ocurrir, podemos escribir un *bucle infinito* con una sentencia `break`.

Veamos un ejemplo leyendo una entrada desde teclado con la función `input()` hasta que se pulse la letra "q":
"""

while True:
    texto = input('Introduce aquí texto [type q to quit]: ')
    if texto == 'q':
        break
    print( texto )

"""> Suele ser común, especialmente en principiantes, equivocarnos en la definición de la condición y obtener bucles infinitos. La revisión del código nos permitirá descubrir qué está ocurriendo.

### Continuar un bucle

Hay veces que no queremos romper un bucle sino simplemente queremos saltar adelante hacia la siguiente repetición. Veamos un ejemplo en el que leemos un entero y mostramos su cuadrado si el número es impar o lo saltamos si es par:
"""

while True:
    valor = input('Introduce un entero [q to quit]: ')
    if valor == 'q':
        break
    numero = int(valor)
    if numero % 2 == 0:
        print( 'Es par, saltamos el bucle' )
        continue
    cuadrado = numero * numero
    print( numero, 'el cuadrado es: ', cuadrado)

"""## Iterar con `for`

Python hace uso frecuentemente de **iteradores**.

Esto hace posible *recorrer* estructuras de datos sin conocer el tamaño que tienen o cómo están implementadas. Incluso es posible iterar sobre datos que se crean sobre la marcha, permitiendo el acceso a flujos de datos (*data streams*) que, de otra manera, no cabrían de una vez en la memoria de la máquina.

Para mostrar una iteración necesitamos algo sobre lo que iterar: **iterables**. Veamos un ejemplo con las cadenas de texto:

Recorrer la cadena de forma "*tradicional*":
"""

palabra = 'abcd'
indice = 0
while indice < len(palabra):
    print(palabra[indice])
    indice = indice + 1

"""Pero hay una manera mejor y más "*pitónica*":"""

for letra in palabra:
    print(letra)

"""### Ejercicio

Dada una cadena de texto, indique el número de vocales que contiene:

#### Ejemplo:

➡️ `holaestoesunapruebaenpython`  
⬅️ 12
"""

# Escriba aquí su solución

def contar_vocales(texto):
	contador = 0
	for letra in texto:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

texto = 'holaestoesunapruebaenpython'
cantidad = contar_vocales(texto)
print('En el texto:', (texto), 'hay:', (cantidad), 'vocales.')

"""## Generar secuencias de números

La función `range()` devuelve un flujo de números en el rango especificado, sin necesidad de crear y almacenar previamente una larga estructura de datos. Esto permite generar rangos enormes sin consumir toda la memoria del sistema.

El uso de `range()` es similar a los *slices*: `range(start, stop, step)`. Podemos omitir `start` y el rango empezaría en 0. El único valor requerido es `stop` y el último valor generado será el justo anterior a este. El valor por defecto de `step` es 1, pero se puede ir "hacia detrás" con -1.

`range()` devuelve un objeto *iterable*, así que necesitamos obtener los valores paso a paso con una sentencia `for ... in` (o convertir el objeto a una secuencia como una lista).

Veamos un ejemplo generando el rango $[0, 1, 2]$
"""

for x in range(0, 3):
    print(x)

list(range(0, 3))

"""### Bucles anidados

Es posible escribir un bucle dentro de otro. Esto se conoce como **bucles anidados**.
"""

for i in range(3):
    for j in range(2):
        print(i, j)
    print('---')

"""<h2 id="quiz">Cuestionario sobre Bucles</h2>

Escribe un bucle <code>for</code> que imprima todos los elementos entre <b>-5</b> y <b>5</b> usando la función de rango.
"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar
for i in range(-5,5): 
  print(i)

"""Imprime los elementos de la siguiente lista: <code>Genres=\[ 'rock', 'R\&B', 'Soundtrack', 'R\&B', 'soul', 'pop']</code>
Asegúrate de seguir las convenciones de Python.

"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar
genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for x in genres:
  print(x)

"""<hr>

Escribe un blucle for que imprima la siguiente lista: <code>squares=\['red', 'yellow', 'green', 'purple', 'blue']</code>
"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar

squares=['red', 'yellow', 'green', 'purple', 'blue']

for x in squares:
  print(x)

"""<hr>

Escribe un bucle while para mostrar los valores del Rating de una lista de reproducción de un álbum almacenada en la lista <code>PlayListRatings</code>. Si la puntuación es inferior a 6, sal del bucle. La lista <code>PlayListRatings</code> está dada por: <code>PlayListRatings = \[10, 9.5, 10, 8, 7.5, 5, 10, 10]</code>
"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar
playListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
indice = 0
while indice < len(playListRatings):
    puntuacion = playListRatings[indice]
    if puntuacion < 6:
        break
    print(puntuacion)
    indice=indice + 1

"""Escribe un bucle while para copiar los string <code>'orange'</code> de la lista <code>squares</code> a la lista <code>new_squares</code>. Para y sal del bucle si el valor de la lista no es <code>'orange'</code>:

"""

# Escribe tu código debajo y presiona Shift+Enter para ejecutar

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
#1.Recorrer con while la lista squares
indice = 0
while squares[indice] == 'orange':
  new_squares.append(squares[indice])
  indice = indice + 1
  continue
print(new_squares)

"""### Ejercicio (Opcional)

Imprima los 100 primeros números de la secuencia de Fibonacci: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots$

####  Pista: `_`

Hay situaciones en las que no necesitamos usar la variable que toma valores en el rango, únicamente queremos *repetir una acción un número de veces*.

Para estos casos se suele recomendar usar el **subguión** (*guión bajo*) como nombre de variable, que da a entender que no estamos usando esta variable de forma explícita:
"""

for _ in range(10):
    print('Hello world!')

"""> Simplemente hemos mostrado 10 veces el mensaje `Hello world!` sin necesidad usar un contador."""

# Escriba aquí su solución
# Partiendo del 0 y el 1
a = 0
b = 1
#Bucle:
