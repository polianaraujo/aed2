# Unidade 2 Trabalho 1 - Rede de co-autoria com Gephi

## Alunos:  
- Maria Clara Moura de Freitas (20230093652)
- Poliana Ellen de Araújo (20240001289)

## Objetivo Geral:  
Este trabalho teve como objetivo utilizar o Gephi, aplicar os conhecimentos vistos no curso para analisar a rede de co-autoria dos professores permanentes do Programa de Pós-Graduação em Engenharia Elétrica e de Computação (PPgEEC).

<!-- [**Gov**](https://dados.gov.br/dados/conjuntos-dados/medicamentos-registrados-no-brasil) -->
<!-- [![Botão](https://dummyimage.com/60x20/575757/fff&text=Scopus)](https://www.scopus.com/home.uri?zone=header&origin=) -->


## Desenvolvimento

Para fazer a análise da rede, foi feito o grafo com o Gephi com os dados disponilizados pelo professor. Em seguida foi gerada uma figura destacando o k-core e o k-shell. Por fim, organizar o grafo com diferentes cores para as diferentes comunidades dos dados.

### Requisito 1

Gerar 4 grafos, utilizando como parâmetro de cor dos nós o (i) Degree Centrality, (ii) Closeness Centrality, (iii) Betweenness Centrality, (iv) Eigenvector Centrality.

Os grafos foram gerado com o Gephi, aonde o tamanho do vértice é proporcional à quantidade de vizinhos dele. Outra métrica que faria sentido ser o tamanho do vértice seria Eigenvector Centrality (Centralidade de Autovetor).
Já a métrica que está sendo utilizada para as cores dos nós é a Betweenness Centrality (Centralidade de Intermediação)

|     Degree Centrality       |    Closeness Centrality    |
|-----------------------------|----------------------------|
| ![Degree Centrality](https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/degree.png) | ![Closeness Centrality](https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/closeness.png) |


<div align="center">
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <p>Betweenness Centrality</p>
    <img src="https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/betweenness.png" alt="Betweenness Centrality" width="45%" />
  </div>
  <div style="display: inline-block; text-align: center; margin: 10px;">
    <p>Eigenvector Centrality</p>
    <img src="https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/eigenvector.png" alt="Eigenvector Centrality" width="45%" />
  </div>
</div>


<!--
<p align="center">
  <img src="https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/degree.png" alt="Degree Centrality" width="45%" />
  <img src="https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/closeness.png" alt="Closeness Centrality" width="45%" />
</p>
-->

<!-- 
<p align="center">
  <img src="https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/betweenness.png" alt="Betweenness Centrality" width="45%" />
  <img src="https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/eigenvector.png" alt="Eigenvector Centrality" width="45%" />
</p>
-->

<!-- ![Degree Centrality](https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/degree.png)

![Closeness Centrality](https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/closeness.png)

![Betweenness Centrality](https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/betweenness.png)

![Eigenvector Centrality](https://github.com/polianaraujo/aed2/blob/main/U2T1/Images/eigenvector.png) -->

### Requisito 2
O segundo requisito envolveu destacar o k-core e o k-shell da rede. O k-core representa subgrafos onde todos os nós têm pelo menos k conexões, enquanto o k-shell é obtido removendo iterativamente vértices com grau menor que k. Os tamanhos dos nós foram definidos como proporcionais ao grau (degree). As cores foram usadas para diferenciar os nós do k-core (vermelho), k-shell (azul) e demais nós (preto).


### Requisito 3
Este requisito exigiu a organização do grafo em comunidades, destacadas por cores. Cada comunidade foi identificada por meio de algoritmos específicos no Gephi. O tamanho dos vértices foi ajustado para refletir uma métrica de livre escolha, como o grau ou a centralidade de autovetor.

## Resultados

### Requisito 1


<!-- [Centralidade de Grau](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Grau.png) -->

<!-- [Centralidade de Proximidade](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Proximidade.png) -->

<!-- [Centralidade de Intermediação](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Intermediação.png)  -->

<!-- [Centralidade de Autovetor](https://github.com/polianaraujo/aed2/blob/main/U1T5_2/Images/Centralidade_de_Autovetor.png)  -->

### Requisito 2


  
### Requisito 3


    

## Conclusão
Com base na análise realizada, foi possível identificar padrões estruturais e dinâmicos na rede de co-autoria do PPgEEC. A utilização de métricas de centralidade e o estudo do k-core/k-shell permitiram compreender melhor as interações e a relevância de determinados nós. A detecção de comunidades destacou como os professores estão organizados em subgrupos de colaboração. O trabalho reforça a importância de ferramentas como o Gephi na análise de redes complexas.


## Link para a apresentação do código em vídeo

[**Youtube**]()
