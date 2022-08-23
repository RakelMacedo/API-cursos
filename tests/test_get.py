import requests


headers = {'Authorization' : 'Token 433caf1706718bd559afe0ad6cc889ec71778ba5'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_cursos, headers=headers)
#print(resultado.json())

### Testando se o endpoint esta correto 
assert resultado.status_code == 200

### Testando se temos registros 
assert resultado.json()['count'] != 0

### Testando a quantidade de registros 
assert resultado.json()['count'] == 4

### Testando se o curso esta ativo
assert resultado.json()['results'][0]['ativo'] == True

### Testando se o titulo do primeiro curso esta correto 
assert resultado.json()['results'][0]['titulo'] == 'Desenvolvedor Back-end Python | EBAC'

