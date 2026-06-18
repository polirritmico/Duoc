---
title: Clase 19
date: 2026-06-13T15:58:12.000Z
author: Eduardo Bray
tags:
  - classes
  - fullstack
---
# Gateway

## Eureka

Funciona como mapa de miroservicios. Cada ms se registra al iniciar y el Gateway
lo referencia a través de nombres lógicos.

La implementación es sencilla, pues solo necesitamos agregar la librería y
**una** anotación en cada microservicio que queramos registrar.

Además levantamos un microservicio especial que no tiene packages sino algunas
configuraciones y solo el package Application.

## Auth

Agregamos las configuraciones al `application.properties`.

