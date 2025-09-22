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

    public void run() {
        this.createMenu();
    }
}
