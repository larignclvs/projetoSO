import sys

## pegando a linha de comando
args = sys.argv[1:]

## numero de peginas q serão usadas sendo fornecida pela linha de comando
paginas = int(args[0])

## fazendo a lista de chamada da de páginas
lista = [int(x) for x in args[1].split(",")]

## serão necessários dois vetores, um da ordem de chamada e outro com o cache
cache = []
ordem = []

# Contadores de hits e misses
hits = 0
misses = 0

## implementação do LRU, percorrendo a lista de chamadas
for item in lista:
    print(f"page: {item}")
    
    # Se o item já está no cache (hit)
    if item in cache:
        hits += 1
        ## o ultimo item da lista de ordem é o mais recente usado ai eu removo de onde ele está e coloco no final
        ordem.remove(item)
        ordem.append(item)  # Adiciona o item ao final da ordem
        hit_miss = "(hit)"
    else:
        # Miss: item não está no cache
        misses += 1
        hit_miss = "(miss)"
        
        ## Se o cache está cheio
        if len(cache) >= paginas:
            ## removendo o menos recentemente usado, (o que ta na primeira posição da lista de ordem)
            lru_item = ordem.pop(0)
            lru_index = cache.index(lru_item)  # pegando a posição do que será removido 
            cache[lru_index] = item  # colocando o item novo no lugar onde estava o menos usado
        else:
            # se tiver espaço só colocar aonde está livre 
            cache.append(item)

        # Adiciona o novo item à ordem
        ordem.append(item)
    
    # for do print
    for i in range(paginas):
        if i < len(cache):
            if cache[i] == item:
                print(f"[{cache[i]}] <- {hit_miss}")
            else:
                print(f"[{cache[i]}]")
        else:
            print("[-1]")
    
    print()  # Linha em branco para separar as iterações

# Exibe as taxas de hit e miss
total_accesses = hits + misses
hit_rate = hits / total_accesses
miss_rate = misses / total_accesses
print(f"Hit rate ({hits}/{total_accesses}): {hit_rate:.2f}")
print(f"Miss rate ({misses}/{total_accesses}): {miss_rate:.2f}")
