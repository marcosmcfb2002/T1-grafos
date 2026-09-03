# Execução e Análise de Busca em Largura (BFS)

Este documento detalha a aplicação do algoritmo de Busca em Largura (BFS) sobre o grafo em estudo, incluindo a execução manual, o cálculo de níveis e distâncias, a adaptação solicitada, e o comparativo técnico com a DFS.

## 1. Execução Manual (Passo a Passo)

A BFS explora o grafo em "ondas", visitando todos os vizinhos imediatos antes de avançar para os nós mais profundos. Utilizaremos uma Fila (Queue) para controle. Iniciaremos pelo **vértice 1**.

**Estado Inicial:** 
- Fila `Q = [1]`
- Distância $d[1] = 0$, Predecessor $\pi[1] = Nil$
- Adaptação (Maior Vértice): `max_id = 1`

**Execução:**
1. **Desenfileira `1`:**
   - Vizinhos não visitados: `9`.
   - Visita `9`: $d[9] = 1$, $\pi[9] = 1$. Fila `Q = [9]`.
   - Atualiza `max_id`: $\max(1, 9) = 9$.
2. **Desenfileira `9`:**
   - Vizinhos não visitados: `2` (o `1` já foi visitado).
   - Visita `2`: $d[2] = 2$, $\pi[2] = 9$. Fila `Q = [2]`.
   - Atualiza `max_id`: $\max(9, 2) = 9$.
3. **Desenfileira `2`:**
   - Vizinhos não visitados: `5` (o `9` já foi).
   - Visita `5`: $d[5] = 3$, $\pi[5] = 2$. Fila `Q = [5]`.
   - Atualiza `max_id`: $\max(9, 5) = 9$.
4. **Desenfileira `5`:**
   - Vizinhos não visitados: `7, 8, 10` (o `2` já foi).
   - Visita `7`: $d[7] = 4$, $\pi[7] = 5$. Atualiza `max_id`: $\max(9, 7) = 9$.
   - Visita `8`: $d[8] = 4$, $\pi[8] = 5$. Atualiza `max_id`: $\max(9, 8) = 9$.
   - Visita `10`: $d[10] = 4$, $\pi[10] = 5$. Atualiza `max_id`: $\max(9, 10) = 10$.
   - Fila `Q = [7, 8, 10]`.
5. **Desenfileira `7`:** Vizinho `5` já visitado. Fila `Q = [8, 10]`.
6. **Desenfileira `8`:** Vizinhos `5, 10` já visitados. Fila `Q = [10]`.
7. **Desenfileira `10`:** Vizinhos `5, 8` já visitados. Fila `Q = []`. Fim da execução.

---

## 2. Níveis, Distâncias e Predecessores

A BFS garante que o caminho encontrado entre o vértice de origem e qualquer outro vértice tem o menor número possível de arestas (caminho mínimo em grafos não ponderados).

| Vértice ($v$) | Nível / Distância ($d[v]$) | Predecessor ($\pi[v]$) |
|:---:|:---:|:---:|
| **1**  | 0 | $Nil$ (Origem) |
| **9**  | 1 | 1 |
| **2**  | 2 | 9 |
| **5**  | 3 | 2 |
| **7**  | 4 | 5 |
| **8**  | 4 | 5 |
| **10** | 4 | 5 |

**Árvore de Níveis:**
- **Nível 0:** {1}
- **Nível 1:** {9}
- **Nível 2:** {2}
- **Nível 3:** {5}
- **Nível 4:** {7, 8, 10}

---

## 3. Adaptação Parcial: Maior Vértice Visitado

A adaptação no algoritmo é direta. Introduzimos uma variável de estado `max_visited` inicializada com o valor do nó de origem (no caso, 1). 

Durante o laço de exploração, ao descobrirmos um novo vizinho `v`, aplicamos a lógica de comparação:
```c
if (v > max_visited) {
    max_visited = v;
}
```
Ao final da execução mostrada no passo a passo, a variável `max_visited` reteve corretamente o valor **10**, que é o identificador máximo presente e alcançável na rede.

---

## 4. Comparação entre DFS e BFS e Escolha Justificada

Ambos os algoritmos (BFS e DFS) são plenamente capazes de explorar a conectividade do grafo, visitar todos os vértices da componente conexa e mapear a estrutura.

- **DFS (Busca em Profundidade):** Explora o máximo de profundidade possível antes de retroceder (backtracking), utilizando pilha (recursão ou explícita). Excelente para mapas topológicos e detecção de ciclos.
- **BFS (Busca em Largura):** Explora em camadas (níveis), utilizando uma fila. É a solução canônica para encontrar a distância mínima em grafos não ponderados.

**Escolha Justificada:**
Tanto a BFS quanto a DFS servem perfeitamente para mapear este grafo e rodar a nossa adaptação (rastrear o maior ID de vértice). Como ambas as abordagens possuem rigorosamente a mesma complexidade teórica, **a decisão final sobre qual utilizar no projeto não será teórica, mas sim empírica**. Decidiremos com base em testes práticos (benchmarking), rodando os dois códigos para avaliar qual apresenta melhor aproveitamento do cache da CPU e menor tempo real de execução no hardware de destino.

---

## 5. Integração, Testes e Complexidade

### Complexidade
A complexidade de tempo da BFS implementada utilizando a lista de adjacências é de **$O(|V| + |E|)$**, pois cada vértice é enfileirado no máximo uma vez e cada aresta é examinada estritamente duas vezes (uma por cada extremidade no caso não direcionado). A complexidade espacial é **$O(|V|)$** para acomodar a Fila `Q` e os vetores de distâncias/predecessores.

### Integração
Em um software de engenharia de redes ou automação, a BFS atua como um módulo de *discovery*. Ela pode ser acionada sempre que um novo dispositivo (nó) for conectado à malha para calcular a topologia e as rotas de menor salto, retornando o grafo mapeado para um módulo superior de tomada de decisão.

### Testes
Para garantir a confiabilidade desta implementação, o plano de testes unitários deve contemplar:
1.  **Assertiva de Distância:** Verificar se `distancia[10] == 4` e `distancia[1] == 0`.
2.  **Assertiva de Predecessor:** Garantir que reconstruir o caminho a partir do nó `8` lendo os predecessores (`8 -> 5 -> 2 -> 9 -> 1`) produz a rota correta.
3.  **Assertiva da Adaptação:** O retorno final da função para a variável `max_visited` deve ser estritamente igual a `10` após a varredura completa.
