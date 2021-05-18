teste = list()
teste.append('Tiago')
teste.append(33)
galera = list() #AQUI GALERA É IGUAL A TESTE!
galera.append(teste[:]) # copiei os valores da lista TESTE!
teste[0] = 'Maria' # TROQUEI TIAGO POR MARIA
teste[1] = 22 # TROQUEI 33 POR 22
galera.append(teste) # SE EU NAO COLOCAR ESSE APARECE SÓ A MUDANCA FEITA. SE EU COLOCAR APARECE A LISTA ANTIGA
print(galera)

