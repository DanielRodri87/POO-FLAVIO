type_fuel = str(input("Informe o tipo de combustível: G - Gasolina | A - Alcool"))
quantity_liters = float(input("Informe quantos litros deseja abastecer: "))
if type_fuel == "G":
    if quantity_liters > 20:
        