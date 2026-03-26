---
title: Clase 07
date: 2026-03-25T22:14:23.000Z
author: Eduardo Bray
tags:
  - classes
  - fullstack
---
# Clase 07

> EV1 9 de Abril. Entra todo menos las excepciones con try/catch.

En java, el typing puede ser `<?>` para utilizar cualquier tipo:

```java
@PostMapping("/pago")
public ResponseEntity<?> pagar(@Valid @RequestBody PagoRequest req) {
    try {
        // Lógica de servicio que podría fallar (ej.: saldo insuficiente)
        servicio.procesarPago(req);
        return ResponseEntity.ok().body("✅ Pago procesado");
    } catch (SaldoInsuficienteException e) {
        // 400: error de negocio del cliente
        return ResponseEntity.badRequest().body("❌ " + e.getMessage());
    } catch (Exception e) {
        // 500: error inesperado del servidor
        return ResponseEntity.status(500).body("⚠️ Error interno");
    }
}
```

