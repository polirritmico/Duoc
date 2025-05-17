#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subsidio import Solicitante, Subsidiador, Subsidio


def test_subsidio_ejemplo1() -> None:
    case_solicitante = Solicitante(70, False, 1)
    bonos_extra = [
        lambda sol: 60000,
        lambda sol: 40000 if sol.edad > 65 else 0,
    ]
    tabla_subsidios = {
        1: Subsidio(350000, 280000, bonos_extra),
        2: Subsidio(350000, 280000, bonos_extra),
        3: Subsidio(250000, 200000),
    }
    expected = 450000

    subsidiador = Subsidiador(tabla_subsidios)
    output = subsidiador.subsidiar(case_solicitante)
    assert expected == output


def test_subsidio_arriendo_ejemplo1() -> None:
    case_solicitante = Solicitante(70, False, 1)
    bonos_extra = [
        lambda sol: 60000,
        lambda sol: 40000 if sol.edad > 65 else 0,
    ]
    tabla_subsidios = {
        1: Subsidio(350000, 280000, bonos_extra),
        2: Subsidio(350000, 280000, bonos_extra),
        3: Subsidio(250000, 200000),
    }
    expected = 450000

    subsidiador = Subsidiador(tabla_subsidios)
    output = subsidiador.subsidiar(case_solicitante)
    assert expected == output


def test_subsidio_arriendo_ejemplo2() -> None:
    case_solicitante = Solicitante(45, True, 3)
    bonos_extra = [
        lambda sol: 60000,
        lambda sol: 40000 if sol.edad > 65 else 0,
    ]
    tabla_subsidios = {
        1: Subsidio(350000, 280000, bonos_extra),
        2: Subsidio(350000, 280000, bonos_extra),
        3: Subsidio(250000, 200000),
    }
    expected = 200000

    subsidiador = Subsidiador(tabla_subsidios)
    output = subsidiador.subsidiar(case_solicitante)
    assert expected == output


def test_subsidio_gas_ejemplo1() -> None:
    case_solicitante = Solicitante(70, False, 1)
    bonos_extra = [
        lambda sol: 2000,
        lambda sol: 3000 if sol.edad > 65 else 0,
    ]
    tabla_subsidios = {
        1: Subsidio(10000, 8000, bonos_extra),
        2: Subsidio(10000, 8000, bonos_extra),
        3: Subsidio(6000, 4000),
        4: Subsidio(1500, 1500),
        5: Subsidio(1500, 1500),
    }
    expected = 15000

    subsidiador = Subsidiador(tabla_subsidios)
    output = subsidiador.subsidiar(case_solicitante)
    assert expected == output


def test_subsidio_gas_ejemplo2() -> None:
    case_solicitante = Solicitante(45, True, 3)
    bonos_extra = [
        lambda sol: 2000,
        lambda sol: 3000 if sol.edad > 65 else 0,
    ]
    tabla_subsidios = {
        1: Subsidio(10000, 8000, bonos_extra),
        2: Subsidio(10000, 8000, bonos_extra),
        3: Subsidio(6000, 4000),
        4: Subsidio(1500, 1500),
        5: Subsidio(1500, 1500),
    }
    expected = 4000

    subsidiador = Subsidiador(tabla_subsidios)
    output = subsidiador.subsidiar(case_solicitante)
    assert expected == output
