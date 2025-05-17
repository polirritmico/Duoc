#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable


class GruposFichaSocial:
    def __init__(
        self,
        denominacion: str,
        minimo: int,
        maximo: int,
    ):
        self.denominacion: str = denominacion
        self.minimo: int = minimo
        self.maximo: int = maximo


class Solicitante:
    def __init__(self, puntaje: int, zona: str, edad: int):
        self.puntaje: int = puntaje
        self.zona: str = zona
        self.edad: int = edad
        self.grupo: str = ""


Condicion = Callable[[Solicitante], bool]


class Subsidio:
    def __init__(
        self,
        condiciones: list[Condicion],
        monto: int,
    ):
        self.condiciones: list[Condicion] = condiciones
        self.monto: int = monto

    def cumple_condiciones_del_subsidio(self, solicitante: Solicitante) -> bool:
        for condicion in self.condiciones:
            if not condicion(solicitante):
                return False
        return True


class Subsidiador:
    def __init__(
        self,
        subsidios: list[Subsidio],
        bonos_extra: Callable[[Solicitante], int],
        grupos: list[GruposFichaSocial],
    ):
        self.subsidios: list = subsidios
        self.bonos_extra: Callable[[Solicitante], int] = bonos_extra
        self.grupos_ficha_social: list[GruposFichaSocial] = grupos

    def obtener_monto_subsidio_base(self, solicitante: Solicitante) -> int:
        for subsidio in self.subsidios:
            if subsidio.cumple_condiciones_del_subsidio(solicitante):
                return subsidio.monto

    def obtener_monto_bonos_extra(self, solicitante: Solicitante) -> int:
        monto_bonos: int = 0
        for bono_extra in self.bonos_extra:
            if bono_extra.cumple_condiciones_del_subsidio(solicitante):
                monto_bonos += bono_extra.monto
        return monto_bonos

    def clasificar_solicitante(self, solicitante: Solicitante) -> None:
        if solicitante.grupo:
            return

        for grupo in self.grupos_ficha_social:
            if solicitante.puntaje < grupo.minimo:
                continue
            if solicitante.puntaje > grupo.maximo:
                continue

            solicitante.grupo = grupo.denominacion
            return

        raise ValueError("Grupo socieconómico del solicitante erroneo")

    def subsidiar(self, solicitante: Solicitante) -> int:
        if not solicitante.grupo:
            self.clasificar_solicitante(solicitante)
        monto_subsidio_base: int = self.obtener_monto_subsidio_base(solicitante)
        monto_subsidio_extra: int = self.obtener_monto_bonos_extra(solicitante)
        return monto_subsidio_base + monto_subsidio_extra


class SubsidioGas:
    subsidiador: Subsidiador

    def __init__(self):
        # fmt: off
        def puntaje_bajo(sol: Solicitante) -> bool: return sol.grupo == "Bajo"
        def puntaje_medio(sol: Solicitante) -> bool: return sol.grupo == "Medio"
        def puntaje_alto(sol: Solicitante) -> bool: return sol.grupo == "Alto"

        def zona_sur(sol: Solicitante) -> bool: return sol.zona == "Sur"
        def zona_centro(sol: Solicitante) -> bool: return sol.zona == "Centro"
        def zona_norte(sol: Solicitante) -> bool: return sol.zona == "Norte"
        def zona_cualquiera(sol: Solicitante) -> bool: return True

        def tercera_edad(sol: Solicitante) -> bool: return sol.edad > 65
        # fmt: on

        lista_subsidios = [
            Subsidio([puntaje_bajo, zona_cualquiera], 45000),
            Subsidio([puntaje_medio, zona_sur], 40000),
            Subsidio([puntaje_medio, zona_norte], 30000),
            Subsidio([puntaje_medio, zona_centro], 30000),
            Subsidio([puntaje_alto, zona_sur], 20000),
            Subsidio([puntaje_alto, zona_norte], 10000),
            Subsidio([puntaje_alto, zona_centro], 10000),
        ]
        criterios_puntajes_ficha_social = [
            GruposFichaSocial("Bajo", 0, 4000),
            GruposFichaSocial("Medio", 4001, 7000),
            GruposFichaSocial("Alto", 7001, 10000),
        ]
        bonos_extra = [
            Subsidio([zona_sur], 5000),
            Subsidio([tercera_edad], 15000),
        ]

        self.subsidiador = Subsidiador(
            lista_subsidios, bonos_extra, criterios_puntajes_ficha_social
        )

    def subsidiar(self, solicitante: Solicitante) -> int:
        return self.subsidiador.subsidiar(solicitante)
