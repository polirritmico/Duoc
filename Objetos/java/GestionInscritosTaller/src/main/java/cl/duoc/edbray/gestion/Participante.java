package cl.duoc.edbray.gestion;

public class Participante {
    private String rut;
    private String nombre;
    private String email;
    private boolean activo;

    public Participante(String rut, String nombre, String email, boolean activo) {
        this.rut = rut;
        this.nombre = nombre;
        this.email = email;
        this.activo = activo;
    }

    @Override
    public String toString() {
        String res = "Usuario: [";
        res += "Rut: " + rut;
        res += ", Nombre: " + nombre;
        res += ", Email: " + email;
        res += ", Estado: " + (activo ? "participando" : "inactivo");
        res += "]";
        return res;
    }

    @Override
    public boolean equals(Object other) {
        if (other == null) return false;
        if (this.getClass() != other.getClass()) return false;

        return this.rut.equals(((Participante) other).rut);
    }

    @Override
    public int hashCode() {
        if (rut.isBlank()) return 0;
        return Integer.parseInt(rut);
    }

    public String getRut() {
        return rut;
    }

    public void setRut(String rut) {
        this.rut = rut;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public boolean isActivo() {
        return activo;
    }

    public void setActivo(boolean activo) {
        this.activo = activo;
    }
}
