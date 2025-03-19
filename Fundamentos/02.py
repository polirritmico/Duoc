#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Preguntar año nacimiento
# 2. Calcular edad
# 3. Entregar la edad con un mensaje

from datetime import date
from typing import Any


def get_user_input(msg: str, ExpectedType: Any) -> Any:
    while True:
        response = input(msg)
        try:
            output = ExpectedType(response)
            return output
        except Exception:
            raise Exception


def ask_year_of_birth(msg: str | None = None) -> int:
    msg = msg or "Ingresar año de nacimiento: "
    age: int = get_user_input(msg, int)
    return age


def calc_age(born_year: int) -> int:
    current_year = date.today().year
    age = current_year - born_year
    return age


def main():
    year_of_birth = ask_year_of_birth()
    age = calc_age(year_of_birth)
    print(f"Este año cumplirás: {age}")


if __name__ == "__main__":
    main()
