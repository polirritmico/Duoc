#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import Callable


class GrupoFichaSocial:
    def __init__(self, denominacion: str, minimo: int, maximo: int):
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
    """Un subsidio es una lista de condiciones que un solicitante debe cumplir
    para obtener un monto de beneficio."""

    def __init__(self, condiciones: list[Condicion], monto: int):
        self.condiciones: list[Condicion] = condiciones
        self.monto: int = monto

    def cumple_condiciones(self, solicitante: Solicitante) -> bool:
        for condicion in self.condiciones:
            if not condicion(solicitante):
                return False
        return True


class Subsidiaria:
    def __init__(
        self,
        subsidios: list[Subsidio],
        bonos_extra: list[Subsidio],
        grupos_ficha_social: list[GrupoFichaSocial],
    ):
        self.subsidios: list = subsidios
        self.bonos_extra: list[Subsidio] = bonos_extra
        self.grupos_ficha_social: list[GrupoFichaSocial] = grupos_ficha_social

    def obtener_monto_subsidio_base(self, solicitante: Solicitante) -> int:
        for subsidio in self.subsidios:
            if subsidio.cumple_condiciones(solicitante):
                return subsidio.monto
        return 0

    def obtener_monto_bonos_extra(self, solicitante: Solicitante) -> int:
        monto_bonos: int = 0
        for bono_extra in self.bonos_extra:
            if bono_extra.cumple_condiciones(solicitante):
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
            GrupoFichaSocial("Bajo", 0, 4000),
            GrupoFichaSocial("Medio", 4001, 7000),
            GrupoFichaSocial("Alto", 7001, 10000),
        ]
        bonos_extra = [
            Subsidio([zona_sur], 5000),
            Subsidio([tercera_edad], 15000),
        ]

        self.subsidiaria = Subsidiaria(
            lista_subsidios, bonos_extra, criterios_puntajes_ficha_social
        )

    def input_usuario(self, mensaje: str, minimo: int, maximo: int) -> int:
        mensaje_de_error: str = "No se reconoce el valor ingresado."
        while True:
            valor_ingresado_raw: str = input(mensaje)

            if not valor_ingresado_raw.isdecimal():
                print(mensaje_de_error)
                continue
            valor_ingresado: int = int(valor_ingresado_raw)

            if minimo > valor_ingresado or maximo < valor_ingresado:
                print(mensaje_de_error)
                continue
            return valor_ingresado

    def crear_solicitante(self) -> Solicitante:
        print("Ingrese los datos requeridos:")

        msg = "Puntaje de ficha social (0-1000): "
        puntaje = self.input_usuario(msg, 0, 10000)

        msg = "Zona geográfica (1 Norte, 2 Centro, 3 Sur): "
        zona_idx = self.input_usuario(msg, 1, 3) - 1  # convert to 0-idx
        zona = ["Norte", "Centro", "Sur"][zona_idx]

        edad = self.input_usuario("Edad: ", 1, 127)

        solicitante = Solicitante(puntaje, zona, edad)
        return solicitante

    def subsidiar(self, solicitante: Solicitante | None = None) -> int:
        if not solicitante:
            solicitante = self.crear_solicitante()
        return self.subsidiaria.subsidiar(solicitante)


def main():
    print("----------\nBienvenido\n----------\n")

    subsidio_gas = SubsidioGas()
    monto_subsidio = subsidio_gas.subsidiar()

    mensaje = f"El valor del subsidio de gas es ${monto_subsidio:,}"
    print(mensaje.replace(",", "."))

    return 0


if __name__ == "__main__":
    main()
