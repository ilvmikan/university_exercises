package cofre_de_moedas;

class Dolar extends Moeda {

	private static final double TAXA_DE_CAMBIO = 4.79;
	
    public Dolar(double valor) {
        super(valor);
    }

    @Override
    public void info() {
        System.out.println("Dólar: " + valor);
    }

    //
    @Override
    public double converter() {
        return valor * TAXA_DE_CAMBIO;
    }
}
