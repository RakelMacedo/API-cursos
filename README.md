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

- Inicie o servidor de desenvolvimento:
```
$ python3 manage.py runserver
```

### ✅ Com o servidor rodando, basta você visitar os endpoints do projeto com o seu navegador ou ferramenta preferida para testar APIs como o Postman ou Insomnia! =)
