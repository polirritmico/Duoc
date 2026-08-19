-------------------------------------------------------------------------------
-- Script SQL Modelo Escuelas Artísticas
-- Eduardo Bray
-- ed.bray@duocuc.cl
-- Santiago, 2025-12-13
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
-- Borrado de tablas
-------------------------------------------------------------------------------

/**/
DROP TABLE adjudicacion_recursos CASCADE CONSTRAINTS;
DROP TABLE afp CASCADE CONSTRAINTS;
DROP TABLE centros_eventos CASCADE CONSTRAINTS;
DROP TABLE ciudades CASCADE CONSTRAINTS;
DROP TABLE comunas CASCADE CONSTRAINTS;
DROP TABLE contratos CASCADE CONSTRAINTS;
DROP TABLE detalle_inversiones CASCADE CONSTRAINTS;
DROP TABLE directores CASCADE CONSTRAINTS;
DROP TABLE escuelas CASCADE CONSTRAINTS;
DROP TABLE especialidades CASCADE CONSTRAINTS;
DROP TABLE estados_civiles CASCADE CONSTRAINTS;
DROP TABLE formularios CASCADE CONSTRAINTS;
DROP TABLE instituciones_educativas CASCADE CONSTRAINTS;
DROP TABLE isapres CASCADE CONSTRAINTS;
DROP TABLE municipalidades CASCADE CONSTRAINTS;
DROP TABLE nacionalidades CASCADE CONSTRAINTS;
DROP TABLE profesiones CASCADE CONSTRAINTS;
DROP TABLE profesores CASCADE CONSTRAINTS;
DROP TABLE regiones CASCADE CONSTRAINTS;
DROP TABLE telefonos CASCADE CONSTRAINTS;
DROP TABLE tipos_contrato CASCADE CONSTRAINTS;
DROP TABLE tipos_escuela CASCADE CONSTRAINTS;
DROP TABLE tipos_institucion CASCADE CONSTRAINTS;
DROP TABLE tipos_inversion CASCADE CONSTRAINTS;
DROP TABLE tipos_telefono CASCADE CONSTRAINTS;
DROP TABLE turnos_escuela_profesor CASCADE CONSTRAINTS;
DROP TABLE turnos_trabajo CASCADE CONSTRAINTS;
--*/

-------------------------------------------------------------------------------
-- Creación de tablas
-------------------------------------------------------------------------------

CREATE TABLE adjudicacion_recursos (
    id_adjudicacion_recurso NUMBER(10) NOT NULL,
    puntaje                 NUMBER(5),
    monto_asignado          NUMBER(10),
    cumple_requisitos       CHAR(1)
);

ALTER TABLE adjudicacion_recursos ADD CONSTRAINT adjudicacion_recursos_pk PRIMARY KEY ( id_adjudicacion_recurso );

CREATE TABLE afp (
    id_afp NUMBER(10) NOT NULL,
    nombre VARCHAR2(255) NOT NULL
);

ALTER TABLE afp ADD CONSTRAINT afp_pk PRIMARY KEY ( id_afp );

CREATE TABLE centros_eventos (
    id_centro_eventos NUMBER(10) NOT NULL,
    nombre            VARCHAR2(255) NOT NULL,
    id_municipalidad  NUMBER(10) NOT NULL
);

ALTER TABLE centros_eventos ADD CONSTRAINT centros_eventos_pk PRIMARY KEY ( id_centro_eventos );

CREATE TABLE ciudades (
    id_ciudad NUMBER(10) NOT NULL,
    nombre    VARCHAR2(255) NOT NULL,
    d_region  NUMBER(10) NOT NULL
);

ALTER TABLE ciudades ADD CONSTRAINT ciudades_pk PRIMARY KEY ( id_ciudad );

CREATE TABLE comunas (
    id_comuna NUMBER(10) NOT NULL,
    nombre    VARCHAR2(255) NOT NULL,
    id_ciudad NUMBER(10) NOT NULL
);

ALTER TABLE comunas ADD CONSTRAINT comunas_pk PRIMARY KEY ( id_comuna );

