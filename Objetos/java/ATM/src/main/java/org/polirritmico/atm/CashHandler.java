package org.polirritmico.atm;

import java.util.Map;

public class CashHandler {
    private Map<Integer, Integer> cash;

    public void setCash(Map<Integer, Integer> initialCash) {
        this.cash = initialCash;
    }

    public Integer getAmount() {
        int res = 0;
        for (Integer denomination: cash.keySet()) {
            res += denomination * this.cash.get(denomination);
        }
        return res;
    }

    public boolean validateWithdraw(int amount) {
        return false;
    }

    public void withdraw(int amount) {

    }
}
