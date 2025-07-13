#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Función si return y sin parámetros
def menu_principal() -> None:
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")


def obtener_opcion2():
    while True:
        try:
            opcion = int(input("ingresa una opcion"))
            if opcion > 5 or opcion < 1:
                obtener_opcion2()
            else:
                return opcion
        except Exception:
            continue


# Función con return y sin parámetros
def obtener_opcion() -> int:
    msg_error: str = "Valor inválido"
    minimo: int = 1
    maximo: int = 4

    while True:
        input_usuario_raw: str = input("Ingresa una opción")
        if not input_usuario_raw.isdecimal():
            print(msg_error)
            continue

        input_usuario: int = int(input_usuario_raw)
        if minimo > input_usuario or maximo < input_usuario:
            print(msg_error)
            continue

        return input_usuario


# Función sin return y con parámetros
def ejecutar_caso(opcion: int) -> None:
    if opcion == 1:
        print("1.- Ingresar usuario.")
    if opcion == 2:
        print("2.- Buscar usuario.")
    if opcion == 3:
        print("3.- Eliminar usuario.")
    if opcion == 4:
        print("4.- Salir.")
    if opcion == 5:
        print("Listado de usuarios")
    else:
        print("Opción inválida")


# menu_principal()
# obtener_opcion()
option = obtener_opcion2()
print(option)
