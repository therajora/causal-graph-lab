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
