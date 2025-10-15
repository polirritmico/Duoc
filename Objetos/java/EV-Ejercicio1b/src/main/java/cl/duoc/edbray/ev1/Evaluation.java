package cl.duoc.edbray.ev1;

public class Evaluation {
    private Painting painting;
    private Critic critic;
    private Integer score;
    private final int minimumScoreForExhibition = 40;

    public Evaluation() {
    }

    public Evaluation(Painting painting, Critic critic, int score) {
        this.painting = painting;
        this.critic = critic;
        this.score = score;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public Critic getCritic() {
        return critic;
    }

    public void setCritic(Critic critic) {
        this.critic = critic;
    }

    public Painting getPainting() {
        return painting;
    }

    public void setPainting(Painting painting) {
        this.painting = painting;
    }

    public boolean shouldBeExhibited() {
        return score != null && score >= minimumScoreForExhibition;
    }

}
