## 📜 API-cursos
Com o objetivo de servir um aplicativo para Cursos, pode-se criar cursos e avaliações para os mesmos, assim como editar e excluir.

<br>

### 📑 Versões das tecnologias usadas:

<table>
  <tr>
    <td>Python</td>
    <td>Django</td>    
    <td>SQLite</td>
    <td>Django Rest Framework</td>
    <td>Requests</td>
    <td>Pytest</td>
  </tr>
  <tr>
    <td>3.*</td>
    <td>4.1</td>
    <td>3</td>
    <td>3.13</td>
    <td>2.28</td>
    <td>7.1</td>
  </tr>
</table>

<br>

### 🛠️ Instalando o projeto:

- Clone o repositório:
```
$ git clone https://github.com/RakelMacedo/API-cursos.git
$ cd API-cursos/
```

- Crie seu ambiente virtual:
```
$ python3 -m venv venv
```

- E ative seu ambiente virtual:
```
$ source venv/bin/activate
```

- Instale as depencências:
```
$ pip install -r requirements.txt
```

- Crie a estrutura no banco de dados:
``` 
$ python3 manage.py migrate
```  
<br>

## ⚠️ ATENÇÃO

Nossa API está configurada para **apenas** usuários que passem seu **Token** possam usar os métodos **POST, PUT e DELETE.**

   1. Você pode deixar desta maneira e seguir o passo a passo **Criando um super usuário e gerando um Token** para gerar seu super usuário e seu Token e envia-lo em *headers* através de uma ferramenta como Postman ou Insomnia.

   2. Caso queira deixar a forma de Autenticação via sessão, basta editar o final do arquivo settings.py e deixa-lo desta forma:
```python 
# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    #   'rest_framework.authentication.TokenAuthentication',
    ),
    .
    .
}

```  
   Você precisará apenas criar seu super usuário para se logar em Django Admin --> http://127.0.0.1:8000/admin/ 
   
   E se logar em --> http://127.0.0.1:8000/auth/login/?next=/api/v2/cursos/ , para usar todos os recursos normalmente.
   
<br>

### Criando um super usuário e gerando um Token:

- Crie um super usuário informando os dados requisitados:
``` 
$ python3 manage.py createsuperuser
```  
Guarde bem seu usuario e senha ;)

<br>

- Inicie o servidor de desenvolvimento:
```
$ python3 manage.py runserver
```
<br>

- Visite em seu navegador a url abaixo, e preencha o painel de login com seu usuario e senha criado acima:
```
http://127.0.0.1:8000/admin/
```
<br>

- Agora, vamos gerar um Token para você!

Após o Login, em **Tokens** clique em *Adicionar* > *Selecione o usuario* > *Salvar* 
<br>
![api-cursos](https://user-images.githubusercontent.com/78339857/186071486-8d157c0c-8e5a-4104-8ac3-a993d1da812a.jpg)





### ✅ Com o servidor rodando, basta você visitar os endpoints do projeto com o seu navegador ou ferramenta preferida para testar APIs como o Postman ou Insomnia! =)
