def quick_sort(dados, inicio, fim) -> None:
    if inicio < fim:
        posicao_de_particionamento = particionar(dados, inicio, fim)
        quick_sort(dados, inicio, posicao_de_particionamento - 1)
        quick_sort(dados, posicao_de_particionamento + 1, fim)

def particionar(dados, inicio, fim) -> int:
    pivo = dados[inicio]
    esquerda = inicio + 1
    direita = fim
    concluido = False
    while not concluido:
        while esquerda <= direita and dados[esquerda] <= pivo:
            esquerda = esquerda + 1
        while dados[direita] >= pivo and direita >= esquerda:
            direita = direita - 1
        if direita < esquerda:
            concluido = True
        else:
            elemento_temporario = dados[esquerda]
            dados[esquerda] = dados[direita]
            dados[direita] = elemento_temporario
    elemento_temporario = dados[inicio]
    dados[inicio] = dados[direita]
    dados[direita] = elemento_temporario
    return direita

dados = [1, 5, 9, 23, 45, 3, 222]
quick_sort(dados, 0, len(dados)-1)
print(dados)


