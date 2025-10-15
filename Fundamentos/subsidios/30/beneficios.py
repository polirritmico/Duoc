#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable


class Estudiante:
    def __init__(
        self,
        promedio: float,
        quintil: int,
    ):
        self.promedio: float = promedio
        self.quintil: int = quintil


Condicion = Callable[[Estudiante], bool]


class Beneficio:
    def __init__(
        self,
        condiciones: list[Condicion],
        descuento: float,
    ):
        self.condiciones: list[Condicion] = condiciones
        self.descuento: float = descuento

    def cumple_condiciones(self, estudiante: Estudiante) -> bool:
        for condicion in self.condiciones:
            if not condicion(estudiante):
                return False
        return True

    def get_descuento(self) -> float:
        return self.descuento


class Beneficiadora:
    def __init__(
        self,
        beneficios_arancel: list[Beneficio],
        beneficios_matricula: list[Beneficio],
        monto_arancel_base: int,
        monto_matricula: int,
    ):
        self.beneficios_arancel: list[Beneficio] = beneficios_arancel
        self.beneficios_matricula: list[Beneficio] = beneficios_matricula
        self.monto_arancel_base: int = monto_arancel_base
        self.monto_matricula: int = monto_matricula

    def calcular_montos_beneficios(self, estudiante: Estudiante) -> tuple[int, int]:
        rebaja_arancel: float = self.obtener_rebaja_arancel(estudiante)
        rebaja_matricula: float = self.obtener_rebaja_matricula(estudiante)

        monto_arancel: int = int(
            self.monto_arancel_base - (self.monto_arancel_base * rebaja_arancel)
        )
        monto_matricula: int = int(
            self.monto_matricula - (self.monto_matricula * rebaja_matricula)
        )

        return (monto_arancel, monto_matricula)

    def obtener_rebaja_arancel(self, estudiante: Estudiante) -> float:
        for beneficio in self.beneficios_arancel:
            if beneficio.cumple_condiciones(estudiante):
                return beneficio.get_descuento()
        return 0

    def obtener_rebaja_matricula(self, estudiante: Estudiante) -> float:
        porcentaje_descuento: float = 0.0
        for beneficio in self.beneficios_matricula:
            if beneficio.cumple_condiciones(estudiante):
                porcentaje_descuento += beneficio.get_descuento()
        return porcentaje_descuento


class BeneficiadoraCaso:
    beneficiadora: Beneficiadora

    def __init__(self):
        # fmt: off
        def quintil_1(e: Estudiante) -> bool: return e.quintil == 1
        def quintil_2(e: Estudiante) -> bool: return e.quintil == 2
        def quintil_3(e: Estudiante) -> bool: return e.quintil == 3
        def quintil_4(e: Estudiante) -> bool: return e.quintil == 4
        def quintil_5(e: Estudiante) -> bool: return e.quintil == 5

        def promedio_mayor_62(e: Estudiante) -> bool: return e.promedio > 6.2
        def promedio_mayor_55(e: Estudiante) -> bool: return e.promedio > 5.5
        def promedio_menor_o_igual_62(e: Estudiante) -> bool: return e.promedio <= 6.2
        def promedio_mayor_o_igual_60(e: Estudiante) -> bool: return e.promedio >= 6.0
        # fmt: on

        beneficios_arancel: list[Beneficio] = [
            Beneficio([promedio_mayor_62, quintil_1], 0.17),
            Beneficio([promedio_mayor_62, quintil_2], 0.17),
            Beneficio([promedio_mayor_62, quintil_3], 0.13),
            Beneficio([promedio_mayor_62, quintil_4], 0.13),
            Beneficio([promedio_mayor_55, promedio_menor_o_igual_62, quintil_1], 0.10),
            Beneficio([promedio_mayor_55, promedio_menor_o_igual_62, quintil_2], 0.10),
            Beneficio([promedio_mayor_55, promedio_menor_o_igual_62, quintil_3], 0.07),
            Beneficio([promedio_mayor_55, promedio_menor_o_igual_62, quintil_4], 0.07),
        ]
        beneficios_matricula: list[Beneficio] = [
            Beneficio([quintil_1], 0.08),
            Beneficio([quintil_2], 0.08),
            Beneficio([quintil_3], 0.08),
            Beneficio([quintil_1, promedio_mayor_o_igual_60], 0.05),
            Beneficio([quintil_2, promedio_mayor_o_igual_60], 0.05),
            Beneficio([quintil_3, promedio_mayor_o_igual_60], 0.05),
        ]

        monto_arancel_base: int = 1800000
        monto_matricula: int = 90000

        self.beneficiadora = Beneficiadora(
            beneficios_arancel,
            beneficios_matricula,
            monto_arancel_base,
            monto_matricula,
        )

    def calcular_beneficio(self, estudiante: Estudiante) -> tuple[int, int]:
        arancel, matricula = self.beneficiadora.calcular_montos_beneficios(estudiante)
        return (arancel, matricula)
