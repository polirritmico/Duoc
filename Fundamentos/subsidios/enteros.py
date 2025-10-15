#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def input_usuario(minimo: int, maximo: int) -> int:
    mensaje_de_error = "Valor fuera de rango. Vuelva a intentarlo."

    while True:
        input_usuario_raw: str = input("Intente adivinar: ")
        if not input_usuario_raw.isdecimal():
            print(mensaje_de_error)
            continue

        input_usuario = int(input_usuario_raw)
        if minimo > input_usuario or maximo < input_usuario:
            print(mensaje_de_error)
            continue

        return input_usuario


def primer_intento(numero_a_adivinar: int, intentos: list[int]) -> bool:
    pass


def segundo_intento(numero_a_adivinar: int, intentos: list[int]) -> bool:
    pass


def tercer_intento(numero_a_adivinar: int, intentos: list[int]) -> bool:
    pass


def main():
    inferior: int = 0
    superior: int = 10

    numero_a_adivinar: int = randint(inferior, superior)
    intentos: list[int] = []

    if primer_intento(numero_a_adivinar, intentos):
        return

    if segundo_intento(numero_a_adivinar, intentos):
        return

    if tercer_intento(numero_a_adivinar, intentos):
        pass


if __name__ == "__main__":
    main()
