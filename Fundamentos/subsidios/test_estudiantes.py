#!/usr/bin/env python
# -*- coding: utf-8 -*-

from estudiantes import BeneficiosCaso1, Estudiante


def test_ejemplo1() -> None:
    case = {"promedio": 6.5, "quintil": 1}
    expected_arancel = 1440000
    expected_matricula = 75500

    estudiante = Estudiante(**case)
    beneficiaria = BeneficiosCaso1()
    output = beneficiaria.calcular_beneficio(estudiante)

    output_arancel, output_matricula = output
    assert expected_arancel == output_arancel
    assert expected_matricula == output_matricula
