package org.polirritmico.atm;

public class Action {
    private String name = "Unset name";
    private Function run;

    public void setFunction(Function func) {
        this.run = func;
    }
}
