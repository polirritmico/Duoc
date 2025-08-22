public class SentenciasControl {
    public static void main(String[] args) {
        System.out.println("Sentencias de control");

        int a = 5;
        int b = 10;

        if (a > b) { // los bloques no llevan ;
            System.out.println("a es mayor que b");
        }

        if (a < b) {
            System.out.println("a es menor que b");
        }

        int c = 20;
        int d = 15;

        if (c > d) {
            System.out.println("c es mayor que d");
        } else if (c < d) {
            System.out.println("c es menor que d");
        } else {
            System.out.println("c es igual a d");
        }
    }
}
