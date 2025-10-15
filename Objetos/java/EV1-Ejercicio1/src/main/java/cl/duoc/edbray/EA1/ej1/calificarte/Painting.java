package cl.duoc.edbray.EA1.ej1.calificarte;

public class Painting {
    private String uniqueCode;
    private String title;
    private String author;
    private int creationYear;
    private Gallery exhibitionGallery;

    public Painting() {}

    public Painting(
            String uniqueCode,
            String title,
            String author,
            int creationYear,
            Gallery exhibitionGallery
    ) {
        this.uniqueCode = uniqueCode;
        this.title = title;
        this.author = author;
        this.creationYear = creationYear;
        this.exhibitionGallery = exhibitionGallery;
    }

    public String getUniqueCode() {
        return uniqueCode;
    }

    public void setUniqueCode(String uniqueCode) {
        this.uniqueCode = uniqueCode;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public int getCreationYear() {
        return creationYear;
    }

    public void setCreationYear(int creationYear) {
        this.creationYear = creationYear;
    }

    public Gallery getExhibitionGallery() {
        return exhibitionGallery;
    }

    public void setExhibitionGallery(Gallery exhibitionGallery) {
        this.exhibitionGallery = exhibitionGallery;
    }
}
