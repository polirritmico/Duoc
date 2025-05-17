#!/usr/bin/env python
# -*- coding: utf-8 -*-


from subsidio_academico import Solicitante, Subsidiador, Subsidio


def test_caso1():
    case_solicitante = Solicitante(6.5, 1)
    expected_arancel = 1440000
    expected_matricula = 76500
    valores_base = {
        "arancel": 1800000,
        "matricula": 90000,
    }
    bonos_extra_quintil_1_2_3 = [
        lambda sol: {"matricula": 8},
        lambda sol: {"matricula": 5} if sol.notas >= 6 else {},
    ]
    tabla_subsidios = {
        1: Subsidio(350000, 280000, bonos_extra_quintil_1_2_3),
        2: Subsidio(350000, 280000, bonos_extra_quintil_1_2_3),
        3: Subsidio(250000, 200000, bonos_extra_quintil_1_2_3),
        4: Subsidio(250000, 200000),
        5: Subsidio(250000, 200000),
    }

    subsidiador = Subsidiador(valores_base, tabla_subsidios)
    output = subsidiador.subsidiar(case_solicitante)
    assert expected_arancel == output.get("arancel")
    assert expected_matricula == output.get("matricula")


def test_caso2():
    case_solicitante = Solicitante(4.0, 5)
    expected_arancel = 1800000
    expected_matricula = 90000
