
/*
Programa que lea dos variables enteras n y m y  le quite a n sus m ultimas cifras
Ejemplo : si n= 12345678 y m = 3 el nuevo valor de n es 12345
 */
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        /*
         * int n;
         * int m;
         * int d;
         */

        int n, m, d;
        System.out.println("Por favor , ingrese el numero n: ");
        n = sc.nextInt();

        System.out.println("Por favor , ingrese el numero m: ");
        m = sc.nextInt();

        d = (int) Math.pow(10, m);
        n = n / d;

        System.out.println("Numero Modificado: " + n);

    }
}
