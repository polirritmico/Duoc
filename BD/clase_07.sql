SELECT * FROM credito_cliente

SELECT
	count(*) AS count,
	sum(monto_solicitado) AS monto_solicitado,
	-- sql primero genera el valor y luego suma, es decir aplica la
	-- multiplicación y luego la suma.
	sum(monto_solicitado * 1.01) AS "monto_al_1%",
	avg(monto_credito) AS promedio_monto_credito
FROM credito_cliente
;

-- Cuantos créditos solicita cada cliente
SELECT
	nro_cliente,
	-- count(*) va a fallar sin group by
	count(*) AS cantidad_creditos
FROM credito_cliente
-- WHERE filtra los registros antes de agruparlos
GROUP BY nro_cliente
HAVING -- filtra la funcion de grupo
	-- cantidad_credito >= 2 va a fallar porque no puede usar un alias
	count(*) >= 2
ORDER BY cantidad_creditos DESC
;

----------------------------------

SELECT
	-- desde la tabla cliente:
	c.PNOMBRE || ' ' || c.APPATERNO || ' ' || c.APMATERNO AS nombre,
	-- desde la tabla credito_cliente:
	cc.nro_cliente,
	cc.nro_solic_credito,
	cc.monto_solicitado,
	cc.total_cuotas_credito
FROM credito_cliente cc
 -- no es necesario poner INNER, es el tipo por defecto
INNER JOIN cliente c ON cc.nro_cliente = c.nro_cliente
;

SELECT
	*
FROM cliente;

---

SELECT
	c.pnombre || ' ' || c.appaterno AS nombre,
	fp.NOMBRE_FORMA_PAGO,
	count(fp.nombre_forma_pago)
FROM credito_cliente cc
	JOIN cliente c ON cc.nro_cliente = c.NRO_CLIENTE 
	JOIN cuota_credito_cliente ccc ON ccc.NRO_SOLIC_CREDITO = cc.NRO_SOLIC_CREDITO
	JOIN FORMA_PAGO fp ON fp.COD_FORMA_PAGO = ccc.COD_FORMA_PAGO
GROUP BY
	c.PNOMBRE,
	c.APPATERNO,
	fp.NOMBRE_FORMA_PAGO
ORDER BY nombre
;