"""
    Linked list
        - Dados esparsos na memória
        - Nó/Nodo
        - Ponteiros
        - Head [HEAD == 4 -> 15 -> 7 -> 40 -> NULL POINTER]
        - Dinâmica
        - Não disperdiça memória
"""

class ElementoDaListaSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __repr__(self):
        return self.dado

class Linked_list:
    def __init__(self, node = None):
        self.head = None
        if node is not None:
            node = ElementoDaListaSimples(dado=elem)
            node = node.proximo

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.dado)
            node = node.proximo
        nodes.append("None")
        return " -> ".join(nodes)

teste = ListaEncadeadaSimples()

