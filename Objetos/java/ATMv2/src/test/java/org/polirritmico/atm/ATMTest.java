package org.polirritmico.atm;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.function.Function;

import org.polirritmico.atm.ATM;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

public class ATMTest {
    @Test
    public void getMenuShouldReturnNonEmptyString() {
        ATM atm = new ATM();
        String output = atm.getMenu();
        assertNotEquals("", output);
    }

    @Test
    public void ShouldReturnSameEntriesAsActions() {
        List<Runnable> actions = List.of(
                arg -> "foo",
                arg -> "bar",
        );
        ATM atm = new ATM();
        atm.setActions(actions);
    }
}
