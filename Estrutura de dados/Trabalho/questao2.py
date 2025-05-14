print("Nome: Gabriel de Souza Novais")
print("RU: 4323456")

class Node:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class HashTable:
    def __init__(self):
        self.tabela = [None] * 10 

    def hash_function(self, sigla):
        if sigla == "DF":
            return 7
        else:
            ascii1 = ord(sigla[0])
            ascii2 = ord(sigla[1])
            return (ascii1 + ascii2) % 10

    def insert_to_head(self, pos, nodo):
        nodo.proximo = self.tabela[pos]
        self.tabela[pos] = nodo

    def print_table(self):
        for i in range(len(self.tabela)):
            print(f"{i}: ", end="")
            nodo = self.tabela[i]
            while nodo is not None:
                print(f"{nodo.sigla} -> ", end="")
                nodo = nodo.proximo
            print("None")

    def insert_states(self):
        estados = [
            ("AC", "Acre"),
            ("AL", "Alagoas"),
            ("AM", "Amazonas"),
            ("AP", "Amapá"),
            ("BA", "Bahia"),
            ("CE", "Ceará"),
            ("DF", "Distrito Federal"), 
            ("ES", "Espírito Santo"),
            ("GO", "Goiás"),
            ("MA", "Maranhão"),
            ("MT", "Mato Grosso"),
            ("MS", "Mato Grosso do Sul"),
            ("MG", "Minas Gerais"),
            ("PA", "Pará"),
            ("PB", "Paraíba"),
            ("PR", "Paraná"),
            ("PE", "Pernambuco"),
            ("PI", "Piauí"),
            ("RJ", "Rio de Janeiro"),
            ("RN", "Rio Grande do Norte"),
            ("RO", "Rondônia"),
            ("RR", "Roraima"),
            ("SC", "Santa Catarina"),
            ("RS", "Rio Grande do Sul"),
            ("SE", "Sergipe"),
            ("SP", "São Paulo"),
            ("TO", "Tocantins"),
        ]

        for sigla, nome in estados:
            nodo = Node(sigla, nome)
            pos = self.hash_function(sigla)
            self.insert_to_head(pos, nodo)

    def insert_fictitious(self):
        estado_ficticio = ("BK", "Bruno Kostiuk")
        nodo_ficticio = Node(estado_ficticio[0], estado_ficticio[1])
        pos_ficticio = self.hash_function(estado_ficticio[0])
        self.insert_to_head(pos_ficticio, nodo_ficticio)

def start():
    hash_table = HashTable()

    print("antes de inserir qualquer informação:")
    hash_table.print_table()

    hash_table.insert_states()

    print("\napós inserir os 26 estados e o DF:")
    hash_table.print_table()

    hash_table.insert_fictitious()

    print("\napós inserir os 26 estados, DF e o estado fictício:")
    hash_table.print_table()

if __name__ == "__main__":
    start()
