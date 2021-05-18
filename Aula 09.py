frase = ('Tiago de Oliveira Faria')
print(frase[0])
print(frase[18:23])
print(frase[9:17])
print(frase[:5])
print(frase[9:])
print(frase[9::3])
print(len(frase)) #comprimento da frase
print(frase.count('o')) #quantas letras "o"s, diferencia de maiúsculas
print(frase.count('a'))
print(frase.count('a',0,17)) #quantas letras "o" no intervalo de 0 a 13
print(frase.find('de')) #quantas vezes encontrou "de", mas na posição que começou
print(frase.find("Silva")) #se não tiver a palavra vai reportar -1
print('Faria'in frase)