CREATE TABLE contratos (
    id_contrato      NUMBER(10) NOT NULL,
    folio            VARCHAR2(10) NOT NULL,
    sueldo_base      NUMBER(10),
    valor_hora       NUMBER(7),
    horas_mensuales  NUMBER(3),
    id_tipo_contrato NUMBER(10) NOT NULL,
    id_profesor      NUMBER(10) NOT NULL,
    id_escuela       NUMBER(10) NOT NULL
);

ALTER TABLE contratos ADD CONSTRAINT contratos_pk PRIMARY KEY ( id_contrato );

CREATE TABLE detalle_inversiones (
    id_detalle_inversion NUMBER(10) NOT NULL,
    monto_uf             NUMBER(3) NOT NULL,
    nombre_proyecto      VARCHAR2(255),
    id_tipo_inversion    NUMBER(10) NOT NULL
);

ALTER TABLE detalle_inversiones ADD CONSTRAINT detalle_inversiones_pk PRIMARY KEY ( id_detalle_inversion );

CREATE TABLE directores (
    id_director      NUMBER(10) NOT NULL,
    primer_nombre    VARCHAR2(255) NOT NULL,
    segundo_nombre   VARCHAR2(255),
    primer_apellido  VARCHAR2(255) NOT NULL,
    segundo_apellido VARCHAR2(255),
    direccion        VARCHAR2(255),
    email            VARCHAR2(255) NOT NULL,
    id_estado_civil  NUMBER(10) NOT NULL,
    id_profesion     NUMBER(10) NOT NULL,
    id_nacionalidad  NUMBER(10) NOT NULL,
    id_comuna        NUMBER(10) NOT NULL
);

ALTER TABLE directores ADD CONSTRAINT directores_pk PRIMARY KEY ( id_director );

CREATE TABLE escuelas (
    id_escuela        NUMBER(10) NOT NULL,
    nombre            VARCHAR2(255) NOT NULL,
    direccion         VARCHAR2(255) NOT NULL,
    sitio_web         VARCHAR2(255) NOT NULL,
    id_tipo_escuela   NUMBER(10) NOT NULL,
    id_director       NUMBER(10) NOT NULL,
    id_comuna         NUMBER(10) NOT NULL,
    id_centro_eventos NUMBER(10) NOT NULL
);

ALTER TABLE escuelas ADD CONSTRAINT escuelas_pk PRIMARY KEY ( id_escuela );

CREATE TABLE especialidades (
    id_especialidad NUMBER(10) NOT NULL,
    nombre          VARCHAR2(255) NOT NULL
);

ALTER TABLE especialidades ADD CONSTRAINT especialidades_pk PRIMARY KEY ( id_especialidad );

CREATE TABLE estados_civiles (
    id_estado_civil NUMBER(10) NOT NULL,
    nombre          VARCHAR2(255) NOT NULL
);

ALTER TABLE estados_civiles ADD CONSTRAINT estados_civiles_pk PRIMARY KEY ( id_estado_civil );

CREATE TABLE formularios (
    id_formulario           NUMBER(10) NOT NULL,
    folio                   VARCHAR2(10) NOT NULL,
    firma                   BLOB,
    fecha_firma             DATE,
    id_adjudicacion_recurso NUMBER(10) NOT NULL,
    id_detalle_inversion    NUMBER(10) NOT NULL,
    id_escuela              NUMBER(10) NOT NULL,
    id_director             NUMBER(10) NOT NULL
);

ALTER TABLE formularios ADD CONSTRAINT formularios_pk PRIMARY KEY ( id_formulario );

CREATE TABLE instituciones_educativas (
    id_institucion_educativa NUMBER(10) NOT NULL,
    nombre                   VARCHAR2(255) NOT NULL,
    id_tipo_institucion      NUMBER(10) NOT NULL
);

ALTER TABLE instituciones_educativas ADD CONSTRAINT instituciones_educativas_pk PRIMARY KEY ( id_institucion_educativa );

CREATE TABLE isapres (
    id_isapre NUMBER(10) NOT NULL,
    nombre    VARCHAR2(255) NOT NULL
);

ALTER TABLE isapres ADD CONSTRAINT isapres_pk PRIMARY KEY ( id_isapre );

