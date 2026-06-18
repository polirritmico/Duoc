---
title: Clase 18
date: 2026-06-10T23:15:26.000Z
author: Eduardo Bray
tags:
  - classes
  - fullstack
---
# Hateoas

Viene a complementar swagger. Agrega información dentro del response sobre los
otros endpoints de la API en relación con la entidad.

Por ejemplo tenemos un GetIdResponse:

```json
{
  "Foo": {
    "id": "123",
    "data": "Some data"
  },
  "link": {
    "post": "http://localhost/api/v1/foo",
    "delete": "http://localhost/api/v1/foo",
    "put": "http://localhost/api/v1/foo"
  }
}
```

## Spring Boot

1. Agregamos la librería

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-hateoas</artifactId>
</dependency>
```

En el application.properties:

```properties
springdoc.enable-hateoars=false
```

2. Agregamos la anotación a nuestro controller:

Antes

```java
public ResponseEntity<FooResponse> foo() {
  ...
  return ResponseEntity.ok(response);
}
```

Después

```java
import static org.static;

public ResponseEntity<EntityModel<FooResponse>> foo() {
  ...
  FooResponse response = service.foo();

  EntityModel<FooResponse> resource = EntityModel.of(response);
  resource.add(linkTo(methodOn(FooController.class).login().withSelfRel());
  return ResponseEntity.ok(resource);
}
```

