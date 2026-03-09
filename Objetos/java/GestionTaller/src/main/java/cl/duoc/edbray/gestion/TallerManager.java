package cl.duoc.edbray.gestion;

public class TallerManager {
    private Taller taller;

    public TallerManager(Taller taller) {
        this.taller = taller;
    }

    public boolean registrar(Participante participante) {
        if (!validarParticipante(participante)) {
            return false;
        }
    }

    private boolean validarParticipante(Participante participante) {
        if (participante == null) return false;
        if (participante.rut)
    }
}
