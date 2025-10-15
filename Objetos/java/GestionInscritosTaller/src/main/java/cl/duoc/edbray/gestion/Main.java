package cl.duoc.edbray.gestion;

public class Main {
    public static void main(String[] args) {
        System.out.println("[Caso de uso:]\n");

        System.out.println("1. Carga inicial...");
        System.out.println(" → Crear taller");
        TallerManager tm = new TallerManager(new Taller("Taller Java", 5));

        System.out.println(" → Insertar participantes");
        tm.registrar(new Participante("11111111-1", "Alan Brito", "alan.brito@mail.cl", true));
        tm.registrar(new Participante("22222222-2", "Susana Oria", "susana.oria@mail.cl", true));
        tm.registrar(new Participante("33333333-3", "Mario Neta", "mario.neta@mail.cl", true));

        System.out.println("\n2. Registro con validaciones");
        System.out.println(" → Registro rut duplicado:");
        tm.registrar(new Participante("33333333-3", "Rut Duplicado", "rutduplicado@mail.cl", true));

        System.out.println(" → Registro correo inválido:");
        tm.registrar(new Participante("4444444-4", "Mail Incorrecto", "aquiles.brindo-mail.cl", true));

        System.out.println(" → Registro con cupo máximo");
        tm.registrar(new Participante("44444444-4", "Soila Cerda", "soila.cerda@mail.cl", true));
        tm.registrar(new Participante("55555555-5", "Esteban Quito", "esteban.quito@mail.cl", false));
        tm.registrar(new Participante("66666666-6", "Elsa Pato", "elsapato@mail.cl", true));

        System.out.println("\n3. Actualización de rut");
        Participante seleccionado = tm.taller.getParticipantes().getFirst();
        System.out.println(" → Antes: " + seleccionado);
        tm.actualizarRut(seleccionado, "9999999-9");
        System.out.println(" → Después: " + seleccionado);

        System.out.println("\n4. Cambio de estado");
        System.out.println(" → Antes: " + seleccionado);
        tm.cambiarEstado(seleccionado);
        System.out.println(" → Después: " + seleccionado);

        System.out.println("\n5. Búsqueda");
        System.out.println(" → Encontrados ('an'):");
        for (Participante match : tm.buscarPorNombre("an"))
            System.out.println(match);

        System.out.println("\n6. Eliminación");
        System.out.println(" → Eliminando rut 22222222-2:");
        System.out.println("Participantes antes: " + tm.taller.getParticipantes().size());
        tm.eliminarPorRut("22222222-2");
        System.out.println("Participantes después: " + tm.taller.getParticipantes().size());

        System.out.println(" → Mostrar estado:");
        tm.mostrarEstadoTaller();
    }
}
