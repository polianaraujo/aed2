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


![Centralidade de Grau](https://github.com/polianaraujo/aed2/blob/main/U1T5/Images/Centralidade_de_Grau.png)

- Centralidade de Proximidade
Essa métrica mede o quão próximo um nó está de todos os outros nós da rede. Isso é feito calculando a soma das distâncias mais curtas (em termos de número de arestas) entre o nó e todos os outros nós. Portanto, vai informar a distância média para todos os outros nós.


![Centralidade de Proximidade](https://github.com/polianaraujo/aed2/blob/main/U1T5/Images/Centralidade_de_Proximidade.png)


- Centralidade de Intermediação
Ela mede quantas vezes um nó aparece como um intermediário em caminhos mais curtos entre outros pares de nós. Em outras palavras, quantas vezes um nó atua como um "ponte" entre outros nós.


![Centralidade de Intermediação](https://github.com/polianaraujo/aed2/blob/main/U1T5/Images/Centralidade_de_Intermediação.png)

- Centralidade de Autovetor
Pontuação de autoridade baseada na pontuação dos vizinhos. Não apenas considera o número de conexões que um nó possui, mas também a qualidade dessas conexões. Um nó é considerado importante se estiver conectado a outros nós que também são importantes.


![Centralidade de Autovetor](https://github.com/polianaraujo/aed2/blob/main/U1T5/Images/Centralidade_de_Autovetor.png)


### Requisito 2
Realizamos a análise dos graus dos nós utilizando gráficos de CDF e PDF, que fornecem informações sobre a distribuição de conexões na rede. A análise foi realizada com a biblioteca Seaborn para visualização. Os gráficos mostram a distribuição dos graus e nos permitem observar a concentração de nós com poucos ou muitos graus.

### Requisito 3
Para observar as relações entre as diferentes métricas, realizamos uma análise multivariada com PairGrid, que permite identificar correlações visuais entre as métricas. Esse processo destaca como as métricas podem estar relacionadas em uma análise conjunta.

### Requisito 4
Para identificar e visualizar a estrutura de núcleo (core) e casca (shell) da rede, podemos usar o número do núcleo de cada nó, que é calculado pela função nx.core_number(). O núcleo de um grafo é composto por nós que têm pelo menos um certo número de conexões, enquanto a casca é formada por nós que estão fora do núcleo.

Aqui está um código que utiliza o número do núcleo para separar os nós em diferentes camadas e, em seguida, plota a rede, destacando essas camadas.

o grafo contém laços (self-loops), que não são permitidos ao calcular o número do núcleo em NetworkX. Para resolver esse problema, você precisa remover esses laços do grafo antes de calcular o número do núcleo.

##Conclusão
As análises revelaram a distribuição da mobilidade e conectividade no entorno da UFRN, com bairros como Lagoa Nova e Capim Macio mostrando altos valores de centralidade. Com base nas métricas, identificamos locais potenciais para a instalação de dock-stations de bicicletas compartilhadas, considerando áreas com alta conectividade e proximidade.

Essa análise é uma base para futuras decisões de mobilidade na região, auxiliando na criação de um sistema de transporte mais integrado e sustentável ao redor da UFRN.