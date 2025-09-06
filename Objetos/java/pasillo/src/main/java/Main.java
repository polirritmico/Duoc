public class Main {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.name = "Pedro";
        persona1.age = 10;

        Persona persona2 = new Persona();
        persona2.name = "María";
        persona2.age = 12;

        persona1.mostrarEdad();
        persona1.cumpleAnios();
        persona1.mostrarEdad();
    }
}
