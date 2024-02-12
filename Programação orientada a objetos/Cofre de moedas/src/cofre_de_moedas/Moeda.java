package cofre_de_moedas;

abstract class Moeda {
    protected double valor;

    public Moeda(double valor) {
        this.valor = valor;
    }

    public abstract double converter();
    public abstract void info();
}