package org.polirritmico.atm.state;

import org.polirritmico.atm.ATMState;
import org.polirritmico.atm.Action;

import java.util.ArrayList;

public class NoCard implements ATMState {
    public void handleInput(Integer input) {

    }

    public void setMenu(ArrayList<Action> actions) {

    }

    public void showMenu() {

    }

    public ATMState nextState(String input) {
        return null;
    }

    public ATMState canTransitionTo(String input) {
        return null;
    }

    public void onEnter() {
        ATMState.super.onEnter();
    }

    public void onExit() {
        ATMState.super.onExit();
    }
}
