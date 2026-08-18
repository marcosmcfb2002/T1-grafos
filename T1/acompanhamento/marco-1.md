# Modelagem - Marco 1: Ladder Takahashi

* **Alunos:** Nycaio Bezerra (2220230) e Marcos Mendes (2310532)
* **Orientador:** Prof. Me. Ricardo Carubbi
* **Disciplina:** Resolução de Problemas com Grafos
* **Instituição:** Centro de Ciências Tecnológicas (CCT) - Universidade de Fortaleza (UNIFOR)

---

## Agenda

* Descrição do Problema
* Definição da Estrutura do Grafo
* Instância Pequena e Resultado Esperado
* Hipótese Inicial de Solução

---

## 1. Descrição do Problema: Ladder Takahashi

* **Problema:** Definição formal do enunciado, entradas, saídas e restrições.
* **Estrutura de Grafo:** Vértices, arestas e tipo do grafo modelado.
* **Instância Pequena:** Exemplo concreto com caminho percorrido e resultado esperado.
* **Hipótese de Solução:** Algoritmo proposto, estratégia de travessia e tratamento de escala.

---

## 2. Definição da Estrutura de Grafo

### 1. Vértices ($V$)
* Os andares $u$ envolvidos nas conexões de escadas, além do andar 1 (ponto de partida obrigatório).
* O número total de vértices distintos é de no máximo $2N + 1$.

### 2. Arestas ($E$)
* As escadas que conectam os andares $A_i$ e $B_i$.
* Cada escada corresponde a exatamente uma aresta no grafo, totalizando $N$ arestas.

### 3. Tipo do Grafo
* **Grafo não-direcionado:** As escadas podem ser percorridas em ambas as direções.
* **Grafo não-ponderado:** Todas as conexões têm custo unitário de transição.
* O grafo resultante possui no máximo $2N + 1$ vértices e exatamente $N$ arestas, com estrutura esparsa adequada para travessia eficiente via DFS ou BFS.

---

## 3. Instância Pequena e Resultado Esperado

### Entrada de Exemplo
* $N = 4$
* Conexões:
  * $(1, 4)$
  * $(4, 3)$
  * $(4, 10)$
  * $(8, 3)$

### Caminho Percorrido
1. **Início no andar 1:** Ponto de partida obrigatório.
2. **Escada $(1, 4)$:** Utilizada para alcançar o andar 4.
3. **Andares 3 e 10:** A partir do andar 4, obtém-se acesso aos andares 3 e 10.
4. **Andar 8:** Visitando o andar 3, ganha-se acesso ao andar 8.

### Resultado Esperado
* **Conjunto Alcançável / Valor Máximo:** Andar 10.

---

## 4. Hipótese Inicial de Solução

### Algoritmo Proposto
O problema reduz-se a **encontrar o valor máximo entre todos os vértices pertencentes à componente conexa** que contém o vértice de origem 1.

### Estrutura de Travessia
Pode ser resolvido através de uma **Busca em Profundidade (DFS)** ou **Busca em Largura (BFS)** iniciada no nó 1. Ambas percorrem todos os vértices da componente conexa em tempo $O(V + E)$.

### Tratamento da Escala da Entrada
Como os índices dos andares podem ir até $10^9$, não é viável utilizar um vetor estático ou matriz de adjacência tradicional.

A solução deve seguir uma das duas abordagens:
* **Opção A - Estrutura Dinâmica:** Utilização de lista de adjacência dinâmica como `std::map<int, vector<int>>` em C++ ou `defaultdict(list)` em Python.
* **Opção B - Compressão de Coordenadas:** Mapeamento dos andares (até $2N$) para índices contínuos de $0$ a $2N$, permitindo o uso de um vetor estático de tamanho $2N + 1$.
