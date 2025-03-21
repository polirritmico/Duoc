# CheatSheet PSeint <=> Python

## Variables y Tipos de Datos

```pseint
Definir foo Como Numero;   // Float: 1, 1.234
Definir foo Como Real;     // Float: 1, 1.234
Definir foo Como Entero;   // Integer: 1, 2, 3

Definir foo Como Caracter; // String: alfanumérico

Definir foo Como Logico;   // Boolean: Verdadero o Falso
```

```python
foo: int = 1      # Integer
foo: float = 1.0  # Float
foo: str = ""     # String
foo: boolean = True # Boolean True/False
```

## Entrada y Salida

```pseint
Escribir "Foo";   // Imprime `Foo` en la pantalla (sin comillas)
Definir foo Como Caracter; // ¡Primero definir para evitar fallo!
foo = "Foo";
Leer foo; // Output: Foo
```

```python
print("Foo") # Imprime `Foo` en pantalla

foo = input("Mensaje") # Captura el input como string
```

---

## Operadores

### Aritméticos

| Símbolo | Descripción    | Python |
| ------- | -------------- | ------ |
| `+`     | Suma           | `+`    |
| `-`     | Resta          | `-`    |
| `*`     | Multiplicación | `*`    |
| `/`     | División       | `/`    |
| `^`     | Potencia       | `**`   |
| `%`     | Módulo         | `%`    |

Python también tiene división sin decimales `//` (trim).

### Relacionales

| Símbolo | Descripción       | Python |
| ------- | ----------------- | ------ |
| `==`    | Igualdad          | `==`   |
| `<>`    | Diferente         | `!=`   |
| `<`     | Menor que         | `<`    |
| `>`     | Mayor que         | `>`    |
| `<=`    | Menor o igual que | `<=`   |
| `>=`    | Mayor o igual que | `>=`   |

### Lógicos

| Símbolo | Descripción    | Python |
| ------- | -------------- | ------ |
| `Y`     | Y (AND)        | `and`  |
| `O`     | O (OR)         | `or`   |
| `NO`    | Negación (NOT) | `not`  |

---

## Funciones

```pseint
Funcion retorno <- Bar (arg)
	Definir retorno Como Caracter; // ¡Definir el output si no es un argumento!
	retorno = arg;
FinFuncion

Proceso Main
	Definir foo Como Caracter;
	foo = Bar("Foo");
	Escribir foo;
FinProceso // output: Foo
```

```python
def bar(arg):
    retorno = arg
    return retorno

foo = bar("foo")
print(foo)
```

---

## Condicionales

```pseint
Definir booleano Como Logico;
booleano = Verdadero;

Si booleano Entonces
  Escribir "True";
SiNo
    Escribir "False";
FinSi // output: True
```

```python
booleano = True
if booleano:
    print("True")
else:
    print("False")
```

## Switches

```pseint
Definir foo como Entero;
Definir bar como Entero;
Definir buz como Entero;
Definir seleccion como Entero;
foo = 1;
bar = 2;
buz = 3;
seleccion = buz;


Segun seleccion Hacer
    foo:
      Escribir "Foo";
    bar:
      Escribir "Bar";
    3:
      Escribir "Buz";

    De Otro Modo:
        Escribir "Default";
FinSegun // Output: Buz
```

Python >= 3.10 (Versiones antiguas usar `if-elif-else`):

```python
seleccion = 3
match seleccion:
    case 1:
        print("Foo")
    case 2:
        print("Bar")
    case 3:
        print("Buz")
    case _:
        print("Default")
```

---

## Bucles

### For

```pseint
Para i <- 1 Hasta 10 Con Paso 2 Hacer
    Escribir i
FinPara
```

```python
for i in range(1, 11, 2):
    print(i)
```

### While

```pseint
Definir x Como Entero;
x = 0;

Mientras x < 5 Hacer
  Escribir x;
  x = x + 1;
FinMientras // Output: 0 1 2 3 4
```

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

### Do While

```pseint
Definir iteracion Como Entero;
iteracion = 0;

Repetir
  Escribir iteracion;

  iteracion = iteracion + 1;
Hasta Que iteracion > 4
// Output: 0 1 2 3 4
```

```python
iteracion = 0

while True:
  print(iteracion)

  iteracion += 1
  if iteracion > 4:
    break
```

## Arrays

```pseint
Definir foo Como Caracter; // Definir tipo de datos del arreglo
Dimension foo[2]; // Definir tamaño. ¡Debe ser un literal no una variable!

foo[0] = "Foo";
foo[1] = "Bar";

Definir index Como Entero;
Para index = 0 Hasta 1 Hacer // "Hasta" es inclusivo (Ej: "Hasta 3" incluye el 3)
  Escribir foo[index];
FinPara // output: Foo Bar
```

```python
foo = ["Foo", "Bar"]
numbers_of_elements_in_foo = len(foo)
for i in range(numbers_of_elements_in_foo): # range es no inclusivo
  print(element)
```

O la alternativa más ergonómica:

```python
foo = ["Foo", "Bar"]
for element in foo:
  print(element)
```

### Pseudo arreglo variable

PSeint no permite definir el tamaño de un arreglo en tiempo de ejecución, pero
podemos definir una variable con el tamaño para que se comporte de esta forma:

```pseint
Definir arraySize Como Entero; // Variable con el tamaño que usaremos del arreglo
Definir array Como Caracter; // Tipo de datos del arreglo
Dimension array[9999]; // Le reservamos mucho espacio (debe ser mayor al arraySize)

arraySize = 2; // el verdadero tamaño del arreglo
array[0] = "Foo";
array[1] = "Bar";

Definir index Como Entero;
Para index = 0 Hasta arraySize - 1 Hacer // Menos 1 porque "Hasta" es inclusivo
  Escribir array[index];
FinPara
```

```python
array = ["Foo", "Bar"]
for i in range(len(array)):
  print(array[i])
```

## Matrices

```pseint
Definir matrix Como Caracter;
Dimension matrix[3,3]; // de 0 hasta 2 (n-1)

matrix[0,0] = "0";
matrix[0,1] = "1";
matrix[0,2] = "2";
matrix[1,0] = "3";
matrix[1,1] = "4";
matrix[1,2] = "5";
matrix[2,0] = "6";
matrix[2,1] = "7";
matrix[2,2] = "8";

Definir columna Como Entero;
Definir fila Como Entero;

Definir linea Como Caracter;

Para fila = 0 Hasta 2 Hacer
  linea = "";
  Para columna = 0 Hasta 2 Hacer
    linea = linea + matrix[fila, columna];
  FinPara
  Escribir linea;
FinPara // output: 012 345 678
```

```python
matrix = [
    ["0", "1", "2"],
    ["3", "4", "5"],
    ["6", "7", "8"],
]

for fila in range(3):
    linea = ""
    for columna in range(3):
        linea += matrix[fila][columna]
    print(linea)
```
