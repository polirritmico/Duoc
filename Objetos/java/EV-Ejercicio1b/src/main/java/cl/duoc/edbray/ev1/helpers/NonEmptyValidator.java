package cl.duoc.edbray.ev1.helpers;

public class NonEmptyValidator {
    public static boolean check(String arg) {
        if (arg == null || arg.isBlank()) {
            return false;
        }
        return true;
    }
}
