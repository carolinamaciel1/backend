# desafio_drf

 Certifique-se de que você tem o Python 3 instalado, clone o repositorio e:

- Crie uma máquina virtual python3 -m venv myvenv
- Inicie a máquina virtual source myvenv/bin/activate
- instale as dependências usando pip install -r requirements.txt
- crie o banco de dados sqlite3 usando python manage.py migrate
- suba o servidor: python manage.py runserver
- o aplicativo roda em localhost:8000 e você pode acessar a página de admin em /admin
__________________________________________

Para criar um superusuário 

- python manage.py createsuperuser 

____________________________________________

API

[POST] Token superusuário

URL
    
    http://127.0.0.1:8000/auth-token/

Permission

       AllowAny

Body

      username:str
     
      password:str

Success status code

      200 OK
      
Example
    
    # Request 
      curl --location --request POST 'http://127.0.0.1:8000/auth-token/' \
      --data-raw '{
          "username": "gestor",
          "password":"admin123"
      }' 

      # Response
      {
          "token": "f80cf05e1a1a45ecd80d01ad3fe733c7a281786e"
      }
      
      
****

[GET] especialidades

URL
    
    http://127.0.0.1:8000/especialidades/

Permission

        IsAuthenticated with valid UserAdmin

Headers 

      Authorization: Token f80cf05e1a1a45ecd80d01ad3fe733c7a281786e

Success status code

      200 OK
      
 Example
    
    # Request 
      curl --location --request GET 'http://127.0.0.1:8000/especialidades/' \
      --data-raw '{
      }' 

    # Response
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "id": 9,
                  "nome": "Pediatria"
              }
          ]
      }
      
   
   * Filtro
   
      GET http://127.0.0.1:8000/especialidades/?search=ped
      
      
***      
      

[GET] medicos

URL
    
    http://127.0.0.1:8000/medicos/

Permission

        IsAuthenticated with valid UserAdmin

Headers 

      Authorization: Token f80cf05e1a1a45ecd80d01ad3fe733c7a281786e

Success status code

      200 OK
      
Example
    
    # Request 
      curl --location --request GET 'http://127.0.0.1:8000/medicos/' \
      --data-raw '{
      }' 

    # Response
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "id": 4,
                  "crm": "09crm2020",
                  "nome": "Carla Gomes",
                  "especialidade": {
                      "id": 9,
                      "nome": "Pediatria"
                  }
              }
          ]
      }
      
  * Filtro
        
        GET http://127.0.0.1:8000/medicos/?search=carla

***


[POST] user register

URL
    
    http://127.0.0.1:8000/users/register/

Permission

        AllowAny

Body 

      name: str
      email: str
      password: str
      re_password: str

Success status code

      201 CREATED
      
Example
    
    # Request 
      curl --location --request GET 'http://127.0.0.1:8000/users/register/' \
      --data-raw '{
            "name": "Maria Clara Fernades Costa",
            "email":"mclaratester@gmail.com"
            "password":"mclarauser123"
            "re_passowrd:"mclarauser123"
        
      }' 

    # Response
      {
          "email": "mclaratester@gmail.com",
          "name": "Maria Clara Fernades Costa",
          "password": "pbkdf2_sha256$216000$gJ6bP7cXlnaX$SMwd3Yz9Fj7cewaGJ9+qwzGyf95fV2OtPJwPeNS66a4=",
          "re_password": "pbkdf2_sha256$216000$0UWGxz9pCQMM$ekWHp4yLf7Hwk0f3e8wIDHXBMwEZSBn1xTCj2Ai3IVw="
      }


TODO
  - Consultas: Usuário cria uma consulta
  - Agenda: Mostrar apenas a agenda do usuário logado 
