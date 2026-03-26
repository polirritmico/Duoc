# Oracle Database Free con Docker

Aquí están las instrucciones

## Requisitos

- Docker
- Docker compose

Para revisar que esté todo funcionando:

```bash
$ docker compose version
Docker Compose version v2.39.3  # o la version que esté instalada
```

> [!NOTE]
>
> Cuando termines de usar la BD, baja la instancia. Sino, es probable que se
> inicie automáticamente cada vez que lanzas docker:
>
> ```bash
> docker compose down  # desde la carpeta con el docker-compose.yml
> ```

## 1. Levantar el contenedor

En una ruta con el archivo `docker-compose.yml` ejecutar:

```bash
docker compose up -d
```

## 2. Conexión administrativa

Para crear el usuario nos tenemos que conectar a la conexión administrativa
Container DataBase (CDB). Para ello apuntamos al **Service Name** `FREE`.

En SQL Developer agregamos una nueva conexión:

| Campo            | Valor              | Nota                                             |
| ---------------- | ------------------ | ------------------------------------------------ |
| **Name**         | `OracleAdmin_CDB`  | O cualquier nombre                               |
| **Username**     | `SYSTEM`           |                                                  |
| **Password**     | `MiPasswordSeguro` | Definida en el `compose.yaml`                    |
| **Hostname**     | `localhost`        |                                                  |
| **Port**         | `1521`             |                                                  |
| **Service Name** | **`FREE`**         | **¡Importante!** No usar SID. Usar Service Name. |

## 3. Creación del Usuario

Una vez conectado en `OracleAdmin_CDB`, ejecutar la siguiente query.

```sql
CREATE USER C##BDY1102 IDENTIFIED BY "BDY1101practica_1"
DEFAULT TABLESPACE USERS
TEMPORARY TABLESPACE TEMP;
CREATE ROLE C##RESOURCE CONTAINER=ALL;
GRANT CREATE SESSION, CREATE TABLE, CREATE SEQUENCE, CREATE VIEW TO C##RESOURCE CONTAINER=ALL;
GRANT C##RESOURCE TO C##BDY1102 CONTAINER=ALL;
ALTER USER C##BDY1102 DEFAULT ROLE C##RESOURCE;
ALTER USER C##BDY1102 QUOTA UNLIMITED ON USERS;
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

## Preparación esquemas para los ejercicios

Para crear los entornos de práctica vamos a crearlos en un procedimiento y luego
solo faltaría agregar cada conexión manualmente en el programa que utilicemos
para conectarnos.

Para los nombres de usuario se utiliza `BDY1102_X` donde `X` es el número de la
práctica y `014V` la contraseña común.

```sql
ALTER SESSION SET CONTAINER = FREEPDB1;

BEGIN
   FOR i IN 1..17 LOOP
      EXECUTE IMMEDIATE 'CREATE USER BDY1102_' || i ||
                        ' IDENTIFIED BY "014V"' ||
                        ' DEFAULT TABLESPACE USERS' ||
                        ' TEMPORARY TABLESPACE TEMP';

      EXECUTE IMMEDIATE 'ALTER USER BDY1102_' || i || ' QUOTA UNLIMITED ON USERS';
      EXECUTE IMMEDIATE 'GRANT CREATE SESSION, RESOURCE TO BDY1102_' || i;
      EXECUTE IMMEDIATE 'ALTER USER BDY1102_' || i || ' DEFAULT ROLE RESOURCE';
   END LOOP;
END;
/
```

## Conexión al esquema

Estos son los datos de conexión para los esquemas:

| Campo            | Valor (Ejemplo para P1) | Nota                                      |
| ---------------- | ----------------------- | ----------------------------------------- |
| **Username**     | `BDY1102_1`             | Cambiar el número según la práctica.      |
| **Password**     | `014V`                  | Contraseña única para todos los esquemas. |
| **Hostname**     | `localhost`             |                                           |
| **Port**         | `1521`                  |                                           |
| **Service Name** | **`FREEPDB1`**          | **Obligatorio:** Conexión a la PDB.       |

---

## Fuente

Toda la info viene de aquí:

https://container-registry.oracle.com/ords/f?p=113:4:3230503938894:::4:P4_REPOSITORY,AI_REPOSITORY,AI_REPOSITORY_NAME,P4_REPOSITORY_NAME,P4_EULA_ID,P4_BUSINESS_AREA_ID:1863,1863,Oracle%20Database%20Free,Oracle%20Database%20Free,1,0&cs=3Bz34yUiA9Dj-MZORoPqiWdyIF97pBP9xGGs6XLKSs7iFUp2-a_7JKnnqfVzfNI9B3zQNhcgVKs_Mn34vUen0og

Se adaptaron las instrucciones de Podman a Docker y finalmente al compose.
