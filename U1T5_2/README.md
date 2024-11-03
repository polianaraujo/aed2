# Unidade 1 Trabalho 5 - Mobilidade ao entorno da UFRN

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo (i) utilizar métricas de centralidade e gerar imagens da rede destacadas por elas, (ii) fazer a análise CDF e PDF dos graus dos nós, (iii) fazer uma análise multivariada das métricas de centralidade e (iv) analisar o core/shell da rede.

<!-- [**Gov**](https://dados.gov.br/dados/conjuntos-dados/medicamentos-registrados-no-brasil) -->
<!-- [![Botão](https://dummyimage.com/60x20/575757/fff&text=Scopus)](https://www.scopus.com/home.uri?zone=header&origin=) -->


## Desenvolvimento

Com base nos valores fornecidos:

Norte: -5.795
Sul: -5.821
Leste: -35.194
Oeste: -35.227
Essas coordenadas representam uma área que inclui partes dos bairros de Natal, RN. Ao analisar essas coordenadas:

Latitude Norte (-5.795) e Latitude Sul (-5.821): O limite norte está em -5.795, o que é mais ao norte do centro da cidade, enquanto o limite sul está em -5.821, que é mais ao sul. Essas latitudes podem abranger partes de bairros como Lagoa Nova, Capim Macio e Neópolis.

Longitude Leste (-35.194) e Longitude Oeste (-35.227): Esses limites de longitude vão de -35.227 (oeste) a -35.194 (leste), o que pode abranger áreas próximas ao Parque das Dunas e parte da Praia de Ponta Negra.

### Requisito 1 - Métricas de centralidade

- Centralidade de Grau
Essa métrica vai informar o número de conexões diretas (arestas) que um nó possui, ou seja, é a contagem de vizinhos de um nó. Um nó com um alto grau de centralidade é considerado "importante" porque está diretamente conectado a muitos outros nós.


![Centralidade de Grau](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Grau.png)

- Centralidade de Proximidade
Essa métrica mede o quão próximo um nó está de todos os outros nós da rede. Isso é feito calculando a soma das distâncias mais curtas (em termos de número de arestas) entre o nó e todos os outros nós. Portanto, vai informar a distância média para todos os outros nós.


![Centralidade de Proximidade](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Proximidade.png)


- Centralidade de Intermediação
Ela mede quantas vezes um nó aparece como um intermediário em caminhos mais curtos entre outros pares de nós. Em outras palavras, quantas vezes um nó atua como um "ponte" entre outros nós.


![Centralidade de Intermediação](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Intermediação.png)

- Centralidade de Autovetor
Pontuação de autoridade baseada na pontuação dos vizinhos. Não apenas considera o número de conexões que um nó possui, mas também a qualidade dessas conexões. Um nó é considerado importante se estiver conectado a outros nós que também são importantes.


![Centralidade de Autovetor](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Autovetor.png)


### Requisito 2
Realizamos a análise dos graus dos nós utilizando gráficos de CDF e PDF, que fornecem informações sobre a distribuição de conexões na rede. A análise foi realizada com a biblioteca Seaborn para visualização. Os gráficos mostram a distribuição dos graus e nos permitem observar a concentração de nós com poucos ou muitos graus.

![Cumulative Density Function](https://github.com/polianaraujo/aed2/blob/7acd2621b8ecd4f82aae876cb91d2e0858c85d33/U1T5_2/Images/cumulative_density_function.png)

![Probability Density Function](https://github.com/polianaraujo/aed2/blob/7acd2621b8ecd4f82aae876cb91d2e0858c85d33/U1T5_2/Images/probability_density_function.png)

### Requisito 3
Para observar as relações entre as diferentes métricas, realizamos uma análise multivariada com PairGrid, que permite identificar correlações visuais entre as métricas. Esse processo destaca como as métricas podem estar relacionadas em uma análise conjunta.

### Requisito 4
Para identificar e visualizar a estrutura de núcleo (core) e casca (shell) da rede, podemos usar o número do núcleo de cada nó, que é calculado pela função nx.core_number(). O núcleo de um grafo é composto por nós que têm pelo menos um certo número de conexões, enquanto a casca é formada por nós que estão fora do núcleo.

Aqui está um código que utiliza o número do núcleo para separar os nós em diferentes camadas e, em seguida, plota a rede, destacando essas camadas.

o grafo contém laços (self-loops), que não são permitidos ao calcular o número do núcleo em NetworkX. Para resolver esse problema, você precisa remover esses laços do grafo antes de calcular o número do núcleo.

## Resultados
Requisito 1 -

Requisito 2 -
No primeiro gráfico, temos a Função de Densidade de Probabilidade (PDF) sobreposta ao histograma dos graus dos nós na rede. A PDF mostra a probabilidade de ocorrência de um determinado grau. Observamos que:
* O grau mais frequente na rede é em torno de 6, indicando que a maioria dos nós (ou locais de interseção na rede) tende a ter aproximadamente 6 conexões.
* Há uma leve assimetria, pois a distribuição tem uma "cauda" à direita, indicando que existem alguns nós com grau superior a 6, embora sejam menos frequentes.
* Esse pico principal sugere uma conectividade relativamente alta em alguns pontos da rede, o que pode indicar áreas onde há um fluxo significativo de acessos.

O segundo gráfico exibe a Função de Densidade Acumulada (CDF), que mostra a probabilidade acumulada até um determinado grau. Isso permite ver, por exemplo, que:
* Cerca de 80% dos nós têm um grau menor ou igual a 6, confirmando que essa é uma região central da distribuição de graus.
* A curva da CDF se estabiliza perto de 1 (ou 100%) após o grau 8, o que sugere que poucos nós têm graus superiores a este valor.
* Esse comportamento acumulativo ajuda a identificar a presença de uma distribuição concentrada, com uma pequena proporção de nós mais conectados que poderiam funcionar como hubs locais na rede.

Os resultados sugerem uma estrutura de rede com alta densidade de conexões locais em torno de nós específicos, o que é típico de redes urbanas bem conectadas. Esse padrão pode ser um indicativo de boas oportunidades para instalar dock-stations em pontos com graus mais altos, onde o fluxo de bicicletas seria potencialmente maior. Esses gráficos também indicam que a rede não possui uma estrutura com graus muito dispersos, o que poderia sugerir uma topologia bem planejada para suportar a mobilidade.
  
Requisito 3 -
Esse gráfico de análise multivariada das métricas de centralidade apresenta a distribuição e as relações entre quatro medidas de centralidade (degree, closeness, betweenness e eigenvector) na rede de mobilidade.
1. Degree Centrality:
  * No histograma da diagonal, a distribuição do grau mostra picos distintos, indicando que a maioria dos nós possui graus específicos, possivelmente alinhados aos padrões de conectividade da rede.
  * As distribuições nos gráficos de dispersão sugerem que o grau centralidade tem uma correlação limitada com as demais métricas.
    
2. Closeness Centrality:
  * A distribuição da centralidade de proximidade apresenta uma maior densidade entre os valores de 0,04 e 0,06.
  * Existe uma correlação positiva entre closeness e degree, o que indica que nós com maior conectividade (grau) também tendem a ter um acesso mais rápido aos demais nós da rede.
  * A relação entre closeness e betweenness é bem interessante, pois mostra um padrão em que alguns nós com alta proximidade também têm valores mais altos de intermediação (betweenness), sugerindo que esses nós servem como pontos de ligação entre várias partes da rede.

3. Betweenness Centrality:
  * A centralidade de intermediação (betweenness) tem uma distribuição com uma densidade maior próxima a valores baixos, sugerindo que a maioria dos nós não está frequentemente em caminhos mais curtos entre outros nós. No entanto, alguns nós com valores de betweenness mais altos parecem desempenhar um papel importante como "hubs" na rede, como visto na correlação com closeness.
    
4. Eigenvector Centrality:
   * A centralidade de autovetor (eigenvector) também possui uma densidade maior em valores baixos, o que indica que poucos nós têm uma alta centralidade de autovetor. Isso sugere que apenas alguns nós estão conectados a outros nós altamente conectados, sendo estes possivelmente os "nós influentes" ou centrais na rede.
  * A correlação com degree é notável, onde nós com maior grau tendem a ter uma centralidade de autovetor mais alta, sugerindo que esses nós conectam-se a outros nós importantes.

Essas análises mostram que há uma diversidade de conectividade e influência na rede. Os nós que apresentam alta centralidade em múltiplas métricas (especialmente closeness e betweenness) .... TERMIANR DE ESCREVER
    
Requisito 4 - 
1. Padrões Sociais de Grau
No primeiro gráfico (representado pelo mapa de calor de grau), observamos como os nós estão distribuídos em termos de conectividade (grau) dentro da rede. A coloração mais quente (vermelha) indica áreas de maior concentração de nós com altos valores de grau, enquanto as cores frias (azul) indicam nós com grau mais baixo. Esse padrão ajuda a identificar clusters ou zonas onde há uma maior densidade de conexões, sugerindo pontos de alta acessibilidade e importância dentro da rede.

Este tipo de visualização é útil para apontar onde existem nós altamente conectados, que podem servir como pontos centrais para o tráfego e a mobilidade no entorno da UFRN. Esses nós são potenciais locais para dock-stations de bicicletas, pois eles estão acessíveis a partir de vários pontos na rede.

3. Estrutura Core/Shell
O segundo gráfico apresenta a análise de core/shell da rede. Nesta análise, os nós da rede foram classificados de acordo com o número de conexões, separando-os em diferentes camadas:
1-shell: Representado em azul, inclui nós periféricos com menor conectividade.
2-core: Representado em vermelho, inclui nós mais conectados e centrais na estrutura da rede.

Observamos que a rede possui uma alta densidade de nós no 2-core, mostrando que há uma boa conectividade interna. Esses nós centrais (2-core) indicam a existência de uma estrutura robusta na rede, onde muitos pontos estão conectados de maneira eficiente. Isso é benéfico para a mobilidade, pois esses nós são mais resilientes a falhas e mais acessíveis. A presença de um core forte também sugere que existem caminhos alternativos para alcançar diversos pontos na rede, o que é ideal para sistemas de mobilidade urbana.

A análise do core/shell confirma que a rede possui uma estrutura central densa e conectada, com nós principais que atuam como hubs de mobilidade. Esses hubs (2-core) seriam ideais para receber infraestrutura adicional, como dock-stations, pois oferecem maior acessibilidade e conectividade na rede. A estrutura periférica (1-shell) poderia ser conectada ou ampliada para melhorar o acesso às áreas menos conectadas, promovendo uma distribuição mais uniforme da mobilidade ao longo do entorno da UFRN.

## Conclusão
As análises revelaram a distribuição da mobilidade e conectividade no entorno da UFRN, com bairros como Lagoa Nova e Capim Macio mostrando altos valores de centralidade. Com base nas métricas, identificamos locais potenciais para a instalação de dock-stations de bicicletas compartilhadas, considerando áreas com alta conectividade e proximidade.

Essa análise é uma base para futuras decisões de mobilidade na região, auxiliando na criação de um sistema de transporte mais integrado e sustentável ao redor da UFRN.
