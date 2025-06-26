# Ejercicio tipo prueba 4

Haga un programa que permita generar un menú de gestión de entradas para el
Concierto de Trap con el “Conejo Simpático”. El menú principal debe permitir
mostrar 4 opciones:

```
MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.
```

Todas las opciones del menú deben estar implementadas mediante funciones
separadas del código principal (main).

Al ingresar a la opción 1.- Comprar entrada, se debe permitir ingresar nombre de
comprador, tipo de entrada y código de confirmación por separado. Para que la
compra sea exitosa se debe cumplir lo siguiente: a) el nombre de comprador no
debe estar repetido, b) el tipo de entrada solo permite “G” (General) o “V”
(VIP), c) el código de confirmación debe tener largo mínimo de 6 caracteres,
debe tener al menos 1 letra mayúscula, al menos 1 número y no puede tener
espacio en blanco.

En caso de cumplir todas las condiciones, la entrada se registra exitosamente.

Al ingresar la opción 2.- Consultar comprador, el menú debe permitir buscar
compradores mediante el nombre. Si el comprador existe, debe mostrar los datos
asociados: tipo de entrada y código de confirmación. Si no existe, debe mostrar
un mensaje indicando que “El comprador no se encuentra.”

Al ingresar la opción 3.- Cancelar compra, el menú debe permitir eliminar la
compra y toda la información asociada mediante el ingreso de un nombre de
comprador por teclado. Si la compra se cancela, se debe mostrar “¡Compra
cancelada!”, pero si el comprador no existe, se muestra “No se pudo cancelar la
compra.”

Al ingresar la opción 4.- Salir, el programa debe terminar mostrando: Programa
terminado...

Si se ingresa una opción distinta (que no sea 1, 2, 3 o 4), debe mostrarse:

Debe ingresar una opción válida!!

---

## Ejemplo:

```
MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.

Ingrese opción: 1
Ingrese nombre de comprador: Joe el trapeador
Ingrese tipo de entrada (G/V): G
Ingrese código de confirmación: 123
Código no válido. Intente otra vez.
Ingrese código de confirmación: Acceso123
Código validado. ¡Entrada registrada con éxito!

MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.

Ingrese opción: 2
Ingrese nombre de comprador a buscar: Joe del trap
El comprador no se encuentra.

MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.

Ingrese opción: 2
Ingrese nombre de comprador a buscar: Joe el trapeador
Tipo de entrada: G, Código: Acceso123

MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.

Ingrese opción: 1
Ingrese nombre de comprador: Lucia del trap
Ingrese tipo de entrada (G/V): v
Ingrese código de confirmación: Acceso123
Código validado. ¡Entrada registrada con éxito!

MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.

Ingrese opción: 3
Ingrese nombre de comprador a cancelar: Joe el trapeador
¡Compra cancelada!

MENU PRINCIPAL
1.- Comprar entrada.
2.- Consultar comprador.
3.- Cancelar compra.
4.- Salir.

Ingrese opción: 4
Programa terminado...
```
