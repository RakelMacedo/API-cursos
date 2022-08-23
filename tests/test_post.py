import requests


headers = {'Authorization' : 'Token c5ab3349b1dcad47fb2d3a1b34eb556bf984ac7d'}

url_cursos = 'http://localhost:8000/api/v2/cursos/'
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo" : "Scrum para Desenvolvedores de Software",
    "url" : "https://www.udemy.com/course/scrum-para-desenvolvedores/"
}

resultado = requests.post(url=url_cursos, headers=headers, data=novo_curso)

### Testando o codigo de status HTTP 201
assert resultado.status_code == 201

### Testando se o titulo do curso retornado e o mesmo do informado 
assert resultado.json()['titulo'] == novo_curso['titulo']
