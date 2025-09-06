public class Persona {
    public String name = "No name";
    public Integer age = 0;

    public void showName() {
        System.out.println(name);
    }

    public void happyBD() {
        age = age + 1;
    }

    public void showInfo() {
        String message = "Name: " + name + " | Age: " + age;
        System.out.println(message);
    }
}