#!/usr/bin/env python
# -*- coding: utf-8 -*-


from matricula import BonoMatriculaDuoc, Solicitante


def test_ejemplo1() -> None:
    case = {
        "tipo": "Primer ingreso",
        "puntaje": 720,
        "zona_rural": True,
        "discapacidad": False,
    }
    expected = 35

    solicitante = Solicitante(**case)
    output = BonoMatriculaDuoc().calcular_bono(solicitante)

    assert expected == output


def test_ejemplo2() -> None:
    case = {
        "tipo": "Regular",
        "puntaje": 640,
        "zona_rural": False,
        "discapacidad": True,
    }
    expected = 10

    solicitante = Solicitante(**case)
    output = BonoMatriculaDuoc().calcular_bono(solicitante)

    assert expected == output
