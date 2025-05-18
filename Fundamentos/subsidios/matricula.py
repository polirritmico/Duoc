#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable


class Solicitante:
    def __init__(
        self,
        tipo: str,
        puntaje: int,
        zona_rural: bool,
        discapacidad: bool,
    ):
        self.tipo: str = tipo
        self.puntaje: int = puntaje
        self.zona_rural: bool = zona_rural
        self.discapacidad: bool = discapacidad


Condicion = Callable[[Solicitante], bool]


class Beneficio:
    def __init__(self, condiciones: list[Condicion], monto: int):
        self.condiciones: list[Condicion] = condiciones
        self.monto: int = monto

    def cumple_condiciones(self, solicitante: Solicitante) -> bool:
        for condicion in self.condiciones:
            if not condicion(solicitante):
                return False
        return True


class Descontador:
    def __init__(self, beneficios: list[Beneficio], bonos_extra: list[Beneficio]):
        self.beneficios: list[Beneficio] = beneficios
        self.bonos_extra: list[Beneficio] = bonos_extra

    def calcular_bono(self, solicitante: Solicitante) -> int:
        for beneficio in self.beneficios:
            if beneficio.cumple_condiciones(solicitante):
                return beneficio.monto
        return 0

    def calcular_bono_extra(self, solicitante: Solicitante) -> int:
        monto_bonos: int = 0
        for bono_extra in self.bonos_extra:
            if bono_extra.cumple_condiciones(solicitante):
                monto_bonos += bono_extra.monto

        return monto_bonos

    def obtener_descuento(self, solicitante: Solicitante) -> int:
        monto_bono_base: int = self.calcular_bono(solicitante)
        monto_bono_extra: int = self.calcular_bono_extra(solicitante)

        return monto_bono_base + monto_bono_extra


class BonoMatriculaDuoc:
    descontador: Descontador

    def __init__(self):
        # fmt: off
        def primer_ingreso(sol: Solicitante) -> bool: return sol.tipo == "Primer ingreso"
        def regular(sol: Solicitante) -> bool: return sol.tipo == "Regular"
        def reingreso(sol: Solicitante) -> bool: return sol.tipo == "Reingreso"

        def puntaje_min_700(sol: Solicitante) -> bool: return sol.puntaje >= 700
        def puntaje_min_650(sol: Solicitante) -> bool: return sol.puntaje >= 650
        def puntaje_min_600(sol: Solicitante) -> bool: return sol.puntaje >= 600

        def zona_rural(sol: Solicitante) -> bool: return sol.zona_rural
        def discapacidad(sol: Solicitante) -> bool: return sol.discapacidad
        # fmt: on

        tabla_descuentos: list[Beneficio] = [
            Beneficio([primer_ingreso, puntaje_min_700], 30),
            Beneficio([primer_ingreso, puntaje_min_600], 20),
            Beneficio([regular, puntaje_min_650], 15),
            Beneficio([reingreso, puntaje_min_600], 10),
        ]
        bonos_adicionales: list[Beneficio] = [
            Beneficio([primer_ingreso, zona_rural], 5),
            Beneficio([discapacidad], 10),
        ]

        self.descontador = Descontador(tabla_descuentos, bonos_adicionales)

    def calcular_bono(self, solicitante: Solicitante | None = None) -> int:
        if not solicitante:
            solicitante = self.crear_solicitante()
        bono: int = self.descontador.obtener_descuento(solicitante)
        return bono

    def input_usuario(self, mensaje: str, minimo: int, maximo: int) -> int:
        mensaje_de_error: str = "Error de entrada. Vuelva a intentarlo."
        while True:
            respuesta_usuario_raw: str = input(mensaje)

            if not respuesta_usuario_raw.isdecimal():
                print(mensaje_de_error)
                continue

            respuesta_usuario: int = int(respuesta_usuario_raw)
            if minimo > respuesta_usuario or maximo < respuesta_usuario:
                print(mensaje_de_error)
                continue

            return respuesta_usuario

    def crear_solicitante(self) -> Solicitante:
        print("Bienvenido")
        print("Inserte los datos requeridos.")

        msg = "Tipo de estudiante (1: Regular, 2: Reingreso, 3: Primer ingreso): "
        tipo_raw = self.input_usuario(msg, 1, 3)
        tipo = ["", "Regular", "Reingreso", "Primer ingreso"][tipo_raw]

        msg = "Puntaje de ingreso: "
        puntaje = self.input_usuario(msg, 450, 850)

        msg = "¿Vive en zona rural? (1: Sí, 2: No): "
        zona_rural = self.input_usuario(msg, 1, 2) == 1

        msg = "¿Tiene alguna discapacidad acreditada? (1: Sí, 2: No): "
        discapacidad = self.input_usuario(msg, 1, 2) == 1

        solicitante = Solicitante(tipo, puntaje, zona_rural, discapacidad)
        return solicitante


def main() -> int:
    descontador = BonoMatriculaDuoc()
    bono = descontador.calcular_bono()
    print(f"El descuento en matrícula es: %{bono}")


if __name__ == "__main__":
    main()
