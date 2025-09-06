package cl.duoc.foo;

import cl.duoc.foo.cartesian.Point;

public class POO {
    public static void main(String[] args) {
        Point p = new Point();
        String msg = String.format("x = %d, y = %d", p.getX(), p.getY());
        System.out.println(msg);

        Point p = new Point();
        p.setX(10);
        p.setY(15);
        double x = p.getX();
        double y = p.getY();
        String mensaje = String.format("x = &s, y = %d", x, y);
        System.out.println(mensaje);

        Point b = new Point();
        p.setX(10);
        p.setY(15);
        double result = p.calculateDistance(b);
    }
}
