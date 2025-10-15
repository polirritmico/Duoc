package cl.duoc.edbray.gestion;

import java.util.ArrayList;

public class Taller {
    private String nombre;
    private int cupoMaximo;
    private ArrayList<Participante> participantes;

    public Taller(String nombre, int cupoMaximo) {
        this.nombre = nombre;
        this.cupoMaximo = cupoMaximo;
        this.participantes = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public int getCupoMaximo() {
        return cupoMaximo;
    }

    public ArrayList<Participante> getParticipantes() {
        return participantes;
    }
}
