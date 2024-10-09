# Unidade 1 Trabalho 3 - Estudo de Assortatividade em Rede de Medicamentos e Princípios Ativos

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo reforçar conceitos de grafos, utilizando a biblioteca NetworkX em Python, por meio da criação, manipulação e análise de **três redes**, com o intuito de fazer um estudo da assortatividade em rede de medicamentos e princípios ativos.
[**Gov**](https://dados.gov.br/dados/conjuntos-dados/medicamentos-registrados-no-brasil)
<!-- [![Botão](https://dummyimage.com/60x20/575757/fff&text=Scopus)](https://www.scopus.com/home.uri?zone=header&origin=) -->


## Desenvolvimento  

### Rede #01 - Co-ocorrência de Princípios Ativos entre Medicamentos​

#### Pergunta
Medicamentos da mesma categoria regulatória tendem a compartilhar princípios ativos?

- Vértices: Medicamentos.
- Arestas: Mesmo princípio ativo entre dois medicamentos.
- Assortatividade: Calculada com base na categoria regulatória dos medicamentos.


### Rede #02 - Grafo bipartido de medicamentos e princípios ativos

#### Pergunta
Princípios ativos compartilhados por medicamentos complexos tendem a se conectar a medicamentos com perfis de complexidade similar?

- Vértices: Medicamentos e princípios ativos.
- Arestas: Medicamento ao seus respectivos princípios ativos.
- Assortatividade: Calcular a assortatividade por grau dentro do grafo bipartido para determinar se os princípios ativos que se conectam a medicamentos complexos (com muitos princípios ativos) tendem a se conectar também a medicamentos com perfis de complexidade semelhante.


### Rede #03 - Co-ocorrência por Empresa ou Classe Terapêutica

#### Pergunta
Medicamentos da mesma empresa ou classe terapêutica tendem a
compartilhar mais princípios ativos?

- Vértices: Medicamentos.
- Arestas: Aresta entre medicamentos com mesmo princípio ativo.
- Assortatividade: Calcular a assortatividade com base na empresa ou classe terapêutica dos medicamentos.


## Resultados e Discussão

- Rede #1:

<!-- ![Grafo Completo](https://github.com/polianaraujo/aed2/blob/82c557030227345dce829bcf0e727370f78199ec/U1T2/imagens/grafo%20completo.png) -->

- Rede #2: 

<!-- ![Subgrafo](https://github.com/polianaraujo/aed2/blob/82c557030227345dce829bcf0e727370f78199ec/U1T2/imagens/subgrafo.png) -->

- Rede #3:

<!-- ![Histograma](https://github.com/polianaraujo/aed2/blob/82c557030227345dce829bcf0e727370f78199ec/U1T2/imagens/histograma.png) -->

Com base nos gráficos e nas análises feitas, é possível tirar algumas conclusões sobre :
- 1
- 2
- 3

## Conclusão

x

## Formas de executar o código

O código completo está disponível neste repositório do Github, juntamente com o arquivo de dados em formato .csv. Para executar o código é recomendável usar o Google Colab, que já possui as bibliotecas necessárias. No caso do uso de outro ambiente, talvez seja necessário instalar algumas dessas bibliotecas.

## Link para a apresentação do código em vídeo

<!-- [**Youtube**](https://www.youtube.com/watch?v=x3NFGJoGZpQ) -->
