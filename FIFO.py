memory = []  # lista onde armazenaremos as páginas na memória
hits = 0  # contador de acessos onde a página já estava na memória
misses = 0  # contador de acessos onde a página não estava na memória

memory_size = int(input("Tamanho da memória: "))  # tamanho da memória física
page_sequence = input("Sequência de páginas : ").split(',')  # recebe sequência de acesso separada por vírgulas

for page in page_sequence:
    print(f"page: {page}")
    if page in memory:
        hits += 1
        status = "hit"
    else:
        misses += 1
        status = "miss"
        if len(memory) >= memory_size:
            memory.pop(0)  # se o tamanho limite da memória tiver sido atingido, remove a página mais antiga.
        memory.append(page)
    for p in memory:
        print(f"[{p:^3}]")
    for _ in range(memory_size - len(memory)):
        print("[-1]")
    print(f"\n[ {page} ] <- ({status})\n")

total_accesses = hits + misses
print(f"Hit rate ({hits}/{total_accesses}):")
print(f"Miss rate ({misses}/{total_accesses}):")
