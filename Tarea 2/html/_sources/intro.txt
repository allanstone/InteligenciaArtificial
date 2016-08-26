Tarea 2: Cifrado
****************

Puede revisar la defición de la tarea en la siguiente `presentación <http://dicyg.fi-c.unam.mx:8080/lalo/ia/presentaciones/introduccion-a-la-inteligencia-artificial#page=8>`_

Objetivo
========

Consiste en hacer un código que se encargue de cifrar y descifrar texto de acuerdo
al método mostrado a continuación.

Descripción
===========

1. Este tipo de cifrado por columna con palabra clave consiste en formar una tabla con tantas
columnas como letras tenga la palabra clave; a continuación, se escribe el texto en la tabla
de izquierda a derecha y de arriba hacia abajo (sin espacios y, si hace falta, se rellenan los
espacios de la última fila con algún caracter): 

**Texto : LA CRIPTOGRAFIA ES ROMANTICA**
**Clave : HOLA**

+---+---+---+---+
| H | O | L | A |
+===+===+===+===+
| L | A | C | R |
+---+---+---+---+
| I | P | T | O |
+---+---+---+---+
| G | R | A | F |
+---+---+---+---+
| I | A | E | S |
+---+---+---+---+
| R | O | M | A |
+---+---+---+---+
| N | T | I | C | 
+---+---+---+---+
| A | S | S | S |
+---+---+---+---+

2. A continuación se reordenan las columnas alfabéticamente de acuerdo a la palabra clave (si
hay repetición, el criterio de desempate es el orden de aparición en la palabra):

+---+---+---+---+
| A | H | L | O |
+===+===+===+===+
| R | L | C | A |
+---+---+---+---+
| O | I | T | P |
+---+---+---+---+
| F | G | A | R |
+---+---+---+---+
| S | I | E | A |
+---+---+---+---+
| A | R | M | O |
+---+---+---+---+
| C | N | I | T |
+---+---+---+---+
| S | A | S | S |
+---+---+---+---+

3. Finalmente se toman los caracteres por columna de arriba hacia abajo y de izquierda a
derecha obteniendo finalmente el texto codificado:

**ROFSACSLIGIRNACTAEMISAPRAOTS**

Para descifrar un texto codificado con este método, es necesario saber la palabra clave, y a continuación
se aplican las operaciones siguientes, mostradas para descrifrar el ejemplo anterior:

**Texto : ROFSACSLIGIRNACTAEMISAPRAOTS**
**Clave : HOLA**

1. Se divide el texto en tantas partes como letras tiene la palabra clave (es exacta):

**Grupos : ROFSACS LIGIRNA CTAEMIS APRAOTS**

2. Se ordena alfabéticamente la palabra clave:

**Clave : HOLA**
**Ordenada : AHLO**

3. Se coloca cada grupo bajo cada letra de la palabra clave ordenada:

+---+---+---+---+
| A | H | L | O |
+===+===+===+===+
| R | L | C | A |
+---+---+---+---+
| O | I | T | P |
+---+---+---+---+
| F | G | A | R |
+---+---+---+---+
| S | I | E | A |
+---+---+---+---+
| A | R | M | O |
+---+---+---+---+
| C | N | I | T |
+---+---+---+---+
| S | A | S | S |
+---+---+---+---+

4. Se reacomoda la palabra clave junto con su columna correspondiente:

+---+---+---+---+
| H | O | L | A |
+===+===+===+===+
| L | A | C | R |
+---+---+---+---+
| I | P | T | O |
+---+---+---+---+
| G | R | A | F |
+---+---+---+---+
| I | A | E | S |
+---+---+---+---+
| R | O | M | A |
+---+---+---+---+
| N | T | I | C |
+---+---+---+---+
| A | S | S | S |
+---+---+---+---+

5. Se concatena cada línea de la tabla para obtener el texto el claro:

**LACRIPTOGRAFIAESROMANTICASSS**

Paradigma
---------

Orientado a objetos


Lenguaje de programación
------------------------
Python

Versión
+++++++
3.2>=
