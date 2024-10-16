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
- Arestas: Medicamentos que compartilham o mesmo princípio ativo.
- Assortatividade: A assortatividade foi calculada com base na categoria regulatória dos medicamentos. Nesse contexto, a assortatividade mede se medicamentos de uma mesma categoria regulatória (por exemplo, genérico, similar, biológico) tendem a compartilhar mais princípios ativos entre si do que com medicamentos de outras categorias.

A Rede #01 foi criada com o objetivo de investigar se a categoria regulatória de um medicamento influencia a probabilidade de ele compartilhar o mesmo princípio ativo com outros medicamentos. A visualização em formato circos plot, gerada com a biblioteca nxviz, ajuda a destacar esses grupos e suas interações, possibilitando identificar padrões de compartilhamento de princípios ativos.

### Rede #02 - Grafo bipartido de medicamentos e princípios ativos

#### Pergunta
Princípios ativos compartilhados por medicamentos complexos tendem a se conectar a medicamentos com perfis de complexidade similar?

- Vértices: Medicamentos e princípios ativos.
- Arestas: Medicamento conectado aos seus respectivos princípios ativos
- Assortatividade:  A assortatividade por grau foi calculada dentro do grafo bipartido. Nesse caso, avaliamos se medicamentos com maior complexidade (medicamentos com vários princípios ativos) tendem a se conectar a princípios ativos que também são compartilhados com outros medicamentos de alta complexidade.

A Rede #02 tem como foco principal explorar o nível de complexidade dos medicamentos, definido pela quantidade de princípios ativos que um medicamento contém. Essa análise é útil para entender se medicamentos com muitos princípios ativos possuem padrões de conectividade diferenciados em relação a medicamentos menos complexos.

### Rede #03 - Co-ocorrência por Empresa ou Classe Terapêutica

#### Pergunta
Medicamentos da mesma empresa ou classe terapêutica tendem a
compartilhar mais princípios ativos?

- Vértices: Medicamentos.
- Arestas:  Medicamentos que compartilham o mesmo princípio ativo
- Assortatividade: A assortatividade foi calculada com base na empresa fabricante ou classe terapêutica dos medicamentos. Assim, medimos se medicamentos da mesma empresa ou pertencentes à mesma classe terapêutica apresentam uma tendência maior de compartilhar princípios ativos.

A Rede #03 visa analisar se a empresa fabricante ou a classe terapêutica de um medicamento influencia a sua probabilidade de compartilhar princípios ativos com outros medicamentos. O objetivo aqui é entender se padrões de co-ocorrência de princípios ativos estão relacionados com fatores comerciais ou terapêuticos.

## Resultados e Discussão

- Rede #1: A Rede #1 foi criada com o objetivo de investigar se a categoria regulatória de um medicamento influencia a probabilidade de ele compartilhar o mesmo princípio ativo com outros medicamentos. A visualização em formato circos plot, gerada com a biblioteca nxviz, ajudou a destacar esses grupos e suas interações. O cálculo da assortatividade por categoria regulatória resultou em um valor de 0.353, indicando uma tendência moderada de medicamentos dentro da mesma categoria compartilharem princípios ativos.
<!-- ![Grafo Completo](https://github.com/polianaraujo/aed2/blob/82c557030227345dce829bcf0e727370f78199ec/U1T2/imagens/grafo%20completo.png) -->

- Rede #2: A Rede #2 foi calculada a assortatividade por grau para o grafo bipartido, que avalia a correlação entre medicamentos com base no número de conexões que eles têm com princípios ativos. O valor encontrado foi de -0.452, sugerindo que medicamentos com um número diferente de princípios ativos tendem a estar mais conectados entre si, o que caracteriza uma disassortatividade. Esse resultado indica que medicamentos com muitos princípios ativos tendem a compartilhar esses princípios com medicamentos que têm poucos princípios ativos.
<!-- ![Subgrafo](https://github.com/polianaraujo/aed2/blob/82c557030227345dce829bcf0e727370f78199ec/U1T2/imagens/subgrafo.png) -->

- Rede #3:
  - Classe Terapêutica: Foi calculada a assortatividade com base na classe terapêutica dos medicamentos, que resultou em um valor de 0.697, indicando uma alta assortatividade. Isso significa que medicamentos da mesma classe terapêutica tendem a compartilhar mais princípios ativos entre si do que com medicamentos de outras classes.
  - Empresa: A assortatividade por empresa foi baixa, com um valor de 0.023, indicando que a empresa detentora do registro não influencia significativamente o compartilhamento de princípios ativos entre medicamentos.
Essa rede foi fundamental para entender como medicamentos de diferentes classes terapêuticas e empresas compartilham princípios ativos. O alto valor de assortatividade por classe terapêutica sugere que medicamentos da mesma classe têm um perfil farmacológico mais homogêneo, reforçando a ideia de que há uma divisão clara no mercado entre classes de medicamentos.
<!-- ![Histograma](https://github.com/polianaraujo/aed2/blob/82c557030227345dce829bcf0e727370f78199ec/U1T2/imagens/histograma.png) -->

Com base nos gráficos e nas análises feitas, é possível tirar algumas conclusões sobre :
- 1 O circos plot é ideal para destacar os padrões de conectividade entre categorias regulatórias e medicamentos. A visualização ajuda a ver quais categorias tendem a compartilhar mais princípios ativos entre si. No nosso caso, exite uma alta variedade de medicamentos e existem tendências de co-ocorrência dentro de algumas categorias específicas.
- 2: A rede bipartida foi visualizada com uma disposição de medicamentos e princípios ativos em lados opostos, facilitando a análise das conexões entre eles. Essa representação ajudou a identificar padrões na forma como os princípios ativos são distribuídos entre medicamentos de diferentes níveis de complexidade.
- 3: No grafo, muitos do nós estão posicionados em um anel externo, isso significa que tem muitas conexões (muitos compartilhamentos de principios ativos) enquanto os subgrupos de nós na região central formam uma estrutura com poucas conexões.

## Conclusão

O estudo de assortatividade em redes de medicamentos e princípios ativos revelou diferentes padrões de conectividade entre medicamentos. Medicamentos da mesma categoria regulatória e da mesma classe terapêutica tendem a compartilhar princípios ativos com mais frequência, enquanto medicamentos de empresas diferentes apresentam uma conectividade mais dispersa. Além disso, o grafo bipartido mostrou uma disassortatividade por grau, sugerindo que medicamentos com muitos princípios ativos se conectam mais frequentemente com medicamentos de menor complexidade.

Essas análises reforçam a importância da categorização de medicamentos para entender sua conectividade em termos de princípios ativos, além de fornecer uma base para a aplicação prática desses conceitos na área da farmacologia e no desenvolvimento de políticas de regulação de medicamentos.

## Formas de executar o código

O código completo está disponível neste repositório do Github, juntamente com o arquivo de dados em formato .csv. Para executar o código é recomendável usar o Google Colab, que já possui as bibliotecas necessárias. No caso do uso de outro ambiente, talvez seja necessário instalar algumas dessas bibliotecas.

## Link para a apresentação do código em vídeo

[**Youtube**](https://youtu.be/YPIjYDZaxYo) 
