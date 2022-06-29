
#1 - Criei uma lista chamada `filmes` com o nome dos 10 primeiros filmes mais bem avaliados no site no [IMDB]. Imprima o resultado.

filmes = [ 'Um Sonho de Liberdade', 'O Poderoso Chefão', ' Batman: O Cavaleiro das Trevas',
           'O Poderoso Chefão II ', '12 Homens e uma Sentença', ' A Lista de Schindler ',
           'O Senhor dos Anéis: O Retorno do Rei', 'Pulp Fiction: Tempo de Violência', ' O Senhor dos Anéis: A Sociedade do Anel',
            'Três Homens em Conflito']

print('-' * 30)

for i in range(0, 10):
    print(f'{i+1}º - {filmes[i]}')


#Simule a movimentação do *ranking*. Utilize os métodos `insert` e `pop` para trocar a posição do primeiro e do segundo filme da lista. Imprima o resultado.

print()
print('-' * 30)
filmes.insert(0, 'Vingadores: Ultimato')
filmes.insert(1, 'Vingadores: Guerra Infinita')

tamanho = len(filmes)

for i in range(0, tamanho):
    print(f'{i+1}º - {filmes[i]}')

print()
print('-' * 30)
filmes.pop(0)
filmes.pop(1)

tamanho = len(filmes)

for i in range(0, tamanho):
    print(f'{i+1}º - {filmes[i]}')

print('-' * 30)
print()


#-----------------------------------------------------------

#2 - Aconteceu um erro no seu *ranking*. Simule a duplicação dos três últimos filmes da lista. Imprima o resultado.

filmes_erro = [ 'Um Sonho de Liberdade', 'O Poderoso Chefão', ' Batman: O Cavaleiro das Trevas',
           'O Poderoso Chefão II ', '12 Homens e uma Sentença', ' A Lista de Schindler ',
           'O Senhor dos Anéis: O Retorno do Rei', 'Pulp Fiction: Tempo de Violência', ' O Senhor dos Anéis: A Sociedade do Anel',
            'Três Homens em Conflito', ' Vingadores: Ultimato ',  'Vingadores: Ultimato' ]

print(filmes_erro)
print()
print('-' * 30)

filmes_erro_set = { 'Um Sonho de Liberdade', 'O Poderoso Chefão', ' Batman: O Cavaleiro das Trevas',
                  'O Poderoso Chefão II ', '12 Homens e uma Sentença', ' A Lista de Schindler ',
                  'O Senhor dos Anéis: O Retorno do Rei', 'Pulp Fiction: Tempo de Violência', ' O Senhor dos Anéis: A Sociedade do Anel',
                  'Três Homens em Conflito', ' Vingadores: Ultimato ',  'Vingadores: Ultimato' }

print(filmes_erro_set)

print()
print()

#-----------------------------------------------------------

#3 - Repita os exercícios da parte 1 (listas). Os elementos da lista `filmes` devem ser dicionários no seguinte formato: `{'nome': <nome-do-filme>, 'ano': <ano do filme>}, 'sinopse': <sinopse do filme>}`. 


lista_filmes = {1:{'nome': 'Um Sonho de Liberdade', 'ano': '1994', 'sinopse':'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.'},
          2:{'nome': ' O Poderoso Chefão', 'ano': '1972', 'sinopse':'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.'},
          3:{'nome': 'Batman: O Cavaleiro das Trevas', 'ano': '2008', 'sinopse':'Quando a ameaça conhecida como O Coringa surge de seu passado, causa estragos e caos nas pessoas de Gotham. O Cavaleiro das Trevas deve aceitar um dos maiores testes para combater a injustiça.'},
          4:{'nome': 'O Poderoso Chefão II ', 'ano': '1974', 'sinopse':'Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque.'},
          5:{'nome': '12 Homens e uma Sentença', 'ano': '1957', 'sinopse':'Um jurado que se aposenta tenta evitar um erro judicial forçando seus colegas a reconsiderarem as evidências.'},
          6:{'nome': 'A Lista de Schindler', 'ano': '1993', 'sinopse':'Depois de testemunhar a perseguição dos judaicos na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler se começa a preocupar com sua força de trabalho judaica.'},
          7:{'nome': 'O Senhor dos Anéis: O Retorno do Rei', 'ano': '2003', 'sinopse':'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel.'},
          8:{'nome': 'Pulp Fiction: Tempo de Violência', 'ano': '1994', 'sinopse':'As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.'},
          9:{'nome': 'O Senhor dos Anéis: A Sociedade do Anel ', 'ano': '2001', 'sinopse':'Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-média das Trevas.'},
          10:{'nome': 'Três Homens em Conflito', 'ano': '1966', 'sinopse':'Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério.'}}

for i in range(1, 11):
	print(f'Filme - {i}: {lista_filmes[i]}')


