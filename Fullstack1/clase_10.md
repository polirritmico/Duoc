---
title: Clase 10
date: 2026-04-08T23:22:45.000Z
author: Eduardo Bray
tags:
  - classes
  - fullstack
---
# Persistencia

Almacenar los datos en sistemas externos como bases de datos relacionales y no
relacionales.

En java se ocupa `Jakarta Persistence` (conocida como JPA) que realiza un mapeo
objeto-relacional (ORM). Es decir, convierte la clase modelo a una tabla
automáticamente. Los atributos de la clase se convierten en atributos de la
clase.

---

## Jakarta

Para configurar el proyecto spring utiliza la carpeta resources. Se recomienda
tener 4 archivos `application.properties`.

```
src/main/resources/application-dev.properties
src/main/resources/application-prod.properties
src/main/resources/application-test.properties
src/main/resources/application.properties
```

Y en el application.properties apuntamos al profile específico (dev, prod,
etc.).

