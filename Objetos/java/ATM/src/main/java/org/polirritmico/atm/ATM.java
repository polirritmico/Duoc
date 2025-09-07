package org.polirritmico.atm;

public class ATM {
    CashHandler cash;
    ATMState currentState;

    public ATM(CashHandler cashHandler, ATMState currentState) {
        this.cash = cashHandler;
        this.currentState = currentState;
    }

    public void setState(ATMState newState) {
        this.currentState = newState;
    }
}
