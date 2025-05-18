#!/usr/bin/env python
# -*- coding: utf-8 -*-


from subsidio_gas import Solicitante, SubsidiadoraGas


def test_ejemplo1() -> None:
    case = {"quintil": 1, "con_empleo": False, "edad": 70}
    expected = 15000

    solicitante = Solicitante(**case)
    subsidiadora = SubsidiadoraGas()
    output = subsidiadora.subsidiar(solicitante)

    assert expected == output


def test_ejemplo2() -> None:
    case = {"quintil": 3, "con_empleo": True, "edad": 45}
    expected = 4000

    solicitante = Solicitante(**case)
    subsidiadora = SubsidiadoraGas()
    output = subsidiadora.subsidiar(solicitante)

    assert expected == output
