public class App {
    public static void main(String[] args) throws Exception {

        String cadena = "EstoesunaCadenaDeCaracteres";
        int longitud = 0;

        longitud = cadena.length();
        System.out.println("La longitud de la cadena es: " + longitud); // 27
        System.out.println("Indice de caracter t: " + cadena.indexOf('t')); // 2
        // System.out.println("Posicion del caracter '2': " + cadena.charAt(index:2));
        // //t

        System.out.println("Devuelve la sub-cadena desde la posicion1 hata 9:  " + cadena.substring(1, 9)); // stoesuna

        System.out.println("Devuelve la cadena convertida en mayuscula: " + cadena.toUpperCase()); // ESTOESUNACADENADECARACTERES

        System.out.println("Devuelve la cadena convertida en minuscula: " + cadena.toLowerCase()); // estoesunacadenadecaracteres

        System.out.println("Elimina los espacios al inicio y final de una cadena de caracteres " + cadena.trim());// EstoesunaCadenaDeCaracteres

    }
}
