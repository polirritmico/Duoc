#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable


class Solicitante:
    def __init__(self, quintil: int, con_empleo: bool, edad: int):
        self.quintil: int = quintil
        self.con_empleo: bool = con_empleo
        self.edad: int = edad


Condicion = Callable[[Solicitante], bool]


class Subsidio:
    def __init__(self, lista_condiciones: list[Condicion], monto: int):
        self.lista_condiciones: list[Condicion] = lista_condiciones
        self.monto: int = monto

    def cumple_condiciones(self, solicitante: Solicitante) -> bool:
        for condicion in self.lista_condiciones:
            if not condicion(solicitante):
                return False
        return True


class Subsidiadora:
    def __init__(
        self, lista_subsidios: list[Subsidio], lista_bonos_extra: list[Subsidio]
    ):
        self.lista_subsidios: list[Subsidio] = lista_subsidios
        self.lista_bonos_extra: list[Subsidio] = lista_bonos_extra

    def calcular_monto_base(self, solicitante: Solicitante) -> int:
        for subsidio in self.lista_subsidios:
            if subsidio.cumple_condiciones(solicitante):
                return subsidio.monto
        return 0

    def calcular_monto_bonos_extra(self, solicitante: Solicitante) -> int:
        monto: int = 0
        for bono_extra in self.lista_bonos_extra:
            if bono_extra.cumple_condiciones(solicitante):
                monto += bono_extra.monto
        return monto

    def subsidiar(self, solicitante: Solicitante) -> int:
        monto_subsidio_base: int = self.calcular_monto_base(solicitante)
        monto_bonos_extra: int = self.calcular_monto_bonos_extra(solicitante)
        return monto_subsidio_base + monto_bonos_extra


class SubsidiadoraGas:
    subsidiadora: Subsidiadora

    def __init__(self):
        # fmt: off
        def quintil_1(sol: Solicitante) -> bool: return sol.quintil == 1
        def quintil_2(sol: Solicitante) -> bool: return sol.quintil == 2
        def quintil_3(sol: Solicitante) -> bool: return sol.quintil == 3
        def quintil_4(sol: Solicitante) -> bool: return sol.quintil == 4
        def quintil_5(sol: Solicitante) -> bool: return sol.quintil == 5

        def desempleado(sol: Solicitante) -> bool: return sol.con_empleo is False
        def empleado(sol: Solicitante) -> bool: return sol.con_empleo is True

        def mayor_de_65(sol: Solicitante) -> bool: return sol.edad > 65
        # fmt: on

        lista_de_subsidios: list[Subsidio] = [
            Subsidio([quintil_1, desempleado], 10000),
            Subsidio([quintil_2, desempleado], 10000),
            Subsidio([quintil_1, empleado], 8000),
            Subsidio([quintil_2, empleado], 8000),
            Subsidio([quintil_3, desempleado], 6000),
            Subsidio([quintil_3, empleado], 4000),
            Subsidio([quintil_4, empleado], 1500),
            Subsidio([quintil_4, desempleado], 1500),
            Subsidio([quintil_5, empleado], 1500),
            Subsidio([quintil_5, desempleado], 1500),
        ]
        lista_de_bonos_extra: list[Subsidio] = [
            Subsidio([quintil_1], 2000),
            Subsidio([quintil_2], 2000),
            Subsidio([quintil_1, mayor_de_65], 3000),
            Subsidio([quintil_2, mayor_de_65], 3000),
        ]

        self.subsidiadora = Subsidiadora(lista_de_subsidios, lista_de_bonos_extra)

    def pedir_input_usuario(self, mensaje: str, minimo: int, maximo: int) -> int:
        mensaje_de_error = "No se reconoce el valor ingresado. Inténtelo de nuevo."

        while True:
            input_usuario_raw: str = input(mensaje)

            if not input_usuario_raw.isdecimal():
                print(mensaje_de_error)
                continue

            input_usuario: int = int(input_usuario_raw)
            if minimo > input_usuario or maximo < input_usuario:
                print(mensaje_de_error)
                continue

            return input_usuario

    def crear_solicitante(self) -> Solicitante:
        print("Bienvenido")
        print("Ingrese los datos requeridos.")

        msg = "Quintil (1-5): "
        quintil = self.pedir_input_usuario(msg, 1, 5)

        msg = "Condición laboral (1. Empleado, 2. Desempleado): "
        con_empleo = self.pedir_input_usuario(msg, 1, 2) == 1

        msg = "Edad: "
        edad = self.pedir_input_usuario(msg, 1, 120)

        solicitante = Solicitante(quintil, con_empleo, edad)
        return solicitante

    def subsidiar(self, solicitante: Solicitante | None = None) -> int:
        if not solicitante:
            solicitante = self.crear_solicitante()
        return self.subsidiadora.subsidiar(solicitante)


def main():
    subsidiadora = SubsidiadoraGas()
    monto = subsidiadora.subsidiar()

    msg = f"El valor del subsidio de gas es: ${monto:,}"
    print(msg.replace(",", "."))


if __name__ == "__main__":
    main()
