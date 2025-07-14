#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import IntEnum


class IndexProduct(IntEnum):
    BRAND = 0
    SCREEN = 1
    RAM = 2
    HD_TYPE = 3
    HD_CAP = 4
    CPU = 5
    GPU = 6


products: dict[str, list[str | float | int]] = {
    "8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i5", "Nvidia GTX1050"],
    "2175HD": ["lenovo", 14, "4GB", "SSD", "512GB", "Intel Core i5", "Nvidia GTX1050"],
    "JjfFHD": ["Asus", 14, "16GB", "SSD", "256GB", "Intel Core i7", "Nvidia RTX2080Ti"],
    "fgdxFHD": ["HP", 15.6, "8GB", "DD", "1T", "Intel Core i3", "integrada"],
    "GF75HD": ["Asus", 15.6, "8GB", "DD", "1T", "Intel Core i7", "Nvidia GTX1050"],
    "123FHD": ["lenovo", 14, "6GB", "DD", "1T", "AMD Ryzen 5", "integrada"],
    "342FHD": ["lenovo", 15.6, "8GB", "DD", "1T", "AMD Ryzen 7", "Nvidia GTX1050"],
    "UWU131HD": ["Dell", 15.6, "8GB", "DD", "1T", "AMD Ryzen 3", "Nvidia GTX1050"],
}


class IndexStock(IntEnum):
    PRICE = 0
    AMOUNT = 1


stock: dict[str, list[int, int]] = {
    "8475HD": [387990, 10],
    "2175HD": [327990, 4],
    "JjfFHD": [424990, 1],
    "fgdxFHD": [664990, 21],
    "123FHD": [290890, 32],
    "342FHD": [444990, 7],
    "GF75HD": [749990, 2],
    "UWU131HD": [349990, 1],
    "FS1230HD": [249990, 0],
}
