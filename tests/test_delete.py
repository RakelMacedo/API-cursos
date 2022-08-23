import requests

headers = {'Authorization' : 'Token c5ab3349b1dcad47fb2d3a1b34eb556bf984ac7d'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

### Buscando o curso com id 18
#curso = requests.get(url=f'{url_cursos}18', headers=headers)
#print(curso.json())

resultado = requests.delete(url=f'{url_cursos}18', headers=headers)

### Testando o codigo HTTP 204 
assert resultado.status_code == 204

### Testando se o tamanho do conteúdo do retorno é 0 
assert len(resultado.text) == 0 
