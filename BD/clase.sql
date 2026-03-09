drop table comuna cascade constraints;

drop table cliente cascade constraints;

-------------------------------------------------------------------------------
create table (
  id_comuna number (3) not null,
  nom_comuna varchar2 (60) not null
);

alter table comuna add constraint comuna_pk primary key (id_comuna);

insert into
  comuna
values
  (100, 'Providencia');

insert into
  comuna
values
  (105, 'Santiago');

insert into
  comuna
values
  (110, 'Ñuñoa');

insert into
  comuna
values
  (115, 'La Florida');

insert into
  comuna
values
  (120, 'Maipú');

-- ----------------------------------------------------------------------------
-- Tabla cliente
create table (
  id_cliente number not null,
  nombre_cliente varchar2 (35) not null,
  direccion varchar2 (50) not null,
  telefono varchar2 (15) not null
);

alter table cliente add constraint cliente_pk primary key (id_cliente);

alter table cliente add constraint fk_cliente_comuna foreign key (id_comuna) references cliente (id_cliente);

-- insert into
--   comuna
-- values
--   (100, 'Providencia');
