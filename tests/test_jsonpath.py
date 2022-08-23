import requests
import jsonpath

### GET avaliacoes 
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

### Pegando o resultado de avaliacoes 
#resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
#print(resultados)

### Pegando a primeira avaliacao 
#primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
#print(primeira)

### Pegando o nome do primeiro usuario que fez a primeira avaliacao 
#nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
#print(nome)

### Tentando pegar o email - O email é privado, logo o retorno será False
#email = jsonpath.jsonpath(avaliacoes.json(), 'results[0].email')
#print(email)

### Pegando a nota do curso da primeira avaliacao 
#nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
#print(nota)

### Pegando o id do curso daquela avaliacao
#curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
#print(curso_id)

### Todos os nomes dos alunos que avaliaram o curso 
#nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
#print(nomes)

### Todas as notas dos cursos 
#notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
#print(notas)
