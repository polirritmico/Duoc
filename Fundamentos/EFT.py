#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pybooks tienda
notebooks -> dict productos
notebooks: key: modelo, val: list[marca, pantalla, RAM, tipo disco, capacidad disco, cpu, gpu]

disco: DD mecánico o SSD estado sólido
stock: dict[str, list[int, int]] -> key: modelo, val: [precio, stock]
"""

productos: dict[str, list[str | float | int]] = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
}

stock: dict[str, list[int, int]] = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
    "123FHD": [290890, 32],
    "342FHD": [444990, 7],
    "GF75HD": [749990, 2],
    "UWU131HD": [349990, 1],
    "FS1230HD": [249990, 0],
}

STOCK_PRECIO = 0
STOCK_CANTIDAD = 1

PROD_MARCA = 0
PROD_PANTALLA = 1
PROD_RAM = 2
PROD_DD_TIPO = 3
PROD_DD_CAP = 4
PROD_CPU = 5
PROD_GPU = 6


def mostrar_menu() -> None:
    menu: list[str] = [
        "",
        "*** MENU PRINCIPAL ***",
        "1. Stock marca.",
        "2. Búsqueda por precio.",
        "3. Actualizar precio.",
        "4. Salir",
        "",
    ]
    for index, entry in enumerate(menu):
        print(entry)


def pedir_opcion_usuario(valor_maximo) -> int:
    mensaje: str = "Ingrese una opción: "
    mensaje_de_error: str = "¡¡Debe seleccionar una opción válida!!"

    while True:
        input_usuario_raw: str = input(mensaje)

        if not input_usuario_raw.isdecimal():
            print(mensaje_de_error)
            continue

        input_usuario: int = int(input_usuario_raw)
        if 1 > input_usuario or valor_maximo < input_usuario:
            print(mensaje_de_error)
            continue

        print()
        return input_usuario


def stock_marca(marca: str) -> None:
    marca = marca.lower()
    cantidad = 0
    for modelo, info in productos.items():
        if info[PROD_MARCA].lower() == marca:
            cantidad += stock.get(modelo)[STOCK_CANTIDAD]
    print(f"El stock es: {cantidad}")


def revisar_stock_marca() -> None:
    marca_a_revisar = input("Ingrese marca a consultar: ")
    stock_marca(marca_a_revisar)


def pedir_precio_sin_rango(mensaje: str) -> int:
    while True:
        input_usuario_raw = input(mensaje)

        try:
            input_usuario = int(input_usuario_raw)
        except Exception:
            print("¡¡Debe ingresar valores enteros!!")
            continue

        if input_usuario < 0:
            print("Valor debe ser un entero positivo.")
            continue

        return input_usuario


def pedir_precio_usuario(mensaje: str, valor_minimo: int, valor_maximo: int) -> int:
    while True:
        input_usuario_raw = input(mensaje)

        try:
            input_usuario = int(input_usuario_raw)
        except Exception:
            print("¡¡Debe ingresar valores enteros!!")
            continue

        if input_usuario < valor_minimo or input_usuario > valor_maximo:
            print("Valor fuera de rango. Inténtelo de nuevo.")
            continue

        return input_usuario


def busqueda_precio(p_min: int, p_max: int) -> None:
    equipos = []
    for modelo, datos in stock.items():
        precio = datos[STOCK_PRECIO]
        if p_min > precio:
            continue
        if p_max < precio:
            continue
        if modelo not in productos:
            continue

        marca = productos[modelo][PROD_MARCA]
        equipos.append(f"{marca}--{modelo}")

    if not equipos:
        print("No hay notebooks en ese rango de precios.")
        return

    equipos.sort(key=str.lower)
    print(f"Los notebooks entre los precios consultas son: {equipos}")


def busqueda_por_precio() -> None:
    precio_minimo = pedir_precio_sin_rango("Ingrese precio mínimo: ")
    precio_maximo = pedir_precio_usuario(
        "Ingrese precio máximo: ", precio_minimo, 999999999
    )
    busqueda_precio(precio_minimo, precio_maximo)


def actualizar_precio(modelo: str, p: int) -> bool:
    if modelo not in stock:
        return False

    datos_modelo = stock[modelo]
    datos_modelo[STOCK_PRECIO] = p
    return True


def pregunta_si_no(mensaje) -> bool:
    while True:
        input_usuario = input(mensaje).lower()
        if input_usuario in ["s", "si", "sí"]:
            return True
        if input_usuario in ["n", "no"]:
            return False
        print("Respuesta inválida. Intentelo de nuevo")


def opcion_actualizar_precio() -> None:
    continuar = True
    while continuar:
        modelo = input("Ingrese modelo a actualizar: ")
        precio = pedir_precio_sin_rango("Ingrese precio nuevo: ")

        if actualizar_precio(modelo, precio):
            print("¡¡Precio actualizado!!")
        else:
            print("¡¡El modelo no existe!!")

        continuar = pregunta_si_no("¿Desea actualizar otro precio de notebook? (s/n): ")


def salir_del_programa() -> None:
    print("Programa finalizado")
    exit()


def ejecutar_opcion(opcion: int) -> None | bool:
    if opcion == 1:
        revisar_stock_marca()
    elif opcion == 2:
        busqueda_por_precio()
    elif opcion == 3:
        opcion_actualizar_precio()
    elif opcion == 4:
        salir_del_programa()
    else:
        raise ValueError(f"Valor de opcion no reconocida: '{opcion}'")


def main() -> None:
    try:
        while True:
            mostrar_menu()
            opcion: int = pedir_opcion_usuario(4)
            ejecutar_opcion(opcion)

    except Exception as err:
        msg = (
            "Ha ocurrido un error inesperado. "
            "Póngase en contacto con el desarrollador y comparta el siguiente mensaje:\n"
        )
        print(msg, err)


if __name__ == "__main__":
    main()
