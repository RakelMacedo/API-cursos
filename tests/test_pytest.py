import requests


class TestCursos:
    headers = {'Authorization': 'Token 433caf1706718bd559afe0ad6cc889ec71778ba5'}
    url_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.url_cursos, headers=self.headers)
        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_cursos}1', headers=self.headers)
        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso para Teste",
            "url": "http://www.cursos.com.br/"
        }

        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']

    def test_put_curso(self):
        atualizado = {
            "titulo": "Novo Curso para Teste",
            "url": "http://www.cursos.com.br/testando"
        }

        resposta = requests.put(url=f'{self.url_cursos}21', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_cursos}21', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0


class TestAvaliacoes:
    headers = {'Authorization': 'Token 433caf1706718bd559afe0ad6cc889ec71778ba5'}
    url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

    def test_get_avaliacoes(self):
        resposta = requests.get(url=self. url_avaliacoes, headers=self.headers)
        assert resposta.status_code == 200

    def test_get_avaliacao(self):
        resposta = requests.get(url=f'{self.url_avaliacoes}1', headers=self.headers)
        assert resposta.status_code == 200

    def test_post_avaliacao(self):
        novo = {
            "curso": 1,
            "nome": "Maria Testando",
			"comentario": "O curso é otimo!",
			"avaliacao": "5.0"
        }

        resposta = requests.post(url=self.url_avaliacoes, headers=self.headers, data=novo)
        assert resposta.status_code == 201
        assert resposta.json()['avaliacao'] == novo['avaliacao']

    def test_put_avaliacao(self):
        atualizado = {
            "curso": 1,
            "nome": "Joana Atualizado",
			"comentario": "O curso é péssimo!",
			"avaliacao": "1.0" 
        }

        resposta = requests.put(url=f'{self.url_avaliacoes}8', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
        assert resposta.json()['avaliacao'] == atualizado['avaliacao']

    def test_delete_avaliacao(self):
        resposta = requests.delete(url=f'{self.url_avaliacoes}8', headers=self.headers)
        assert resposta.status_code == 204 and len(resposta.text) == 0
