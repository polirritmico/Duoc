public class EjemploHolaMundo {
    public static void main(String[] args) {
        System.out.println("¡Hola, mundo!");

        // Definición y de variables y tipos de datos básicos

        int num_int;
        short num_short;
        long num_long; // doble de bits que long
        double num_double; // doble de bits que double

        int number = 2; // asignación literal
        int number2 = number; // asignación por variable
        int number3 = 2 + 3; // asignación por operatoria
        int number4 = number2 * number3; // asignación por operatoria de variables
        long long_number = 1_000_000_000_000L; // para evitar errores se usa L o l
        float float_number = 1.23456789f; //
        double double_number = 1.23456789d;

        // Los tipos anteriores son en minúscula porque son primitivos, es decir
        // guardan su propio valor.

        // Concatenación de strings
        String texto = "numero: " + number3;
        System.out.println(texto)
    }
}
