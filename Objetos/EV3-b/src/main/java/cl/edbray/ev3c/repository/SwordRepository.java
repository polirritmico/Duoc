/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cl.edbray.ev3c.repository;

import cl.edbray.ev3c.model.Sword;
import java.util.List;
import java.util.Optional;

/**
 *
 * @author eduardo
 */
public interface SwordRepository {

    Optional<Sword> searchById(int id);

    List<Sword> listAll();

    Sword save(Sword sword);

    void update(Sword sword);
}
