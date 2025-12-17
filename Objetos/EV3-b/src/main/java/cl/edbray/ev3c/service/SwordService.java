/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cl.edbray.ev3c.service;

import cl.edbray.ev3c.repository.SwordRepository;
import cl.edbray.ev3c.model.Sword;
import java.util.List;

/**
 *
 * @author eduardo
 */
public class SwordService {

    private final SwordRepository repository;

    public SwordService(SwordRepository repository){
        this.repository = repository;
    }

    public List<Sword> listAll() {
        return repository.listAll();
    }

    public void create(Sword sword) {
        validateInputData(sword);

        repository.listAll().stream()
            .filter(s -> s.getMaterial().equals(sword.getMaterial()))
            .findAny()
            .ifPresent(s -> {
                throw new IllegalArgumentException("El material ingresado ya existe.");
            });

        repository.save(sword);
    }

    public void update(Sword sword) {
        validateInputData(sword);
        repository.update(sword);
    };

    private void validateInputData(Sword sword) {
        if (sword.getMaterial() == null || sword.getMaterial().trim().isEmpty()) {
            throw new IllegalArgumentException("El material de la espada es obligatorio.");
        }

        if (sword.getLength() < 1) {
            throw new IllegalArgumentException("La longitud de la espada debe ser mayor a cero.");
        }
    }
}
