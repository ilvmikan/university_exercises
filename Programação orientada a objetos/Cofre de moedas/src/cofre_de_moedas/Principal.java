package cofre_de_moedas;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Principal {
	
    private static final int OP_ADICIONAR_MOEDA = 0;
    private static final int OP_REMOVER_MOEDA = 1;
    private static final int OP_LISTAR_MOEDAS = 2;
    private static final int OP_CALCULAR_TOTAL = 3;
    private static final int OP_ENCERRAR = 4;

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        Cofrinho cofrinho = new Cofrinho();

        int input = 0;

        while (input != OP_ENCERRAR) {
            exibir_menu();
            
            while(!teclado.hasNextInt()) {
            	System.out.println("Por favor, digite um numero valido");
            	teclado.next();
            }
            
        	input = teclado.nextInt();
        	System.out.println(">> " + input);
            
            switch (input) {
                case OP_ADICIONAR_MOEDA:
                    adicionar_moeda(teclado, cofrinho);
                    break;

                case OP_REMOVER_MOEDA:
                    remover_moeda(teclado, cofrinho);
                    break;

                case OP_LISTAR_MOEDAS:
                    cofrinho.listar();
                    break;

                case OP_CALCULAR_TOTAL:
                    double convertido = cofrinho.calcularValorTotalEmReal();
                    System.out.printf("Total convertido para REAL: %.2f\n", convertido);
                    break;
                
                case OP_ENCERRAR:
                    System.out.println("encerrando...");
                    break;
                   
                default:
                    System.out.println("Digite uma opcao valida!!!");
                    break;
            }
        }
        teclado.close();
    }

    private static void exibir_menu() {
        System.out.println("----- Menu -----");
        System.out.println(OP_ADICIONAR_MOEDA + " - Adicionar moeda");
        System.out.println(OP_REMOVER_MOEDA + " - remover moeda");
        System.out.println(OP_LISTAR_MOEDAS + " - Listar moedas");
        System.out.println(OP_CALCULAR_TOTAL + " - Calcular o total para ser convertido para real");
        System.out.println(OP_ENCERRAR + " - sair");
        System.out.print(">> ");
    }

    private static void adicionar_moeda(Scanner teclado, Cofrinho cofrinho) {
        double valor;
        int opcao_escolhida;

        System.out.println("Qual moeda voce deseja adicionar?");
        System.out.println(">> 1 - dolar");
        System.out.println(">> 2 - Euro");
        System.out.println(">> 3 - Real");
        opcao_escolhida = teclado.nextInt();

        System.out.print("Digite o valor da moeda >> ");
        valor = teclado.nextDouble();

        Moeda moeda_nova;
        switch (opcao_escolhida) {
            case 1:
                moeda_nova = new Dolar(valor);
                break;
            case 2:
                moeda_nova = new Euro(valor);
                break;
            case 3:
                moeda_nova = new Real(valor);
                break;
            default:
                System.out.println("Voce escolheu uma opcao invalida!!!!!!");
                return;
        }

        cofrinho.adicionarMoeda(moeda_nova);
        System.out.println("A moeda foi adicionada com sucesso!!!");
    }

    private static void remover_moeda(Scanner teclado, Cofrinho cofrinho) {
        System.out.println("Por favor, digite o número da moeda que deseja remover (primeira coluna):");
        cofrinho.listar();
        System.out.print(">> ");

        int tamanhoListaMoedas = cofrinho.getListaMoedas().size();
        int moedaRemover = obterMoeda(teclado, tamanhoListaMoedas);

        if (moedaRemover >= 0 && moedaRemover < tamanhoListaMoedas) {
            Moeda moeda = cofrinho.getListaMoedas().get(moedaRemover);
            cofrinho.remover(moeda);
            System.out.println("Moeda removida com sucesso!");
        } else {
            System.out.println("Opção inválida!");
        }
    }

    private static int obterMoeda(Scanner teclado, int tamanhoListaMoedas) {
        try {
            return teclado.nextInt();
        } catch (InputMismatchException e) {
            System.out.println("Digite um numero valido!!!");
            teclado.next();
            return obterMoeda(teclado, tamanhoListaMoedas); 
        }
    }
}