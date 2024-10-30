# Unidade 1 Trabalho 4 - Estudo de Métricas

## Aluna:  
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo é analisar as diferentes métricas estudadas (Cycles, Average Shortest Path Length, Diameter of Network, Shortest Path Length, Connected Components, Giant Connected Components, number connected components, BFS, DFS, SCC, WCC e Clustering Coefficient) aplicando à rede formada pela cidade de Natal/RN utilizando a biblioteca OSMnx, que é utilizada para fazer a análise de redes urbanas.
<!-- [**Gov**](https://dados.gov.br/dados/conjuntos-dados/medicamentos-registrados-no-brasil) -->
<!-- [![Botão](https://dummyimage.com/60x20/575757/fff&text=Scopus)](https://www.scopus.com/home.uri?zone=header&origin=) -->


## Desenvolvimento e Resultados

### 0. Rede de Natal/RN

![Rede de Natal/RN](https://github.com/polianaraujo/aed2/blob/main/U1T4/Images/rede_natal.png)

### 1. Cycles (Ciclos)

No contexto de grafos, um ciclo independente é um ciclo que não pode ser decomposto em outros ciclos presentes no grafo. Esta métrica indica o número de ciclos independentes, que mostra a quantidade de loops na rede e como estão distribuídos.

P: Quantos ciclos independentes existem na rede de Natal?

R: ```Número de ciclos independentes na rede: 9414```

Um número elevado, como 9414, indica que a rede de ruas tem muitas malhas ou seções fechadas, o que sugere uma boa conectividade e alternativas de rotas. Em redes urbanas, uma quantidade alta de ciclos pode ser positiva, pois implica a possibilidade de múltiplos caminhos entre locais, o que pode melhorar a acessibilidade e flexibilidade na mobilidade urbana.

### 2. Average Shortest Path Length (Comprimento Médio do Caminho Mais Curto)

Esta métrica reflete a facilidade ou dificuldade de navegação pela cidade, com valores menores indicando uma rede mais conectada e acessível.

P: Qual é o comprimento médio do caminho mais curto?

R: ```Comprimento médio do caminho mais curto (na maior componente conectada): 79.5658127079651```

Esse número indica que, em média, você precisaria percorrer cerca de 79,57 arestas (ou segmentos de ruas) para ir de um nó a outro dentro da maior componente conectada do grafo.

### 3. Diameter of Network (Diâmetro da Rede)

O diâmetro da rede é a maior distância mínima entre quaisquer dois nós no grafo. O diâmetro mostra a extensão máxima da rede, refletindo o maior percurso possível na cidade sem desconexões.

P: Qual é o maior caminho dentro da rede?

R: ```Diâmetro da rede (na maior componente conectada): 209```

O valor 209 significa que, na maior componente conectada da rede de ruas, a distância máxima entre dois nós (ou pontos) conectados é de 209 arestas. Para dois nós que estão no caminho mais distante possível dentro dessa componente, seria necessário passar por 209 segmentos de ruas para ir de um ao outro, usando o caminho mais curto disponível.

### 4. Shortest Path Length (Caminho Mais Curto)

Escolhemos dois pontos aleatórios para verificar a distância entre eles, e medimos a distância mais curta entre os pontos selecionados, ajudando a entender a conectividade prática.

P: Qual é o menor caminho entre dois pontos principais?

R: ```Comprimento do caminho mais curto entre dois pontos: 57```

O valor 57 significa que, para viajar do nó nodes[0] ao nó nodes[-1] na rede, o caminho mais curto entre esses dois pontos envolve atravessar 57 arestas. Ou seja, existe uma rota mínima entre esses dois nós que passa por 57 segmentos de ruas, que pode ser entendida como a rota mais eficiente em termos de número de segmentos.

### 5. Giant Connected Component (Maior Componente Conectado)

O número de componentes conectados indica quantas sub-redes existem na cidade. Isso mostra quantas partes independentes existem na rede e se há áreas desconectadas.

P: Quantos componentes conectados existem na rede?

R: ```Número de nós no maior componente conectado: 18668```

O valor 18.668 nós indica que a maior parte da rede viária de Natal está conectada em um grande componente. Esse número representa o maior subgrafo da cidade, composto principalmente por ruas interligadas, onde há rotas acessíveis de um ponto a outro. Os nós fora desse maior componente representam pequenas redes isoladas (como ruas privadas ou ruas desconectadas), mas são geralmente menos significativos em termos de mobilidade urbana, pois não estão interligados ao restante da cidade.

## Conclusão

1. O número 9414 ciclos independentes sugere que a rede de ruas de Natal-RN possui uma estrutura interconectada com várias rotas alternativas, refletindo uma boa acessibilidade dentro da maior componente conectada. Isso é geralmente desejável em redes urbanas, pois melhora a navegação e aumenta a eficiência dos caminhos disponíveis para deslocamentos dentro da cidade.

2. Em resumo, 79,5658 fornece uma visão geral da conectividade na maior componente conectada da rede de ruas de Natal-RN, ajudando a avaliar a acessibilidade e a eficiência das rotas na cidad

3. O valor 209 para o diâmetro indica que a maior componente conectada da rede de ruas de Natal-RN tem um alcance amplo, com a maior distância (em termos de segmentos de rua) entre dois pontos sendo relativamente elevada. Essa medida de diâmetro ajuda a compreender o limite máximo de deslocamento entre os pontos mais distantes da cidade, considerando apenas o caminho mais curto entre eles.

4. O valor 57 indica que, na rede de ruas de Natal-RN, a rota mais curta entre os nós nodes[0] e nodes[-1] requer passar por 57 segmentos de ruas. Este é o menor número de segmentos necessários para conectar esses dois pontos, representando a eficiência da rede de ruas entre eles.

5. 


## Formas de executar o código

A maneira mais fácil de rodar esse código é abrir o arquivo .ipynb no Google Colab ou no Jupyter, em que as células de código poderão ser rodadas em sequência.


## Link para a apresentação do código em vídeo

<!-- [**Youtube**](colocar) -->
