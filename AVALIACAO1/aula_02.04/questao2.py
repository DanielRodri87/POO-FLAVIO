v = input("Informe uma palavra: ")
v = v.upper().strip()
texto = 'daniel Rodrigues'
texto = texto.upper().strip()
count = 0
for i in texto:
    if i == v:
        count += 1
        
print(count)