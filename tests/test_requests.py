import requests

# urls de cursos e avaliacoes
url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


###  GET Avaliacoes
avaliacoes = requests.get(url_avaliacoes)

####  Acessando o código de status HTTTP
#print(avaliacoes.status_code)

###  Acessando os dados da resposta
#print(avaliacoes.json())
#print(type(avaliacoes.json()))

###  Acessando a quantidade de avaliacoes
#print(avaliacoes.json()['count'])

###  Acessando a próxima página de resultados de avaliacoes
#print(avaliacoes.json()['next'])

###  Acessando os resultados desta página
#print(avaliacoes.json()['results'])
#print(type(avaliacoes.json()['results']))

###  Aceessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])

###  Aceessando o último elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])

###  Acessando somente o nome da pessoa que fez a última avaliação
#print(avaliacoes.json()['results'][-1]['nome'])


###  GET Avaliacao
#avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/4')
#print(avaliacao.json())

###  GET Cursos
#headers = {'Authorization': 'Token c5ab3349b1dcad47fb2d3a1b34eb556bf984ac7d'}
#cursos = requests.get(url=url_cursos, headers=headers)
#print(cursos.status_code)
#print(cursos.json())