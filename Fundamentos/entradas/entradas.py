#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Se utilizará esta estructura de datos para las ventas:

    venta: dict[str, str] = {
        "nombre": "Usuario",
        "tipo": "G",
        "codigo": "abc123",
    }

Un diccionario con las llaves "usuario", "tipo" y "codigo". Cada una de estas
llaves de tipo string contiene a su vez un valor de tipo string, de ahí el
tipeado: `dict[str, str]`.
"""


def mostrar_menu() -> None:
    menu = [
        "",
        "MENU PRINCIPAL",
        "1.- Comprar entrada",
        "2.- Consultar comprador",
        "3.- Cancelar compra",
        "4.- Salir",
        "",
    ]
    for opcion in menu:
        print(opcion)


def pedir_opcion(valor_maximo_permitido: int) -> int:
    mensaje = "Ingrese una opción: "
    mensaje_de_error = "¡¡Debe ingresar una opción válida!!"

    while True:
        input_usuario_raw = input(mensaje)

        if not input_usuario_raw.isdecimal():
            print(mensaje_de_error)
            continue

        input_usuario = int(input_usuario_raw)
        if 1 > input_usuario or valor_maximo_permitido < input_usuario:
            print(mensaje_de_error)
            continue

        return input_usuario


def pedir_nombre() -> str:
    nombre = input("Escriba el nombre de usuario a buscar: ")
    return nombre


def pedir_datos_entrada() -> dict:
    nombre = input("Ingrese nombre de usuario: ")
    tipo = input("Ingrese tipo de venta (G/V): ")
    codigo = pedir_codigo_de_configuracion()
    venta = {
        "nombre": nombre,
        "tipo": tipo.upper(),
        "codigo": codigo,
    }

    return venta


def pedir_codigo_de_configuracion() -> str:
    mensaje = "Ingrese el código de confirmación: "
    mensaje_de_error = "Valor de código inválido."
    mensaje_de_exito = "Código validado."

    while True:
        codigo = input(mensaje)

        if validar_codigo_de_confirmacion(codigo):
            print(mensaje_de_exito)
            return codigo
        else:
            print(mensaje_de_error)


def validar_nombre_unico(nombre: str, ventas: list[dict]) -> bool:
    nombre_unico = buscar_venta_por_nombre_de_usuario(nombre, ventas) is None
    if nombre_unico:
        return False
    return True


def validar_tipo_de_entrada(tipo: str) -> bool:
    if tipo == "V" or tipo == "G":
        return True
    return False


def validar_codigo_con_almenos_una_letra(codigo: str) -> bool:
    tiene_solo_numeros = codigo.isdecimal()
    if tiene_solo_numeros:
        return False
    return True


def validar_codigo_con_almenos_un_numero(codigo: str) -> bool:
    tiene_solo_letras = codigo.isalpha()
    if tiene_solo_letras:
        return False
    return True


def validar_codigo_longitud_minima(longitud_minima: int, codigo: str) -> bool:
    if len(codigo) >= longitud_minima:
        return True
    return False


def validar_codigo_sin_espacios(codigo: str) -> bool:
    tiene_espacios = " " in codigo
    if tiene_espacios:
        return False
    return True


def validar_codigo_tiene_solo_numeros_y_letras(codigo: str) -> bool:
    return codigo.isalnum()


def validar_codigo_de_confirmacion(codigo) -> bool:
    if not validar_codigo_tiene_solo_numeros_y_letras(codigo):
        return False

    if not validar_codigo_con_almenos_una_letra(codigo):
        return False

    if not validar_codigo_con_almenos_un_numero(codigo):
        return False

    if not validar_codigo_longitud_minima(6, codigo):
        return False

    if not validar_codigo_sin_espacios(codigo):
        return False

    return True


def validar_venta(entrada: dict, ventas: list[dict]) -> bool:
    if not validar_nombre_unico(entrada["nombre"], ventas):
        return False

    if not validar_tipo_de_entrada(entrada["tipo"]):
        return False

    return True


def mostrar_info_venta(venta: dict) -> None:
    print("\nDetalle de la venta:")
    # print(f"Nombre: {venta["nombre"]}")
    print(f"Tipo de entrada: {venta["tipo"]}")
    print(f"Código de confirmación: {venta["codigo"]}")


def cancelar_compra(nombre: str, ventas: list[dict]) -> None:
    venta_encontrada = buscar_venta_por_nombre_de_usuario(nombre, ventas)
    if venta_encontrada:
        ventas.remove(venta_encontrada)
        print("Compra cancelada")
    else:
        print("No se ha cancelado la compra")


def buscar_venta_por_nombre_de_usuario(nombre: str, ventas: list[dict]) -> dict | None:
    for venta in ventas:
        if nombre == venta["nombre"]:
            return venta
    return


def consultar_comprador(nombre: str, ventas: list[dict]) -> None:
    venta_encontrada = buscar_venta_por_nombre_de_usuario(nombre, ventas)
    if venta_encontrada:
        mostrar_info_venta(venta_encontrada)
    else:
        print("El comprador no se encuentra.")


def realizar_venta(entrada: dict, ventas: list[dict]) -> None:
    ventas.append(entrada)


def comprar_entrada(ventas: list[dict]) -> None:
    entrada = pedir_datos_entrada()

    venta_valida = validar_venta(entrada, ventas)
    if not venta_valida:
        print("Datos inválidos. No se ha realizado la venta.")
    else:
        realizar_venta(entrada, ventas)
        print("¡Entrada registrada con éxito!")


def cerrar_programa() -> None:
    print("Programa terminado...")
    exit()


def ejecutar_opcion(opcion: int, ventas: list) -> None:
    if opcion == 1:
        comprar_entrada(ventas)

    elif opcion == 2:
        nombre = pedir_nombre()
        consultar_comprador(nombre, ventas)

    elif opcion == 3:
        nombre = pedir_nombre()
        cancelar_compra(nombre, ventas)

    elif opcion == 4:
        cerrar_programa()


def main() -> None:
    ventas = []

    while True:
        mostrar_menu()
        opcion = pedir_opcion(valor_maximo_permitido=4)
        ejecutar_opcion(opcion, ventas)


if __name__ == "__main__":
    main()
