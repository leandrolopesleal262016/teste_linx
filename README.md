# App previsão do tempo

Aplicação web feita em Python com a biblioteca django que é um framework bem prático para desenvolvimento web em python.

App faz uma pesquisa sobre o clima da cidade informada no campo buscando as informaçoes através de requisição
em https://openweathermap.org, insere os dados no banco de dados (postgreSQL) e mostra na interface 
todas as cidades pesquisadas e inseridas no banco com a informação de clima atualizada, podendo ser removida do banco pela interface atravéz do botão X.
O App póssui filtro para evitar duplicidade de cidades e notifica quando a cidade digitada não existe.


  Dependencias:
  
    - Python 3
    
    - Instalar o django
    
        sudo pip3 install django # Debian 9 
        
    - Ter instalado banco de dados postgreesql
    
        sudo apt-get install postgresql postgresql-contrib # Debian 9
        
    -Instalar connector postgreesql para python 3 "psycopg2"
    
        sudo apt-get install python3-psycopg2 # Debian 9

    - Criar banco de Dados no posgresql com o nome "mydb" # Instruções para terminal linux Debian 9
    
        sudo su - postgres # acessa como usuario padrão do postgresql
        createdb mydb
        psql mydb # acessa o banco mysql
        
        Após acessar o banco com o comando acima:

        -Criar usuario admin:
            CREATE USER leandro SUPERUSER INHERIT CREATEDB CREATEROLE;
            
        Depois entre com o comando:

            ALTER USER leandro PASSWORD '5510';
            
        - Criar a tabela "weather_city" com os campos "id" e "nome" no banco mydb
        
            CREATE TABLE weather_city (id SERIAL PRIMARY KEY, name VARCHAR(25));
            
        - Dentro da pasta "the_weather" rodar o comando: (Pasta que contem o arquivo manage.py)
        
            python3 manage.py migrate # Para implementar as tabelas
            python3 manage.py runserver # Roda o servidor
           
           Acessar no navegador o endereço 127.0.0.1:8000
        
    Dados do servidor postgreSQL:
    
      banco: mydb
      user: leandro
      senha: 5510
      host: localhost
      port: 5432
