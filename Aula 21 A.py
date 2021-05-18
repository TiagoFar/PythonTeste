from time import sleep
def contador (i, f, p): #abrir aspas duplas 3x e dar enter.
    """
    -> Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Aula 21 do Curso de Python 3.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        sleep(0.3)
        c += 1
    print('Fim')

contador(2, 10, 2)
help(contador)