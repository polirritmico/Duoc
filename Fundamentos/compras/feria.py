#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable

type Producto = list[str, int]
NOMBRE = 0
PRECIO = 1

type Menu = list[str, list[list[str, Callable]]]
TITULO = 0
OPCIONES = 1


def comprar_pantalones():
    pass


menu_principal: Menu = [
    "=== Falaferia ===",
    [
        "Pantalones",
        "Poleras",
        "Pagar",
        "Salir",
        # ["Pantalones", menu_pantalones],
        # ["Poleras", menu_poleras],
        # ["Pagar", comprar],
        # ["Salir", salir_del_programa],
    ],
]

menu_pantalon: Menu = [
    "=== Pantalones ===",
    [
        "Pantalón Rojo",
        "Pantalón Azul",
        "Jeans",
        "Pantalón Chino",
        "Volver",
    ],
]


def comprar(articulo: str, precio: int, venta_completa: list[Producto]) -> None:
    venta: Producto = [articulo, precio]
    venta_completa.append(venta)


def pedir_opcion_al_usuario(maximo: int, mensaje: str = None) -> int:
    if not mensaje:
        mensaje = "Seleccione una opción: "
    mensaje_de_error: str = "Valor inválido."

    while True:
        input_usuario_raw: str = input(mensaje)

        if not input_usuario_raw.isdecimal():
            print(mensaje_de_error)
            continue

        input_usuario: int = int(input_usuario_raw)
        if 1 > input_usuario or maximo < input_usuario:
            print(mensaje_de_error)
            continue

        return input_usuario


def mostrar_menu(menu: Menu) -> None:
    print("\n" + menu[TITULO])
    for opcion in menu[OPCIONES]:
        print(opcion)
    print("\n")


def accion_menu_principal(opcion: int, menu: Menu, compras: list[Producto]) -> bool:
    if opcion == 4:
        return True

    if opcion == 1:
        menu_pantalones(compras)
    elif opcion == 2:
        menu_poleras(compras)
    elif opcion == 3:
        pass

    return False


def ejecutar_accion_pantalones():
    pass


def contar_opciones_del_menu(menu) -> int:
    opciones: int = len(menu[OPCIONES])
    return opciones


def main():
    todas_las_compras: list[Producto] = []
    salir: bool = False

    while not salir:
        mostrar_menu(menu_principal)
        cantidad_de_opciones: int = contar_opciones_del_menu(menu_principal)
        opcion = pedir_opcion_al_usuario(cantidad_de_opciones)
        salir = accion_menu_principal(opcion, menu_principal, todas_las_compras)


if __name__ == "__main__":
    main()
