# Unidade 1 Trabalho 2 - Rede de Co-Autoria

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo reforçar conceitos de grafos, utilizando a biblioteca NetworkX em Python, por meio da criação e manipulação de uma rede de co-autoria a partir de dados reais extraídos da plataforma Scopus.

## Desenvolvimento  

### Passo #01 - Extração dos Dados  
Obtemos um arquivo .csv na plataforma Scopus, contendo informações de artigos publicados por autores da Universidade Federal do Rio Grande do Norte (UFRN). Os artigos selecionados estão dentro da área de Redes Neurais, e o arquivo contém as seguintes informações:  
- Nome dos autores
- Identificadores únicos dos autores
- Título do artigo
- Ano de publicação

### Passo #02  
Criação da Rede de Co-Autoria: Utilizando os dados extraídos, vocês deverão criar uma rede de co-autoria. Neste grafo, os vértices serão os autores e as arestas representarão a colaboração entre eles. Por exemplo, se um artigo foi escrito por três autores (A1, A2, A3), as arestas (A1, A2), (A1, A3), e (A2, A3) serão criadas no grafo.

### Passo #03  
Análises na Rede: Com a rede criada, vocês deverão realizar as seguintes análises utilizando o NetworkX (use as funções já implementadas na ferramenta):  
○ Densidade da Rede: Calcular a densidade, que mede o quão conectados estão os autores em relação ao número máximo possível de conexões.  
○ Sub-Grafo: Gerar um sub-grafo contendo apenas os vértices que possuem pelo menos X vizinhos (X será um valor a ser definido por vocês). Calcular a densidade desse sub-grafo.  
○ Histograma dos Graus: Criar um gráfico de histograma mostrando a distribuição do grau dos vértices da rede. O grau de um vértice representa o número de co-autores com os quais ele colaborou.

### Passo #04  
Entrega e Avaliação:  
- O trabalho deve ser entregue em formato de repositório no GitHub, onde vocês deverão incluir todos os códigos utilizados, dados processados e um arquivo README explicando o processo.
- Na submissão mencionar o link do repositório e inserir os códigos desenvolvidos em um .zip no anexo.
- Além disso, cada grupo deverá gravar um vídeo explicativo de até 10 minutos na plataforma Loom ou software similar, descrevendo o que foi feito e justificando as escolhas feitas durante o desenvolvimento.
- O trabalho vale 1,5 pontos na Unidade 1.

### Passo #05  
Regras:
- O trabalho pode ser realizado individualmente ou em duplas.
- Vocês devem seguir boas práticas de programação, incluindo
comentários explicativos no código.
- O repositório deverá estar bem organizado, com o arquivo README
explicando o que foi feito, descrevendo resultados, mostrando imagens geradas, link da gravação do vídeo, e outras informações que acharem pertinentes.
- Indicar ainda no início do arquivo README os nomes completos dos componentes do grupo.
- Prazo: 08 de outubro, terça-feira até às 23h59.
- Os grupos estão livres para uso de ferramentas de inteligência artificial
que auxilie na solução do trabalho.
