package cl.duoc.edbray.clase1;

import java.util.Arrays;

public class App {
    private final InputsUsuario inputUsuario = new InputsUsuario();

    public void run() {
        int cantidadPersonas = 5;
        Persona[] grupoPersonas = crearGrupoPersonas(cantidadPersonas);

        mostrarPersonas(grupoPersonas);
    }

    private Persona[] crearGrupoPersonas(int cantidad) {
        Persona[] grupo = new Persona[cantidad];

        for (int i = 0; i < cantidad; i++) {
            Persona nuevaPersona = new Persona();
            nuevaPersona.pedirDatosAlUsuario();

            grupo[i] = nuevaPersona;
        }
    }

    private void mostrarPersonas(Persona[] grupo) {
        Persona persona;

        System.out.println("Listado de personas en grupo:");
        for (int i = 0; i < grupo.length; i++) {
            persona = grupo[i];
            System.out.println(" - " + persona.toString());
        }
    }
}
