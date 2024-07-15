lista= []

for i in range(5):
   lista.append(int(input(f"Informe o {i+1} valor: ")))
   
   
print(f"Antes {lista}")
for i in range(5):
    for j in range(5):
        aux = lista[i]
        if lista[i] < lista[j]:
            lista[i] = lista[j]
            lista[j] = aux
        
        
print(f"Depois {lista}")
