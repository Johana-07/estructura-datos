public class App {
    public static void main(String[] args) throws Exception {
        BecaUniversitaria becaUniversitaria = new BecaUniversitaria();
        System.out.println(becaUniversitaria.calcularInteresSimple());
        System.out.println(becaUniversitaria.calcularInteresCompuesto());
        System.out.println(becaUniversitaria.compararInversion(60, 13000, 1.4));

        BecaUniversitaria becaUniversitaria2 = new BecaUniversitaria(48, 10000, 2.0);
        System.out.println(becaUniversitaria2.calcularInteresSimple());
        System.out.println(becaUniversitaria2.calcularInteresCompuesto());
        System.out.println(becaUniversitaria2.compararInversion());

        BecaUniversitaria becaUniversitaria3 = new BecaUniversitaria();
        System.out.println(becaUniversitaria3.calcularInteresSimple());
        System.out.println(becaUniversitaria3.calcularInteresCompuesto());
        System.out.println(becaUniversitaria3.compararInversion());
    }
}

class BecaUniversitaria {

    // -----------------------------------------------------
    // Atributos
    // -----------------------------------------------------

    // Valor del tiempo
    private int tiempo;

    // Valor de la Beca Universitaria
    private double monto;

    // Tasa de interes efectiva mensual del proyecto
    private double interes;

    // -----------------------------------------------------
    // Constructores de la clase
    // -----------------------------------------------------

    /*
     * Construye el proyecto
     * Se crea un nuevo proyefcto con los siguientes valores
     */
    public BecaUniversitaria() {
        tiempo = 0;
        monto = 0;
        interes = 0;
    }

    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres) {
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;
    }

    // -----------------------------------------------------
    // Metodos
    // -----------------------------------------------------

    // -----------------------------------------------------
    // Retorna el interes simple, monto ,capital en una cadena de texto
    // @return el total de interes simple generado en un numero
    // -----------------------------------------------------

    public double calcularInteresSimple() {
        double interesSimple = monto * (interes / 100) * tiempo;
        return Math.round(interesSimple);
    }

    // -----------------------------------------------------
    // Retorna el interes compuesto, monto ,capital en una cadena de texto
    // @return el total de interes completo generado en un numero
    // -----------------------------------------------------
    public double calcularInteresCompuesto() {
        double interesCompuesto = monto * (Math.pow(1 + interes / 100, tiempo) - 1);
        return Math.round(interesCompuesto);
    }

    // Metodo para comparar la diferencia en el total de intereses genrados para el
    // @param pTiempo
    // @param pMonto
    // @param pMonto
    // @return Respuesta al reto 1

    public String compararInversion(int pTiempo, double pMonto, double pInteres) {
        this.tiempo = pTiempo;
        this.monto = pMonto;
        this.interes = pInteres;

        // Calculo de la diferencia entre los tios de intereses
        double diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        if (diferencia != 0) {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

    public String compararInversion() {
        double diferencia = 0;

        // Calcular la diferencia entre tipo de intereses
        diferencia = calcularInteresCompuesto() - calcularInteresSimple();

        // Revisar la diferencia obtenida
        if (diferencia != 0) {
            return "La diferencia entre la proyección de interés compuesto e interés simple es: $" + diferencia;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

}