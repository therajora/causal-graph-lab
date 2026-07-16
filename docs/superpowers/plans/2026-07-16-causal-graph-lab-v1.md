# causal-graph-lab v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar uma base didatica inicial (exemplos + conceitos + referencias) para estudo de grafos causais, com um pacote Python minimo apenas para apoiar os exemplos.

**Architecture:** Conteudo (referencias/notebooks/exemplos) e o foco principal; o codigo em `src/` fica pequeno e reutilizavel, com estruturas simples para DAGs e utilitarios de demonstracao. Testes garantem correcoes nas regras basicas de grafo.

**Tech Stack:** Python (pyproject.toml + setuptools), pytest (dev), numpy (opcional para exemplos), Jupyter (opcional para notebooks).

---

## Estrutura alvo

- `README.md`: visao geral e como rodar exemplos
- `pyproject.toml`: empacotamento e dependencias opcionais
- `src/causal_graph_lab/`: pacote minimo
  - `core/dag.py`: representacao simples de DAG causal
- `tests/`: testes do nucleo
- `references/`: bibliografia e notas teoricas
- `examples/`: scripts executaveis
- `notebooks/`: notebooks introdutorios (com narrativa)

---

### Task 1: Bootstrap do repositorio Python

**Files:**
- Create: `/workspace/causal-graph-lab/pyproject.toml`
- Create: `/workspace/causal-graph-lab/.gitignore`
- Create: `/workspace/causal-graph-lab/src/causal_graph_lab/__init__.py`
- Create: `/workspace/causal-graph-lab/src/causal_graph_lab/core/__init__.py`
- Modify: `/workspace/causal-graph-lab/README.md`

- [ ] **Step 1: Criar `pyproject.toml`**

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "causal-graph-lab"
version = "0.1.0"
description = "Base didatica para estudo de grafos causais: exemplos, conceitos e referencias."
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.optional-dependencies]
dev = ["pytest>=8.0"]
examples = ["numpy>=1.26"]
notebooks = ["jupyter>=1.0"]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 2: Criar `.gitignore`**

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.python-version
.venv/
dist/
build/
*.egg-info/
.ipynb_checkpoints/
```

- [ ] **Step 3: Criar pacote minimo (`__init__.py`)**

`src/causal_graph_lab/__init__.py`

```python
from .core.dag import CausalDAG

__all__ = ["CausalDAG"]
```

`src/causal_graph_lab/core/__init__.py`

```python
from .dag import CausalDAG

__all__ = ["CausalDAG"]
```

- [ ] **Step 4: Ajustar README para refletir estrutura e instalacao**

Atualizar `README.md` para incluir:

```markdown
## Estrutura

- references/: notas e bibliografia
- examples/: scripts executaveis
- notebooks/: narrativa e exploracao
- src/: pacote minimo de apoio

## Instalacao (opcional)

pip install -e ".[dev,examples,notebooks]"

## Rodar testes

pytest -q
```

- [ ] **Step 5: Validar que o repo instala e pytest roda**

Run:

```bash
python -m pip install -e ".[dev]"
pytest -q
```

Expected: PASS (ou "no tests ran" ate Task 2).

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml .gitignore README.md src/causal_graph_lab/__init__.py src/causal_graph_lab/core/__init__.py
git commit -m "chore: bootstrap python package"
```

---

### Task 2: DAG causal minimo (estrutura + consultas basicas)

**Files:**
- Create: `/workspace/causal-graph-lab/src/causal_graph_lab/core/dag.py`
- Create: `/workspace/causal-graph-lab/tests/test_dag.py`

- [ ] **Step 1: Escrever teste falhando para operacoes basicas**

`tests/test_dag.py`

```python
import pytest

from causal_graph_lab.core.dag import CausalDAG


def test_add_edge_and_parents_children():
    g = CausalDAG()
    g.add_edge("Z", "X")
    g.add_edge("Z", "Y")
    g.add_edge("X", "Y")

    assert g.parents("Y") == {"Z", "X"}
    assert g.parents("X") == {"Z"}
    assert g.children("Z") == {"X", "Y"}


def test_ancestors_descendants():
    g = CausalDAG()
    g.add_edge("Z", "X")
    g.add_edge("X", "Y")
    g.add_edge("W", "Z")

    assert g.ancestors("Y") == {"Z", "X", "W"}
    assert g.descendants("W") == {"Z", "X", "Y"}


def test_reject_cycle():
    g = CausalDAG()
    g.add_edge("A", "B")
    g.add_edge("B", "C")

    with pytest.raises(ValueError):
        g.add_edge("C", "A")
```

