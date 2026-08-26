# Execução e Análise de Busca no Grafo

Considerando as métricas solicitadas (tempos de descoberta e término, estados de visita, predecessores), o algoritmo que perfeitamente modela esses requisitos na teoria dos grafos é a **Busca em Profundidade (DFS - Depth-First Search)**. 

Este documento apresenta a execução analítica da DFS sobre o nosso grafo esparso, assumindo a ordem crescente dos identificadores para desempate na escolha dos vizinhos.

## 1. Estados de Visita (Coloração de Vértices)
A DFS utiliza três estados para rastrear o progresso e evitar ciclos infinitos:
*   **Branco (Não descoberto):** O vértice ainda não foi alcançado pela busca.
*   **Cinza (Descoberto):** O vértice foi alcançado (tempo de descoberta $d$), mas seus vizinhos ainda estão sendo explorados.
*   **Preto (Finalizado):** Todos os vizinhos do vértice foram explorados (tempo de término $f$).

No início, todos os vértices $\{1, 2, 5, 7, 8, 9, 10\}$ estão **Brancos**.

---

## 2. Execução Manual (Passo a Passo)
Iniciamos a busca a partir do vértice de menor ID, o **vértice 1**, inicializando o relógio de tempo (t = 1).

1.  **t=1:** Visita `1` (Branco $\rightarrow$ Cinza). $d[1] = 1$. Vizinho disponível: `9`.
2.  **t=2:** Visita `9` (Branco $\rightarrow$ Cinza). $d[9] = 2$. Vizinhos: `1` (Cinza), `2`. Avança para `2`.
3.  **t=3:** Visita `2` (Branco $\rightarrow$ Cinza). $d[2] = 3$. Vizinhos: `5`, `9` (Cinza). Avança para `5`.
4.  **t=4:** Visita `5` (Branco $\rightarrow$ Cinza). $d[5] = 4$. Vizinhos: `2` (Cinza), `7`, `8`, `10`. Avança para `7`.
5.  **t=5:** Visita `7` (Branco $\rightarrow$ Cinza). $d[7] = 5$. Vizinho: `5` (Cinza). Fim dos vizinhos de `7`.
6.  **t=6:** Finaliza `7` (Cinza $\rightarrow$ Preto). $f[7] = 6$. Retorna para `5`.
7.  **t=7:** De volta ao `5`, próximo vizinho branco é `8`. Visita `8` (Branco $\rightarrow$ Cinza). $d[8] = 7$.
8.  **t=8:** Em `8`, vizinhos: `5` (Cinza), `10`. Avança para `10`.
9.  **t=9:** Visita `10` (Branco $\rightarrow$ Cinza). $d[10] = 8$. Vizinhos: `5` (Cinza), `8` (Cinza). Como ambos já foram descobertos, fim dos vizinhos. Aresta (10,5) é detectada como aresta de retorno (*back edge*).
10. **t=10:** Finaliza `10` (Cinza $\rightarrow$ Preto). $f[10] = 9$. Retorna para `8`.
11. **t=11:** De volta ao `8`. Fim dos vizinhos. Finaliza `8`. $f[8] = 10$. Retorna para `5`.
12. **t=12:** De volta ao `5`. O vizinho `10` já é Preto. Fim dos vizinhos. Finaliza `5`. $f[5] = 11$. Retorna para `2`.
13. **t=13:** De volta ao `2`. Fim dos vizinhos. Finaliza `2`. $f[2] = 12$. Retorna para `9`.
14. **t=14:** De volta ao `9`. Fim dos vizinhos. Finaliza `9`. $f[9] = 13$. Retorna para `1`.
15. **t=15:** De volta ao `1`. Fim dos vizinhos. Finaliza `1`. $f[1] = 14$.

*A busca é encerrada, pois não restam vértices brancos no grafo.*

---

## 3. Tempos de Descoberta ($d$) e Término ($f$) e Predecessores ($\pi$)

A tabela abaixo sumariza o estado final da execução, onde $\pi$ representa o nó pai na árvore de busca:

| Vértice ($v$) | Descoberta ($d[v]$) | Término ($f[v]$) | Predecessor ($\pi[v]$) |
|:---:|:---:|:---:|:---:|
| **1**  | 1 | 14 | $Nil$ (Raiz) |
| **9**  | 2 | 13 | 1 |
| **2**  | 3 | 12 | 9 |
| **5**  | 4 | 11 | 2 |
| **7**  | 5 | 6  | 5 |
| **8**  | 7 | 10 | 5 |
| **10** | 8 | 9  | 8 |

---

## 4. Árvore de Busca e Alcançabilidade

### Alcançabilidade
A partir do vértice inicial (1), foi possível transitar para o estado **Preto** em todos os $V$ vértices do grafo. Isso comprova que **o grafo é um Componente Conexo único**, ou seja, qualquer nó é alcançável a partir de qualquer outro.

### Árvore de Busca em Profundidade (Spanning Tree)
As arestas percorridas para descobrir novos vértices brancos formam a árvore de busca. No nosso grafo, as arestas da árvore são definidas pelos predecessores:
*   **Arestas da Árvore (Tree Edges):** $\{(1,9), (9,2), (2,5), (5,7), (5,8), (8,10)\}$

Qualquer aresta que não pertença a esta árvore e ligue um vértice a um ancestral na árvore é uma **Aresta de Retorno (Back Edge)**. 
*   **Arestas de Retorno:** Aresta $(10,5)$, descoberta no passo 9, pois quando estávamos em 10, o vértice 5 ainda estava na pilha de execução (Cinza). A presença dessa aresta comprova matematicamente a existência de um **ciclo** no grafo (o ciclo $5-8-10-5$).

---

## 5. Aplicabilidade ao Problema e Adaptações

### Aplicabilidade
Como estudante de engenharia, compreender a DFS com esses atributos (tempos, cores, predecessores) permite resolver problemas complexos como:
1.  **Detecção de Ciclos:** Como evidenciado pela aresta de retorno (10,5). Fundamental em detecção de impasses (deadlocks) em sistemas operacionais ou verificação de circuitos lógicos sem loops fechados.
2.  **Identificação de Componentes Conexos:** Se o grafo fosse desconexo, a execução manual reiniciaria em um nó branco, permitindo classificar sub-redes isoladas.
3.  **Ordenação Topológica:** Embora restrita a grafos direcionados (DAGs), ordenar os nós pelo tempo de término decrescente ($f[v]$) resolve cadeias de dependências em compilação de software (ex: `make`) ou grade de disciplinas da faculdade.

### Adaptação Parcial quando Pertinente
*   **Busca por Alvo Específico (Early Exit):** Se o objetivo do problema for encontrar um vértice específico (ex: verificar se o nó 10 existe na rede), podemos adaptar o algoritmo para abortar a execução no passo 9 ($d[10]=8$), retornando imediatamente o caminho construído via array de predecessores $\pi$, economizando processamento.
*   **Limite de Profundidade (Iterative Deepening DFS):** Em contextos de árvores/grafos muito profundos (como modelagem de estados ou I.A. básica), o rastreio de descoberta pode ser podado a uma profundidade máxima ($L$), evitando *stack overflow* da memória em vértices muito distantes da raiz.
