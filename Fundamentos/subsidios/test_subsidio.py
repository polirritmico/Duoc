#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subsidio import Solicitante, SubsidioGas


def test_subsidio_de_gas_ejemplo1() -> None:
    case = {"puntaje": 3200, "zona": "Sur", "edad": 70}
    expected = 65000

    case = Solicitante(**case)
    subsidiaria = SubsidioGas()
    output = subsidiaria.subsidiar(case)

    assert expected == output


def test_subsidio_de_gas_ejemplo2() -> None:
    case = {"puntaje": 8000, "zona": "Norte", "edad": 40}
    expected = 10000

    solicitante = Solicitante(**case)
    subsidiaria = SubsidioGas()
    output = subsidiaria.subsidiar(solicitante)

    assert expected == output
