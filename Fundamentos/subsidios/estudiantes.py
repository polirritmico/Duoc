#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable


class Estudiante:
    def __init__(self, promedio: float, quintil: int):
        self.promedio: float = promedio
        self.quintil: int = quintil


Condicion = Callable[[Estudiante], bool]


class Beneficio:
    def __init__(self, lista_condiciones: list[Condicion], monto: int):
        self.lista_condiciones: list[Condicion] = lista_condiciones
        self.monto: int = monto

    def cumple_condiciones(self, estudiante: Estudiante) -> bool:
        for condicion in self.lista_condiciones:
            if not condicion(estudiante):
                return False
        return True


class Beneficiadora:
    def __init__(
        self,
        beneficios_arancel: list[Beneficio],
        beneficios_matricula: list[Beneficio],
    ):
        self.beneficios_arancel: list[Beneficio] = beneficios_arancel
        self.beneficios_matricula: list[Beneficio] = beneficios_matricula

    def get_monto_arancel(self, estudiante: Estudiante) -> int:
        for beneficio in self.beneficios_arancel:
            if beneficio.cumple_condiciones(estudiante):
                return beneficio.monto
        return 0

    def get_monto_matricula(self, estudiante: Estudiante) -> int:
        monto: int = 0
        for beneficio_adicional in self.beneficios_matricula:
            if beneficio_adicional.cumple_condiciones(estudiante):
                monto += beneficio_adicional.monto
        return monto

    def get_montos_con_beneficios(
        self,
        estudiante: Estudiante,
        arancel_base: int,
        matricula_base: int,
    ) -> tuple[int, int]:
        beneficio_arancel: int = self.get_monto_arancel(estudiante)
        beneficio_matricula: int = self.get_monto_matricula(estudiante)

        monto_arancel = int(arancel_base * (100 - beneficio_arancel) / 100)
        monto_matricula = int(matricula_base * (100 - beneficio_matricula) / 100)

        return (monto_arancel, monto_matricula)


class BeneficiosCaso1:
    beneficiadora: Beneficiadora
    arancel_base: int
    matricula_base: int

    def __init__(self):
        # fmt: off
        def promedio_mayor_62(e: Estudiante) -> bool: return e.promedio > 6.2
        def promedio_mayor_o_igual_55(e: Estudiante) -> bool: return e.promedio > 5.5
        def promedio_mayor_o_igual_60(e: Estudiante) -> bool: return e.promedio >= 6.0
        def promedio_menor_62(e: Estudiante) -> bool: return e.promedio <= 6.2

        def quintil_1(e: Estudiante) -> bool: return e.quintil == 1
        def quintil_2(e: Estudiante) -> bool: return e.quintil == 2
        def quintil_3(e: Estudiante) -> bool: return e.quintil == 3
        def quintil_4(e: Estudiante) -> bool: return e.quintil == 4
        def quintil_5(e: Estudiante) -> bool: return e.quintil == 5
        # fmt: on

        beneficios_arancel: list[Beneficio] = [
            Beneficio([promedio_mayor_62, quintil_1], 17),
            Beneficio([promedio_mayor_62, quintil_2], 17),
            Beneficio([promedio_mayor_62, quintil_3], 13),
            Beneficio([promedio_mayor_62, quintil_4], 13),
            Beneficio([promedio_mayor_o_igual_55, promedio_menor_62, quintil_1], 10),
            Beneficio([promedio_mayor_o_igual_55, promedio_menor_62, quintil_2], 10),
            Beneficio([promedio_mayor_o_igual_55, promedio_menor_62, quintil_3], 7),
            Beneficio([promedio_mayor_o_igual_55, promedio_menor_62, quintil_4], 7),
        ]
        beneficios_matricula: list[Beneficio] = [
            Beneficio([quintil_1], 8),
            Beneficio([quintil_2], 8),
            Beneficio([quintil_3], 8),
            Beneficio([quintil_1, promedio_mayor_o_igual_60], 5),
            Beneficio([quintil_2, promedio_mayor_o_igual_60], 5),
            Beneficio([quintil_3, promedio_mayor_o_igual_60], 5),
        ]

        beneficiadora = Beneficiadora(beneficios_arancel, beneficios_matricula)

        self.beneficiadora = beneficiadora
        self.arancel_base = 1800000
        self.matricula_base = 90000

    def calcular_beneficio(
        self, estudiante: Estudiante | None = None
    ) -> tuple[int, int]:
        modo_manual: bool = estudiante is None

        if modo_manual:
            estudiante = self.crear_estudiante()
            beneficios = self.beneficiadora.get_montos_con_beneficios(
                estudiante, self.arancel_base, self.matricula_base
            )

            arancel, matricula = beneficios
            print(f"El valor del arancel es: {arancel:,}".replace(",", "."))
            print(f"El valor de la matrícula es: {matricula:,}".replace(",", "."))
        else:
            beneficios = self.beneficiadora.get_montos_con_beneficios(
                estudiante, self.arancel_base, self.matricula_base
            )

        return beneficios

    def crear_estudiante(self) -> Estudiante:
        print("Bienvenido")
        print("Ingrese los datos requeridos.")

        msg = "Promedio de notas: "
        promedio = self.input_usuario(msg, 1, 7)

        msg = "Quintil (1, 2, 3, 4, 5): "
        quintil = int(self.input_usuario(msg, 1, 5))

        estudiante = Estudiante(promedio, quintil)
        return estudiante

    def input_usuario(self, mensaje: str, minimo: int, maximo: int) -> float:
        mensaje_de_error: str = "No se reconoce el valor ingresado. Intente nuevamente."

        while True:
            entrada_usuario_raw = input(mensaje)
            if not entrada_usuario_raw.isdecimal():
                print(mensaje_de_error)
                continue

            entrada_usuario: float = float(entrada_usuario_raw)
            if minimo > entrada_usuario or maximo < entrada_usuario:
                print(mensaje_de_error)
                continue

            return entrada_usuario
