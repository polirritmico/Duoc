package demo;

import static org.junit.jupiter.api.Assertions.*;
import demo.Validador;

class ValidadorTest {
    @org.junit.jupiter.api.Test
    void testSinAdmin() {
        String caseValue = "Debería ser true con admin";
        Boolean esperado = true;

        Validador validador = new Validador();
        Boolean salida = validador.sinAdmin(caseValue);

        assertEquals(esperado, salida);
    }
;}