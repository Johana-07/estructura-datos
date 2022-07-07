package co.utp.misiontic2022.c2;

public final class MiPrimerClase {
    // Atributos
    private static final Double PI = 3.1416;
    private Integer contador;
    private Integer numHoras;

    // Constructor
    public MiPrimerClase() {
        contador = 0;
    }

    public MiPrimerClase(Integer contador) {
        this.contador = contador;
    }

    public MiPrimerClase(Integer contador, Integer numHoras) {
        this.contador = contador;
        this.numHoras = numHoras;
    }

    // Métodos

    // método para incrementar el atributo contador
    public void incrementarContador(Integer contador) {
        this.contador += contador;
    }

    // método para visualizar el valor del atributo contador
    public Integer getContador() {
        return contador;
    }

    // método para asignar un valor al atributo contador
    public void setContador(Integer contador) {
        this.contador = contador;
    }

    public Integer getNumHoras() {
        return numHoras;
    }

    public void setNumHoras(Integer numHoras) {
        this.numHoras = numHoras;
    }
}