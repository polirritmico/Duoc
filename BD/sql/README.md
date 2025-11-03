# Oracle Database Free con Docker

Aquí estan las instrucciones

## 1. Levantar el contenedor

```bash
docker compose up -d
```

## 2. Conexión administrativa

Para crear el usuario nos tenemos que conectar a la conexión administrativa
Container DataBase (CDB). Para ello apuntamos al **Service Name** `FREE`.

En SQL Developer agregamos una nueva conexión:

| Campo            | Valor              | Nota                                             |
| ---------------- | ------------------ | ------------------------------------------------ |
| **Name**         | `OracleAdmin_CDB`  | O el nombre que prefieras                        |
| **Username**     | `SYSTEM`           |                                                  |
| **Password**     | `TuPasswordSeguro` | Definida en el `compose.yaml`                    |
| **Hostname**     | `localhost`        |                                                  |
| **Port**         | `1521`             |                                                  |
| **Service Name** | **`FREE`**         | **¡Importante!** No usar SID. Usar Service Name. |

## 3. Creación del Usuario

Una vez conectado en `OracleAdmin_CDB`, ejecutar la siguiente query.

```sql
CREATE USER C##BDY1102 IDENTIFIED BY "BDY1101practica_1"
DEFAULT TABLESPACE USERS
TEMPORARY TABLESPACE TEMP
CONTAINER=ALL;

GRANT CONNECT, RESOURCE TO C##BDY1102 CONTAINER=ALL;

ALTER USER C##BDY1102 QUOTA UNLIMITED ON USERS CONTAINER=ALL;

GRANT SET CONTAINER TO C##BDY1102 CONTAINER=ALL;
```

Este script crea un usuario que puede acceder tanto a la raíz como a las bases
de datos conectables.

## 4. Conexión de usuario (PDB)

Nos conectamos a la **Pluggable Database (PDB)** usando el usuario recién creado
con estos datos:

| Campo            | Valor               | Nota                                  |
| ---------------- | ------------------- | ------------------------------------- |
| **Name**         | `BDY1102_PDB`       | Conexión de trabajo                   |
| **Username**     | `C##BDY1102`        | El usuario creado en el paso anterior |
| **Password**     | `BDY1101practica_1` |                                       |
| **Hostname**     | `localhost`         |                                       |
| **Port**         | `1521`              |                                       |
| **Service Name** | **`FREEPDB1`**      | Apuntamos a la PDB específica         |

**Listo, todo debería estar funcionando.**

## Fuente

Toda la info viene de aquí:

https://container-registry.oracle.com/ords/f?p=113:4:3230503938894:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:1863,1863,Oracle%20Database%20Free,Oracle%20Database%20Free,1,0&cs=3Bz34yUiA9Dj-MZORoPqiWdyIF97pBP9xGGs6XLKSs7iFUp2-a_7JKnnqfVzfNI9B3zQNhcgVKs_Mn34vUen0og

Se adaptaron las instrucciones de Podman a Docker y finalmente al compose.