CREATE TABLE municipalidades (
    id_municipalidad NUMBER(10) NOT NULL,
    nombre           VARCHAR2(255) NOT NULL,
    id_comuna        NUMBER(10) NOT NULL
);

ALTER TABLE municipalidades ADD CONSTRAINT municipalidades_pk PRIMARY KEY ( id_municipalidad );

CREATE TABLE nacionalidades (
    id_nacionalidad NUMBER(10) NOT NULL,
    nombre          VARCHAR2(100) NOT NULL
);

ALTER TABLE nacionalidades ADD CONSTRAINT nacionalidades_pk PRIMARY KEY ( id_nacionalidad );

CREATE TABLE profesiones (
    id_profesion NUMBER(10) NOT NULL,
    nombre       VARCHAR2(255) NOT NULL
);

ALTER TABLE profesiones ADD CONSTRAINT profesiones_pk PRIMARY KEY ( id_profesion );

CREATE TABLE profesores (
    id_profesor              NUMBER(10) NOT NULL,
    primer_nombre            VARCHAR2(255) NOT NULL,
    segundo_nombre           VARCHAR2(255),
    primer_apellido          VARCHAR2(255) NOT NULL,
    segundo_apellido         VARCHAR2(255),
    run                      NUMBER(9) NOT NULL,
    dv                       CHAR(1) NOT NULL,
    direccion                VARCHAR2(255) NOT NULL,
    id_institucion_educativa NUMBER(10) NOT NULL,
    id_isapre                NUMBER(10) NOT NULL,
    id_afp                   NUMBER(10) NOT NULL,
    id_especialidad          NUMBER(10) NOT NULL,
    id_comuna                NUMBER(10) NOT NULL
);

ALTER TABLE profesores ADD CONSTRAINT profesores_pk PRIMARY KEY ( id_profesor );

CREATE TABLE regiones (
    id_region NUMBER(10) NOT NULL,
    nombre    VARCHAR2(255) NOT NULL
);

ALTER TABLE regiones ADD CONSTRAINT regiones_pk PRIMARY KEY ( id_region );

CREATE TABLE telefonos (
    id_telefono      NUMBER(10) NOT NULL,
    numero           VARCHAR2(12) NOT NULL,
    id_tipo_telefono NUMBER(10) NOT NULL,
    id_director      NUMBER(10) NOT NULL
);

ALTER TABLE telefonos ADD CONSTRAINT telefonos_pk PRIMARY KEY ( id_telefono );

CREATE TABLE tipos_contrato (
    id_tipo_contrato NUMBER(10) NOT NULL,
    nombre           VARCHAR2(255) NOT NULL
);

ALTER TABLE tipos_contrato ADD CONSTRAINT tipos_contrato_pk PRIMARY KEY ( id_tipo_contrato );

CREATE TABLE tipos_escuela (
    id_tipo_escuela NUMBER(10) NOT NULL,
    nombre          VARCHAR2(255) NOT NULL
);

ALTER TABLE tipos_escuela ADD CONSTRAINT tipos_escuela_pk PRIMARY KEY ( id_tipo_escuela );

CREATE TABLE tipos_institucion (
    id_tipo_institucion NUMBER(10) NOT NULL,
    nombre              VARCHAR2(255) NOT NULL
);

ALTER TABLE tipos_institucion ADD CONSTRAINT tipos_institucion_pk PRIMARY KEY ( id_tipo_institucion );

CREATE TABLE tipos_inversion (
    id_tipo_inversion NUMBER(10) NOT NULL,
    nombre            VARCHAR2(255) NOT NULL
);

ALTER TABLE tipos_inversion ADD CONSTRAINT tipos_inversion_pk PRIMARY KEY ( id_tipo_inversion );

CREATE TABLE tipos_telefono (
    id_tipo_telefono NUMBER(10) NOT NULL,
    nombre           VARCHAR2(255) NOT NULL
);

ALTER TABLE tipos_telefono ADD CONSTRAINT tipos_telefono_pk PRIMARY KEY ( id_tipo_telefono );

