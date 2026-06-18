---
title: Excepciones
date: 2026-04-29T23:14:11.000Z
author: Eduardo Bray
tags:
  - classes
  - fullstack
---
```java
@RestControllerAdvice // Esta clase maneja excepciones
public class GlobalExceptionHandler { // Nombre estándar

    @ExceptionHandler(MethodArgumentNotValidException.class) // Este método maneja esta clase de excepciones
    public ResponseEntity<Map<String, String>> handleValidationErrors(MethodArgumentNotValidException ex) {
        Map<String, String> errors = new HashMap<>(); // Dado que pueden ser muchs exepciones las capturaremos en un
                                                      // HashMap

        ex.getBindingResult().getFieldErrors().forEach(err -> {
            errors.put(err.getField(), err.getDefaultMessage());
        });

        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errors); // Creamos la excepción
    };
}
```

