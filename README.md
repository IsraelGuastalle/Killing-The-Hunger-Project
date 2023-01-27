# 1. Problema de Negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO da empresa foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards.

O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que fez. Ele precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas. Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.

Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas de crescimento:

## Métricas Gerais:

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## Métricas por País:

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Métricas por Cidade:

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Métricas por Restaurante:

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Métricas por Tipo de Culinária:

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
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

## 1. Visão do crescimento da empresa:
  1. Pedidos por dia.
  2. Porcentagem de pedidos por condições de Trânsito.
  3. Quantidade de pedidos por tipo e por cidade.
  4. Pedidos por semana.
  5. Quantidade de pedidos por tipo de entrega.
  6. Quantidade de pedidos por condições de trânsito e tipo de cidade

## 2. Visão do crescimento dos restaurantes:
  1. Quantidade de pedidos únicos.
  2. Distância média percorrida.
  3. Tempo médio de entrega durante festival e dias normais.
  4. Desvio Padrão do tempo de entrega durante festivais e dias normais.
  5. Tempo de entrega médio por cidade.
  6. Distribuição do tempo médio de entrega por cidade.
  7. Tempo médio de entrega por tipo de pedido.

## 3. Visão do crescimento dos entregadores:
  1. Idade do entregador mais velho e do mais novo.
  2. Avaliação do melhor e do pior veículo.
  3. Avaliação média por entregador.
  4. Avaliação média por condições de trânsito.
  5. Avaliação média por condições climáticas.
  6. Tempo médio do entregador mais rápido.
  7. Tempo médio do entregador mais rápido por cidade.

# 4. Top 3 Insights de dados

1. A sazonalidade da quantidade de pedidos é diária. Há uma variação de aproximadamente 10% do número de pedidos em dias sequenciais.
2. As cidades do tipo Semi-Urban não possuem condições baixas de trânsito.
3. As maiores variações no tempo de entrega, acontecem durante o clima ensolarado. 

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
