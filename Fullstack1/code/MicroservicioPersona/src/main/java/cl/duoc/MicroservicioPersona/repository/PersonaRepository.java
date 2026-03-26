package cl.duoc.MicroservicioPersona.repository;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import cl.duoc.MicroservicioPersona.model.Persona;

@Repository
public class PersonaRepository {
    private List<Persona> listaPersonas = new ArrayList<>();

    public List<Persona> getPersonas() {
        return new ArrayList<>(listaPersonas);
    }

    public Persona getByRut(int rut) {
        for (Persona persona : listaPersonas) {
            if (persona.getRut() == rut) {
                return persona;
            }
        }
        return null;
    }

    public Persona createPersona(Persona newPersona) {
        Persona personaInDB = getByRut(newPersona.getRut());
        if (personaInDB != null) {
            throw new RuntimeException("Ya existe la persona.");
        }
        listaPersonas.add(newPersona);
        return newPersona;
    }

    public Persona updatePersona(Persona personaABuscar) {
        for (Persona personaInDB : listaPersonas) {
            if (personaABuscar.getRut() == personaInDB.getRut()) {
                personaInDB.setNombre(personaABuscar.getNombre());
                return personaInDB;
            }
        }
        throw new RuntimeException("Persona no encontrada.");
    }

    public Persona deletePersona(int rut) {
        Persona persona = getByRut(rut);
        listaPersonas.remove(persona);
        return persona;
    }
}
