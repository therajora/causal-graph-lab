import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_example(relative_path: str) -> str:
    completed = subprocess.run(
        [sys.executable, str(ROOT / relative_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def test_smoking_and_cancer_example_runs_with_contextualized_output() -> None:
    output = run_example("examples/01_smoking_and_cancer.py")

    assert "Pergunta causal: fumar aumenta o risco de cancer de pulmao?" in output
    assert "Pais de lung_cancer:" in output


def test_vaccination_and_infection_example_runs_with_intervention_question() -> None:
    output = run_example("examples/03_vaccination_and_infection.py")

    assert "Pergunta causal: o que mudaria se pudessemos intervir na vacinacao?" in output
    assert "operador do" in output.lower()
