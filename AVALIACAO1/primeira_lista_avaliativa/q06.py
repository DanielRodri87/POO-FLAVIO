total_cost = 200.0
base_price = 5.0
base_sales = 120
sales_increase_per_price = 26
range_price = 0.50

max_profit = 0
max_price = 0
max_profit = 0

price = base_price
while price >= 1.0:
    vendas = base_sales + ((base_price - price) / range_price) * sales_increase_per_price
    lucro = (price * vendas) - total_cost
    print(f"preço ingresso = R$ {price:.2f}, quantidade = {int(vendas)}, lucro = R$ {lucro:.2f}")
    
    if lucro > max_profit:
        max_profit = lucro
        max_price = price
        max_profit = vendas
    
    price -= range_price
    
print(f"Lucro Esperado: R$ {max_profit:.2f}")
print(f"Preço do Ingresso: R$ {max_price:.2f}")
print(f"Quantidade Vendida: {int(max_profit)}")
