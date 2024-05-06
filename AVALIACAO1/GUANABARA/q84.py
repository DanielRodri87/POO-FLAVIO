nomes = []
pesos = []

while True:
    nome = input("Informe o nome: ")
    peso = float(input("Informe o peso: "))
    nomes.append(nome)
    pesos.append(peso)
    
    continuar = input("Deseja continuar? [S/N] ").strip().lower()
    if continuar != 's':
        break

menor_peso = min(pesos)
maior_peso = max(pesos)

nomes_menor_peso = [nomes[i] for i, p in enumerate(pesos) if p == menor_peso]
nomes_maior_peso = [nomes[i] for i, p in enumerate(pesos) if p == maior_peso]

print("====================================================")
print(f"Pessoas Cadastradas: {len(nomes)}")
print(f"O menor peso: {menor_peso} da(s) pessoa(s): {', '.join(nomes_menor_peso)}")
print(f"O maior peso: {maior_peso} da(s) pessoa(s): {', '.join(nomes_maior_peso)}")
