#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subsidio_arriendo import Solicitante, SubsidioArriendo


def test_ejemplo1() -> None:
    case = {"quintil": 1, "tiene_empleo": False, "edad": 70}
    expected = 450000

    solicitante = Solicitante(**case)
    subsidio_arriendo = SubsidioArriendo()
    output = subsidio_arriendo.calcular(solicitante)

    assert expected == output


def test_ejemplo2() -> None:
    case = {"quintil": 3, "tiene_empleo": True, "edad": 45}
    expected = 200000

    solicitante = Solicitante(**case)
    subsidio_arriendo = SubsidioArriendo()
    output = subsidio_arriendo.calcular(solicitante)

    assert expected == output
