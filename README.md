# Teste Linx App previsão do tempo

Aplicação web feita em Python com a biblioteca django.

App faz uma pesquisa sobre o clima da cidade informada no campo buscando as informaçoes através de requisição
em https://openweathermap.org, insere os dados no banco de dados (postgreSQL) e mostra na interface 
todas as cidades cadastradas e o seu clima, podendo ser removida do banco pela interface.
O App póssui filtro para evitar duplicidade de cidades e notifica quando a cidade digitada não existe.


  Dependencias:
  
    - Python 3
    - Ter instalado banco de dados postgreesql
        sudo apt-get install postgresql postgresql-contrib # Debian 9
        
    -Instalar connector postgreesql para python 3 "psycopg2"
        sudo apt-get install python3-psycopg2 # Debian 9

    - Criar banco de Dados no posgresql com o nome "mydb" # Instruções para terminal linux Debian 9
        sudo su - postgres # acessa como usuario padrão do postgresql
        createdb mydb
        psql mydb; # acessa o banco mysql

    -Criar usuario admin:
        createuser -a -d -E -P leandro; # cria o usuário
        GRANT ALL PRIVILEGES ON DATABASE mydb TO leandro; # Concede os privilegios ao usuario

    - Dentro da pasta "the_weather" rodar o comando:
        python3 manage.py migrate # Para implementar as tabelas
        python3 manage.py runserver # Roda o servidor
        acessar o endereço 127.0.0.1:8000 
