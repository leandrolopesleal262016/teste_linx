# teste_linx

Aplicação web feita em Python com a biblioteca django.

App faz uma pesquisa sobre o clima da cidade informada no campo buscando as informaçoes através de requisição
em https://openweathermap.org, insere os dados no banco de dados postgreSQL e mostra na interface 
todas as cidades cadastradas e o seu clima, podendo ser removida do banco pela interface.
O App póssui filtro para evitar duplicidade de cidades e notifica quando a cidade digitada não existe.
