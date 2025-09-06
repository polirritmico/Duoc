public class Persona {
    public String name = "Sin nombre";
    public Integer age = 0;
    public static Integer id_gloablh = 1;
    public Integer id;


    public void cumpleAnios() {
        age = age + 1;
    }

    public void nacer() {
        id = id_gloablh;
        id_gloablh = id_gloablh + 1;
    }

    public void mostrarEdad() {
        String mensaje = String.format("La edad es: %d", age);
        System.out.println(mensaje);
    }
}