CREATE TABLE turnos_escuela_profesor (
    id_turno_escuela_profesor NUMBER(10) NOT NULL,
    id_escuela                NUMBER(10) NOT NULL,
    id_profesor               NUMBER(10) NOT NULL,
    id_turno_trabajo          NUMBER(10) NOT NULL
);

ALTER TABLE turnos_escuela_profesor ADD CONSTRAINT turnos_escuela_profesor_pk PRIMARY KEY ( id_turno_escuela_profesor );

CREATE TABLE turnos_trabajo (
    id_turno_trabajo NUMBER(10) NOT NULL,
    dia              NUMBER(1) NOT NULL,
    hora_inicio      DATE NOT NULL,
    hora_fin         DATE NOT NULL
);

-------------------------------------------------------------------------------
-- Claves Foráneas
-------------------------------------------------------------------------------

ALTER TABLE turnos_trabajo ADD CONSTRAINT turnos_trabajo_pk PRIMARY KEY ( id_turno_trabajo );

ALTER TABLE centros_eventos
    ADD CONSTRAINT centros_ev_muni_fk FOREIGN KEY ( id_municipalidad )
        REFERENCES municipalidades ( id_municipalidad );

ALTER TABLE ciudades
    ADD CONSTRAINT ciudades_regiones_fk FOREIGN KEY ( d_region )
        REFERENCES regiones ( id_region );

ALTER TABLE comunas
    ADD CONSTRAINT comunas_ciudades_fk FOREIGN KEY ( id_ciudad )
        REFERENCES ciudades ( id_ciudad );

ALTER TABLE contratos
    ADD CONSTRAINT contratos_escuelas_fk FOREIGN KEY ( id_escuela )
        REFERENCES escuelas ( id_escuela );

ALTER TABLE contratos
    ADD CONSTRAINT contratos_profesores_fk FOREIGN KEY ( id_profesor )
        REFERENCES profesores ( id_profesor );

ALTER TABLE contratos
    ADD CONSTRAINT contratos_tipos_contrato_fk FOREIGN KEY ( id_tipo_contrato )
        REFERENCES tipos_contrato ( id_tipo_contrato );

ALTER TABLE detalle_inversiones
    ADD CONSTRAINT det_inv_tipo_inv_fk FOREIGN KEY ( id_tipo_inversion )
        REFERENCES tipos_inversion ( id_tipo_inversion );

ALTER TABLE directores
    ADD CONSTRAINT directores_comunas_fk FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );

ALTER TABLE directores
    ADD CONSTRAINT directores_estados_civiles_fk FOREIGN KEY ( id_estado_civil )
        REFERENCES estados_civiles ( id_estado_civil );

ALTER TABLE directores
    ADD CONSTRAINT directores_nacionalidades_fk FOREIGN KEY ( id_nacionalidad )
        REFERENCES nacionalidades ( id_nacionalidad );

ALTER TABLE directores
    ADD CONSTRAINT directores_profesiones_fk FOREIGN KEY ( id_profesion )
        REFERENCES profesiones ( id_profesion );

ALTER TABLE escuelas
    ADD CONSTRAINT escuelas_centros_ev_fk FOREIGN KEY ( id_centro_eventos )
        REFERENCES centros_eventos ( id_centro_eventos );

ALTER TABLE escuelas
    ADD CONSTRAINT escuelas_comunas_fk FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );

ALTER TABLE escuelas
    ADD CONSTRAINT escuelas_directores_fk FOREIGN KEY ( id_director )
        REFERENCES directores ( id_director );

ALTER TABLE escuelas
    ADD CONSTRAINT escuelas_tipos_escuela_fk FOREIGN KEY ( id_tipo_escuela )
        REFERENCES tipos_escuela ( id_tipo_escuela );

ALTER TABLE formularios
    ADD CONSTRAINT form_adj_recursos_fk FOREIGN KEY ( id_adjudicacion_recurso )
        REFERENCES adjudicacion_recursos ( id_adjudicacion_recurso );

ALTER TABLE formularios
    ADD CONSTRAINT form_detalle_inv_fk FOREIGN KEY ( id_detalle_inversion )
        REFERENCES detalle_inversiones ( id_detalle_inversion );

ALTER TABLE formularios
    ADD CONSTRAINT form_directores_fk FOREIGN KEY ( id_director )
        REFERENCES directores ( id_director );

