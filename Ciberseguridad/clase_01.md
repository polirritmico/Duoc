---
title: Clase 01
date: 2026-03-14T00:00:00.000Z
author: Eduardo Bray
tags: Ciberseguridad
---
# Clase 01

Ponderación de las pruebas:

- 30% 06-04
- 35% 11-05
- 35% 22-06

## Ciberseguridad ofensiva

Se preocupa de encontrar vulnerabilidades antes que los atacantes. Simula
ataques reales y propone soluciones a incidentes graves.

### Pentesting

Técnica de la ciberseguridad ofensiva en la que un equipo **autorizado** simula
ataques al sistema o red para identificar vulnerabilidades.

Tipos de pentesting

#### Black Box

- No se tiene información del sistema
- Simula un ataque externo
- Toma mucho tiempo y puede no encontrar vulnerabilidades internas

#### White Box

- Acceso completo a la documentación interna, credenciales e información técnica
  del sistema objetivo.

- Revisión de código fuente.

#### Grey Box

- Credenciales de acceso
- Conocimiento de la arquitectura
- Perspectiva interna y externa

### Fases del pentesting

1. Reconocimiento: Recopilar información del objetivo. Por ejemplo, stack
   tecnológico en anuncios de empleos, OSINT.
2. Escaneo: Explorar el sistema en busca de vulnerabilidades. Herramientas como
   Nmap, Nessus, OpenVAS, etc.
3. Explotación: Intentar explotar las vulnerabilidades entonctradas para obtener
   acceso no autorizado. Herramientas como Metasploit, Zap Proxy y BurpSuite.
4. Post-explotación: Elevar privilegios, exfiltrar datos o moverse lateralmente
   por la red (pivoting).
5. Generación de informes: Documentar los hallazgos y proponer soluciones para
   mitigar las vulnerabilidades.

---

## Caso: Vulnerabilidad en el sistema de autenticación de una aplicación web

Se te ha asignado la tarea de evaluar la seguridad de una aplicación web
corporativa interna utilizada por los empleados para acceder a recursos
sensibles (informes financieros, bases de datos de clientes, etc.). El sistema
de autenticación utiliza credenciales de usuario (nombre de usuario y
contraseña) para conceder acceso.

Durante la fase de reconocimiento y escaneo inicial descubriste que el
formulario de inicio de sesión no tiene protección contra ataques de fuerza
bruta. Además, el sistema no implementa medidas de protección adicionales como
bloqueos de cuenta tras múltiples intentos fallidos de inicio de sesión

### Tareas

1. Identificación de vulnerabilidades: Basado en el análisis del sistema de
   autenticación, identifica la vulnerabilidad principal relacionada con la
   falta de protección contra ataques de fuerza bruta.
   - Describe cómo un atacante podría aprovecharse de esta debilidad para
     obtener acceso a la aplicación.

2. Ataque:
   - Usando herramientas como Hydra o Burp Suite, un atacante podría realizar un
     ataque de fuerza bruta para probar diferentes combinaciones de credenciales
     hasta encontrar una que funcione.
   - Explica cómo funcionaría este ataque en detalle, y qué señales podría
     buscar el atacante para saber que ha logrado vulnerar el sistema.

3. Implicaciones éticas:
   - Reflexiona sobre las responsabilidades de un pentester al realizar pruebas
     de fuerza bruta. ¿Hasta qué punto es apropiado continuar con el ataque sin
     comprometer la integridad del sistema o de los usuarios?
   - Considera cómo debe comunicarse la vulnerabilidad encontrada al cliente y
     qué precauciones debe tomar el pentester durante las pruebas.

4. Propuesta de mitigación:
   - Sugiere mejoras en el sistema de autenticación, como implementar mecanismos
     de bloqueo temporal tras varios intentos fallidos, utilizar captchas para
     prevenir la automatización de ataques, y habilitar la autenticación de
     múltiples factores (MFA).
   - Describe cómo estas medidas de mitigación evitarían que un atacante explote
     esta vulnerabilidad en el futuro.

---

## Respuestas

1. Se identifica la falta de mecanismos de bloqueo para múltiples intentos de
   logeo fallido. Un atacante podría aprovechar esta vulnerabilidad para
   realizar ataques de fuerza bruta contra la página de logeo.
2. Este ataque consistiría en intentar millones de combinaciones de nombre de
   usuario y password hasta encontrar una que pase la validación y de acceso al
   sistema.
3. El ataque debería continuar mientras no se comprometa la estabilidad del
   sitio o infraestructura del sistema; o hasta otros límites establecidos en el
   acuerdo con la empresa a cargo del sistema objetivo. En caso de lograr un
   login exitoso a una cuenta con privilegios informaría de inmediato. En caso
   de tener acceso a cuentas de usuario con menores permisos informaría en el
   reporte.
4. Para mitigar la vulnerabilidad encontrada se sugieren las siguientes
   acciones: Añadir o incrementar timeouts entre intentos, bloquear cuentas
   pasado cierto threshold de intentos fallidos, incrementar los requisitos de
   las contraseñas (longitud mínima, obligar el uso de símbolos, números y
   letras mayúsculas y minúsculas) e integrar sistemas de autenticación MFA. En
   conjunto estas estrategias harían inviable un ataque de fuerza bruta.