- [ ] **Step 2: Rodar teste para confirmar falha**

Run:

```bash
pytest -q
```

Expected: FAIL (modulo/objeto ainda nao existe).

- [ ] **Step 3: Implementar `CausalDAG` minimo**

`src/causal_graph_lab/core/dag.py`

```python
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class CausalDAG:
    _children: dict[str, set[str]] = field(default_factory=dict)
    _parents: dict[str, set[str]] = field(default_factory=dict)

    def add_node(self, node: str) -> None:
        if node not in self._children:
            self._children[node] = set()
        if node not in self._parents:
            self._parents[node] = set()

    def add_edge(self, parent: str, child: str) -> None:
        self.add_node(parent)
        self.add_node(child)
        if parent == child:
            raise ValueError("self-loop is not allowed in a DAG")
        if self._creates_cycle(parent, child):
            raise ValueError("edge would create a cycle")
        self._children[parent].add(child)
        self._parents[child].add(parent)

    def nodes(self) -> set[str]:
        return set(self._children.keys()) | set(self._parents.keys())

    def parents(self, node: str) -> set[str]:
        self.add_node(node)
        return set(self._parents[node])

    def children(self, node: str) -> set[str]:
        self.add_node(node)
        return set(self._children[node])

    def ancestors(self, node: str) -> set[str]:
        self.add_node(node)
        visited: set[str] = set()
        stack = list(self._parents[node])
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            stack.extend(self._parents.get(cur, set()))
        return visited

    def descendants(self, node: str) -> set[str]:
        self.add_node(node)
        visited: set[str] = set()
        stack = list(self._children[node])
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            stack.extend(self._children.get(cur, set()))
        return visited

    def _creates_cycle(self, parent: str, child: str) -> bool:
        return parent in self.descendants(child) or child in self.ancestors(parent)

    def to_edges(self) -> set[tuple[str, str]]:
        edges: set[tuple[str, str]] = set()
        for p, kids in self._children.items():
            for c in kids:
                edges.add((p, c))
        return edges

    @classmethod
    def from_edges(cls, edges: Iterable[tuple[str, str]]) -> CausalDAG:
        g = cls()
        for p, c in edges:
            g.add_edge(p, c)
        return g
```

- [ ] **Step 4: Rodar testes**

Run:

```bash
pytest -q
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/causal_graph_lab/core/dag.py tests/test_dag.py
git commit -m "feat: add minimal causal DAG structure"
```

---

### Task 3: Base teorica (leituras + conceitos) e indexacao por topico

**Files:**
- Create: `/workspace/causal-graph-lab/references/README.md`
- Create: `/workspace/causal-graph-lab/references/reading-list.md`
- Create: `/workspace/causal-graph-lab/references/01-dags-and-scm.md`
- Create: `/workspace/causal-graph-lab/references/02-d-separation.md`
- Create: `/workspace/causal-graph-lab/references/03-backdoor.md`
- Create: `/workspace/causal-graph-lab/references/04-do-operator.md`

- [ ] **Step 1: Criar indice de referencias**

`references/README.md`

```markdown
# Referencias

Este diretorio organiza notas curtas e referencias por topico.

- reading-list.md: bibliografia base
- 01-dags-and-scm.md
- 02-d-separation.md
- 03-backdoor.md
- 04-do-operator.md
```

- [ ] **Step 2: Criar lista de leitura base**

`references/reading-list.md`

```markdown
# Reading list (base)

## Livros

- Judea Pearl. Causality: Models, Reasoning, and Inference. 2nd ed.
- Jonas Peters, Dominik Janzing, Bernhard Scholkpf. Elements of Causal Inference.
- Miguel A. Hernan, James M. Robins. Causal Inference: What If.

## Artigos / notas

- Judea Pearl. The do-calculus revisited.
- Spirtes, Glymour, Scheines. Causation, Prediction, and Search (leituras selecionadas).

## Materiais praticos

- Documentacao do DoWhy (conceitos e exemplos).
- Documentacao do CausalNex (modelagem com DAGs).
```

- [ ] **Step 3: Criar notas por topico (curtas e diretas)**

`references/01-dags-and-scm.md`

