lista = []

for i in range(100):
    lista.append(float(input()))
    
for i in range(100):
    if lista[i] <= 10:
        print(f"A[{i}] = {lista[i]:.1f}")