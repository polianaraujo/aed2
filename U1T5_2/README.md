# Unidade 1 Trabalho 5 - Mobilidade ao entorno da UFRN

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo (i) utilizar métricas de centralidade e gerar imagens da rede destacadas por elas, (ii) fazer a análise CDF e PDF dos graus dos nós, (iii) fazer uma análise multivariada das métricas de centralidade e (iv) analisar o core/shell da rede.

<!-- [**Gov**](https://dados.gov.br/dados/conjuntos-dados/medicamentos-registrados-no-brasil) -->
<!-- [![Botão](https://dummyimage.com/60x20/575757/fff&text=Scopus)](https://www.scopus.com/home.uri?zone=header&origin=) -->


## Desenvolvimento

O trabalho foi desenvolvido utilizando os dados obtidos dos bairros de Candelária, Capim Macio e Lagoa Nova, retirando a UFRN.

![Grafo de Natal](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/rede_natal.png)

### Requisito 1 - Métricas de centralidade

- Centralidade de Grau: 
Essa métrica vai informar o número de conexões diretas (arestas) que um nó possui, ou seja, é a contagem de vizinhos de um nó. Um nó com um alto grau de centralidade é considerado "importante" porque está diretamente conectado a muitos outros nós.


![Centralidade de Grau](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Grau.png)

- Centralidade de Proximidade: 
Essa métrica mede o quão próximo um nó está de todos os outros nós da rede. Isso é feito calculando a soma das distâncias mais curtas (em termos de número de arestas) entre o nó e todos os outros nós. Portanto, vai informar a distância média para todos os outros nós.


![Centralidade de Proximidade](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Proximidade.png)


- Centralidade de Intermediação: 
Ela mede quantas vezes um nó aparece como um intermediário em caminhos mais curtos entre outros pares de nós. Em outras palavras, quantas vezes um nó atua como um "ponte" entre outros nós.


![Centralidade de Intermediação](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Intermediação.png)

- Centralidade de Autovetor: 
Pontuação de autoridade baseada na pontuação dos vizinhos. Não apenas considera o número de conexões que um nó possui, mas também a qualidade dessas conexões. Um nó é considerado importante se estiver conectado a outros nós que também são importantes.


![Centralidade de Autovetor](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Autovetor.png)


### Requisito 2

Realizamos a análise dos graus dos nós utilizando gráficos de CDF e PDF, que fornecem informações sobre a distribuição de conexões na rede. A análise foi realizada com a biblioteca Seaborn para visualização. Os gráficos mostram a distribuição dos graus e nos permitem observar a concentração de nós com poucos ou muitos graus.

![Cumulative Density Function](https://github.com/polianaraujo/aed2/blob/7acd2621b8ecd4f82aae876cb91d2e0858c85d33/U1T5_2/Images/funcao_densidade_cumulativa.png)

![Probability Density Function](https://github.com/polianaraujo/aed2/blob/7acd2621b8ecd4f82aae876cb91d2e0858c85d33/U1T5_2/Images/funcao_densidade_probabilidade.png)

### Requisito 3
Para observar as relações entre as diferentes métricas, realizamos uma análise multivariada com PairGrid, que permite identificar correlações visuais entre as métricas. Esse processo destaca como as métricas podem estar relacionadas em uma análise conjunta.

### Requisito 4
Para identificar e visualizar a estrutura de núcleo (core) e casca (shell) da rede, podemos usar o número do núcleo de cada nó, que é calculado pela função nx.core_number(). O núcleo de um grafo é composto por nós que têm pelo menos um certo número de conexões, enquanto a casca é formada por nós que estão fora do núcleo.

Aqui está um código que utiliza o número do núcleo para separar os nós em diferentes camadas e, em seguida, plota a rede, destacando essas camadas.

o grafo contém laços (self-loops), que não são permitidos ao calcular o número do núcleo em NetworkX. Para resolver esse problema, você precisa remover esses laços do grafo antes de calcular o número do núcleo.

## Resultados

### Requisito 1

- Centralidade de Grau: 
O grafo se mostra bem uniforme, indicante que a maioria dos nós possuiem uma quantidade semelhante de vizinhos. O bairro de Lagoa Nova aparenta ter mais nós com mais vizinhos na região central.

- Centralidade de Proximidade: 
O grafo mostra que os nós centrais estão próximos de mais nós, enquanto os nós mais aos extremos estão próximos de menos nós.

- Centralidade de Intermediação: 
Já que essa métrica mede quantas vezes um nó aparece como um intermediário em caminhos mais curtos entre outros pares de nós, o grafo indica que os nós que mais atuam como "pontes", em espeical, nós em Candelária e na Avenida Senador Salgado Filho.

- Centralidade de Autovetor: 
O grafo obtido mostra que os nós na região nordeste de Lagoa Nova possui os nós que possuem grande influência.

### Requisito 2

No primeiro gráfico, temos a Função de Densidade de Probabilidade (PDF) sobreposta ao histograma dos graus dos nós na rede. A PDF mostra a probabilidade de ocorrência de um determinado grau. Observamos que:

* O grau mais frequente na rede é em torno de 6, indicando que a maioria dos nós (ou locais de interseção na rede) tende a ter aproximadamente 6 conexões.
* Há uma leve assimetria, pois a distribuição tem uma "cauda" à direita, indicando que existem alguns nós com grau superior a 6, embora sejam menos frequentes.
* Esse pico principal sugere uma conectividade relativamente alta em alguns pontos da rede, o que pode indicar áreas onde há um fluxo significativo de acessos.

O segundo gráfico exibe a Função de Densidade Acumulada (CDF), que mostra a probabilidade acumulada até um determinado grau. Isso permite ver, por exemplo, que:

* Cerca de 80% dos nós têm um grau menor ou igual a 6, confirmando que essa é uma região central da distribuição de graus.
* A curva da CDF se estabiliza perto de 1 (ou 100%) após o grau 8, o que sugere que poucos nós têm graus superiores a este valor.
* Esse comportamento acumulativo ajuda a identificar a presença de uma distribuição concentrada, com uma pequena proporção de nós mais conectados que poderiam funcionar como hubs locais na rede.

Os resultados sugerem uma estrutura de rede com alta densidade de conexões locais em torno de nós específicos, o que é típico de redes urbanas bem conectadas. Esse padrão pode ser um indicativo de boas oportunidades para instalar dock-stations em pontos com graus mais altos, onde o fluxo de bicicletas seria potencialmente maior. Esses gráficos também indicam que a rede não possui uma estrutura com graus muito dispersos, o que poderia sugerir uma topologia bem planejada para suportar a mobilidade.
  
### Requisito 3

Esse gráfico de análise multivariada das métricas de centralidade apresenta a distribuição e as relações entre quatro medidas de centralidade (degree, closeness, betweenness e eigenvector) na rede de mobilidade.
1. Degree Centrality:
  * O gráfico de densidade (primeira linha e coluna) indica que a maioria dos nós possui valores baixos de grau, o que sugere uma rede dispersa, com poucos nós altamente conectados.
  * Na análise cruzada, o grau parece ter pouca correlação com as outras métricas de centralidade, exceto uma leve correlação com a intermediação (Betweenness), indicando que nós com um grau maior podem também desempenhar um papel de intermediação, conectando partes diferentes da rede
    
2. Closeness Centrality:
  * O gráfico de densidade para a proximidade mostra uma concentração em torno de valores intermediários, sugerindo que muitos nós estão a uma distância média dos demais.
  * A proximidade parece ter alguma correlação com a intermediação (betweenness), mas apresenta uma dispersão significativa quando cruzada com o grau (Degree Centrality) e o autovetor (Eigenvector). Isso pode indicar que estar "perto" de outros nós nem sempre está relacionado a ter um alto grau ou a importância em termos de intermediação.

3. Betweenness Centrality:
  * A intermediação apresenta uma distribuição altamente concentrada em valores baixos, com alguns picos para valores mais altos, indicando que poucos nós atuam como pontos de passagem principais dentro da rede.
  * A intermediação possui uma correlação mais clara com a proximidade e uma menor com o autovetor, sugerindo que nós centrais na rede em termos de passagem podem não ser os mais bem conectados (grau) ou importantes em termos de eigenvector.
    
4. Eigenvector Centrality:
  * A centralidade de autovetor também está concentrada em valores baixos, indicando que a maioria dos nós não tem grande importância em termos de influenciar outros nós na rede.
  * Observa-se uma relação entre o autovetor e a proximidade, indicando que os nós mais influentes estão mais próximos de outros nós na rede.

A análise multivariada das métricas de centralidade sugere uma rede onde poucos nós possuem um papel destacado, seja por conexões (grau), proximidade, intermediação ou influência (autovetor). Esse tipo de estrutura pode indicar áreas específicas com alta importância para a mobilidade, o que é crucial para decidir a localização de dock-stations. A baixa correlação entre algumas métricas sugere que diferentes tipos de centralidade devem ser considerados para garantir a cobertura e acessibilidade na rede de bicicletas.
    
### Requisito 4

1. Core/Shell (k-core):
A primeira imagem destaca a separação entre o 1-shell (em azul) e o 2-core (em vermelho).   
  * Distribuição: A maior parte dos nós da rede está no 2-core, indicando uma conectividade mais forte e centralizada. Esses nós centrais são mais interligados e formam uma espécie de "esqueleto" da rede, que mantém a estrutura coesa.
  * Periferia (1-shell): Os nós em azul representam os 1-shell, ou seja, aqueles nós que têm menor conectividade e estão mais na periferia da rede. Isso sugere áreas ou pontos da rede com menos conexões diretas, possivelmente indicando ruas menos centrais ou áreas com menor fluxo de mobilidade.
  * Interpretação: Essa estrutura com um núcleo denso e uma periferia menos conectada é comum em redes de mobilidade urbana. O núcleo (2-core) provavelmente representa vias principais e áreas com maior centralidade na mobilidade, enquanto a periferia inclui ruas locais com menos acessibilidade.

2. Padrões Sociais de Grau (Cores de Grau):
Na segunda imagem, vemos uma visualização colorida que representa diferentes padrões de grau dos nós (número de conexões):
  * Gradiente de Cores: Os nós têm colorações variadas, do azul (graus mais baixos) ao vermelho (graus mais altos), o que permite ver o quão conectados estão os diferentes pontos da rede. As áreas em vermelho indicam regiões com maior número de conexões, possivelmente áreas com maior fluxo e conectividade na mobilidade dos bairros próximos à UFRN.
  * Clusterização de Altos Graus: Nós com graus elevados, destacados em cores mais quentes (próximas do vermelho), provavelmente representam hubs ou pontos centrais na rede de mobilidade, como rotas principais que interconectam diversas áreas.
  * Distribuição do Grau: A variação de cores mostra uma distribuição de grau heterogênea, onde alguns nós possuem muitos vizinhos (conexões), enquanto outros são menos conectados. Essa heterogeneidade é típica de redes de mobilidade, onde algumas ruas ou avenidas concentram mais tráfego e interligam diferentes partes da cidade.

Essas duas análises juntas sugerem uma rede de mobilidade com uma estrutura central forte (core) e periferias mais fragmentadas (shells). O núcleo da rede conecta áreas de grande movimento, enquanto as áreas periféricas, com menor grau de conectividade, indicam possíveis regiões de acesso secundário. Essa configuração é comum em redes urbanas e reflete a importância de rotas principais na mobilidade e acessibilidade dos bairros analisados.

## Conclusão

Este trabalho permitiu uma compreensão detalhada da mobilidade urbana ao redor da UFRN, revelando a importância de vias centrais para a coesão da rede de transporte nos bairros estudados. Com base nas métricas, identificamos locais potencias para a instalação de dock-stations de bicicletas compartilhadas, considerando áreas com alta conectividade e proximidade. As metodologias aplicadas, envolvendo análise de centralidade e estrutura core/shell, fornecem uma base robusta para futuras análises de mobilidade e planejamento urbano. No futuro, recomenda-se expandir o estudo para incluir dados temporais e informações sobre fluxos de tráfego, o que pode enriquecer a análise e fornecer uma visão ainda mais abrangente da dinâmica de mobilidade nesses bairros.
