/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cl.edbray.ev3c.model;

/**
 *
 * @author eduardo
 */
public class Sword {
    private int id;
    private String material;
    private int length;

    public Sword() {}

    public Sword(int id, String material, int length) {
        this.id = id;
        this.material = material;
        this.length = length;
    }

    public Sword(String material, int length) {
        this.id = 0;
        this.material = material;
        this.length = length;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
}
