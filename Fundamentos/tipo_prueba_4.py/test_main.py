#!/usr/bin/env python
# -*- coding: utf-8 -*-

from main import Usuario, Menu


def test_foo() -> None:
    user = Usuario("123", "Foo", "Bar")
    output = print(user)
    assert "" == output



