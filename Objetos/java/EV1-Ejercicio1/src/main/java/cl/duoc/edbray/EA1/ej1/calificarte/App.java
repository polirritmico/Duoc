package cl.duoc.edbray.EA1.ej1.calificarte;

import java.util.Scanner;

public class App {
    private final Scanner scanner = new Scanner(System.in);

    private Gallery gallery;
    private Critic critic;
    private Painting painting;
    private Evaluation evaluation;

    private int currentSelection;
    private boolean shouldExit = false;

    public App(){}

    private void showMenu () {
        System.out.println("""
=== SISTEMA DE REGISTRO DE CUADROS Y EVALUACIONES ===
1. Ingresar Galería
2. Ingresar Crítico
3. Ingresar Cuadro
4. Ingresar Evaluación
5. Calcular Resultados
6. Salir
""");
    }

    public void run() {
        String selection;
        do {
            showMenu();
            selection = askUserSelection();
            executeSelectedAction(selection);
        } while (!exitRequested());
    }

    private void executeSelectedAction(String selection) {
        switch (selection) {
            case "1" -> addGalleryAction();
            case "2" -> addCriticAction();
            case "3" -> addPaintingAction();
            case "4" -> addEvaluationAction();
            case "5" -> scoreResultsAction();
            case "6" -> exitAction();
            default -> invalidSelectionAction();
        }
    }

    private String askStringToUser(String message) {
        String userInput;
        do {
            System.out.println(message + ": ");
            userInput = scanner.nextLine();
        } while (userInput.isBlank());
        return userInput;
    }

    private int askNumberToUser(String message) {
        int userInput;
        while (true) {
            System.out.println(message + ": ");
            String userInputRaw = scanner.next();

            if (userInputRaw.isBlank()) {
                continue;
            }

            userInput = Integer.parseInt(userInputRaw);
            break;
        }
        return userInput;
    }

    private void addGalleryAction() {
        System.out.println("--- INGRESO DE GALERÍA ---");

        gallery = new Gallery();
        gallery.setUniqueCode(askStringToUser("Ingrese código de galería"));
        gallery.setName(askStringToUser("Ingrese nombre de galería"));
        gallery.setCity(askStringToUser("Ingrese ciudad"));

        System.out.println("Galería registrada con éxito.\n");
        System.out.println("Presione Enter para continuar...");
        scanner.nextLine();
    }

    private void addCriticAction() {
        System.out.println("--- INGRESO DE CRÍTICO ---\n");

        critic = new Critic();
        critic.setName(askStringToUser("Ingrese nombre"));
        critic.setRut(askStringToUser("Ingrese RUT"));
        critic.setSpeciality(askStringToUser("Ingrese especialidad"));
        critic.setExperienceYears(askNumberToUser("Ingrese años de experiencia"));

        System.out.println("Crítico registrado con éxito.\n");
        System.out.println("Presione Enter para continuar...");
        scanner.nextLine();
    }

    private void addPaintingAction() {
        System.out.println("--- INGRESO DE CUADRO ---\n");

        painting = new Painting();
        painting.setTitle(askStringToUser("Ingrese título"));
        painting.setAuthor(askStringToUser("Ingrese autor"));
        painting.setUniqueCode(askStringToUser("Ingrese código único"));
        painting.setCreationYear(askNumberToUser("Ingrese año de creación"));

        painting.setExhibitionGallery(gallery);
        System.out.println("Agregado a la galería: " + gallery.getName());

        System.out.println("Cuadro registrado con éxito.\n");
        System.out.println("Presione Enter para continuar...");
        scanner.nextLine();
    }

    private void addEvaluationAction() {
        System.out.println("addEvaluationAction");
    }

    private void scoreResultsAction() {
        System.out.println("scoreResultsAction");
    }

    private void exitAction() {
       shouldExit = true;
    }

    private void invalidSelectionAction() {
        System.out.println("Opción inválida. Intente nuevamente.");
    }

    private String askUserSelection() {
        String message = "Seleccione una opción: ";
        System.out.println(message);
        return scanner.next();
    }

    private boolean exitRequested() {
        return shouldExit;
    }
}
