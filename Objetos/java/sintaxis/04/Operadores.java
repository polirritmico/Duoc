public class Operadores {
    public static void main(String[] args) {
        // Operadores

        // Aritméticos: +, -, *, /, %
        int a = 10 + 5;
        int b = 10 - 5;
        int c = 10 * 5;
        int d = 10 / 5;
        int e = 10 % 5;

        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("c = " + c);
        System.out.println("d = " + d);
        System.out.println("e = " + e);

        String format = String.format(
            "a = %d, b = %d, b = %d, c = %d, e = %d", a, b, c, d, e
        );
        System.out.println(format);

        // Operadores de comparación: <, >, ==, <=, >=, != para primitivos
        // retornan un valor booleano
        boolean esMenor = a < b;
        boolean esMayor = a > b;
        boolean esIgual = a == b;
        boolean esMenorIgual = a <= b;
        boolean esMayorIgual = a >= b;
        boolean esDistinto = a != b;

        System.out.println("esMenor = a < b" + esMenor);
        System.out.println("esMayor = a > b" + esMayor);
        System.out.println("esIgual = a == b" + esIgual);
        System.out.println("esMenorIgual = a <= b" + esMenorIgual);
        System.out.println("esMayorIgual = a >= b" + esMayorIgual);
        System.out.println("esDistinto = a != b" + esDistinto);

        // Operadores lógicos: ||, &&, !
        boolean esMayorOIgual = esMayor || esIgual;
        boolean esMayorEIgual = esMayor && esIgual;
        boolean esMayorODistinto = esMayor || esDistinto;
        boolean esMayorYDistinto = esMayor && esDistinto;

        System.out.println("esMayorOIgual = esMayor || esIgual = " + esMayorOIgual);
        System.out.println("esMayorEIgual = esMayor && esIgual = " + esMayorEIgual);
        System.out.println("esMayorODistinto = esMayor || esDistinto = " + esMayorODistinto);
        System.out.println("esMayorYDistinto = esMayor && esDistinto = " + esMayorYDistinto);
    }
}
