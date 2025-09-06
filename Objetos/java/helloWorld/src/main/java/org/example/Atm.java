package org.example;

public class Atm {
    private Int money;
    private String welcomeMessage;

    public Atm(Int startingMoneyAmount) {
        this.money = startingMoneyAmount;
    }

    public void setWelcome(String welcomeMessage) {
        this.welcomeMessage = welcomeMessage;
    }

    public void showMenu() {
        System.out.println("Menu");
        System.out.println(String.format("Money: %d", money));
    }

    public void run() {

    }
}
