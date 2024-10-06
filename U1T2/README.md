# Unidade 1 Trabalho 2 - Rede de Co-Autoria

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo reforçar conceitos de grafos, utilizando a biblioteca NetworkX em Python, por meio da criação e manipulação de uma rede de co-autoria a partir de dados reais extraídos da plataforma
[**Scopus**](https://www.scopus.com/home.uri?zone=header&origin=)
<!-- [![Botão](https://dummyimage.com/60x20/575757/fff&text=Scopus)](https://www.scopus.com/home.uri?zone=header&origin=) -->


## Desenvolvimento  

### Passo #01 - Extração dos Dados 🎲​
Obtemos um arquivo .csv na plataforma Scopus, contendo informações de artigos publicados por autores da Universidade Federal do Rio Grande do Norte (UFRN). Os artigos selecionados estão dentro da área de Redes Neurais, e o arquivo contém as seguintes informações:  
- Nome dos autores
- Identificadores únicos dos autores
- Título do artigo
- Ano de publicação

### Passo #02 - Criação da rede de Co-Autoria 📝​
Criação da Rede de Co-Autoria: Foi criada uma rede de co-autoria utilizando os dados extraídos. Os vértices presentes neste grafo são os autores e as arestas a colaboração entre eles.

Para a visualização dessa rede, utilizamos as bibliotecas *matplotlib* e *plotly*. A visualização com *matplotlib* forneceu uma versão estática do grafo completo, enquanto *plotly* foi utilizado para criar uma versão interativa do subgrafo, permitindo explorar melhor as conexões mais relevantes.

Imagem do grafo estático:

COLOCAR IMAGEM DO GRAFO

### Passo #03 - Análises da rede ​​📊​
Após a construção da rede de co-autoria, foram analisadas algumas características dessa rede utilizando as funcionalidades da biblioteca *NetworkX*:
- Densidade da Rede: Calculamos a densidade da rede, que mede o quão conectados estão os autores em relação ao número máximo possível de conexões. Uma densidade próxima de 1 indica que a maioria dos autores tem colaboração entre si, enquanto uma densidade baixa indica que a rede é mais esparsa, ou seja, há poucos autores colaborando diretamente.
- Sub-Grafo: Para aprofundar a análise, criamos um subgrafo contendo apenas os nós que possuem pelo menos X vizinhos (X foi definido como 15). Com isso, conseguimos identificar quais são os autores mais colaborativos dentro da rede, ou seja, aqueles que participaram de muitos artigos em conjunto. A densidade desse subgrafo também foi calculada, permitindo comparar o quão conectados estão os autores mais ativos em relação aos demais.
- Histograma dos Grau: Criamos um gráfico de histograma mostrando a distribuição do grau dos vértices da rede. O grau de um vértice representa o número de co-autores com os quais ele colaborou. Essa análise nos permite visualizar quantos autores são altamente conectados e quantos colaboram esporadicamente. Isso ajuda a entender a estrutura da rede e a distribuição de colaborações.

## Resultados e Discussão

- Grafo Completo de Coautoria: No grafo completo, é possível observar a densidade das conexões entre os autores. A densidade de um grafo refere-se à fração de todas as possíveis conexões entre os nós que realmente estão presentes. Se a densidade for alta, isso sugere que há uma grande quantidade de colaboração entre os autores da UFRN na área de Redes Neurais, indicando uma comunidade bem conectada e cooperativa. Em contrapartida, uma densidade baixa pode indicar colaborações mais esporádicas e menos integradas entre os autores. Além disso, os autores mais centrais na rede, ou seja, aqueles com um alto grau de conexão (número de coautores), têm um papel fundamental na disseminação do conhecimento e na promoção de colaborações dentro do grupo. Esses autores podem ser identificados visualmente no grafo como aqueles que têm um grande número de arestas conectando-os a outros nós, ou através de métricas como grau de centralidade.

- Subgrafo: Ao analisar o subgrafo que representa os componentes principais, é importante destacar os autores que ocupam posições centrais. Esses nós centrais geralmente indicam autores que servem como “ponte” entre diferentes grupos de pesquisa, promovendo a integração entre áreas específicas dentro do campo de Redes Neurais. Esses autores têm um papel essencial na coesão da rede, garantindo que as informações fluam de maneira mais eficiente entre diferentes subgrupos. Podemos também observar a existência de pequenos componentes isolados ou menos conectados, o que pode indicar a presença de grupos de pesquisa menores que têm pouca ou nenhuma colaboração com outros grupos.

- Histograma de Grau de Conexão dos Autores: O histograma do grau de conexão dos autores fornece uma visão mais quantitativa sobre o número de coautores que cada pesquisador tem. Se a maioria dos autores tiver um número baixo de coautores, isso pode indicar uma colaboração limitada, onde os autores tendem a publicar com um grupo restrito de colaboradores, possivelmente do mesmo grupo de pesquisa ou departamento. Esse comportamento é comum em áreas mais especializadas ou em estágios iniciais de formação de redes colaborativas. Por outro lado, autores com um número significativamente maior de coautores podem ser considerados líderes na área, responsáveis por promover colaborações amplas e, muitas vezes, interdisciplinares.

Com base nos gráficos e nas análises feitas, é possível tirar algumas conclusões sobre o estado da colaboração em pesquisa na UFRN na área de Redes Neurais:
- Densidade e Centralidade: Uma alta densidade e a presença de autores centrais sugerem uma rede coesa, onde o conhecimento flui facilmente entre os membros.
- Componentes Menores: A presença de pequenos componentes isolados indica que existem grupos menores que não estão integrados na rede maior, sugerindo a possibilidade de promover mais colaborações.
- Distribuição de Grau: A distribuição do grau mostra que existem alguns líderes que conectam muitos outros pesquisadores, enquanto a maioria parece colaborar com apenas um pequeno número de colegas.

## Conclusão

A criação da rede de coautoria e suas análises permitiram observar o padrão de colaboração entre os autores da UFRN na área de Redes Neurais. Notamos que, embora a maioria dos autores colabore com um número restrito de coautores, há um núcleo bem conectado que atua como ponto central na disseminação do conhecimento e na promoção de colaborações, indicando uma estrutura de rede composta por grupos menores com forte integração interna e alguns líderes que conectam diferentes subgrupos. Essas análises fornecem um panorama útil para entender as dinâmicas de colaboração e podem ser usadas para identificar áreas onde iniciativas para aumentar a cooperação entre os grupos seriam mais efetivas.

Esse projeto também demonstrou o potencial das ferramentas de análise de grafos, como o NetworkX, para estudar redes complexas e fornecer insights relevantes sobre padrões de colaboração científica.

## Não sei um bom titulo mas seria meio que uma parte dizendo o que é necessário para reproduzir o nosso trabalho (não sei nem se é necessário colocar isso)

O código completo está disponível neste repositório do Github, juntamente com o arquivo de dados em formato .csv. Para executar o código é recomendável usar o Google Colab ou outro ambiente que suporte Python, mas talvez seja necessário instalar algumas bibliotecas que foram utilizadas.
