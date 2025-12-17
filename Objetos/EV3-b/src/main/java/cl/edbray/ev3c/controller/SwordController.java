/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cl.edbray.ev3c.controller;

import cl.edbray.ev3c.model.Sword;
import cl.edbray.ev3c.service.SwordService;
import java.util.List;

/**
 *
 * @author eduardo
 */
public class SwordController {
    private final SwordService service;

    public SwordController(SwordService service) {
        this.service = service;
    }

    public List<Sword> listAll() {
        return service.listAll();
    }

    public void create(String material, String lengthText) {
        int length;
        try {
            length = Integer.parseInt(lengthText);
        } catch (NumberFormatException e) {
            throw new RuntimeException("La longitud de la espada no es un número válido.");
        }

        Sword newSword = new Sword(material, length);
        service.create(newSword);
    }

}
