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

### Requisito 1

### Requisito 2

### Requisito 3

### Requisito 4

Para identificar e visualizar a estrutura de núcleo (core) e casca (shell) da rede, podemos usar o número do núcleo de cada nó, que é calculado pela função nx.core_number(). O núcleo de um grafo é composto por nós que têm pelo menos um certo número de conexões, enquanto a casca é formada por nós que estão fora do núcleo.

Aqui está um código que utiliza o número do núcleo para separar os nós em diferentes camadas e, em seguida, plota a rede, destacando essas camadas.

o grafo contém laços (self-loops), que não são permitidos ao calcular o número do núcleo em NetworkX. Para resolver esse problema, você precisa remover esses laços do grafo antes de calcular o número do núcleo.