```markdown
# DAGs e SCM (visao inicial)

## Ideia

Um DAG causal representa suposicoes causais (direcoes de influencia) entre variaveis. Um SCM (Structural Causal Model) formaliza mecanismos com equacoes estruturais e ruido exogeno.

## Termos

- Pais de Y: variaveis com setas apontando para Y
- Descendentes: alcancaveis por caminhos direcionados a partir de um no
- Confundidor: causa comum de X e Y

## Referencias

- Pearl, Causality, cap. 1-3
- Peters et al., Elements of Causal Inference, cap. 1-2
```

`references/02-d-separation.md`

```markdown
# d-separation (intuicao)

## Ideia

d-separation fornece um criterio grafico para inferir independencias condicionais implicadas por um DAG causal.

## Padroes classicos

- Cadeia: X -> Z -> Y
- Garfo (fork): X <- Z -> Y
- Colisor (collider): X -> Z <- Y

## Referencias

- Pearl, Causality, secao sobre d-separation
- Peters et al., cap. sobre independencias e separacao
```

`references/03-backdoor.md`

```markdown
# Backdoor (ajuste)

## Ideia

O criterio de backdoor identifica conjuntos de ajuste que bloqueiam caminhos espurios entre X e Y iniciando com uma seta entrando em X.

## Intuicao

Ajustar por confundidores (causas comuns) pode tornar X e Y comparaveis como se fossem randomizados, dentro de estratos.

## Referencias

- Pearl, Causality, criterio de backdoor
- Hernan & Robins, What If (ajuste e confundimento)
```

`references/04-do-operator.md`

```markdown
# Operador do (intervencao)

## Ideia

`do(X=x)` representa uma intervencao que fixa X em x, quebrando o mecanismo causal que normalmente determinaria X.

## Diferenca chave

Associacao (ver) nao e o mesmo que intervencao (fazer). O operador `do` formaliza essa diferenca.

## Referencias

- Pearl, Causality, cap. sobre intervencoes
- Hernan & Robins, g-formula e intervencoes
```

- [ ] **Step 4: Commit**

```bash
git add references
git commit -m "docs: add initial theory notes and reading list"
```

---

### Task 4: Exemplos executaveis (com foco pedagogico)

**Files:**
- Create: `/workspace/causal-graph-lab/examples/README.md`
- Create: `/workspace/causal-graph-lab/examples/01_dag_basics.py`
- Create: `/workspace/causal-graph-lab/examples/02_confounding_backdoor_simulation.py`

- [ ] **Step 1: Criar README de exemplos**

`examples/README.md`

```markdown
# Examples

Scripts pequenos, cada um focado em uma ideia.

## Rodar

python examples/01_dag_basics.py
python examples/02_confounding_backdoor_simulation.py
```

- [ ] **Step 2: Criar exemplo de DAG basico**

`examples/01_dag_basics.py`

```python
from causal_graph_lab import CausalDAG


def main() -> None:
    g = CausalDAG()
    g.add_edge("Z", "X")
    g.add_edge("Z", "Y")
    g.add_edge("X", "Y")

    print("edges:", sorted(g.to_edges()))
    print("parents(Y):", sorted(g.parents("Y")))
    print("ancestors(Y):", sorted(g.ancestors("Y")))


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Criar simulacao simples de confundimento e ajuste**

`examples/02_confounding_backdoor_simulation.py`

```python
from __future__ import annotations

import math
import random


def mean(xs: list[float]) -> float:
    return sum(xs) / len(xs)


def cov(x: list[float], y: list[float]) -> float:
    mx = mean(x)
    my = mean(y)
    return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / len(x)


def var(x: list[float]) -> float:
    return cov(x, x)


def ols_slope(x: list[float], y: list[float]) -> float:
    return cov(x, y) / var(x)


def ols_slope_adjusted(x: list[float], y: list[float], z: list[float]) -> float:
    bz = ols_slope(z, x)
    x_res = [xi - bz * zi for xi, zi in zip(x, z)]

    ay = ols_slope(z, y)
    y_res = [yi - ay * zi for yi, zi in zip(y, z)]

    return ols_slope(x_res, y_res)


def simulate(n: int, seed: int) -> tuple[list[float], list[float], list[float]]:
    rng = random.Random(seed)
    z = [rng.gauss(0.0, 1.0) for _ in range(n)]
    x = [0.8 * zi + rng.gauss(0.0, 1.0) for zi in z]
    y = [1.0 * xi + 0.8 * zi + rng.gauss(0.0, 1.0) for xi, zi in zip(x, z)]
    return z, x, y


