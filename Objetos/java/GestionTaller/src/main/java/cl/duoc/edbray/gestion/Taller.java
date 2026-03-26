package cl.duoc.edbray.gestion;

import java.util.ArrayList;

public class Taller {
    private String nombre;
    private int cupoMaximo;
    private ArrayList<Participante> participantes;

    public Taller(String nombre, int cupoMaximo) {
        this.nombre = nombre;
        this.cupoMaximo = cupoMaximo;
        participantes = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getCupoMaximo() {
        return cupoMaximo;
    }

    public void setCupoMaximo(int cupoMaximo) {
        this.cupoMaximo = cupoMaximo;
    }

    public ArrayList<Participante> getParticipantes() {
        return participantes;
    }

    public void setParticipantes(ArrayList<Participante> participantes) {
        this.participantes = participantes;
    }
}