ALTER TABLE formularios
    ADD CONSTRAINT form_escuelas_fk FOREIGN KEY ( id_escuela )
        REFERENCES escuelas ( id_escuela );

ALTER TABLE instituciones_educativas
    ADD CONSTRAINT inst_edu_tipos_inst_fk FOREIGN KEY ( id_tipo_institucion )
        REFERENCES tipos_institucion ( id_tipo_institucion );

ALTER TABLE municipalidades
    ADD CONSTRAINT muni_comunas_fk FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );

ALTER TABLE profesores
    ADD CONSTRAINT prof_inst_edu_fk FOREIGN KEY ( id_institucion_educativa )
        REFERENCES instituciones_educativas ( id_institucion_educativa );

ALTER TABLE profesores
    ADD CONSTRAINT profesores_afp_fk FOREIGN KEY ( id_afp )
        REFERENCES afp ( id_afp );

ALTER TABLE profesores
    ADD CONSTRAINT profesores_comunas_fk FOREIGN KEY ( id_comuna )
        REFERENCES comunas ( id_comuna );

ALTER TABLE profesores
    ADD CONSTRAINT profesores_esp_fk FOREIGN KEY ( id_especialidad )
        REFERENCES especialidades ( id_especialidad );

ALTER TABLE profesores
    ADD CONSTRAINT profesores_isapres_fk FOREIGN KEY ( id_isapre )
        REFERENCES isapres ( id_isapre );

ALTER TABLE telefonos
    ADD CONSTRAINT tel_directores_fk FOREIGN KEY ( id_director )
        REFERENCES directores ( id_director );

ALTER TABLE telefonos
    ADD CONSTRAINT tel_tipos_tel_fk FOREIGN KEY ( id_tipo_telefono )
        REFERENCES tipos_telefono ( id_tipo_telefono );

ALTER TABLE turnos_escuela_profesor
    ADD CONSTRAINT turn_esc_prof_esc_fk FOREIGN KEY ( id_escuela )
        REFERENCES escuelas ( id_escuela );

ALTER TABLE turnos_escuela_profesor
    ADD CONSTRAINT turn_esc_prof_prof_fk FOREIGN KEY ( id_profesor )
        REFERENCES profesores ( id_profesor );

ALTER TABLE turnos_escuela_profesor
    ADD CONSTRAINT turn_esc_prof_tur_tr_fk FOREIGN KEY ( id_turno_trabajo )
        REFERENCES turnos_trabajo ( id_turno_trabajo );

-------------------------------------------------------------------------------
-- Inserts de datos
-------------------------------------------------------------------------------

