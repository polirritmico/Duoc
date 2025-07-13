#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any, Protocol, Callable, Dataclass
from dataclasses import dataclass

@dataclass
class Usuario:
    rut: str
    nombre: str
    apellido: str

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}: {self.rut}"



class Usermatic:
    def __init__(self, usuarios: list[Usuario]):
        self.usuarios:list[Usuario] = usuarios

    def show_usuarios(self) -> None:
        for usuario in self.usuarios:
            print(usuario)


