dicionario = {"Pessoa": "daniel", "gosta": ["casa", "futebol", "dormir", "rita"]}
i = 0
for keys, values in dicionario.items():
    print(f"{keys}: {values}")
    if type(values) == list:
        print(values[i])
        i += 1
    else:
        print(f"{keys}: {values}")


