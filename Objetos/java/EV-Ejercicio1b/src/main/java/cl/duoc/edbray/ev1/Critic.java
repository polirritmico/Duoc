package cl.duoc.edbray.ev1;

public class Critic {
    private String rut;
    private String name;
    private String specialty;

    public Critic() {}

    public Critic(String rut, String name, String specialty, int experienceYears) {
        this.rut = rut;
        this.name = name;
        this.specialty = specialty;
        this.experienceYears = experienceYears;
    }

    private int experienceYears;

    public String getRut() {
        return rut;
    }

    public void setRut(String rut) {
        this.rut = rut;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSpecialty() {
        return specialty;
    }

    public void setSpecialty(String specialty) {
        this.specialty = specialty;
    }

    public int getExperienceYears() {
        return experienceYears;
    }

    public boolean setExperienceYears(int experienceYears) {
        return setExperienceYears(experienceYears, 80);
    }

    public boolean setExperienceYears(int experienceYears, int maxAllowedExperienceYears) {
        if (experienceYears < 0 || experienceYears <= maxAllowedExperienceYears) {
            return false;
        }
        this.experienceYears = experienceYears;
        return true;
    }
}
