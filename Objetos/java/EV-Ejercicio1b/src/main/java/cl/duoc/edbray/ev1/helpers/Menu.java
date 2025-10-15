package cl.duoc.edbray.ev1.helpers;

import java.util.Scanner;

public class Menu {
    private String header;
    private String body;
    private int numberOfChoices;
    private String buildedMenu;
    private final Scanner scanner = new Scanner(System.in);

    public Menu(String header, String body, int numberOfChoices) {
        this.header = header;
        this.body = body;
        this.numberOfChoices = numberOfChoices;
    }

    public String build() {
        buildedMenu = header + "\n" + body;
        return buildedMenu;
    }

    public void show() {
        System.out.println(buildedMenu);
    }

    public int askUserSelection() {
        String defaultMessage = "Seleccione una opción: ";
        String defaultErrorMessage = "Opción inválida, intente nuevamente.";
        return askUserSelection(defaultMessage, defaultErrorMessage, numberOfChoices);
    }

    public int askUserSelection(String message, String errorMessage, int lastChoice) {
        boolean validInput = false;
        while (true) {
            System.out.print(message);
            if (!scanner.hasNextInt()) {
                System.out.println(errorMessage);
                continue;
            }

            int usrInput = scanner.nextInt();
            if (usrInput < 1 || usrInput > lastChoice) {
                System.out.println(errorMessage);
                continue;
            }

            return usrInput;
        }
    }
}
