# FIFO

memory = [] #lista onde armazenaremos as páginas na memória
hits = 0 #contador de acessos onde a pagina já estava na memória
misses = 0 #contadir de acessos onde a página nãoo estava na memória
memory_size = int(input("Tamanho da memória: ")) #tamanho da memória física
page_sequence = input("Sequência de páginas: ").split(' ') #recebe sequência de acesso
page_sequence = [page.strip() for page in page_sequence if page.strip()]

for page in page_sequence: #lê a sequência de páginas 
    print(f"{page} |", end=" ")

    if page in memory: 
        print("Hit") # se já estiver na memória, um hit é incrementado
        hits += 1
    else:
        print("Miss")
        misses += 1 # senão, um miss é incrementado
        
        if len(memory) >= memory_size:
            memory.pop(0)  #se o tamanho limite da memória tiver sido atingido, remove a página mais antiga.
        memory.append(page)  
        
print("Total: ", (hits + misses))
print("Hit rate:", hits, "/", (hits + misses))
print("Miss rate:", misses, "/", (hits + misses))
