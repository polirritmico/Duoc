package org.polirritmico.calificarte.actions;

public class FooAction implements Action {
    @Override
    public String getMenuEntry() {
        return "This is the Foo action";
    }

    @Override
    public void run() {
        System.out.println("Run foo");
    }
}