def main() -> None:
    z, x, y = simulate(n=5000, seed=7)

    naive = ols_slope(x, y)
    adjusted = ols_slope_adjusted(x, y, z)

    print("naive slope (confounded):", round(naive, 3))
    print("adjusted slope (backdoor via Z):", round(adjusted, 3))
    print("expected causal effect of X on Y:", 1.0)
    print("note: this is a toy simulation, not a full causal identification pipeline")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4: Rodar exemplos e checar saida**

Run:

```bash
python examples/01_dag_basics.py
python examples/02_confounding_backdoor_simulation.py
```

Expected:
- imprime arestas/ancestrais no primeiro script
- imprime `adjusted` proximo de `1.0` e `naive` tipicamente diferente de `1.0`

- [ ] **Step 5: Commit**

```bash
git add examples
git commit -m "docs: add runnable causal graph examples"
```

---

### Task 5: Notebooks iniciais (narrativa curta)

**Files:**
- Create: `/workspace/causal-graph-lab/notebooks/README.md`
- Create: `/workspace/causal-graph-lab/notebooks/00_intro.ipynb`
- Create: `/workspace/causal-graph-lab/notebooks/01_confounding_and_backdoor.ipynb`

- [ ] **Step 1: Criar README dos notebooks**

`notebooks/README.md`

```markdown
# Notebooks

Notebooks introdutorios com narrativa de estudo.

## Rodar (opcional)

pip install -e ".[notebooks,examples]"
jupyter notebook
```

- [ ] **Step 2: Criar notebook 00 (markdown-only, curto)**

`notebooks/00_intro.ipynb`

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Introducao\\n",
        "\\n",
        "Este notebook apresenta a diferenca entre associacao e causalidade e o papel de DAGs causais como linguagem de suposicoes.\\n",
        "\\n",
        "## Ideias centrais\\n",
        "\\n",
        "- Um DAG causal codifica suposicoes direcionais entre variaveis.\\n",
        "- Confundimento surge com causas comuns de X e Y.\\n",
        "- Intervencao `do(X=x)` nao e a mesma coisa que observar `X=x`.\\n",
        "\\n",
        "## Leitura sugerida\\n",
        "\\n",
        "- Pearl, *Causality*\\n",
        "- Hernan & Robins, *What If*\\n"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
```

- [ ] **Step 3: Criar notebook 01 (conectando exemplo e teoria)**

`notebooks/01_confounding_and_backdoor.ipynb`

```json
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Confundimento e Backdoor\\n",
        "\\n",
        "Objetivo: construir intuicao para confundimento e por que ajustar por um confundidor pode recuperar o efeito causal em exemplos simples.\\n",
        "\\n",
        "Referencias:\\n",
        "- Pearl, criterio de backdoor\\n",
        "- Hernan & Robins, confundimento\\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {},
      "outputs": [],
      "source": [
        "from causal_graph_lab import CausalDAG\\n",
        "\\n",
        "g = CausalDAG()\\n",
        "g.add_edge('Z', 'X')\\n",
        "g.add_edge('Z', 'Y')\\n",
        "g.add_edge('X', 'Y')\\n",
        "\\n",
        "sorted(g.to_edges())\\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "Para ver a diferenca entre associacao e ajuste, rode tambem o script `examples/02_confounding_backdoor_simulation.py`.\\n"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
```

- [ ] **Step 4: Validar formato do JSON**

Run:

```bash
python -c "import json; json.load(open('notebooks/00_intro.ipynb')); json.load(open('notebooks/01_confounding_and_backdoor.ipynb')); print('ok')"
```

Expected: `ok`

- [ ] **Step 5: Commit**

```bash
git add notebooks
git commit -m "docs: add introductory notebooks"
```

---

## Self-review (plan)

- Cobertura da spec: estrutura didatica + referencias + exemplos + pacote minimo + notebooks presentes nas Tasks 1-5.
- Sem placeholders: cada task tem arquivos, conteudo e comandos.
- Consistencia: nome do pacote `causal_graph_lab` e nome do projeto `causal-graph-lab` usados de forma consistente.

---

## Execucao

Implementar em iteracoes pequenas, fazendo `git commit` ao final de cada task, para revisar a evolucao passo a passo.
