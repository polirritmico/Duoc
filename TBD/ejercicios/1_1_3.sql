-- Guía 1.1.3
-- 3.
DECLARE
  TYPE t_cliente IS RECORD (
    nro cliente.nro_cliente%TYPE
    ,nombre VARCHAR2(255)
    ,tipo tipo_cliente.nombre_tipo_cliente%TYPE
    ,profesion profesion_oficio.nombre_prof_ofic%TYPE
    ,nombre_comuna comuna.nombre_comuna%TYPE
    ,edad NUMERIC(3)
    ,antiguedad NUMERIC(2)
  );

  v_nro_cliente NUMERIC := 3;
  v_cliente t_cliente;
  v_data cliente%ROWTYPE;

BEGIN
  SELECT * INTO v_data FROM cliente
    WHERE nro_cliente = v_nro_cliente;

  v_cliente.nro := v_nro_cliente;
  v_cliente.nombre := v_data.pnombre
    ||' '||v_data.snombre
    ||' '||v_data.appaterno
    ||' '||v_data.apmaterno;
  v_cliente.edad := trunc(months_between(sysdate, v_data.fecha_nacimiento)/12);
  v_cliente.antiguedad := trunc(months_between(sysdate, v_data.fecha_inscripcion)/12);

  SELECT nombre_comuna INTO v_cliente.nombre_comuna FROM comuna
  WHERE cod_region = v_data.cod_region
    AND cod_provincia = v_data.cod_provincia
    AND cod_comuna = v_data.cod_comuna;

  SELECT nombre_tipo_cliente INTO v_cliente.tipo FROM tipo_cliente
  WHERE cod_tipo_cliente = v_data.cod_tipo_cliente;

  SELECT nombre_prof_ofic INTO v_cliente.profesion FROM profesion_oficio
  WHERE cod_prof_ofic = v_data.cod_prof_ofic;

  DBMS_OUTPUT.PUT_LINE('===== PERFIL COMERCIAL =====');
  DBMS_OUTPUT.PUT_LINE('Cliente N     : '||v_cliente.nro);
  DBMS_OUTPUT.PUT_LINE('Nombre        : '||v_cliente.nombre);
  DBMS_OUTPUT.PUT_LINE('Tipo cliente  : '||v_cliente.tipo);
  DBMS_OUTPUT.PUT_LINE('Profesion     : '||v_cliente.profesion);
  DBMS_OUTPUT.PUT_LINE('Comuna        : '||v_cliente.nombre_comuna);
  DBMS_OUTPUT.PUT_LINE('Edad          : '||v_cliente.edad);
  DBMS_OUTPUT.PUT_LINE('Antiguedad    : '||v_cliente.antiguedad);
END;

-- 4.
DECLARE
  TYPE t_resumen_cuotas IS RECORD (
     cuotas_pagadas NUMERIC := 0
    ,monto_pagado NUMERIC := 0
    ,monto_pendiente NUMERIC := 0
    ,avance NUMERIC(4,1) := 0
  );

  TYPE t_credito IS RECORD (
     nro_solicitud credito_cliente.nro_solic_credito%TYPE
    ,producto credito.nombre_credito%TYPE
    ,monto credito_cliente.monto_credito%TYPE
    ,cuotas_pactadas credito_cliente.total_cuotas_credito%TYPE
    ,resumen t_resumen_cuotas
  );

  FMT VARCHAR2(14):= 'FM$999g999g999';

  v_nro_credito NUMERIC := 2001;
  v_data_credito credito_cliente%ROWTYPE;
  v_resumen_cuotas t_resumen_cuotas;
  v_credito t_credito;

BEGIN
  SELECT * INTO v_data_credito FROM credito_cliente
    WHERE nro_solic_credito = v_nro_credito;

  SELECT nombre_credito INTO v_credito.producto FROM credito
    WHERE cod_credito = v_data_credito.cod_credito;

  SELECT
     count(fecha_pago_cuota)
    ,sum(monto_pagado)
  INTO
     v_resumen_cuotas.cuotas_pagadas
    ,v_resumen_cuotas.monto_pagado
  FROM cuota_credito_cliente
    WHERE nro_solic_credito = v_nro_credito
      AND fecha_pago_cuota IS NOT NULL;

  v_credito.nro_solicitud := v_nro_credito;
  v_credito.monto := v_data_credito.monto_credito;
  v_credito.cuotas_pactadas := v_data_credito.total_cuotas_credito;
  v_resumen_cuotas.monto_pendiente := v_credito.monto - v_resumen_cuotas.monto_pagado;
  v_resumen_cuotas.avance := ROUND((v_resumen_cuotas.monto_pagado/v_credito.monto) * 100, 1);
  v_credito.resumen := v_resumen_cuotas;

  DBMS_OUTPUT.PUT_LINE('===== ESTADO DEL CRÉDITO =====');
  DBMS_OUTPUT.PUT_LINE('Solicitud N     : '||v_credito.nro_solicitud);
  DBMS_OUTPUT.PUT_LINE('Producto        : '||v_credito.producto);
  DBMS_OUTPUT.PUT_LINE('Monto crédito   : '||to_char(v_credito.monto, FMT));
  DBMS_OUTPUT.PUT_LINE('Cuotas pactadas : '||v_credito.cuotas_pactadas);
  DBMS_OUTPUT.PUT_LINE('------------------------------');
  DBMS_OUTPUT.PUT_LINE('Cuotas pagadas  : '||v_credito.resumen.cuotas_pagadas);
  DBMS_OUTPUT.PUT_LINE('Monto pagado    : '||to_char(v_credito.resumen.monto_pagado, FMT));
  DBMS_OUTPUT.PUT_LINE('Monto pendiente : '||to_char(v_credito.resumen.monto_pendiente, FMT));
  DBMS_OUTPUT.PUT_LINE('Avance          : '||v_credito.resumen.avance||'%');
END;
