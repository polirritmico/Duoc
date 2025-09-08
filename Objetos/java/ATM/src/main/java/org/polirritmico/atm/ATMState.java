package org.polirritmico.atm;

import java.util.ArrayList;
import org.polirritmico.atm.Action;
import org.polirritmico.atm.ATMState;

public interface ATMState {
    void handleInput(Integer input);
    void setMenu(ArrayList<Action> actions);
    void showMenu();

    ATMState nextState(String input);
    ATMState canTransitionTo(String input);

    default void onEnter() {};
    default void onExit() {};
}
