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
