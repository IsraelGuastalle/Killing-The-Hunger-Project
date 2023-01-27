# 1. Problema de Negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO da empresa foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards.

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que fez. Ele precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas. Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.

Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento:

## Métricas Gerais:

01. Quantos restaurantes únicos estão registrados?
02. Quantos países únicos estão registrados?
03. Quantas cidades únicas estão registradas?
04. Qual o total de avaliações feitas?
05. Qual o total de tipos de culinária registrados?

## Métricas por País:

01. Qual o nome do país que possui mais cidades registradas?
02. Qual o nome do país que possui mais restaurantes registrados?
03. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
04. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
05. Qual o nome do país que possui a maior quantidade de avaliações feitas?
06. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
07. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
08. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
09. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Métricas por Cidade:

01. Qual o nome da cidade que possui mais restaurantes registrados?
02. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
03. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
04. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
05. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
06. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
07. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
08. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Métricas por Restaurante:

01. Qual o nome do restaurante que possui a maior quantidade de avaliações?
02. Qual o nome do restaurante com a maior nota média?
03. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
04. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
05. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
06. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
07. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
08. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Métricas por Tipo de Culinária:

01. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
02. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
03. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
04. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
05. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
06. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
07. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
08. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
09. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

# 2. Premissas assumidas para a Análise

1. Marketplace foi o modelo de negócio assumido.
2. A análise foi realizada com dados de restaurantes cadastrados em diversos países.
3. Caso uma pergunta do CEO possua dois ou mais registros iguais como resposta, será apresentado o restaurante cadastrado mais antigo.
4. As 4 principais visões do negócio foram: Visão Geral (Main Page), Visão Países (Countries), Visão Cidades (Cities) e Visão Culinária (Cuisines).

# 3. Estratégia da Solução

O painel estratégico foi desenvolvido utilizando as métricas que refletem as 4 principais visões do modelo de negócio da empresa:

1. Visão Geral (Main Page)
2. Visão Países (Countries)
3. Visão Cidades (Cities)
4. Visão Culinária (Cuisines)

Cada visão é representada pelo seguinte conjunto de métricas:

## 3.1. Visão Geral (Main Page):
  1. Quantidade de Restaurantes Cadastrados.
  2. Quantidade de Países Cadastrados.
  3. Quantidade de Cidades Cadastradas.
  4. Quantidade de Avaliações Feitas na Plataforma.
  5. Quantidade de Tipos de Culinárias Oferecidas.
  6. Localização dos Restaurantes Agrupados por Região em um Mapa. 

## 3.2. Visão Países (Countries):
  1. Quantidade de Restaurantes Registrados por País.
  2. Quantidade de Cidades Registradas por País.
  3. Média de Avaliações Realizadas por País.
  4. Média de Preço de um Prato para Duas Pessoas por País.

## 3.3. Visão Cidades (Cities):
  1. Top 10 Cidades com mais Restaurantes na Base de Dados (Segmentado por País).
  2. Top 7 Cidades com Restaurantes que possuem Média de Avaliação Acima de 4 (Segmentado por País).
  3. Top 7 Cidades com Restaurantes que possuem Média de Avaliação abaixo de 2.5 (Segmentado por País).
  4. Top 10 Cidades com Restaurantes com mais Tipos de Culinária Distintos na Base de Dados (Segmentado por País).

## 3.4. Visão Culinária (Cuisines):
  1. Nome do Melhor Restaurante de Culinária Italiana com sua respectiva Nota de Avaliação Média.
  2. Nome do Melhor Restaurante de Culinária Americana com sua respectiva Nota de Avaliação Média.
  3. Nome do Melhor Restaurante de Culinária Árane com sua respectiva Nota de Avaliação Média.
  4. Nome do Melhor Restaurante de Culinária Japonesa com sua respectiva Nota de Avaliação Média.
  5. Nome do Melhor Restaurante de Culinária Brasileira com sua respectiva Nota de Avaliação Média.
  6. Nome do Melhor Restaurante de Culinária Chinesa com sua respectiva Nota de Avaliação Média.
  7. Detalhes dos Top 20 Restaurantes mais bem avaliados (Segmentado por País e Culinária).
  8. Top 10 Melhores Tipo de Culinária (Segmentado por País).
  9. Top 10 Melhores Piores de Culinária (Segmentado por País).

# 4. Top 3 Insights de dados

1. Restaurantes Top 20 de Culinária Brasileira possuem uma quantidade menor de avaliações se comparado as demais culinárias.
2. A maioria dos Restaurantes Cadastrados estão concentrados na região da África do Sul e Reino Unido.
3. A média de preço de um prato para duas pessoas na Indonésia e Austrália é muito superior aos demais países podendo representar outliers.

# 5. O Produto Final do Projeto

Painel online, hospedado em Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: https://israelguastalle-projects-killing-the-hunger-home.streamlit.app/

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO. 

Da visão empresa (Visão Tática), podemos concluir que o número de pedidos cresceu entrea semana 06 e a semana 13 do ano de 2022.

# 7. Próximos passos

1. Reduzir o número de métricas.
2. Criar novos filtros.
3. Adicionar novas visões de negócio.
