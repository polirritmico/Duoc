/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package cl.edbray.ev3c.repository.impl;

import cl.edbray.ev3c.model.Sword;
import cl.edbray.ev3c.repository.SwordRepository;
import cl.edbray.ev3c.utils.MysqlDBConnectionFactory;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

/**
 *
 * @author eduardo
 */
public class SwordRepositoryMysql implements SwordRepository {

    public SwordRepositoryMysql() {
    }

    @Override
    public Optional<Sword> searchById(int id) {
        String sql = "SELECT id, material, longitud FROM espada"
            + " WHERE id = ?"
            + " ORDER BY Material ASC";

        try (
            Connection conn = MysqlDBConnectionFactory.getConnection();
            PreparedStatement ps = conn.prepareStatement(sql);
        ) {
            ps.setInt(1, id);

            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    return Optional.of(mapSword(rs));
                }
            }
        } catch (SQLException e){
            System.err.println("Error al buscar espada por ID: " + id);
            e.printStackTrace();
        }
        return Optional.empty();
    }

    @Override
    public List<Sword> listAll() {
        String sql = "SELECT id, material, longitud FROM espada "
            + "ORDER BY id ASC";

        List<Sword> swords = new ArrayList<>();

        try (
            Connection conn = MysqlDBConnectionFactory.getConnection();
            PreparedStatement ps = conn.prepareStatement(sql);
            ResultSet rs = ps.executeQuery();
        ) {
            while (rs.next()) {
                swords.add(mapSword(rs));
            }
        } catch (SQLException e){
            System.err.println("Error al listar todas las espadas");
            e.printStackTrace();
        }
        return swords;
    }

    @Override
    public Sword save(Sword sword) {
        String sql = "INSERT INTO espada (material, longitud)"
            + " VALUES (?, ?)";

        try (
            Connection conn = MysqlDBConnectionFactory.getConnection();
            PreparedStatement ps = conn.prepareStatement(sql, Statement.RETURN_GENERATED_KEYS);
        ) {
            ps.setString(1, sword.getMaterial());
            ps.setInt(2, sword.getLength());

            int rowsAffected = ps.executeUpdate();

            if (rowsAffected == 0) {
                throw new RuntimeException("No se pudo insertar la espada en la BD");
            }

            try (ResultSet rs = ps.getGeneratedKeys()) {
                if (rs.next()) {
                    return new Sword(
                        rs.getInt(1),
                        sword.getMaterial(),
                        sword.getLength()
                    );
                } else {
                    throw new RuntimeException("No se pudo obtener la ID de la nueva espada");
                }
            }
        } catch (SQLException e){
            throw new RuntimeException("Error al registrar espada", e);
        }
    }

    @Override
    public void update(Sword sword) {
        String sql = "UPDATE sword"
            + " SET material = ?, longitud = ?"
            + " WHERE id = ?";

        try (
            Connection conn = MysqlDBConnectionFactory.getConnection();
            PreparedStatement ps = conn.prepareStatement(sql)
        ) {
            ps.setString(1, sword.getMaterial());
            ps.setInt(2, sword.getLength());
            ps.setInt(3, sword.getId());

            int rowsAffected = ps.executeUpdate();
            if (rowsAffected == 0) {
                throw new RuntimeException("No se encuentra espada ID: " + sword.getId());
            }

        } catch (SQLException e) {
            throw new RuntimeException("Error al actualizar espada ID: " + sword.getId(), e);
        }
    }

    private Sword mapSword(ResultSet rs) throws SQLException {
        Sword sword = new Sword();
        sword.setId(rs.getInt("id"));
        sword.setMaterial(rs.getString("material"));
        sword.setLength(rs.getInt("longitud"));

        return sword;
    }
}
