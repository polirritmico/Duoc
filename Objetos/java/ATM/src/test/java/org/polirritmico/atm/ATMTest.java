package org.polirritmico.atm;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import java.util.Map;

import org.polirritmico.atm.state.NoCard;

public class ATMTest {
    @Test
    void testInitialBalanceCount() {
        int expected = 50_000;
        Map<Integer, Integer> testCase = Map.of (
                20_000, 1,
                10_000, 2,
                5_000, 2
        );

        CashHandler pesosHandler = new CashHandler();
        pesosHandler.setCash(testCase);
        ATMState defaultState = new NoCard();
        ATM atm = new ATM(pesosHandler, defaultState);
        int output = atm.getCashAmount();

        Assertions.assertEquals(expected, output);
    }

    @Test
    void testWithdrawCash() {
        Integer testCase = 40_000;
        Map<Integer, Integer> testCash = Map.of(20_000: 2);
        Map<Integer, Integer> expected = Map.of(20_000, 0);

        CashHandler pesosHandler = new CashHandler();
        pesosHandler.setCash(testCash);
        ATMState defaultState = new StandBy();
        ATM atm = new ATM(pesosHandler, defaultState);

        Assertions.assertEquals(expected, output);
    }
}
