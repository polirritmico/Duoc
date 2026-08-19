-------------------------------------------------------------------------------
-- Eliminación de tablas
--/*
DROP TABLE servicios CASCADE CONSTRAINTS;
DROP TABLE tipos_servicio CASCADE CONSTRAINTS;

DROP TABLE vehiculos CASCADE CONSTRAINTS;
DROP TABLE tipos_combustible CASCADE CONSTRAINTS;
DROP TABLE modelos_vehiculos CASCADE CONSTRAINTS;
DROP TABLE marcas_vehiculos CASCADE CONSTRAINTS;

DROP TABLE comunas CASCADE CONSTRAINTS;
DROP TABLE ciudades CASCADE CONSTRAINTS;
DROP TABLE regiones CASCADE CONSTRAINTS;

DROP TABLE mecanicos CASCADE CONSTRAINTS;
DROP TABLE clientes CASCADE CONSTRAINTS;

DROP TABLE ordenes CASCADE CONSTRAINTS;
DROP TABLE talleres CASCADE CONSTRAINTS;
--*/

-------------------------------------------------------------------------------
-- Tablas (en orden de creación)

CREATE TABLE marcas_vehiculos (
    id_marca_vehiculo NUMBER(10) NOT NULL,
    nombre            VARCHAR2(40) NOT NULL
);
ALTER TABLE marcas_vehiculos ADD CONSTRAINT marcas_vehiculos_pk PRIMARY KEY ( id_marca_vehiculo );

CREATE TABLE modelos_vehiculos (
    id_modelo_vehiculo NUMBER(10) NOT NULL,
    nombre             VARCHAR2(40) NOT NULL,
    id_marca_vehiculo  NUMBER(10) NOT NULL
);
ALTER TABLE modelos_vehiculos ADD CONSTRAINT modelos_vehiculos_pk PRIMARY KEY ( id_modelo_vehiculo );

CREATE TABLE tipos_combustible (
    id_tipo_combustible NUMBER(10) NOT NULL,
    nombre              VARCHAR2(40) NOT NULL
);
ALTER TABLE tipos_combustible ADD CONSTRAINT tipos_combustible_pk PRIMARY KEY ( id_tipo_combustible );

CREATE TABLE vehiculos (
    id_vehiculo                           NUMBER(10) NOT NULL,
    patente                               VARCHAR2(6) NOT NULL,
    anio                                  NUMBER(4) NOT NULL,
    kilometraje                           NUMBER(10),
    id_modelo_vehiculo  NUMBER(10) NOT NULL,
    id_tipo_combustible NUMBER(10) NOT NULL
);
ALTER TABLE vehiculos ADD CONSTRAINT vehiculos_pk PRIMARY KEY ( id_vehiculo );

--

CREATE TABLE regiones (
    id_region NUMBER(10) NOT NULL,
    nombre    VARCHAR2(40) NOT NULL
);
ALTER TABLE regiones ADD CONSTRAINT regiones_pk PRIMARY KEY ( id_region );

CREATE TABLE ciudades (
    id_ciudad NUMBER(10) NOT NULL,
    nombre    VARCHAR2(40) NOT NULL,
    id_region NUMBER(10) NOT NULL
);
ALTER TABLE ciudades ADD CONSTRAINT ciudades_pk PRIMARY KEY ( id_ciudad );

CREATE TABLE comunas (
    id_comuna NUMBER(10) NOT NULL,
    nombre    VARCHAR2(40) NOT NULL,
    id_ciudad NUMBER(10) NOT NULL
);
ALTER TABLE comunas ADD CONSTRAINT comunas_pk PRIMARY KEY ( id_comuna );

--

CREATE TABLE clientes (
    id_cliente       NUMBER(10) NOT NULL,
    primer_nombre    VARCHAR2(255) NOT NULL,
    segundo_nombre   VARCHAR2(255),
    primer_apellido  VARCHAR2(255) NOT NULL,
    segundo_apellido VARCHAR2(255),
    rut              NUMBER(8),
    dv               CHAR(1),
    telefono         NUMBER(11) NOT NULL,
    correo           VARCHAR2(255) NOT NULL,
    direccion        VARCHAR2(255) NOT NULL,
    id_comuna        NUMBER(10) NOT NULL
);
ALTER TABLE clientes ADD CONSTRAINT clientes_pk PRIMARY KEY ( id_cliente );

CREATE TABLE mecanicos (
    id_mecanico      NUMBER(10) NOT NULL,
    primer_nombre    VARCHAR2(255) NOT NULL,
    segundo_nombre   VARCHAR2(255),
    primer_apellido  VARCHAR2(255) NOT NULL,
    segundo_apellido VARCHAR2(255),
    rut              NUMBER(8) NOT NULL,
    dv               CHAR(1) NOT NULL,
    telefono         NUMBER(11) NOT NULL,
    correo           VARCHAR2(255) NOT NULL,
    direccion        VARCHAR2(255) NOT NULL,
    id_comuna        NUMBER(10) NOT NULL
);
ALTER TABLE mecanicos ADD CONSTRAINT mecanicos_pk PRIMARY KEY ( id_mecanico );

