lista = []

while True:
    lista.append(int(input("Informe um valor: ")))
    
    menu = int(input("Deseja continuar? 1 - Sim | 2 - Não "))
    
    if menu == 2:
        break
    
print(lista)

print(f"Quantos numeros foram digitados: {len(lista)}")

print(f"Antes {lista}")
for i in range(len(lista)):
    for j in range(len(lista)):
        aux = lista[i]
        if lista[i] > lista[j]:
            lista[i] = lista[j]
            lista[j] = aux

print(f"Antes {lista}")

if 5 in lista:
    print("Temos esse numero na lista")
else:
    print("Não temos")