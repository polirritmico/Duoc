package org.example;

public class Action {
    private final String name;
    private final Runnable action;

    public Action(String name, Runnable action) {
        this.name = name;
        this.action = action;
    }

    public void run() {
        action.run();
    }

    public String getName() {
        return name;
    }
}
