#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable


class Solicitante:
    def __init__(self, quintil: int, tiene_empleo: bool, edad: int):
        self.quintil: int = quintil
        self.tiene_empleo: bool = tiene_empleo
        self.edad: int = edad


Condicion = Callable[[Solicitante], bool]


class Subsidio:
    def __init__(self, lista_condiciones: list[Condicion], monto: int):
        self.condiciones: list[Condicion] = lista_condiciones
        self.monto: int = monto

    def cumple_condiciones(self, solicitante: Solicitante) -> bool:
        for condicion in self.condiciones:
            result = condicion(solicitante)
            if not result:
                return False
        return True


class Subsidiadora:
    def __init__(
        self,
        lista_subsidios: list[Subsidio],
        lista_bonos_adicionales: list[Condicion],
    ):
        self.lista_subsidios: list[Subsidio] = lista_subsidios
        self.lista_bonos_adicionales: list[Subsidio] = lista_bonos_adicionales

    def calcular(self, solicitante: Solicitante) -> int:
        monto_base = self.calcular_monto_base(solicitante)
        monto_bonos_adicionales = self.calcular_bonos_adicionales(solicitante)
        return monto_base + monto_bonos_adicionales

    def calcular_monto_base(self, solicitante: Solicitante) -> int:
        for subsidio in self.lista_subsidios:
            if subsidio.cumple_condiciones(solicitante):
                return subsidio.monto
        return 0

    def calcular_bonos_adicionales(self, solicitante: Solicitante) -> int:
        monto: int = 0
        for bono_adicional in self.lista_bonos_adicionales:
            if bono_adicional.cumple_condiciones(solicitante):
                monto += bono_adicional.monto
        return monto


class SubsidioArriendo:
    subsidiadora: Subsidiadora

    def __init__(self):
        # fmt: off
        def quintil_1(sol: Solicitante) -> bool: return sol.quintil == 1
        def quintil_2(sol: Solicitante) -> bool: return sol.quintil == 2
        def quintil_3(sol: Solicitante) -> bool: return sol.quintil == 3
        def quintil_4(sol: Solicitante) -> bool: return sol.quintil == 4
        def quintil_5(sol: Solicitante) -> bool: return sol.quintil == 5

        def desempleado(sol: Solicitante) -> bool: return sol.tiene_empleo is False
        def empleado(sol: Solicitante) -> bool: return sol.tiene_empleo is True

        def mayor_de_65(sol: Solicitante) -> bool: return sol.edad > 65
        # fmt: on

        lista_subsidios: list[Subsidio] = [
            Subsidio([quintil_1, desempleado], 350000),
            Subsidio([quintil_2, desempleado], 280000),
            Subsidio([quintil_1, empleado], 280000),
            Subsidio([quintil_1, empleado], 280000),
            Subsidio([quintil_3, desempleado], 250000),
            Subsidio([quintil_3, empleado], 200000),
        ]

        lista_bonos_adicionales: list[Subsidio] = [
            Subsidio([quintil_1], 60000),
            Subsidio([mayor_de_65], 40000),
        ]

        self.subsidiadora = Subsidiadora(lista_subsidios, lista_bonos_adicionales)

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
        print("Inserte datos requeridos.")

        msg = "Quintil (1-5): "
        quintil = self.pedir_input_usuario(msg, 1, 5)

        msg = "Condicion laboral (1 Empleado, 2 Desempleado): "
        tiene_empleo = self.pedir_input_usuario(msg, 1, 2) == 1

        msg = "Edad: "
        edad = self.pedir_input_usuario(msg, 1, 120)

        Solicitante(quintil, tiene_empleo, edad)

    def calcular(self, solicitante: Solicitante) -> int:
        if not solicitante:
            solicitante = self.crear_solicitante()
        return self.subsidiadora.calcular(solicitante)


def main():
    pass


if __name__ == "__main__":
    main()
