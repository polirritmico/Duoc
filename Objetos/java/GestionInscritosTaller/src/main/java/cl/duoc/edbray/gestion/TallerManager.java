package cl.duoc.edbray.gestion;

import java.util.ArrayList;

public class TallerManager {
    Taller taller;

    public TallerManager(Taller taller) {
        this.taller = taller;
    }

    public void mostrarEstadoTaller() {
        System.out.println("\nNombre del taller: " + taller.getNombre());
        System.out.println("Inscritos en el taller: " + taller.getParticipantes().size());
        System.out.println("Detalle de inscritos:");
        for (Participante participante : taller.getParticipantes()) {
            System.out.println("- " + participante);
        }
    }

    public ArrayList<Participante> buscarPorNombre(String fragmento) {
        ArrayList<Participante> res = new ArrayList<>();

        fragmento = fragmento.toLowerCase();
        String nombre_participante;
        for (Participante participante : taller.getParticipantes()) {
            nombre_participante = participante.getNombre().toLowerCase();
            if (nombre_participante.contains(fragmento))
                res.add(participante);
        }
        return res;
    }

    public boolean actualizarRut(Participante participante, String rut) {
        if (rutRepetido(rut)) {
            System.out.println("Rut repetido.");
            return false;
        }
        participante.setRut(rut);
        return true;
    }

    public boolean eliminarPorRut(String rut) {
        Participante participanteAEliminar = buscarPorRut(rut);
        if (participanteAEliminar == null)
            return false;

        taller.getParticipantes().remove(participanteAEliminar);
        return true;
    }

    public void cambiarEstado(String rut) {
        Participante participante = buscarPorRut(rut);
        if (participante == null)
            return;

        participante.setActivo(!participante.isActivo());
    }

    public void cambiarEstado(Participante participante) {
        if (participante == null)
            return;
        participante.setActivo(!participante.isActivo());
    }

    public void actualizarEmail(String rut, String nuevoEmail) {
        if (!emailValido(nuevoEmail)) {
            System.out.println("Correo inválido.");
            return;
        }

        Participante participante = buscarPorRut(rut);
        if (participante == null) {
            System.out.println("Rut no encontrado.");
            return;
        }

        participante.setEmail(nuevoEmail);
        System.out.println("Correo actualizado exitosamente.");
    }

    public Participante buscarPorRut(String rut) {
        for (Participante participante : taller.getParticipantes()) {
            if (participante.getRut().equals(rut))
                return participante;
        }
        return null;
    }

    public boolean registrar(Participante participante) {
        System.out.println("Agregando al participante: " + participante.getNombre());
        if (!validarRegistro(participante)) {
            System.out.println("No se ha registrado al participante.");
            return false;
        }
        taller.getParticipantes().add(participante);

        String cupos = "[Cupos: " + taller.getParticipantes().size();
        cupos += "/" + taller.getCupoMaximo() + "]";
        System.out.println("Participante agregado. " + cupos);

        return true;
    }

    private boolean validarRegistro(Participante postulante) {
        if (postulante == null) {
            System.out.println("No hay postulante");
            return false;
        } else if (rutRepetido(postulante.getRut())) {
            System.out.println("Rut repetido.");
            return false;
        } else if (!emailValido(postulante.getEmail())) {
            System.out.println("Correo inválido.");
            return false;
        } else if (!hayCupo()) {
            System.out.println("Correo inválido.");
            return false;
        }
        return true;
    }

    private boolean hayCupo() {
        return taller.getParticipantes().size() < taller.getCupoMaximo();
    }

    private boolean emailValido(String email) {
        if (email.contains(" ")) return false;
        return email.contains("@") && email.contains(".");
    }

    private boolean rutRepetido(String rut) {
        for (Participante participante : taller.getParticipantes()) {
            if (participante.getRut().equals(rut)) return true;
        }
        return false;
    }
}

