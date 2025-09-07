package org.polirritmico.demo_atm;

import org.polirritmico.atm.ATM;
import org.polirritmico.atm.ATMState;
import org.polirritmico.atm.CashHandler;
import org.polirritmico.atm.state.NoCard;

public class DemoATM {
    private ATM atm;

    public void run() {
        CashHandler cashHandler = new CashHandler();
        ATMState defaultState = new NoCard();

        atm = new ATM(cashHandler, defaultState);
    }
}
