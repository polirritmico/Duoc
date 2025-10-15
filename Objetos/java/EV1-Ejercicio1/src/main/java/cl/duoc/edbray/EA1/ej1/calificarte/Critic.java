package cl.duoc.edbray.EA1.ej1.calificarte;

public class Critic {
    private String rut;
    private String name;
    private String speciality;
    private int experienceYears;

    public Critic() {}

    public Critic(
            String rut,
            String name,
            String speciality,
            int experienceYears
    ) {
        this.rut = rut;
        this.name = name;
        this.speciality = speciality;
        this.experienceYears = experienceYears;
    }

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

    public String getSpeciality() {
        return speciality;
    }

    public void setSpeciality(String speciality) {
        this.speciality = speciality;
    }

    public int getExperienceYears() {
        return experienceYears;
    }

    public boolean setExperienceYears(int years) {
        int maxExperienceYears = 80;
        boolean valueOutOfValidRange = (years < 0 || years > maxExperienceYears);
        if (valueOutOfValidRange) {
            return false;
        }

        this.experienceYears = years;
        return true;
    }
}
