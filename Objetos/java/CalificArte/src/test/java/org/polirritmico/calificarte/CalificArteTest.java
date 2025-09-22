package org.polirritmico.calificarte;

import org.junit.Test;
import org.polirritmico.calificarte.actions.Action;
import org.polirritmico.calificarte.actions.FooAction;

import static org.junit.Assert.assertEquals;

public class CalificArteTest {
    @Test
    public void ShouldRegisterActionAndShowMenu() {
        Action caseAction = new FooAction();
        String expected = "This is the Foo action";

        String output = caseAction.getMenuEntry();

        assertEquals(expected, output);
    }
}