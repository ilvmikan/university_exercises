package cofre_de_moedas;

import java.util.ArrayList;
import java.util.List;

class Cofrinho {
    private List<Moeda> listaMoedas;

    public Cofrinho() {
        listaMoedas = new ArrayList<>();
    }

    public List<Moeda> getListaMoedas() {
        return listaMoedas;
    }
    
    public double calcularValorTotalEmReal() {
        double total = 0;

        for (Moeda moeda : listaMoedas) {
            total += moeda.converter();
        }
		return total;

    }
    
    public void adicionarMoeda(Moeda moeda_nova) {
        listaMoedas.add(moeda_nova);
    }
    
    public void listar() {
        System.out.println("Moedas do cofrinho:");
        for (int i = 0; i < listaMoedas.size(); i++) {
            Moeda moeda = listaMoedas.get(i);
            System.out.printf("%d ", i);
            moeda.info();
        }
    }

    public void remover(Moeda moeda) {
        listaMoedas.remove(moeda);
    }


}
