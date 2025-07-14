#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Callable, Dict

from data import IndexProduct as P
from data import IndexStock as S
from data import products as loaded_products
from data import stock as loaded_stock


class Action:
    name: str

    def __init__(self, name: str, action: Callable[[], None]):
        self.name: str = name
        self.action: Callable = action

    def run(self) -> None:
        self.action()


class Store:
    actions: list[Action]
    header: str
    open_status: bool
    stock: dict[str, list[int, int]]
    products: dict[str, list[str | float | int]]

    def __init__(self):
        self.open_status: bool = True
        self.stock: Dict = {}
        self.products: Dict = {}

    def register_store(self, store: Action) -> None:
        store.is_open = self.is_open
        store.open_store = self.open_store
        store.close_store = self.close_store
        store.set_productos = self.set_products
        store.set_stock = self.set_stock
        store.set_action = self.set_action
        store.execute_action = self.execute_action

    def is_open(self) -> bool:
        return self.open_status

    def open_store(self) -> None:
        self.open_status = True

    def close_store(self) -> None:
        self.open_status = False

    def set_products(self, products: dict[str, list[str | float | int]]) -> None:
        self.products = products.copy()

    def set_stock(self, stock: dict[str, list[int, int]]) -> None:
        self.stock = stock.copy()

    def set_action(self, action: Action) -> None:
        self.actions.append(action)

    def execute_action(self, action: Callable) -> None:
        action()


class PyBooks:
    header: str = "*** MENU PRINCIPAL ***"

    def __init__(self):
        self.store = Store()
        self.store.register_store(self)
        self.store.set_stock(loaded_stock)
        self.store.set_products(loaded_products)

        self.actions: list[Action] = [
            Action("Stock marca", self.show_stock),
            Action("Búsqueda por precio", self.search_models_in_range),
            Action("Actualizar precio", self.update_price),
            Action("Salir", self.exit),
        ]

    def ask_yes_or_no(self, message: str) -> bool:
        while True:
            input_usr: str = input(message).lower()
            if input_usr in ["s", "si", "sí", "y", "yes"]:
                return True
            if input_usr in ["n", "no"]:
                return False

            print("Valor inválido. Inténtelo de nuevo.\n")

    def ask_positive_integer(self, message: str, minimal: int = 0) -> int:
        error_message: str = "Valor inválido. Inténtelo de nuevo."
        while True:
            input_usr_raw: str = input(message)

            if not input_usr_raw.isdecimal():
                print("¡¡Debe ingresar valores enteros positivos!!")
                continue

            input_usr: int = int(input_usr_raw)
            if input_usr < minimal:
                print(error_message)
                continue

            return input_usr

    def update_price(self) -> None:
        keep_running = True
        while keep_running:
            model = input("Ingrese modelo a actualizar: ")

            if model not in self.store.stock:
                print("¡¡El modelo no existe!!")
            else:
                new_price: int = self.ask_positive_integer("Ingrese nuevo precio: ")
                self.store.stock[model][S.PRICE] = new_price
                print("¡¡Precio actualizado!!")

            msg = "¿Desea actualizar otro precio de notebook? (s/n): "
            keep_running = self.ask_yes_or_no(msg)
            print()

    def get_products_in_range(self, minimum: int, maximum: int) -> list[str]:
        found: list[str] = []
        for model, stock in self.store.stock.items():
            price = stock[S.PRICE]
            if price >= minimum and price <= maximum:
                found.append(model)
        return found

    def get_brand_and_model(self, model: str) -> str | None:
        product_info = self.store.products.get(model)
        if not product_info:
            return
        brand = product_info[P.BRAND]
        return f"{brand}--{model}"

    def search_models_in_range(self) -> None:
        minimum = self.ask_positive_integer("Ingrese precio mínimo: ")
        maximum = self.ask_positive_integer("Ingrese precio máximo: ", minimum)

        found: list[str] = []
        products: list[str] = self.get_products_in_range(minimum, maximum)
        for model in products:
            info = self.get_brand_and_model(model)
            if info:
                found.append(info)

        if not found:
            print("No hay notebooks en ese rango de precios.")
            return

        found.sort(key=str.lower)
        print(f"Los notebooks entre los precios consultados son: {found}")

    def show_stock(self) -> None:
        brand = input("Ingrese marca a consultar: ").lower()
        amount = 0
        for model, info in self.store.products.items():
            if info[P.BRAND].lower() == brand:
                amount += self.store.stock.get(model)[S.AMOUNT]

        print(f"El stock es: {amount}")

    def exit(self) -> None:
        self.store.close_store()


class Menu:
    def __init__(self):
        self.current_user_selection = 0
        self.entries_action: dict[int, Callable] = {}
        self.entries_menu: dict[int, str] = {}
        self.header = ""
        self.last_option: int = 0
        self.option_id: int = 1

    def get_selected_option(self, get_id: bool = False) -> int:
        if get_id:
            return self.current_user_selection
        return self.entries_action.get(self.current_user_selection, 0)

    def get_new_option_id(self) -> int:
        new_id: int = self.option_id
        self.option_id += 1
        return new_id

    def add_menu_entry(self, action: Action) -> None:
        id: int = self.get_new_option_id()

        self.entries_action[id] = action.run

        entry: str = action.name.capitalize()
        entry = entry if entry.endswith(".") else entry + "."
        entry = f"{id}. {entry}"
        self.entries_menu[id] = entry

    def set_header(self, header: str) -> None:
        self.header = header

    def set_actions(self, actions: list[Callable]) -> None:
        self.actions: dict[Callable] = []
        for action in actions:
            self.add_menu_entry(action)
            self.last_option += 1

    def show(self) -> None:
        print("\n" + self.header)
        for option in self.entries_menu.values():
            print(option)

        print()

    def ask_usr_selection(
        self,
        message: str = "Ingrese una opción: ",
        error_message: str = "¡¡Debe seleccionar una opción válida!!",
    ) -> int:
        while True:
            usr_input_raw: str = input(message)

            if not usr_input_raw.isdecimal():
                print(error_message)
                continue

            usr_input: int = int(usr_input_raw)
            if 1 > usr_input or self.last_option < usr_input:
                print(error_message)
                continue

            print()
            self.current_user_selection = usr_input
            return usr_input


def main() -> None:
    try:
        pybooks = PyBooks()
        menu = Menu()
        menu.set_header(pybooks.header)
        menu.set_actions(pybooks.actions)

        while pybooks.is_open():
            menu.show()
            menu.ask_usr_selection()
            pybooks.execute_action(menu.get_selected_option())
        print("Programa finalizado.")

    except Exception as err:
        msg: str = (
            "Error inesperado. "
            "Contacte con el desarrollador y comparta el siguiente mensaje: \n\n"
        )
        print(msg, err)

    except KeyboardInterrupt:
        print("\nSe ha forzado el cerrado del programa manualmente.")


if __name__ == "__main__":
    main()
