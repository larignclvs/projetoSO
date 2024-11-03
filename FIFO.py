memory = []
hits = 0
misses = 0
memory_size = int(input("Tamanho da memória: "))
page_sequence = input("Sequência de páginas (separadas por vírgula): ").split(',')
page_sequence = [page.strip() for page in page_sequence if page.strip()]

print("Página solicitada | Status")
for page in page_sequence:
    print(f"{page} |", end=" ")

    if page in memory: 
        print("Hit")
        hits += 1
    else:
        print("Miss")
        misses += 1
        
        if len(memory) >= memory_size:
            memory.pop(0)  
        memory.append(page)  

if hits + misses > 0:
    hit_rate = hits / (hits + misses) * 100
    miss_rate = misses / (hits + misses) * 100
    print(f"Hit rate: {hit_rate:.2f}%")
    print(f"Miss rate: {miss_rate:.2f}%")
