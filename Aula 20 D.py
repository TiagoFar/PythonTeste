def dobra(list):
    pos = 0
    while pos < (len(list)):
        list[pos] *= 2 # *= 2 ( quer dizer O DOBRO)
        pos += 1


valores = [2, 4, 6]
dobra(valores)
print(valores)