--

CREATE TABLE talleres (
    id_taller NUMBER(10) NOT NULL,
    nombre    VARCHAR2(100) NOT NULL,
    direccion VARCHAR2(255) NOT NULL,
    id_comuna NUMBER(10) NOT NULL
);
ALTER TABLE talleres ADD CONSTRAINT talleres_pk PRIMARY KEY ( id_taller );

CREATE TABLE ordenes (
    id_orden                NUMBER(10) NOT NULL,
    fecha_ingreso           DATE NOT NULL,
    fecha_entrega           DATE,
    descripcion             VARCHAR2(500),
    id_cliente              NUMBER(10) NOT NULL,
    id_vehiculo             NUMBER(10) NOT NULL,
    id_mecanico_responsable NUMBER(10) NOT NULL,
    id_taller               NUMBER(10) NOT NULL
);
ALTER TABLE ordenes ADD CONSTRAINT ordenes_pk PRIMARY KEY ( id_orden );

--

CREATE TABLE tipos_servicio (
    id_tipo_servicio NUMBER(10) NOT NULL,
    nombre           VARCHAR2(255) NOT NULL,
    precio_actual    NUMBER(9) NOT NULL
);
ALTER TABLE tipos_servicio ADD CONSTRAINT tipos_servicio_pk PRIMARY KEY ( id_tipo_servicio );

CREATE TABLE servicios (
    id_servicio      NUMBER(10) NOT NULL,
    id_orden         NUMBER(10) NOT NULL,
    id_mecanico      NUMBER(10) NOT NULL,
    id_tipo_servicio NUMBER(10) NOT NULL,
    precio_aplicado  NUMBER(9) NOT NULL,
    observaciones    VARCHAR2(500)
);
ALTER TABLE servicios ADD CONSTRAINT servicios_pk PRIMARY KEY ( id_servicio );

-------------------------------------------------------------------------------
-- Relaciones

ALTER TABLE ciudades
    ADD CONSTRAINT ciudades_regiones_fk FOREIGN KEY ( id_region )
        REFERENCES regiones ( id_region );

ALTER TABLE clientes
    ADD CONSTRAINT clientes_comunas_fk FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );

ALTER TABLE comunas
    ADD CONSTRAINT comunas_ciudades_fk FOREIGN KEY ( id_ciudad )
        REFERENCES ciudades ( id_ciudad );

ALTER TABLE mecanicos
    ADD CONSTRAINT mecanicos_comunas_fk FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );

ALTER TABLE modelos_vehiculos
    ADD CONSTRAINT modelos_marcas_vehiculos_fk FOREIGN KEY ( id_marca_vehiculo )
        REFERENCES marcas_vehiculos ( id_marca_vehiculo );

ALTER TABLE ordenes
    ADD CONSTRAINT ordenes_clientes_fk FOREIGN KEY ( id_cliente )
        REFERENCES clientes ( id_cliente );

ALTER TABLE ordenes
    ADD CONSTRAINT ordenes_mecanicos_fk FOREIGN KEY ( id_mecanico_responsable )
        REFERENCES mecanicos ( id_mecanico );

ALTER TABLE ordenes
    ADD CONSTRAINT ordenes_talleres_fk FOREIGN KEY ( id_taller )
        REFERENCES talleres ( id_taller );

ALTER TABLE ordenes
    ADD CONSTRAINT ordenes_vehiculos_fk FOREIGN KEY ( id_vehiculo )
        REFERENCES vehiculos ( id_vehiculo );

ALTER TABLE servicios
    ADD CONSTRAINT servicios_mecanicos_fk FOREIGN KEY ( id_mecanico )
        REFERENCES mecanicos ( id_mecanico );

ALTER TABLE servicios
    ADD CONSTRAINT servicios_ordenes_fk FOREIGN KEY ( id_orden )
        REFERENCES ordenes ( id_orden );

ALTER TABLE servicios
    ADD CONSTRAINT servicios_tipos_servicio_fk FOREIGN KEY ( id_tipo_servicio )
        REFERENCES tipos_servicio ( id_tipo_servicio );

ALTER TABLE talleres
    ADD CONSTRAINT talleres_comunas_fk FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );

ALTER TABLE vehiculos
    ADD CONSTRAINT vehiculos_modelos_vehiculos_fk FOREIGN KEY ( id_modelo_vehiculo )
        REFERENCES modelos_vehiculos ( id_modelo_vehiculo );

ALTER TABLE vehiculos
    ADD CONSTRAINT vehiculos_tipos_combustible_fk FOREIGN KEY ( id_tipo_combustible )
        REFERENCES tipos_combustible ( id_tipo_combustible );

