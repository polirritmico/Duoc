public class Main {
    public static void main(String[] args) {
        Persona persona1;
        persona1 = new Persona();
        persona1.name = "Alan";
        persona1.age = 37;

        Persona persona2;
        persona2 = new Persona();
        persona2.name = "María";
        persona2.age = 89;

        persona1.happyBD();
        persona1.happyBD();

        persona1.showInfo();
        persona2.showInfo();
        persona2.happyBD();
        persona2.showInfo();
    }
}
