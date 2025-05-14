print("Nome: Gabriel de Souza Novais")
print("RU: 4323456")

class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        elif self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == "A":
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").strip().upper()
        numero = int(input("Digite o número do cartão: "))
        novo_nodo = Nodo(numero, cor)
        
        if self.head is None:
            self.head = novo_nodo
        elif cor == "V":
            self.inserirSemPrioridade(novo_nodo)
        elif cor == "A":
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        atual = self.head
        while atual is not None:
            print(f"Cartão: {atual.numero}, Cor: {atual.cor}")
            atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Não há pacientes na fila.")
        else:
            print(f"Atendendo paciente com cartão cor {self.head.cor} e número {self.head.numero}")
            self.head = self.head.proximo

def menu():
    lista = ListaEncadeadaSimples()

    while True:
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        
        opcao = input(">> ").strip()

        if opcao == '1':
            lista.inserir()
        elif opcao == '2':
            lista.imprimirListaEspera()
        elif opcao == '3':
            lista.atenderPaciente()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor escolha uma opção válida.")

if __name__ == "__main__":
    menu()

