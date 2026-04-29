SELECT
	c.nro_cliente,
	c.NUMRUN,
	c.PNOMBRE,
	cc.FECHA_SOLIC_CRED,
	cc.MONTO_SOLICITADO 
FROM cliente c
	JOIN credito_cliente cc ON c.nro_cliente = cc.NRO_CLIENTE
;

--

SELECT
	c.nro_cliente,
	c.NUMRUN,
	c.PNOMBRE,
	cc.FECHA_SOLIC_CRED,
	cc.MONTO_SOLICITADO 
FROM credito_cliente cc
	JOIN cliente c ON c.nro_cliente = cc.NRO_CLIENTE
;