/*
-- REGIONES
INSERT INTO regiones VALUES (1, 'Región Metropolitana');
INSERT INTO regiones VALUES (2, 'Región de Valparaíso');
INSERT INTO regiones VALUES (3, 'Región del Biobío');

-- CIUDADES
INSERT INTO ciudades VALUES (1, 'Santiago', 1);
INSERT INTO ciudades VALUES (2, 'Valparaíso', 2);
INSERT INTO ciudades VALUES (3, 'Concepción', 3);

-- COMUNAS
INSERT INTO comunas VALUES (1, 'Providencia', 1);
INSERT INTO comunas VALUES (2, 'Viña del Mar', 2);
INSERT INTO comunas VALUES (3, 'San Pedro de la Paz', 3);

-- MUNICIPALIDADES
INSERT INTO municipalidades VALUES (1, 'Municipalidad de Providencia');
INSERT INTO municipalidades VALUES (2, 'Municipalidad de Viña del Mar');
INSERT INTO municipalidades VALUES (3, 'Municipalidad de San Pedro de la Paz');

-- CENTROS DEPORTIVOS
INSERT INTO centros_deportivos VALUES (1, 'Teatro Providencia', 1);
INSERT INTO centros_deportivos VALUES (2, 'Teatro Municipal Valpariso', 2);
INSERT INTO centros_deportivos VALUES (3, 'San Pedro Club', 3);

-- TIPO ESCUELA
INSERT INTO tipo_escuela VALUES (1, 'Escuela de Música');
INSERT INTO tipo_escuela VALUES (2, 'Escuela de Teatro');
INSERT INTO tipo_escuela VALUES (3, 'Escuela de Artes');

-- PROFESIONES
INSERT INTO profesiones VALUES (1, 'Docente de Educación Musical');
INSERT INTO profesiones VALUES (2, 'Actuación');
INSERT INTO profesiones VALUES (3, 'Escultura');

-- TIPOS TELÉFONO
INSERT INTO tipos_telefono VALUES (1, 'Móvil');
INSERT INTO tipos_telefono VALUES (3, 'Fijo');
INSERT INTO tipos_telefono VALUES (3, 'Emergencia');

-- TELÉFONOS
INSERT INTO telefonos VALUES (1, '987654321', 1);
INSERT INTO telefonos VALUES (2, '912345678', 1);
INSERT INTO telefonos VALUES (3, '923456789', 1);

-- DIRECTORES
INSERT INTO directores VALUES
(1, 'Carlos', 'Andrés', 'Muñoz', 'Rojas', 'Av. Providencia 1234',
 'cmunoz@escuela.cl', 'Profesor', 1, 1, 1);

INSERT INTO directores VALUES
(2, 'María', NULL, 'Pérez', 'Lagos', 'Calle Marina 456',
 'mperez@escuela.cl', 'Administradora', 2, 2, 3);

INSERT INTO directores VALUES
(3, 'Juan', 'Pablo', 'Soto', 'Fuentes', 'Av. Michaihue 789',
 'jsoto@escuela.cl', 'Director Deportivo', 3, 3, 3);

-- ESCUELAS

-- ESPECIALIDADES
INSERT INTO especialidades VALUES (1, 'Guitarra');
INSERT INTO especialidades VALUES (2, 'Escenografía');
INSERT INTO especialidades VALUES (3, 'Madera');

-- AFP
INSERT INTO afp VALUES (1, 'AFP Habitat');
INSERT INTO afp VALUES (2, 'AFP Provida');
INSERT INTO afp VALUES (3, 'AFP Capital');

-- ISAPRES
INSERT INTO isapres VALUES (1, 'Colmena');
INSERT INTO isapres VALUES (2, 'Banmédica');
INSERT INTO isapres VALUES (3, 'Consalud');

-- TIPO INSTITUCIÓN
INSERT INTO tipo_institucion VALUES (1, 'Universidad');
INSERT INTO tipo_institucion VALUES (2, 'CFT');
INSERT INTO tipo_institucion VALUES (3, 'Instituto Profesional');

-- INSTITUCIONES EDUCATIVAS
INSERT INTO instituciones_educativas VALUES (1, 'Universidad de Chile', 1);
INSERT INTO instituciones_educativas VALUES (2, 'DUOC UC', 2);
INSERT INTO instituciones_educativas VALUES (3, 'IP Chile', 3);

-- TIPOS_INVERSION

INSERT INTO tipos_inversion VALUES (1, 'Implementos');
INSERT INTO tipos_inversion VALUES (2, 'Infraestructura');
INSERT INTO tipos_inversion VALUES (3, 'Contratos Profesores');

-- DETALLE_INVERSIONES

INSERT INTO detalle_inversiones VALUES (1, 100, 'Guitarras de Chile', 1);
INSERT INTO detalle_inversiones VALUES (2, 150, 'Volvamos al teatro', 2);
INSERT INTO detalle_inversiones VALUES (3, 75, 'Un pincel para todos', 3);

-- SIN PROBAR:

-- PROFESORES
INSERT INTO profesores VALUES(1,'Pedro',NULL,'González','Vera',12345678,'9','Av. Suecia 123',1,1,1,1,1);
INSERT INTO profesores VALUES(2,'Ana','María','López','Riquelme',23456789,'K','Calle Valparaíso 456',2,2,2,2,2);
INSERT INTO profesores VALUES(3,'Luis',NULL,'Ramírez','Pinto',34567890,'5','Av. Michaihue789',3,3,3,3,3);
INSERT INTO Profesores VALUES (4,'Carlos','Joel','Mamani','Rios',14405525,'1','Av. Independencia 1450',1,1,1,1,1);
INSERT INTO Profesores VALUES (5,'Doris','Yanina','Arredondo','Quilpatay',7035298,'4','Pasaje Los Aromos 234',1,1,1,1,1);
INSERT INTO Profesores VALUES (6,'Axel','Miguel','Guzman','Hogger',9074609,'1','Av. Grecia 3250',1,1,1,1,1);
INSERT INTO Profesores VALUES (7,'Andrea',NULL,'Lopez','Guajardo',21037594,'7','Calle San Martín 876',1,1,1,1,1);
INSERT INTO Profesores VALUES (8,'Silvana','Martina','Valenzuela','Duarte',22176845,'2','Av. Vicuña Mackenna 1020',1,1,1,1,1);
INSERT INTO Profesores VALUES (9,'Catalina','Sofia','Pereira','Aguirre',10534912,'4','Pasaje El Bosque 455',1,1,1,1,1);
INSERT INTO Profesores VALUES (10,'Ricardo','Alex','Arias','Amaru',15583473,'2','Av. Pedro de Valdivia 1890',1,1,1,1,1);
INSERT INTO Profesores VALUES (11,'Jose','Miguel','Tapia','Tobar',21454912,'5','Calle Arturo Prat 540',1,1,1,1,1);
INSERT INTO Profesores VALUES (12,'Fabiola','Andrea','Silva','Meneses',14415536,'1','Av. La Florida 6789',1,1,1,1,1);
INSERT INTO Profesores VALUES (13,'Amanda','Fabiola','Marambio','Lizana',22558062,'8','Pasaje Los Copihues 120',1,1,1,1,1);
INSERT INTO Profesores VALUES (14,'Belen','Jacqueline','Sepulveda','Figueroa',6433226,'2','Av. Alemania 945',1,1,1,1,1);
INSERT INTO Profesores VALUES (15,'Hector','Francisco','Toloza','Contreras',23309887,'8','Calle O’Higgins 1330',1,1,1,1,1);
INSERT INTO Profesores VALUES (16,'Andres','Luis','Contreras','Morales',20866870,'2','Av. Costanera Norte 2200',1,1,1,1,1);
INSERT INTO Profesores VALUES (17,'Maria','Eugenia','Rapu','Escobar',9575921,'3','Pasaje Las Acacias 89',1,1,1,1,1);
INSERT INTO Profesores VALUES (18,'Viviana','Andrea','Godoy','Galdames',12173454,'2','Av. Santa Rosa 4120',1,1,1,1,1);
INSERT INTO Profesores VALUES (19,'Sandra','Lorena','Falcon','Aguilar',12362093,'5','Calle Manuel Rodríguez 760',1,1,1,1,1);
INSERT INTO Profesores VALUES (20,'Rodrigo','Fredy','Bernal','Parra',21713768,'5','Av. Pajaritos 5120',1,1,1,1,1);
INSERT INTO Profesores VALUES (21,'Carlos','Rafael','Reiman','Huilcaman',21487946,'K','Pasaje Nahuelbuta 310',1,1,1,1,1);
INSERT INTO Profesores VALUES (22,'Alexis','Fernando','Contreras','Cona',14286265,'6','Av. Pedro Aguirre Cerda 980',1,1,1,1,1);
INSERT INTO Profesores VALUES (23,'Paola','Margarita','Ojeda','Siebert',18936555,'3','Calle Blanco Encalada 145',1,1,1,1,1);
INSERT INTO Profesores VALUES (24,'Sebastian','Manuel','Diaz','Retamal',19348480,'8','Av. Los Carrera 2870',1,1,1,1,1);

-- TURNOS_TRABAJO (fecha fija, solo hora)
INSERT INTO turnos_trabajo VALUES
(1, 2, DATE '2000-01-01' + INTERVAL '15' HOUR,
        DATE '2000-01-01' + INTERVAL '17' HOUR);

INSERT INTO turnos_trabajo VALUES
(2, 3, DATE '2000-01-01' + INTERVAL '15' HOUR,
        DATE '2000-01-01' + INTERVAL '17' HOUR);

INSERT INTO turnos_trabajo VALUES
(3, 6, DATE '2000-01-01' + INTERVAL '11' HOUR,
        DATE '2000-01-01' + INTERVAL '12' HOUR);

-- TURNOS_ESCUELA_PROFESOR
INSERT INTO turnos_escuela_profesor VALUES (1, 1, 1, 1);
INSERT INTO turnos_escuela_profesor VALUES (2, 1, 1, 2);
INSERT INTO turnos_escuela_profesor VALUES (3, 2, 1, 3);

-- TIPO_CONTRATOS
INSERT INTO tipo_contrato VALUES (1, 'Planta');
INSERT INTO tipo_contrato VALUES (2, 'Honorarios');

-- ADJUDICACION_RECURSOS
insert into adjudicacion_recursos values (1, 3508, 34000000, null);

-- CONTRATOS
INSERT INTO contratos VALUES (1,'FOLIO-001',450000,NULL,NULL,1,1,1);
INSERT INTO contratos VALUES (2,'FOLIO-002',NULL,12000,NULL,2,2,1);
INSERT INTO contratos VALUES (3,'FOLIO-003',380000,NULL,NULL,3,1,1);
INSERT INTO contratos VALUES (4,'FOLIO-004',390000,NULL,NULL,4,1,1);
INSERT INTO contratos VALUES (5,'FOLIO-005',750000,NULL,NULL,5,1,1);
INSERT INTO contratos VALUES (6,'FOLIO-006',NULL,11000,NULL,6,2,1);
INSERT INTO contratos VALUES (7,'FOLIO-007',NULL,13000,NULL,7,2,1);
INSERT INTO contratos VALUES (8,'FOLIO-008',550000,NULL,NULL,8,1,1);
INSERT INTO contratos VALUES (9,'FOLIO-009',NULL,14000,NULL,9,2,2);
INSERT INTO contratos VALUES (10,'FOLIO-010',590000,NULL,NULL,10,1,2);
INSERT INTO contratos VALUES (11,'FOLIO-011',450000,NULL,NULL,11,1,2);
INSERT INTO contratos VALUES (12,'FOLIO-012',NULL,15500,NULL,12,2,2);
INSERT INTO contratos VALUES (13,'FOLIO-013',380000,NULL,NULL,13,1,2);
INSERT INTO contratos VALUES (14,'FOLIO-014',420000,NULL,NULL,14,1,2);
INSERT INTO contratos VALUES (15,'FOLIO-015',600000,NULL,NULL,15,1,2);
INSERT INTO contratos VALUES (16,'FOLIO-016',570000,NULL,NULL,16,1,2);
INSERT INTO contratos VALUES (17,'FOLIO-017',NULL,13000,NULL,17,2,3);
INSERT INTO contratos VALUES (18,'FOLIO-018',NULL,13500,NULL,18,2,3);
INSERT INTO contratos VALUES (19,'FOLIO-019',420000,NULL,NULL,19,1,3);
INSERT INTO contratos VALUES (20,'FOLIO-020',690000,NULL,NULL,20,1,3);
INSERT INTO contratos VALUES (21,'FOLIO-021',NULL,10500,NULL,21,2,3);

-- FORMULARIOS
INSERT INTO formularios VALUES (1,'FOL-1001',null,null,1,1,1,1,1,1);

/*
SELECT
    e.nombre as nombre_escuela,
    p.run as rut_empleado,
    p.dv as dv_empleado,
    p.primer_apellido as apellido_paterno,
    concat(p.primer_nombre, ' ', p.segundo_nombre) as nombres,
    tc.nombre as tipo_contrato,
    ti.nombre as tipo_titulo,
    c.sueldo_base,
    c.valor_hora
FROM contratos c
    JOIN profesores p ON p.id_profesor = c.id_profesor
    JOIN escuelas e ON e.id_escuela = c.id_escuela
    JOIN tipo_contrato tc ON tc.id_tipo_contrato = c.id_tipo_contrato
    JOIN instituciones_educativas ie ON ie.id_institucion_educativa = p.id_institucion_educativa
    JOIN tipo_institucion ti ON ti.id_tipo_institucion = ie.id_tipo_institucion
ORDER BY e.nombre ASC
;
--*/

