import requests

headers = {'Authorization' : 'Token c5ab3349b1dcad47fb2d3a1b34eb556bf984ac7d'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo" : "Scrum para Desenvolvedores de Software",
    "url" : "https://www.udemy.com/course/scrum-para-desenvolvedores/",
    "ativo" : True
}

### Buscando o curso com id 15 
#curso = requests.get(url=f'{url_cursos}15', headers=headers)
#print(curso.json())

### Atualizando curso
resultado = requests.put(url=f'{url_cursos}15', headers=headers, data=curso_atualizado)

### Testando o codigo HTTP
assert resultado.status_code == 200

### Testando se o titulo do curso retornado e o mesmo do informado 
assert resultado.json()['titulo'] == curso_atualizado['titulo']