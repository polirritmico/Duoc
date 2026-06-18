---
title: Clase 16
date: 2026-05-06T23:22:06.000Z
author: Eduardo Bray
tags:
  - classes
  - fullstack
---
# Seguridad

Cada microservicio debería recibir peticiones solo si tiene permisos. En la
arquitectura de microservicios tenemos uno especializado en el Auth.

## Microservicio Auth

Una aproximación mínima podría ser la siguiente:

1. Va a tener una tabla de usuario como esta:

   | usuario | password | rol   |
   | ------- | -------- | ----- |
   | Foo     | \*\*\*   | ADMIN |

2. json:{user/pass} -> Auth -> Token (jwt) con fecha de expiración.

Seguridad gobierno: csirt.gob.cl

