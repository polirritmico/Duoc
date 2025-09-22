package org.polirritmico.calificarte;

import org.junit.jupiter.api.Test;
import org.polirritmico.calificarte.actions.Action;
import org.polirritmico.calificarte.actions.FooAction;

import static org.junit.jupiter.api.Assertions.assertEquals;

class MenuTest {
    @Test
    void ShouldAddFormatedEntry() {
        Action caseAction = new FooAction();
        int caseLineNr = 3; // 0 empty, 1 header, 2 first action, etc.
        String expected = "2. This is the foo action.";

        Menu menu = new Menu();
        menu.addMenuEntry(caseAction);
        menu.addMenuEntry(caseAction);

        String output = menu.build().get(caseLineNr);
        assertEquals(expected, output);
    }

}