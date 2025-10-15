#!/usr/bin/env python
# -*- coding: utf-8 -*-

from beneficios import BeneficiadoraCaso, Estudiante


def test_ejemplo1() -> None:
    caso = {"promedio": 6.5, "quintil": 1}
    arancel_esperado: int = 1440000
    matricula_esperada: int = 76500

    estudiante = Estudiante(**caso)
    beneficiadora = BeneficiadoraCaso()
    output_arancel, output_matricula = beneficiadora.calcular_beneficio(estudiante)

    assert arancel_esperado == output_arancel
    assert matricula_esperada == output_matricula
