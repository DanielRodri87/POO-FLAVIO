def menor_media(notas):
    soma_notas = 0
    menor_media = 11
    
    for k, v in dict(notas).items():
        for i in v:
            soma_notas += i
            if (sum(v)/3) <= menor_media:
                nome = k
        
    media = (soma_notas/12)
    return nome, media
    


notas = {'Joao': [8,7,9],
        'Maria': [6, 8, 7],
        'Pedro': [9, 9, 8],
        'Ana': [7,7,6]
}

nome, media = menor_media(notas)
print(nome, media)