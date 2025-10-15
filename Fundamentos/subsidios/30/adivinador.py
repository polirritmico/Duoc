#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randint


def pedir_numero(mensaje: str) -> int:
    mensaje_de_error = "Valor no numérico. Vuelva a intentarlo"
    while True:
        numero_str = input(mensaje)
        if not numero_str.isdecimal():
            print(mensaje_de_error)
            continue

        numero: int = int(numero_str)
        return numero


def pista_mayor_menor(numero: int, numero_secreto: int) -> None:
    pista = "mayor" if numero_secreto > numero else "menor"
    print("El número es " + pista)


def pista_cerca(intento1: int, intento2: int, numero_secreto: int) -> None:
    msg = "El número que buscas está más cerca de {} que de {}"
    distancia_intento1 = abs(numero_secreto - intento1)
    distancia_intento2 = abs(numero_secreto - intento2)
    if distancia_intento1 > distancia_intento2:
        print(msg.format(intento2, intento1))
        return
    if distancia_intento1 < distancia_intento2:
        print(msg.format(intento1, intento2))
        return
    else:
        print("El número que buscas está a la misma distancia de ambos intentos")


def adivinar() -> int:
    num1 = pedir_numero("Ingrese límite inferior: ")
    num2 = pedir_numero("Ingrese límite superior: ")

    numero_secreto: int = randint(num1, num2)

    intento1: int = pedir_numero("Intente adivinar: ")
    if intento1 == numero_secreto:
        print("Felicitaciones, adivinaste al primer intento")
        return 0
    else:
        pista_mayor_menor(intento1, numero_secreto)

    intento2 = pedir_numero("Intente de nuevo: ")
    if intento2 == numero_secreto:
        print("Felicitaciones, adivinaste al segundo intento")
        return 0
    else:
        pista_mayor_menor(intento2, numero_secreto)
        pista_cerca(intento1, intento2, numero_secreto)

    intento3 = pedir_numero("Intente la última vez: ")
    if intento3 == numero_secreto:
        print("Felicitaciones, adivinaste al tercer intento")
        return 0
    else:
        print(f"Perdiste.\nEl número era el {numero_secreto}")


adivinar()
