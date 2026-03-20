package cl.duoc.MicroservicioPersona.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import cl.duoc.MicroservicioPersona.model.Persona;
import cl.duoc.MicroservicioPersona.repository.PersonaRepository;

@Service
public class PersonaService {

    @Autowired
    private PersonaRepository repository;

    public PersonaService(PersonaRepository personaRepository) {
        repository = personaRepository;
    }

    public List<Persona> getAllPersonas() {
        return repository.getPersonas();
    }

    public Persona getPersonaByRut(int rut) {
        return repository.getByRut(rut);
    }

    public Persona savePersona(Persona persona) {
        if (!isValidPersona(persona)) {
            throw new RuntimeException("Persona inválida.");
        }
        return repository.createPersona(persona);
    }

    public boolean deletePersona(int rut) {
        return repository.deletePersona(rut) != null;
    }

    public Persona updatePersona(Persona persona) {
        try {
            return repository.updatePersona(persona);
        } catch (RuntimeException err) {
            return null;
        }

    }

    private boolean isValidPersona(Persona persona) {
        if (persona == null) {
            return false;
        } else if (persona.getNombre() == null || persona.getNombre().isBlank()) {
            return false;
        } else if (persona.getRut() == 0) {
            return false;
        } else if (persona.getDv() == '\0') {
            return false;
        }
        return true;
    }
}
