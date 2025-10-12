package cl.duoc.edbray.clase1;

import java.util.Scanner;

public class InputsUsuario {
    Scanner scanner = new Scanner(System.in);

    public String pedirString(String mensaje) {
        System.out.print(mensaje + ": ");
        String datoIngresado = scanner.nextLine();

        return datoIngresado;
    }

    public int pedirInt(String mensaje) {
        System.out.print(mensaje + ": ");
        String datoIngresado = scanner.nextLine();
        int numero = Integer.parseInt(datoIngresado);

        return numero;
    }
}
