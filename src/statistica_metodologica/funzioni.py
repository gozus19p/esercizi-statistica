import statistics
import math
import scipy.stats as stats
from typing import Union


def mean(values: list[float]) -> float:
    return sum(values)/len(values)


def median(values: list[float]) -> float:
    values = sorted(values)
    # Se i numeri sono pari, restituisco la semisomma dei due centrali
    if len(values) % 2 == 0:
        index_one, index_two = len(values) // 2, len(values) // 2 + 1
        return (values[index_one-1] + values[index_two-1]) / 2.0

    middle_index = len(values)//2
    return values[middle_index-1]


def variance(values: list[float], population: bool = True) -> float:
    mean_ = mean(values)
    to_subtract = 1 if population else 0
    return sum([pow(x - mean_, 2) for x in values]) / (len(values) - to_subtract)


def stdev(values: list[float], population: bool = True) -> float:
    return math.sqrt(variance(values, population))


def mode(values: Union[list[float], list[int]]) -> float:
    return statistics.mode(values)


def covariance(values: list[float], values_2: list[float], population: bool = True) -> float:
    m_x, m_y = mean(values), mean(values_2)
    to_subtract = 1 if population else 0
    return sum([(x - m_x) * (y - m_y) for x, y in zip(values, values_2)]) / (len(values) + len(values_2) - to_subtract)


def binomial_coefficient(n: int, k: int) -> float:
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def test_z_normale(n: int, x: int, p0: float) -> float:
    p_hat = x / n
    return (p_hat - p0) / math.sqrt((p0 * (1 - p0)) / n)


def norm(z: float) -> float:
    return stats.norm.ppf(z)


def dist_binomial(n: int, k: int, p: float) -> float:
    return binomial_coefficient(n, k) * pow(p, k) * pow(1 - p, n - k)