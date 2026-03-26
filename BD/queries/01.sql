select * from empleado;

-- Caso 1
select
    'El empleado '
      || INITCAP(nombre_emp || ' ' || appaterno_emp || ' ' || apmaterno_emp)
      || ' nació el ' || fecnac_emp
      || '.'
    as "listado_de_cumpleanios"
from empleado
;

-- Caso 2
--muestre el run, nombre completo, 
--renta, teléfono fijo y celular de todos los cliente
SELECT * FROM cliente;
SELECT
	to_char(numrut_cli, '999g999g999') || '-' || dvrut_cli AS rut,
	initcap(nombre_cli || ' ' || appaterno_cli || ' ' || apmaterno_cli) AS nombre_cliente,
	'$' || to_char(renta_cli,'999g999g999') AS renta,
	fonofijo_cli AS telefono_fijo,
	celular_cli AS celular
FROM 
	cliente
ORDER BY
	appaterno_cli ASC,
	apmaterno_cli ASC
;

-- Caso 3
SELECT
	nombre_emp || ' ' || appaterno_emp || ' ' || apmaterno_emp AS nombre_empleado,
	sueldo_emp AS sueldo,
	sueldo_emp * 0.5 AS bono_por_capacitacion
FROM EMPLEADO
ORDER BY
	BONO_POR_CAPACITACION DESC
;

-- Caso 4
SELECT 
	nro_propiedad AS nro_propiedad,
	numrut_prop AS rut_propietario,
	direccion_propiedad AS direccion,
	valor_arriendo,
	valor_arriendo * 0.054 AS valor_compensacion
FROM propiedad
ORDER BY
	NUMRUT_PROP
;

-- Caso 5
SELECT
	numrut_emp AS run_empleado,
	nombre_emp || ' ' || appaterno_emp || ' ' || apmaterno_emp AS nombre_empleado,
	sueldo_emp AS salario_actual,
	sueldo_emp * 1.135 AS salario_reajustado,
	sueldo_emp * 0.135 AS reajuste
FROM empleado
ORDER BY
	reajuste desc,
	appaterno_emp desc
;