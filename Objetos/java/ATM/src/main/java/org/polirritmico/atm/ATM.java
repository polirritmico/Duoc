package org.polirritmico.atm;

import org.polirritmico.atm.state.NoCard;

public class ATM {
    CashHandler cash;
    ATMState currentState;

    public ATM(CashHandler cashHandler, ATMState currentState) {
        this.cash = cashHandler;
        this.currentState = currentState;
    }

    public void setDefaultState() {
        this.setState();
    }

    public void setState() {
        this.currentState = new NoCard();
    }

    public void setState(ATMState newState) {
        this.currentState = newState;
    }
}
