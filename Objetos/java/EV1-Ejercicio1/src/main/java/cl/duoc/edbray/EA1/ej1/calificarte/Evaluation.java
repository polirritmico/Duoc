package cl.duoc.edbray.EA1.ej1.calificarte;

import java.util.Objects;

public class Evaluation {
    private final int requiredExhibitionScore;
    private final int minScore;
    private final int maxScore;

    private Painting painting;
    private Critic critic;
    private Integer score;

    public Evaluation() {
        this(40, 0, 70);
    }

    public Evaluation(int requiredExhibitionScore, int minScore, int maxScore) {
        this.requiredExhibitionScore = requiredExhibitionScore;
        this.minScore = minScore;
        this.maxScore = maxScore;
    }

    public void setPainting(Painting painting) {
        this.painting = painting;
    }

    // To fulfill the requirement specs
    public String getPaintingCode() {
        if (painting == null) {
            return "PAINTING NOT SET";
        }
        return painting.getUniqueCode();
    }

    public void setCritic(Critic critic) {
        if (!Objects.equals(this.critic, critic)) {
            this.score = null;
        }
        this.critic = critic;
    }

    // To fulfill the requirement specs
    public String getCriticRut() {
        if (critic == null) {
            return "CRITIC NOT SET";
        }
        return critic.getRut();
    }

    public int getScore() {
        return this.score;
    }

    private boolean isValidScoreValue(int score) {
        return (score <= maxScore && score >= minScore);
    }

    public boolean setScore(int score) {
        if (!this.isValidScoreValue(score)) {
            return false;
        }
        this.score = score;
        return true;
    }

    public boolean paintingMeetExhibitionCriteria() {
        return score >= requiredExhibitionScore;
    }
}
