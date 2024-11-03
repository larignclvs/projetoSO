def opt(tam_mem, seq_pages):
    # Converte a sequência de páginas de string para uma lista de inteiros
    seq_pages = [int(x) for x in seq_pages.split(",")]

    # Memória começa vazia 
    memoria = [-1] * tam_mem  # Inicializa a memória com -1
    hit, miss = 0, 0  # Inicializa as contagens de hits e misses

    # Lendo sequência de páginas que foi dada
    for i, pagina in enumerate(seq_pages):
        print(f"page: {pagina}")

        # Verificando estado da memória
        # Se já estiver na memória, é um hit!
        if pagina in memoria:
            hit += 1
            hit_miss = "(hit)"
        else:  # É um miss
            miss += 1
            hit_miss = "(miss)"
            if -1 in memoria:  # Se houver espaço, adiciona
                primeiro_vazio = memoria.index(-1)  # Primeiro lugar da memória
                memoria[primeiro_vazio] = pagina  # Colocando a página naquele lugar da memória
            else:  # Se a memória estiver cheia, realizar o OPT
                distancias = []  # Criando lista de distâncias

                # Percorrendo a memória
                for pag_mem in memoria:
                    if pag_mem in seq_pages[i + 1:]:  # Se a página na memória está no restante da lista
                        dist = seq_pages[i + 1:].index(pag_mem)  # Pega a distância = índice
                    else:  # Se não tiver, então não será solicitada mais
                        dist = float('inf')  # Usamos float('inf') para facilitar a comparação
                    distancias.append(dist)  # Adicionando distância na lista
                indice = distancias.index(max(distancias))
                memoria[indice] = pagina  # Substituindo a página

        # Exibindo o estado da memória e hit/miss após cada operação
        for j in range(tam_mem):
            if j < len(memoria) and memoria[j] == pagina:
                print(f"[{memoria[j]}] <- {hit_miss}")
            else:
                print(f"[{memoria[j]}]" if memoria[j] != -1 else "[-1]")

        print()  # Linha em branco para separar as iterações

    # Exibe as taxas de hit e miss
    total_accesses = hit + miss
    hit_rate = hit / total_accesses
    miss_rate = miss / total_accesses
    print(f"Hit rate ({hit}/{total_accesses}): {hit_rate:.2f}")
    print(f"Miss rate ({miss}/{total_accesses}): {miss_rate:.2f}")

# Recebe o tamanho da memória e a sequência de páginas do terminal
memory_size = int(input("Digite o tamanho da memória: "))
pages = input("Digite a sequência de páginas (separadas por vírgula, sem espaço): ")
opt(memory_size, pages)
