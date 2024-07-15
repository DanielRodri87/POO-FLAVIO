# Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.

print("-------------------------- JUROS COMPOSTOS ------------------------")
valor_inicial = float(input("Informe o valor inicial: "))
taxa = float(input("Taxa de Juros: "))
meses = 0

while meses < 24:
    valor_inicial = valor_inicial + (valor_inicial * (taxa/100))
    print(f"Mês: {meses+1} | Valor: {valor_inicial}")
    meses += 1
    
print("-------------------------- JUROS SIMPLES ------------------------")
valor_inicial_s = float(input("Informe o valor inicial: "))
taxa_s = float(input("Taxa de Juros: "))
meses_s = 0
valor_juros = valor_inicial_s

while meses_s < 24:
    valor_juros = (valor_inicial * (taxa/100))
    valor_inicial_s += valor_juros
    print(f"Mês: {meses_s+1} | Valor: {valor_inicial_s}")
    meses_s += 1
    
    