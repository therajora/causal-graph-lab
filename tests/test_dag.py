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
