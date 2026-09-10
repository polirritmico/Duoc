create or replace procedure nombre_del_procedimiento (
    p_parametro1 IN number, -- solo se usa para agregar información
    p_parametro2 out varchar2 -- retorno
) is
    v_variable_local number;
begin
    dbms_output.put_line('Hola, ');
exception
    when others then
        dbms_output.put_line('ERROR ');
end nombre_del_procedimiento;
