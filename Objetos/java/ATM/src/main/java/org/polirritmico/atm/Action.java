package org.polirritmico.atm;

import java.util.function.Function;

public class Action {
    private String name = "Unset name";
    private Function run;

    public void setFunction(Function func) {
        this.run = func;
    }
}
