#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

command = "clear" if os.uname().sysname == "Linux" else "clr"
os.system(command)

name: str = input("Name?")

print(f"Hello {name}")
