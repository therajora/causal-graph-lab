from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from causal_graph_lab import CausalDAG


def main() -> None:
    print("Pergunta causal: fumar aumenta o risco de cancer de pulmao?")

    graph = CausalDAG()
    graph.add_edge("genetic_risk", "smoking")
    graph.add_edge("genetic_risk", "lung_cancer")
    graph.add_edge("smoking", "lung_cancer")

    print("DAG:", sorted(graph.to_edges()))
    print("Pais de lung_cancer:", sorted(graph.parents("lung_cancer")))
    print(
        "Mensagem: sem considerar causas comuns, a associacao observada pode misturar efeito causal e confundimento."
    )


if __name__ == "__main__":
    main()
