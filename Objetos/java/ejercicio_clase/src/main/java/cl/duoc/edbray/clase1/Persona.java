package cl.duoc.edbray.clase1;

public class Persona {
    private String nombre;
    private int edad;

    public void ingresarDatos(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public String pedirDatosAlUsuario() {
         "foo"
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + " edad: " + edad + "\n";
    }
}
