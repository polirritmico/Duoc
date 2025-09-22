package org.polirritmico.calificarte.actions;

public class ExitAction implements Action {
    @Override
    public void run() {
        System.exit(0);
    }

    @Override
    public String getMenuEntry() {
        return "Salir";
    }
}
