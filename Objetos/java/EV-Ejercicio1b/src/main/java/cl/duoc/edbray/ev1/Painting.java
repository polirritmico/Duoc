package cl.duoc.edbray.ev1;

public class Painting {
    private String uniqueCode;
    private String title;
    private String author;
    private String creationYear;

    public Painting() {}

    public Painting(
            String uniqueCode,
            String title,
            String author,
            String creationYear,
            Gallery gallery
    ) {
        this.uniqueCode = uniqueCode;
        this.title = title;
        this.author = author;
        this.creationYear = creationYear;
        this.gallery = gallery;
    }

    public Gallery getGallery() {
        return gallery;
    }

    public void setGallery(Gallery gallery) {
        this.gallery = gallery;
    }

    public String getCreationYear() {
        return creationYear;
    }

    public void setCreationYear(String creationYear) {
        this.creationYear = creationYear;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getUniqueCode() {
        return uniqueCode;
    }

    public void setUniqueCode(String uniqueCode) {
        this.uniqueCode = uniqueCode;
    }

    private Gallery gallery;
}
