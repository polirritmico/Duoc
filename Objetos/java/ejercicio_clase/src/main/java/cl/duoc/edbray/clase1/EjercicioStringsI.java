package cl.duoc.edbray.clase1;

public class EjercicioStringsI {
    public void run() {
        String mensaje = "   Hola_mundo secreto__   ";

        String sinEspacios = mensaje.trim();
        String reemplazoGuiones = mensaje.replace("_", " ");
        String mensajeProcesado = mensaje.replace("_", " ").trim();

        String extractoMundo = mensaje.substring(8, 8+5);
        Boolean mundoExtraido = extractoMundo.equals("mundo");

        System.out.println("Mensaje original: '"+ mensaje + "'");
        System.out.println("Mensaje procesado: '" + mensajeProcesado +"'");
        System.out.println("Longitud del mensaje original: " + mensaje.length()); System.out.println("Longitud del mensaje procesado: " + mensajeProcesado.length()); System.out.println("Palabra extraída: '" + extractoMundo +"'");
        System.out.println("¿La palabra es \"mundo\"? " + mundoExtraido);

        System.out.println("----------------------");

        String msg = "maYUsCuLa";
        String res = msg.substring(0,1).toUpperCase() + msg.substring(1).toLowerCase();
        System.out.println(res);
    }
}
