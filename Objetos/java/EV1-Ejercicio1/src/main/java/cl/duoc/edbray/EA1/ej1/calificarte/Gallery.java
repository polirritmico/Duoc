package cl.duoc.edbray.EA1.ej1.calificarte;

public class Gallery {
    private String uniqueCode;
    private String name;
    private String city;

    public Gallery() {}

    public Gallery(String uniqueCode, String name, String city) {
        this.uniqueCode = uniqueCode;
        this.name = name;
        this.city = city;
    }

    public String getUniqueCode() {
        return uniqueCode;
    }

    public void setUniqueCode(String uniqueCode) {
        this.uniqueCode = uniqueCode;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
