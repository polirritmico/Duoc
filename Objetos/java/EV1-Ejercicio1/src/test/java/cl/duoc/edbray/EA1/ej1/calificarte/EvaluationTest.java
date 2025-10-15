package cl.duoc.edbray.EA1.ej1.calificarte;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class EvaluationTest {
    @Test
    void shouldMeetExhibitionCriteriaIfScoreIsFulfilled() {
        int caseCriteria = 40;
        int caseScore = 40;
        boolean expected = true;

        Evaluation evaluation = new Evaluation();
        evaluation.setCriteria(caseCriteria);
        evaluation.setScore(caseScore);
    }
}