-------------------------------------------------------------------------------
-- Datos

INSERT INTO marcas_vehiculos VALUES (1, 'Toyota');
INSERT INTO marcas_vehiculos VALUES (2, 'Hyundai');
INSERT INTO marcas_vehiculos VALUES (3, 'Chevrolet');

INSERT INTO modelos_vehiculos VALUES (1, 'Yaris', 1);
INSERT INTO modelos_vehiculos VALUES (2, 'Elantra', 2);
INSERT INTO modelos_vehiculos VALUES (3, 'Spark', 3);

INSERT INTO tipos_combustible VALUES (1, 'Bencina');
INSERT INTO tipos_combustible VALUES (2, 'Diésel');
INSERT INTO tipos_combustible VALUES (3, 'Eléctrico');
INSERT INTO tipos_combustible VALUES (4, 'Híbrido');

INSERT INTO vehiculos VALUES (1, 'PTCL23', 2018, 85000, 1, 1);
INSERT INTO vehiculos VALUES (2, 'GKSB78', 2020, 42000, 2, 2);
INSERT INTO vehiculos VALUES (3, 'BBCL34', 2016, 110000, 3, 1);

INSERT INTO regiones VALUES (1, 'Región Metropolitana');
INSERT INTO regiones VALUES (2, 'Valparaíso');
INSERT INTO regiones VALUES (3, 'Biobío');

INSERT INTO ciudades VALUES (1, 'Santiago', 1);
INSERT INTO ciudades VALUES (2, 'Valparaíso', 2);
INSERT INTO ciudades VALUES (3, 'Concepción', 3);

INSERT INTO comunas VALUES (1, 'Providencia', 1);
INSERT INTO comunas VALUES (2, 'Viña del Mar', 2);
INSERT INTO comunas VALUES (3, 'Talcahuano', 3);

INSERT INTO clientes VALUES (1, 'Alan', NULL, 'Brito', 'Delgado', 12345678, 'K', 987654321, 'carlos@example.cl', 'Av. Nueva 123', 1);
INSERT INTO clientes VALUES (2, 'María', 'José', 'Dolores', 'Soto', 87654321, '3', 912345678, 'maria@example.cl', 'Calle 456', 2);
INSERT INTO clientes VALUES (3, 'Pedro', 'Pablo', 'Muñoz', 'Valdivia', 13579246, '2', 998877665, 'pedro@example.cl', 'Pasaje Los Robles 789', 3);

INSERT INTO mecanicos VALUES (1, 'Susana', NULL, 'Oria', 'Naranjo', 33444555, '1', 956778899, 'diego.fuentes@taller.cl', 'Calle Dos 345', 3);
INSERT INTO mecanicos VALUES (2, 'Juan', 'Pablo', 'Ramírez', 'Silva', 11222333, '9', 932112233, 'juan.ramirez@taller.cl', 'Las Lilas 123', 1);
INSERT INTO mecanicos VALUES (3, 'Luis', 'Esteban', 'Fernández', 'Gómez', 22333444, 'K', 945556677, 'luis.fernandez@taller.cl', 'Calle Uno 234', 2);

INSERT INTO talleres VALUES (1, 'Taller Central', 'Av. Siempre Viva 742', 1);
INSERT INTO talleres VALUES (2, 'Taller Costero', 'Av. Marina 500', 2);
INSERT INTO talleres VALUES (3, 'Taller Sur', 'Ruta 160 KM 10', 3);

INSERT INTO ordenes VALUES (1, DATE '2025-01-10', DATE '2025-01-15', 'Revisión general', 1, 1, 1, 1);
INSERT INTO ordenes VALUES (2, DATE '2025-01-12', NULL, 'Cambio de frenos', 2, 2, 2, 2);
INSERT INTO ordenes VALUES (3, DATE '2025-01-20', DATE '2025-01-22', 'Problema eléctrico', 3, 3, 3, 3);

INSERT INTO tipos_servicio VALUES (1, 'Cambio de aceite', 35000);
INSERT INTO tipos_servicio VALUES (2, 'Reemplazo de frenos', 85000);
INSERT INTO tipos_servicio VALUES (3, 'Diagnóstico eléctrico', 45000);

INSERT INTO servicios VALUES (1, 1, 1, 1, 35000, 'Todo OK');
INSERT INTO servicios VALUES (2, 2, 2, 2, 85000, 'Pastillas delanteras y traseras');
INSERT INTO servicios VALUES (3, 3, 3, 3, 45000, 'Falla en alternador detectada');
INSERT INTO servicios VALUES (4, 1, 1, 3, 45000, 'Chequeo eléctrico preventivo');
INSERT INTO servicios VALUES (5, 2, 2, 1, 35000, 'Cambio de aceite preventivo');
INSERT INTO servicios VALUES (6, 2, 2, 3, 45000, 'Revisión eléctrica básica');
