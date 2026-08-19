# Marco 2

# Análise Estrutural e Topológica do Grafo

Este documento apresenta as representações visuais (gráficas e matemáticas) das estruturas de dados do grafo, bem como suas métricas topológicas fundamentais.

## 1. Representações Estruturais

Como o grafo possui identificadores não sequenciais ($V = \{1, 2, 5, 7, 8, 9, 10\}$), as estruturas foram mapeadas logicamente.

### A. Matriz de Adjacência (Representação Matemática)
A matriz de adjacência $A$ de dimensões $7 \times 7$ representa o grafo não direcionado. A simetria em relação à diagonal principal reflete a bidirecionalidade das arestas. O valor `1` indica a existência de aresta, e `0` a ausência.

$$
A = 
\begin{bmatrix}
  & \mathbf{1} & \mathbf{2} & \mathbf{5} & \mathbf{7} & \mathbf{8} & \mathbf{9} & \mathbf{10} \\
\mathbf{1}  & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
\mathbf{2}  & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
\mathbf{5}  & 0 & 1 & 0 & 1 & 1 & 0 & 1 \\
\mathbf{7}  & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
\mathbf{8}  & 0 & 0 & 1 & 0 & 0 & 0 & 1 \\
\mathbf{9}  & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
\mathbf{10} & 0 & 0 & 1 & 0 & 1 & 0 & 0 \\
\end{bmatrix}
$$

### B. Lista de Adjacência (Representação Gráfica em Memória)
Abaixo, a representação gráfica de como a Lista de Adjacência é estruturada na memória (um vetor/tabela de dispersão apontando para listas encadeadas de vizinhos). O símbolo `∅` indica o fim da lista encadeada para aquele vértice.

```text
[ Vértice ]      [ Listas Encadeadas de Vizinhos ]
   ( 1 )  ────► [ 9 | • ]─► ∅
   ( 2 )  ────► [ 5 | • ]─► [ 9 | • ]─► ∅
   ( 5 )  ────► [ 2 | • ]─► [ 7 | • ]─► [ 8 | • ]─► [ 10 | • ]─► ∅
   ( 7 )  ────► [ 5 | • ]─► ∅
   ( 8 )  ────► [ 5 | • ]─► [ 10 | • ]─► ∅
   ( 9 )  ────► [ 1 | • ]─► [ 2 | • ]─► ∅
  ( 10 )  ────► [ 5 | • ]─► [ 8 | • ]─► ∅
```

*Nota de Engenharia:* Para este grafo esparso, esta representação reduz o custo espacial de $O(|V|^2)$ da matriz para $O(|V| + |E|)$, otimizando a alocação de memória e a iteração sobre vizinhos.

---

## 2. Leitura e Construção Lógica

**Conjunto de Vértices ($V$):** $\{1, 2, 5, 7, 8, 9, 10\}$ (Ordem: $n = 7$)  
**Conjunto de Arestas ($E$):** $\{(1,9), (2,5), (2,9), (5,7), (5,8), (5,10), (8,10)\}$ (Tamanho: $m = 7$)

---

## 3. Métricas Topológicas

### Grau Médio
O grau $d(v)$ corresponde ao número de arestas incidentes a um vértice.

- $d(1)=1,\; d(2)=2,\; d(5)=4,\; d(7)=1,\; d(8)=2,\; d(9)=2,\; d(10)=2$
- **Somatório dos Graus:** $\sum d(v) = 14$

Pelo *Teorema do Aperto de Mãos*, $\sum d(v) = 2m$.

O **grau médio ($\bar{d}$)** indica a quantidade média de conexões por nó:

$$
\bar{d} = \frac{2m}{n} = \frac{14}{7} = 2.0
$$

**Interpretação:** Em média, cada vértice do grafo está conectado a exatos 2 outros vértices.

### Densidade de Arestas
A densidade ($D$) compara o número de arestas existentes com o máximo de arestas possíveis em um grafo simples ($E_{max}$).

- **Arestas Máximas ($E_{max}$):** $\frac{n(n-1)}{2} = \frac{7 \times 6}{2} = 21$
- **Densidade ($D$):**

$$
D = \frac{m}{E_{max}} = \frac{7}{21} \approx 0.3333
$$

**Interpretação:** O grafo possui **33,33%** das arestas possíveis, caracterizando-o fortemente como um **grafo esparso**.
