---
title: Clase 09
date: 2026-03-28T15:29:58.000Z
author: Eduardo Bray
tags:
  - classes
  - fullstack
---
# Clase 09

## DTO

Data Transfer Object. Son clases que se utilizan como contenedores de datos del
modelo específicos para su transferencia.

En el proyecto:

```
controller/
repository/
service/
dto/
  request/
    FooCreateRequest
    FooUpdateRequest
  response/
    FooResponse
```

Entonces los utilizamos de esta forma

Flujo de entrada:

| Controller | Service                            | Repository |
| ---------- | ---------------------------------- | ---------- |
| -> DTO ->  | -> DTO -> transformamos a Model -> | Model      |

Flujo de salida (derecha a izquierda):

| Controller | Service                          | Repository |
| ---------- | -------------------------------- | ---------- |
| <- DTO <-  | <- DTO <- transformamos a DTO <- | Model      |

