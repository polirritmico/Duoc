package org.polirritmico.calificarte;

import org.polirritmico.calificarte.actions.Action;

import java.util.*;

public class Menu {
    private Map<Integer, Action> entriesAction = new HashMap<>();
    private Map<Integer, String> entriesMenu = new LinkedHashMap<>();
    private String header = "Header not set";
    private int currentSelection = 0;
    private int entryId = 1;
    private int lastEntry = 0;

    public Action getSelectedEntry() {
        return this.entriesAction.get(this.currentSelection);
    }

    private int getNewEntryId() {
        int newId = this.entryId;
        this.entryId += 1;
        return newId;
    }

    private String capitalize(String str) {
        if (str == null || str.isBlank()) {
            return str;
        }
        String res = str.substring(0, 1).toUpperCase();
        res += str.substring(1).toLowerCase();
        return res;
    }

    private String formatEntry(String entry, int id) {
        String res = this.capitalize(entry);
        res = res.endsWith(".") ? res : res + ".";
        res = id + ". " + res;
        return res;
    }

    public void addMenuEntry(Action action) {
        int id = this.getNewEntryId();
        String entry = this.formatEntry(action.getMenuEntry(), id);

        this.entriesAction.put(id, action);
        this.entriesMenu.put(id, entry);
    }

    public void setHeader(String header) {
        this.header = header;
    }

    public void setMenuActions(Action[] actions) {
        for (Action action : actions) {
            this.addMenuEntry(action);
            this.lastEntry++;
        }
    }

    public List<String> build() {
        List<String> menu = new ArrayList<String>();
        menu.add("");
        menu.add(this.header);
        menu.addAll(this.entriesMenu.values());
        menu.add("");
        return menu;
    }

    public void show() {
        for (String line : this.build()) {
            System.out.println(line);
        }
    }

    public void setCurrentSelection(int selection) {
        if (selection < 0 || selection > this.lastEntry) {
            throw new IllegalArgumentException(
                    "Invalid selection value. Should be between 0 and "
                            + this.lastEntry + ". Got " + selection + "."
            );
        }
        this.currentSelection = selection;
    }

    public int askUserSelection() {
        return this.askUserSelection(null, null,null);
    }

    public int askUserSelection(String message, String errorMessage, Scanner scanner) {
        if (message == null || message.isBlank()) {
            message = "Ingrese una opción: ";
        }
        if (errorMessage == null || errorMessage.isBlank()) {
            errorMessage = "¡Debe seleccionar una opción válida!";
        }
        if (scanner == null) {
            scanner = new Scanner(System.in);
        }

        while (true) {
            System.out.print(message);
            String userInputRaw = scanner.nextLine().trim();

            if (userInputRaw.isBlank()) {
                System.out.println(errorMessage);
                continue;
            }

            boolean isDigit = !userInputRaw.chars().allMatch(Character::isDigit);
            if (!isDigit) {
                System.out.println(errorMessage);
                continue;
            }

            int userInput = Integer.parseInt(userInputRaw);
            if (userInput < 1 || userInput > lastEntry) {
                System.out.println(errorMessage);
                continue;
            }

            System.out.println();
            this.setCurrentSelection(userInput);
            return userInput;
        }
    }
}
