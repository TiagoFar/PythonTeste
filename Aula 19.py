alunos = {'nome':'Tiago', 'idade': 33, 'nota1': '10', 'nota2': '9.75'}
alunos2 = {}
print(alunos['nome'])
print(alunos['nota1'])
print(f'O {alunos["nome"]} tem {alunos["idade"]} anos') # como está dentro de aspas simples, tem que usar aspas DUPLAS.Para referenciar usa colchetes, para declarar usa chaves!
print(alunos.keys())
print(alunos.values())
print(alunos.items())
for k in alunos.keys():
    print(k)
for k in alunos.values():
    print(k)
for k, v in alunos.items():
    print(f'{k:<5}...............{v:<5}') # não se usa enumerate no dicionário.
del alunos['nota2'] # sem ponto depois do 'del'/ tirei a última nota
for k, v in alunos.items():
    print(f'{k:<5}..........{v:<5}') #mostrei sem a ultima nota
alunos['nome'] = 'Talita' # troquei o nome
alunos['idade'] = '31' # troquei a idade
print(alunos)
alunos['peso'] = '75kg' # vou adicionado a chave 'peso' com valor '75kg'
print(alunos)






