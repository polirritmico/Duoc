--- Ejercicio 4
SELECT * FROM EMPLEADO e;
SELECT * FROM ARRIENDO_EMBARCACION ae;
SELECT * FROM EMBARCACION em;

SELECT
	TO_CHAR(e.NUMRUN_EMP, '999g999g999') || '-' || e.DVRUN_EMP AS "RUN"
	,initcap(e.PNOMBRE_EMP || ' ' || e.APPATERNO_EMP || ' ' || e.APMATERNO_EMP) AS "Nombre Empleado"
	,count(*) AS "Total Arriendos Mes"
	,count(*) || '%' AS "% Bonif."
	,to_char(count(*) * e.SUELDO_BASE / 100, '$999g999g999') AS "Monto Bonificación"
FROM ARRIENDO_EMBARCACION ae
JOIN EMBARCACION em ON em.matricula = ae.matricula
JOIN EMPLEADO e ON e.NUMRUN_EMP = em.NUMRUN_EMP
WHERE
	TRUNC(ae.fecha_ini_arriendo, 'MM') = TRUNC(SYSDATE, 'MM')
    --TRUNC(ae.fecha_ini_arriendo, 'MM') = DATE '2026-04-01'
GROUP BY
	e.numrun_emp,
	e.dvrun_emp, 
	e.pnombre_emp,
	e.appaterno_emp,
	e.apmaterno_emp,
	e.sueldo_base
HAVING
    count(*) > 1
;


--- Ejercicio 3
SELECT * FROM HIST_ARRIENDO_ANUAL_EMBARCACION ha;
SELECT * FROM ARRIENDO_EMBARCACION ae;

-- Primero trabajamos con el select y luego agregamos el insert
--INSERT INTO HIST_ARRIENDO_ANUAL_EMBARCACION
--	(matricula, anno_proceso, cant_arriendos, total_dias)
SELECT
	matricula,
	EXTRACT(YEAR FROM fecha_ini_arriendo) AS anio,
	COUNT(*) AS CANT_ARRIENDOS,
	SUM(dias_solicitados) AS cant_arriendos
FROM ARRIENDO_EMBARCACION
WHERE
    EXTRACT(YEAR FROM fecha_ini_arriendo) = 2026
-- siempre agrupar las columnas que NO son funcion de grupo
GROUP BY
	matricula,
	EXTRACT(YEAR FROM fecha_ini_arriendo)
-- HAVING siempre aplica a funciones de grupo
HAVING
    COUNT(*) = 1
ORDER BY
	matricula
;


--- Ejercicio 2
SELECT * FROM EMPLEADO;
SELECT * FROM PORC_BONIF_30_ANNOS pba;

SELECT
	e.NUMRUN_EMP || '-' || e.DVRUN_EMP AS "RUN",
	e.pnombre_emp || ' ' || e.APPATERNO_EMP || ' ' || e.APMATERNO_EMP AS "Nombre Completo",
	e.FECHA_CONTRATO AS "Fecha contrato",
	ec.NOMBRE_ESTADO_CIVIL AS "Estado Civil",
	TO_CHAR(e.SUELDO_BASE, '$999g999g999') AS "Sueldo Base",
	e.sueldo_base * pb.PORCENTAJE / 100 AS "Monto Bono 30 años",
	pb.PORCENTAJE || '%' AS "% Sueldo Base"
FROM EMPLEADO e
	JOIN ESTADO_CIVIL ec ON ec.ID_ESTADO_CIVIL = e.ID_ESTADO_CIVIL
	JOIN PORC_BONIF_30_ANNOS pb
		ON e.SUELDO_BASE BETWEEN pb.SUELDO_DESDE AND pb.SUELDO_HASTA
WHERE
	EXTRACT(MONTH FROM e.FECHA_CONTRATO) = EXTRACT(MONTH FROM SYSDATE)
;


--- Ejercicio 1
SELECT * FROM EMBARCACION e;
SELECT * FROM TIPO_EMBARCACION te;
SELECT * FROM EMPLEADO;

SELECT
	te.NOMBRE_TIPO_EMB AS "Tipo Embarcación",
	e.MATRICULA AS "Matrícula",
	e.COLOR AS "Color",
	e.ESLORA AS "Eslora (m)",
	e.MOTOR AS "Motor",
	e.ANIO_FAB AS "Año Fabricación",
	TO_CHAR(e.VALOR_ARRIENDO_DIA, '$999g999g999') AS "Arriendo/Día",
	TO_CHAR(e.VALOR_GARANTIA_DIA, '$999g999g999') AS "Garantía/Día",
	TO_CHAR(e.VALOR_ARRIENDO_DIA + e.VALOR_GARANTIA_DIA, '$999g999g999') AS "Total/Día",
	SUBSTR(e.NUMRUN_EMP, 3, 1)
	|| TRUNC(EXTRACT(YEAR FROM em.FECHA_CONTRATO) * 1.2)
	|| TO_NUMBER(SUBSTR(e.NUMRUN_EMP, -2, 2) - 2)
	|| '@marineexpres.cl' AS "Correo Encargado"
FROM EMBARCACION e
	JOIN TIPO_EMBARCACION te ON e.ID_TIPO_EMB = te.ID_TIPO_EMB
	JOIN EMPLEADO em ON em.NUMRUN_EMP = e.NUMRUN_EMP
ORDER BY
	te.NOMBRE_TIPO_EMB ASC,
	e.VALOR_ARRIENDO_DIA DESC,
	e.VALOR_GARANTIA_DIA ASC,
	e.MATRICULA ASC
;