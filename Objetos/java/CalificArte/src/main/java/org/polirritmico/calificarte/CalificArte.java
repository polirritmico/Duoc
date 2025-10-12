package org.polirritmico.calificarte;

import org.polirritmico.calificarte.actions.Action;

import java.util.ArrayList;
import java.util.List;

public class CalificArte {
    private List<Action> actions = new ArrayList<>();
    private Menu menu;


    private void createMenu() {
        this.menu = new Menu();
        this.menu.setHeader("=== SISTEMA DE REGISTRO DE CUADROS Y EVALUACIONES ===");
    }

    public void setup() {
        this.createMenu();
    }

    private boolean closing() {
        return false;
    };

    public void run() {
        boolean shouldExit = false;
        int userSelection = 0;
        while (true) {
            this.menu.show();
            userSelection = this.menu.askUserSelection();
        }
    }
}
