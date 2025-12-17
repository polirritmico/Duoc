/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cl.edbray.ev3c.utils;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

/**
 *
 * @author eduardo
 */
public class TestDBConnection {

    public static void main(String[] args) {
        System.out.println("Prueba de conexión a Mysql");

        System.out.println("Test 1: Conexión básica");
        boolean connected = MysqlDBConnectionFactory.testConnection();

        if (!connected) {
            System.err.println("\n- ERROR: No se pudo conectar a la base de datos.");
            return;
        }

        System.out.println("\n-------------------------------------------\n");

        System.out.println("Test 2: Consultar espadas");
        try (
            Connection conn = MysqlDBConnectionFactory.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT id, material, longitud FROM espada")
        ) {
            System.out.println("\nEspadas en la base de datos:");
            System.out.println("ID | Material            | longitud");
            System.out.println("---|---------------------|----------");

            int count = 0;
            while (rs.next()) {
                count++;
                int id = rs.getInt("id");
                String material = rs.getString("material");
                int longitud = rs.getInt("longitud");
                System.out.printf("%-3d| %-20s| %d%n", id, material, longitud);
            }
            System.out.println("\nTotal de espadas: " + count);

        } catch (Exception e) {
            System.err.println("ERROR al consultar espadas:");
            e.printStackTrace();
        }

        System.out.println("Prueba completada");
    }
}
