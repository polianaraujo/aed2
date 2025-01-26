
# Unidade 3 Trabalho 1 - Análise de Redes com Processamento de Linguagem Natural

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  

Realizar a análise de redes baseada em textos utilizando técnicas de processamento de linguagem natural (NLP) e ferramentas de grafos. O objetivo principal é identificar e visualizar as relações entre entidades nomeadas (como pessoas, organizações e localizações) presentes em diferentes fontes textuais, comparando suas estruturas de relacionamento e explorando métricas de rede.


## Desenvolvimento

### Requisito 1: Seleção e Preparação dos Textos
Foram selecionados dois livros do acervo do Projeto Gutenberg: "Pride and Prejudice" (Jane Austen) e "A Christmas Carol" (Charles Dickens). A partir de cada texto, extraímos fragmentos contendo dois capítulos para simplificar a análise. Após a seleção, realizamos um pré-processamento para remover caracteres indesejados, normalizar espaços e eliminar descrições de imagens.

|                       **Pride and Prejudice**          |     **Little Women**       |
|--------------------------------------------------------|----------------------------------|
| ![PaP Book](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/PaP_book.jpg) | ![LW Book](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/PaP_book.jpg) |

### Requisito 2: Análise de PoS Tagging e NER
Utilizamos a biblioteca spaCy para realizar a análise de "Part-of-Speech Tagging" (PoS Tagging) e "Named Entity Recognition" (NER). Os textos foram tokenizados em sentenças, e as entidades nomeadas classificadas como PERSON, ORG e GPE foram extraídas. Para cada sentença contendo múltiplas entidades, registramos as conexões entre elas. Como resultado, obtivemos listas de relações que alimentaram as próximas etapas da análise.

|                       **NER - Pride and Prejudice**          |     **NER - Little Women**       |
|--------------------------------------------------------------|----------------------------------|
| ```python                                                    | ```python                        |
| ['Netherfield', 'Michaelmas', 'England', 'Long', 'Morris'],  | ['Jo', 'sadly,--'],              |
| ['Lady Lucas', 'William'],                                   | ['Meg', 'tone,--'],              |
| ['Bingley', 'Lizzy'],                                        | ['Jo', 'Undine'],                |
| ['Lizzy', 'Jane', 'Lydia'],                                  | ['Faber', 'Amy'],                |
| ['Bennet', 'Bingley'],                                       | ['Meg', 'Amy'],                  |
| ```                                                          | ```                              |


### Requisito 3: Geração de Redes
Com as relações extraídas, geramos grafos representando as interações entre entidades. Cada entidade foi representada como um nó, e as conexões entre entidades na mesma sentença foram representadas como arestas. A biblioteca NetworkX foi utilizada para manipular os grafos e calcular suas propriedades, como grau dos nós e componentes conexos.

|     Pride and Prejudice     |         Little Women       |
|-----------------------------|----------------------------|
| ![PaP Graph](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/PaP_graph.png) | ![LW Graph](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/LW_graph.png) |

### Requisito 4: Análise da Rede
As redes geradas para os dois textos foram analisadas com base em métricas como:

* Grau dos nós: Identifica as entidades mais conectadas.

* Centralidade de intermediação: Mede a influência de uma entidade no fluxo de informação na rede.

* Densidade da rede: Avalia a proporção de conexões existentes em relação ao total possível.

Observamos diferenças significativas entre as redes, refletindo a variação nos estilos narrativos dos autores e no contexto dos textos.

|     Pride and Prejudice     |         Little Women       |
|-----------------------------|----------------------------|
| ![PaP Graph Ego](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/PaP_graph_elizab.png) | ![LW Graph Ego](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/LW_graph_amy.png) |

### Requisito 5: Visualização e Produção do Grafo
O grafo foi visualizado utilizando ferramentas como NetworkX e Gephi. Além disso, um grafo interativo foi gerado e publicado em uma página web, permitindo a exploração dinâmica das relações entre as entidades extraídas. A visualização interativa foi fundamental para destacar a estrutura da rede e suas propriedades.

|     Pride and Prejudice     |         Little Women       |
|-----------------------------|----------------------------|
| ![PaP Graph](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/PaP.png) | ![LW Graph](https://github.com/polianaraujo/aed2/blob/main/U3T1/Imagens/PaP.png) |

## Conclusão
A análise realizada demonstrou como é possível explorar relações em textos narrativos por meio de técnicas de NLP e teoria de grafos. As redes geradas permitiram identificar as principais entidades e suas interações, fornecendo insights sobre a estrutura das histórias e os papéis desempenhados pelos personagens.

## Formas de executar o código

O código completo está disponível neste repositório do Github. Para executar o código é recomendável usar o Google Colab, que já possui as bibliotecas necessárias. No caso do uso de outro ambiente, talvez seja necessário instalar algumas dessas bibliotecas.


## Links
Podcast:

Grafo Interativo Pride and Prejudice: https://mclarafreitas.github.io/netdeployu3t1/network/

Grafo Interativo Little Women: https://mclarafreitas.github.io/netdeployu3t1/network2/

## Referências
https://www.gutenberg.org/files/1342/1342-0.txt

https://www.gutenberg.org/files/37106/37106-0.txt

https://spacy.io/

https://networkx.org/

https://github.com/ivanovitchm/datastructure

