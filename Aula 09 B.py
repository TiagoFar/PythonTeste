# TRANSFORMAÇÃO
frase = ('Tiago de Oliveira Faria')
print(frase.replace('Faria','Gostoso')) # troca por uma existente
print(frase.upper()) #todas maiúsculas
print(frase.lower()) # todas minúsculas
print(frase.capitalize()) # só a primeira maiúscula
print(frase.title()) # primeiras letras maiúsculas
frase = ('   Tiago de Oliveira Faria   ')
print(frase.strip()) # remove os espaços em branco, desnecessários, antes e depois da frase.
print(frase.rstrip()) # remove os últimos espaços da direita
print(frase.lstrip()) # remove os espaços da esquerda
#DIVISãO
print(frase.split()) # dividido em uma lista, palavra por palavra.
#JUNÇÂO
print('-'.join(frase))

print("""Irá escrever um texto inteiro se tiver entre 3 aspas""")
