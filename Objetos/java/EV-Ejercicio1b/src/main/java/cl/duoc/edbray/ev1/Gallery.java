package cl.duoc.edbray.ev1;

public class Gallery {
    private String code;
    private String name;

    public Gallery() {}

    public Gallery(String code, String name, String city) {
        this.code = code;
        this.name = name;
        this.city = city;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    private String city;
}
