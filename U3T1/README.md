
# Unidade 3 Trabalho 1 - Análise de Redes com Processamento de Linguagem Natural

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  

Realizar a análise de redes baseada em textos utilizando técnicas de processamento de linguagem natural (NLP) e ferramentas de grafos. O objetivo principal é identificar e visualizar as relações entre entidades nomeadas (como pessoas, organizações e localizações) presentes em diferentes fontes textuais, comparando suas estruturas de relacionamento e explorando métricas de rede.


## Desenvolvimento

### Requisito 1: Seleção e Preparação dos Textos
Foram selecionados dois livros do acervo do Projeto Gutenberg: "Pride and Prejudice" (Jane Austen) e "A Christmas Carol" (Charles Dickens). A partir de cada texto, extraímos fragmentos contendo dois capítulos para simplificar a análise. Após a seleção, realizamos um pré-processamento para remover caracteres indesejados, normalizar espaços e eliminar descrições de imagens.

### Requisito 2: Análise de PoS Tagging e NER
Utilizamos a biblioteca spaCy para realizar a análise de "Part-of-Speech Tagging" (PoS Tagging) e "Named Entity Recognition" (NER). Os textos foram tokenizados em sentenças, e as entidades nomeadas classificadas como PERSON, ORG e GPE foram extraídas. Para cada sentença contendo múltiplas entidades, registramos as conexões entre elas. Como resultado, obtivemos listas de relações que alimentaram as próximas etapas da análise.

### Requisito 3: Geração de Redes
Com as relações extraídas, geramos grafos representando as interações entre entidades. Cada entidade foi representada como um nó, e as conexões entre entidades na mesma sentença foram representadas como arestas. A biblioteca NetworkX foi utilizada para manipular os grafos e calcular suas propriedades, como grau dos nós e componentes conexos.

### Requisito 4: Análise da Rede
As redes geradas para os dois textos foram analisadas com base em métricas como:

* Grau dos nós: Identifica as entidades mais conectadas.

* Centralidade de intermediação: Mede a influência de uma entidade no fluxo de informação na rede.

* Densidade da rede: Avalia a proporção de conexões existentes em relação ao total possível.

Observamos diferenças significativas entre as redes, refletindo a variação nos estilos narrativos dos autores e no contexto dos textos.

### Requisito 5: Visualização e Produção do Grafo




## Conclusão


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

