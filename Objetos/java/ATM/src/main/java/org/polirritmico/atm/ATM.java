package org.polirritmico.atm;

public class ATM {
    CashHandler cash;
    ATMState currentState;

    public ATM(CashHandler cashHandler, ATMState currentState) {
        this.cash = cashHandler;
        this.currentState = currentState;
    }

    public void handleInput(Integer input) {
        this.currentState.handleInput(input);
    }

    public void setState(ATMState newState) {
        this.currentState = newState;
    }

    public int getCashAmount() {
        return this.cash.getAmount();
    }
}
