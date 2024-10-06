# Unidade 1 Trabalho 2 - Rede de Co-Autoria

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo reforçar conceitos de grafos, utilizando a biblioteca NetworkX em Python, por meio da criação e manipulação de uma rede de co-autoria a partir de dados reais extraídos da plataforma Scopus.

## Desenvolvimento  

### Passo #01 - Extração dos Dados 🎲​
Obtemos um arquivo .csv na plataforma Scopus, contendo informações de artigos publicados por autores da Universidade Federal do Rio Grande do Norte (UFRN). Os artigos selecionados estão dentro da área de Redes Neurais, e o arquivo contém as seguintes informações:  
- Nome dos autores
- Identificadores únicos dos autores
- Título do artigo
- Ano de publicação

### Passo #02 - Criação da rede de Co-Autoria 📝​
Criação da Rede de Co-Autoria: Foi criada uma rede de co-autoria utilizando os dados extraídos. Os vértices presentes neste grafo são os autores e as arestas a colaboração entre eles.

COLOCAR IMAGEM DO GRAFO

### Passo #03 - Análises da rede ​​📊​
Foram analisadas as seguintes características do grafo (com o NetworkX):
- Densidade da Rede: Que mede o quão conectados estão os autores em relação ao número máximo possível de conexões.  
- Sub-Grafo: Contendo apenas os vértices que possuem pelo menos X vizinhos (X será um valor a ser definido por vocês). Calcular a densidade desse sub-grafo.  
- Histograma dos Graus: Gráfico de histograma mostrando a distribuição do grau dos vértices da rede. O grau de um vértice representa o número de co-autores com os quais ele colaborou.
