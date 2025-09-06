package org.example;

public class EntryPoint {
    public static void main(String[] args) {
        DuocBank duocBank = new DuocBank();
        Atm machine1 = new Atm(100_000);

        machine1.setWelcome(duocBank.header);
        machine1.setActions(duocBank.actions);

        machine1.run();
    }
}