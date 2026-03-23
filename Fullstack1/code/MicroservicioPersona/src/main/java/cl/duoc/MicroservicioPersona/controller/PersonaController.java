package cl.duoc.MicroservicioPersona.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import cl.duoc.MicroservicioPersona.model.Persona;
import cl.duoc.MicroservicioPersona.service.PersonaService;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PutMapping;

@RestController
@RequestMapping("/api/v1/personas")
public class PersonaController {
    @Autowired
    private PersonaService service;

    @GetMapping
    public List<Persona> getPersonas() {
        return service.getAllPersonas();
    }

    @GetMapping("/get-by-rut/{rut}")
    public Persona getPersonaByRut(@PathVariable int rut) {
        return service.getPersonaByRut(rut);
    }

    @PostMapping
    public Persona storePersona(@RequestBody Persona persona) {
        return service.savePersona(persona);
    }

    @PostMapping("/bulk-create")
    public List<Persona> bulkStorePersonas(@RequestBody List<Persona> personas) {
        return service.bulkSavePersona(personas);
    }

    @DeleteMapping("/{rut}")
    public boolean deletePersona(@PathVariable int rut) {
        return service.deletePersona(rut);
    }

    @PutMapping("/{rut}")
    public Persona updatePersona(@PathVariable int rut, @RequestBody Persona persona) {
        persona.setRut(rut);
        return service.updatePersona(persona);
    }
}