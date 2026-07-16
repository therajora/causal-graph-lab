from __future__ import annotations

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
