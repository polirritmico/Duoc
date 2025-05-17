#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable


class Solicitante:
    def __init__(self, edad: int, tiene_empleo: bool, quintil: int):
        self.edad = edad
        self.tiene_empleo = tiene_empleo
        self.quintil = quintil


class Subsidio:
    def __init__(
        self,
        monto_desempleado: int,
        monto_empleado: int,
        bonos_extra: list[Callable] | None = None,
    ):
        self.monto_desempleado: int = monto_desempleado
        self.monto_empleado: int = monto_empleado
        self.bonos_extra: list[Callable] = bonos_extra if bonos_extra else []

    def obtener_monto(self, solicitante: Solicitante) -> int:
        if solicitante.tiene_empleo:
            monto_subsidio = self.monto_empleado
        else:
            monto_subsidio = self.monto_desempleado
        bonos_extra = self.calcular_bonos_extra(solicitante)
        return monto_subsidio + bonos_extra

    def calcular_bonos_extra(self, solicitante: Solicitante) -> int:
        monto = sum(bono(solicitante) for bono in self.bonos_extra)
        return monto


class Subsidiador:
    def __init__(
        self,
        tabla_subsidios: dict[int, Subsidio],
    ):
        self.tabla_subsidios = tabla_subsidios
        self.validar_tabla_de_subsidios()

    def validar_tabla_de_subsidios(self):
        if not self.tabla_subsidios:
            raise ValueError("Sin tabla de subsidios o tabla sin datos")

    def input_usuario(self, mensaje: str, minimo: int, maximo: int) -> int:
        mensaje_error = "Error de entrada"

        while True:
            input_de_usuario_raw = input(mensaje)
            if not input_de_usuario_raw.isdecimal():
                print(mensaje_error)
                continue

            input_de_usuario: int = int(input_de_usuario_raw)
            if input_de_usuario < minimo or maximo < input_de_usuario:
                print(mensaje_error)
                continue

            return input_de_usuario

    def crear_solicitante(self) -> Solicitante:
        print("Ingrese los datos requeridos:")

        edad = self.input_usuario("Edad (18-120): ", 18, 120)
        quintil = self.input_usuario("Quintil (1-5): ", 1, 5)
        condicion_laboral = self.input_usuario(
            "Condición laboral (1 empleado, 2 desemplado): ", 1, 2
        )
        tiene_empleo = condicion_laboral == 1

        solicitante = Solicitante(edad, tiene_empleo, quintil)
        return solicitante

    def calcular_monto_subsidio(
        self, subsidio: Subsidio, solicitante: Solicitante
    ) -> int:
        return subsidio.obtener_monto(solicitante)

    def subsidiar(self, solicitante: Solicitante | None = None) -> None:
        if not solicitante:
            solicitante = self.crear_solicitante()

        subsidio = self.tabla_subsidios.get(solicitante.quintil)
        if not subsidio:
            raise ValueError("Quintil sin referencia en tabla de subsidios")

        monto = self.calcular_monto_subsidio(subsidio, solicitante)
        mensaje = f"El valor del subsidio es: ${monto:,}".replace(",", ".")
        print(mensaje)

        return monto


def main() -> int:
    print("--- Calculadora de subsidios ---")

    subsidio_quintiles_1_o_2 = Subsidio(10000, 8000)
    subsidio_quintil_3 = Subsidio(6000, 4000)
    subsidio_quintiles_4_o_5 = Subsidio(1500, 1500)

    tabla_subsidios = {
        1: subsidio_quintiles_1_o_2,
        2: subsidio_quintiles_1_o_2,
        3: subsidio_quintil_3,
        4: subsidio_quintiles_4_o_5,
        5: subsidio_quintiles_4_o_5,
    }

    def bono_quintil_1_2(solicitante):
        return 60000 if solicitante.quintil in [1, 2] else 0

    def bono_edad(solicitante):
        return 45000 if solicitante.edad > 65 else 0

    bonos_extra = [bono_quintil_1_2, bono_edad]

    try:
        agencia = Subsidiador(tabla_subsidios, bonos_extra)
        agencia.subsidiar()
    except Exception as err:
        print("Error en la ejecución: ", err)
        return 1
    return 0


if __name__ == "__main__":
    main()
