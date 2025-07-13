#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Constantes
MARCA = 1
COLOR = 0

producto2 = ["Rojo", "HP", 14, "SSD", "512GB", "i5", "Nvidia RTX 1080"]

# print(producto1)

# for elementos in producto1:
#     print(elementos)


producto1 = ["Azul", "Dell", 14, "SSD", "512GB", "i5", "Nvidia RTX 1080"]
producto1 = {
    0: "Azul",
    1: "Dell",
    2: 14,
    3: "SSD",
    4: "512GB",
    5: "i5",
    6: "Nvidia RTX 1080",
    7: ["rj45", "usb2", "power"],
}

# for elemento in producto1:
#     print(producto1[elemento])


# ------------------------------------------------------------------------------

producto3 = {
    "color": "Azul",
    "marca": "Dell",
    "pantalla": 14,
    "tipo_disco": "SSD",
    "capacidad_disco": "512GB",
    "cpu": "i5",
    "gpu": "Nvidia RTX 1080",
    "conectores": ["rj45", "usb3", "power"],
}

producto4 = {
    "color": "Azul",
    "marca": "Dell-falsificado",
    "tipo_disco": "SSD",
    "capacidad_disco": "512GB",
    "cpu": "i5",
    "conectores": ["usb3", "thunderbolt", "power"],
    "gpu": "Nvidia RTX 1080",
}

# ¿Cuántos dispositivos de la coleccion tienen conectores usb3?
coleccion = [producto3, producto4]

contador = 0
for producto in coleccion:
    conectores = producto["conectores"]
    if "usb3" in conectores:
        contador += 1

print(contador)


# 1. Recorremos los productos de la colección. ¿sobre qué operamos cada ciclo del for? -> producto
# 2. Acceder a los conectores del producto.
# 3. Buscar "usb3" dentro de los conectores del producto.
# 4. If lo encontramos: lo contamos

# Ir un nivel más abajo -> ¿qué estaría haciendo al ir un nivel más abajo?
# iterar los elementos


# Son producto3 y producto4 de la misma marca?
marca_de_producto_3 = producto3["marca"]
marca_de_producto_4 = producto4["marca"]

# print(marca_de_producto_3 == marca_de_producto_4)
# print(marca_de_producto_3 in marca_de_producto_4)

# Tiene pantalla el producto 4
# pantalla en producto4
# print("pantalla" in producto4)

# in -> BUSCA lo que hay a la izquierda en lo que hay en la derecha
# izquierda IN derecha

# print(producto4["conectores"])
