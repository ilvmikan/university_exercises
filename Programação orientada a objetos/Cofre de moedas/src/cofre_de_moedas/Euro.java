package cofre_de_moedas;

class Euro extends Moeda {
	private static final double TAXA_DE_CAMBIO = 5.38;
    public Euro(double valor) {
        super(valor);
    }
    
    @Override
    public double converter() {
        return valor * TAXA_DE_CAMBIO;
    }
    
    @Override
    public void info() {
        System.out.println("Euro: " + valor);
    }
}
